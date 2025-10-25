📶 100-Node Optimized Wi-Fi 6 NS-3 Simulation (Python)

This NS-3 Python script simulates a 100-node Wi-Fi 6 (802.11ax) network optimized for high-density wireless traffic testing.

It features multi-channel Wi-Fi groups, EDCA QoS traffic classes, and FlowMonitor integration to measure throughput, delay, and packet loss.

✨ Features

100 Wi-Fi Nodes: Arranged in a 10x10 grid with 15m spacing

Multi-Channel Wi-Fi Groups: 4 channels, nodes divided into 4 groups (25 nodes each) to minimize interference

EDCA QoS Traffic Classes: Voice, Video, Best Effort, Background

Wi-Fi 6 (802.11ax) Support: OFDMA and MU-MIMO for high throughput

UDP Echo Clients/Servers: Simple packet exchange for performance evaluation

FlowMonitor Integration: Measures per-flow throughput, packet loss, and average delay

🧩 Requirements

NS-3 with Python bindings (Linux or WSL2 recommended)

Python 3.x (tested with Python 3.10+)

NS-3 version 3.41+ (for Wi-Fi 6 support)

⚠️ Windows native Python will not work — use WSL2 Ubuntu or a Linux VM.

⚙️ How to Run

Open your Linux terminal / WSL2.

Navigate to your NS-3 Python scripts folder:

cd ~/ns-allinone-3.41/ns-3.41/


Ensure PYTHONPATH includes NS-3 libraries:

export PYTHONPATH=$(pwd)/build/lib:$PYTHONPATH


Save the script as wifi6_100nodes.py.

Run the simulation:

python3 wifi6_100nodes.py


Monitor console output for per-flow throughput, delay, and packet loss.

📊 Output Interpretation

Example output per flow:

Flow 1: 10.1.0.1 -> 10.1.0.2
  Tx Packets: 1000
  Rx Packets: 998
  Lost Packets: 2
  Throughput: 8.19 Mbps
  Average delay: 0.002345 s


Tx Packets: Total packets sent by the client

Rx Packets: Packets successfully received by the server

Lost Packets: Packets lost due to collisions/interference (ideally very low)

Throughput: Measured in Mbps over the simulation period

Average Delay: Per-packet latency in seconds

🧠 Optimization Notes

Multi-Channel Setup: Reduces collisions between nodes

EDCA QoS: Prioritizes high-priority traffic (Voice & Video)

Grid Layout: Prevents nodes from being too close, lowering interference

Wi-Fi 6 Features: OFDMA and MU-MIMO maximize parallel transmissions

Interval Adjustment:

Lower interval → higher traffic load, may increase packet loss

Higher interval → less congestion, safer throughput

🏷️ Tags

#ns3 #wifi6 #802.11ax #simulation #python #networking #udp #flowmonitor #edca #highdensity
