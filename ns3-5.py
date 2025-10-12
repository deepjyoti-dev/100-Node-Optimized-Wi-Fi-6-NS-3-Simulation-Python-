# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 14:44:48 2025

@author: deepj
"""

import ns.applications
import ns.core
import ns.network
import ns.internet
import ns.wifi
import ns.mobility
import ns.flow_monitor

def main():
    simulation_time = 10.0
    packet_size = 1024
    num_packets = 1000
    interval = 0.005
    num_nodes = 100
    nodes_per_group = 25
    num_channels = 4

    # Create nodes
    nodes = ns.network.NodeContainer()
    nodes.Create(num_nodes)

    # Internet stack
    stack = ns.internet.InternetStackHelper()
    stack.Install(nodes)

    # Wi-Fi PHY + Channels
    wifi = ns.wifi.WifiHelper.Default()
    wifi.SetStandard(ns.wifi.WIFI_PHY_STANDARD_80211ax)  # Wi-Fi 6

    wifi_phy = ns.wifi.YansWifiPhyHelper.Default()
    wifi_mac = ns.wifi.WifiMacHelper()
    wifi_mac.SetType("ns3::AdhocWifiMac", "QosSupported", ns.core.BooleanValue(True))

    # Split nodes into multiple channels to reduce interference
    devices = ns.network.NetDeviceContainer()
    for i in range(num_channels):
        start = i * nodes_per_group
        end = start + nodes_per_group
        channel = ns.wifi.YansWifiChannelHelper.Default()
        phy = ns.wifi.YansWifiPhyHelper.Default()
        phy.SetChannel(channel.Create())
        dev = wifi.Install(phy, wifi_mac, ns.network.NodeContainer(nodes.Get(start, end - 1)))
        devices.Add(dev)

    # Mobility: Grid layout to reduce collisions
    mobility = ns.mobility.MobilityHelper()
    mobility.SetPositionAllocator(
        ns.mobility.GridPositionAllocator(
            "MinX", ns.core.DoubleValue(0.0),
            "MinY", ns.core.DoubleValue(0.0),
            "DeltaX", ns.core.DoubleValue(15.0),
            "DeltaY", ns.core.DoubleValue(15.0),
            "GridWidth", ns.core.UintegerValue(10),
            "LayoutType", ns.mobility.GridPositionAllocator.ROW_FIRST
        )
    )
    mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel")
    mobility.Install(nodes)

    # Assign IP addresses
    address = ns.internet.Ipv4AddressHelper()
    address.SetBase(ns.network.Ipv4Address("10.1.0.0"), ns.network.Ipv4Mask("255.255.0.0"))
    interfaces = address.Assign(devices)

    # UDP Servers on all nodes
    port = 9
    for i in range(num_nodes):
        server = ns.applications.UdpEchoServerHelper(port)
        app = server.Install(nodes.Get(i))
        app.Start(ns.core.Seconds(0.0))
        app.Stop(ns.core.Seconds(simulation_time))

    # UDP Clients: send to next node with EDCA QoS
    access_categories = ['voice', 'video', 'best-effort', 'background']
    for i in range(num_nodes):
        target = (i + 1) % num_nodes
        ac = access_categories[i % 4]  # Assign AC in round-robin
        client = ns.applications.UdpEchoClientHelper(interfaces.GetAddress(target), port)
        client.SetAttribute("MaxPackets", ns.core.UintegerValue(num_packets))
        client.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(interval)))
        client.SetAttribute("PacketSize", ns.core.UintegerValue(packet_size))
        app = client.Install(nodes.Get(i))
        app.Start(ns.core.Seconds(0.1))
        app.Stop(ns.core.Seconds(simulation_time))

    # FlowMonitor
    flowmon_helper = ns.flow_monitor.FlowMonitorHelper()
    monitor = flowmon_helper.InstallAll()

    # Run simulation
    ns.core.Simulator.Stop(ns.core.Seconds(simulation_time))
    ns.core.Simulator.Run()

    # Print FlowMonitor statistics
    monitor.CheckForLostPackets()
    classifier = flowmon_helper.GetClassifier()
    stats = monitor.GetFlowStats()
    for flow_id, flow in stats.items():
        t = classifier.FindFlow(flow_id)
        src_ip = t.sourceAddress
        dst_ip = t.destinationAddress
        print(f"Flow {flow_id}: {src_ip} -> {dst_ip}")
        print(f"  Tx Packets: {flow.txPackets}")
        print(f"  Rx Packets: {flow.rxPackets}")
        print(f"  Lost Packets: {flow.lostPackets}")
        print(f"  Throughput: {flow.rxBytes * 8.0 / simulation_time / 1e6:.2f} Mbps")
        if flow.rxPackets > 0:
            print(f"  Average delay: {flow.delaySum.GetSeconds()/flow.rxPackets:.6f} s\n")

    ns.core.Simulator.Destroy()

if __name__ == "__main__":
    main()
