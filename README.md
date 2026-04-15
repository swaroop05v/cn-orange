# SDN-Based Network Delay Measurement Tool

## 📌 Problem Statement

The objective of this project is to implement a Software Defined Networking (SDN) solution using Mininet and the Ryu controller to measure and analyze network delay and throughput between hosts.

---

## 🧠 Objective

* Demonstrate controller-switch interaction using OpenFlow
* Implement flow rule design (match-action)
* Measure network delay (latency) using ping
* Measure throughput using iperf
* Compare performance across different paths

---

## 🏗️ Topology

A linear topology with 3 hosts and 3 switches is used:

h1 — s1 — s2 — s3 — h3
|
h2

* h1 → h2: shorter path
* h1 → h3: longer path

---

## ⚙️ Tools Used

* Mininet
* Ryu Controller
* OpenFlow (OF1.3)
* iperf
* ovs-ofctl

---

## 🚀 Setup and Execution

### 1. Start Controller

```bash
ryu-manager delay_controller.py
```

### 2. Start Mininet

```bash
sudo mn -c
sudo mn --topo linear,3 --controller remote --switch ovsk,protocols=OpenFlow13
```

---

## 🧪 Testing & Results

### 🔹 Connectivity Test

```bash
pingall
```

---

### 🔹 Delay Measurement

```bash
h1 ping h2
h1 ping h3
```

**Observation:**

* h1 → h2 has lower delay
* h1 → h3 has slightly higher delay due to more hops

---

### 🔹 Throughput Measurement

```bash
h2 iperf -s &
h1 iperf -c h2

h3 iperf -s &
h1 iperf -c h3
```

**Observation:**

* Higher throughput for shorter path
* Slightly reduced throughput for longer path

---

### 🔹 Flow Rules

```bash
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

**Observation:**

* Flow rules installed dynamically
* Match-action logic used for forwarding

---

## 📊 Analysis

* Delay increases with number of switches (hop count)
* Throughput slightly decreases with longer paths
* First packet is processed by controller, subsequent packets handled by switches

---

## 🧠 Key Concepts Demonstrated

* Software Defined Networking (SDN)
* Control Plane vs Data Plane
* OpenFlow Protocol
* Flow Table (Match-Action)
* Packet_in event handling

---

## 🎯 Conclusion

This project successfully demonstrates how SDN enables centralized control of network behavior. By analyzing delay and throughput across different paths, we observe how network performance varies based on topology and hop count.

---

## 📸 Screenshots

(Add your screenshots here)

---

## 👨‍💻 Author

Swaroop Venkateshwar

