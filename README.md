📄 README: 100-Node Optimized Wi-Fi 6 NS-3 Simulation (Python)
Overview

This NS-3 Python script simulates a 100-node Wi-Fi 6 (802.11ax) network with:

Multi-channel Wi-Fi groups → reduces collisions and interference.

EDCA QoS traffic classes → prioritizes Voice, Video, Best Effort, and Background traffic.

Static grid positions → zero mobility jitter.

UDP traffic → each node sends packets to the next node in a loop.

FlowMonitor integration → measures per-flow throughput, packet loss, and delay.

This setup is ideal for evaluating network efficiency under high-density wireless traffic in a near-ideal environment.

Features

100 Wi-Fi nodes arranged in a grid (10x10) with 15m spacing.

4 Wi-Fi channels → nodes divided into 4 groups (25 nodes each) to minimize interference.

EDCA QoS support → traffic is distributed among:

Voice

Video

Best Effort

Background

Wi-Fi 6 (802.11ax) → supports OFDMA and MU-MIMO for high throughput.

UDP Echo Clients/Servers → simple packet exchange for performance testing.

FlowMonitor output → prints:

Transmitted / received packets

Lost packets

Throughput per flow (Mbps)

Average delay per flow (seconds)

Requirements

NS-3 with Python bindings installed (Linux or WSL2 recommended).

Python 3.x (tested with Python 3.10+).

NS-3 version 3.41+ recommended for Wi-Fi 6 support.

⚠️ Windows native Python will not work; use WSL2 Ubuntu or a Linux VM.

How to Run

Open your Linux terminal / WSL2.

Navigate to your NS-3 Python scripts folder:

cd ~/ns-allinone-3.41/ns-3.41/


Ensure PYTHONPATH includes NS-3 libraries:

export PYTHONPATH=$(pwd)/build/lib:$PYTHONPATH


Save the script as wifi6_100nodes.py.

Run the simulation:

python3 wifi6_100nodes.py


Monitor console output for per-flow throughput, delay, and packet loss.

Output Interpretation

For each flow, you’ll see:

Flow 1: 10.1.0.1 -> 10.1.0.2
  Tx Packets: 1000
  Rx Packets: 998
  Lost Packets: 2
  Throughput: 8.19 Mbps
  Average delay: 0.002345 s


Tx Packets: total packets sent by the client.

Rx Packets: total packets successfully received by the server.

Lost Packets: packets lost due to collisions/interference (ideally 0 or very low).

Throughput: measured in Mbps over the simulation period.

Average delay: per-packet latency in seconds (helps estimate jitter).

Optimization Notes

Multi-channel setup drastically reduces collisions between nodes.

EDCA QoS prioritizes high-priority traffic like Voice & Video.

Grid layout prevents nodes from being too close, lowering interference.

Wi-Fi 6 features (OFDMA/MU-MIMO) maximize parallel transmissions.

Adjust interval to fine-tune throughput:

Lower interval → higher traffic load, may increase packet loss.

Higher interval → safer, less congestion.
