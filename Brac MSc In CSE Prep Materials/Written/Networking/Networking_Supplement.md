# 🌐 NETWORKING — SUPPLEMENT
### Syllabus-এ আছে কিন্তু মূল ফাইলে ছিল না

> **কেন পড়বে:** Q4 (VLSM/CIDR) এসেছে **CSE 490 (WAN Routing)** থেকে — মানে CCNA-ধর্মী topic scope-এ আছে। একই course-এ VLAN, STP, RIP, OSPF-ও আছে।
> **পড়ার সময়:** ২৫ মিনিট · **অগ্রাধিকার:** মূল Networking ফাইল শেষ করে তারপর

---

## এই ফাইলে যা আছে

| # | Topic | Course | সম্ভাবনা |
|---|---|---|---|
| 1 | **Media Access Control (CSMA/CD, CSMA/CA)** | 421 | 🔴 বেশি |
| 2 | **Routing Protocols (RIP, OSPF, BGP)** | 490 | 🔴 বেশি |
| 3 | **Flow ও Congestion Control** | 421 | 🔴 বেশি |
| 4 | **VLAN ও STP** | 490 | 🟡 মাঝারি |
| 5 | **Shannon ও Nyquist Theorem** | 320 | 🟡 মাঝারি |
| 6 | **Line Coding ও Modulation** | 320 | 🟡 মাঝারি |
| 7 | Framing · WAN Protocol · Security | 320/421 | 🔵 কম |

---
---

# 1️⃣ MEDIA ACCESS CONTROL ⭐⭐⭐

## সমস্যাটা কী
একই media-তে একাধিক device একসাথে পাঠালে **Collision** হয়। কে কখন পাঠাবে — সেটা ঠিক করাই MAC-এর কাজ।

## CSMA/CD ⭐ (তারযুক্ত Ethernet)

**পূর্ণরূপ:** Carrier Sense Multiple Access with **Collision Detection**

### ধাপ
1. **Carrier Sense** — পাঠানোর আগে শোনো, লাইন ব্যস্ত কিনা
2. লাইন খালি থাকলে → **পাঠাও**
3. পাঠানোর সময়ও **শুনতে থাকো**
4. Collision **টের পেলে** → সাথে সাথে থামো, **jam signal** পাঠাও
5. **Random সময়** অপেক্ষা করো (**Binary Exponential Backoff**)
6. আবার চেষ্টা করো

⭐ **মূল কথা:** Collision **ঘটার পর ধরা পড়ে**, তাই "Detection"

## CSMA/CA ⭐ (বেতার Wi-Fi)

**পূর্ণরূপ:** Carrier Sense Multiple Access with **Collision Avoidance**

### ধাপ
1. লাইন শোনো
2. ব্যস্ত থাকলে → random সময় অপেক্ষা
3. খালি থাকলে → **RTS** (Request To Send) পাঠাও
4. Receiver **CTS** (Clear To Send) দিয়ে সাড়া দেয়
5. তারপর data পাঠাও
6. Receiver **ACK** পাঠায়

⭐ **মূল কথা:** Collision **ঘটার আগেই এড়ানো হয়**, তাই "Avoidance"

## কেন বেতারে CD চলে না? ⭐⭐⭐ (নিশ্চিত প্রশ্ন)
```
১. বেতারে device একসাথে পাঠাতে ও শুনতে পারে না (half-duplex)
২. Hidden Terminal Problem —
   A ও C একে অপরকে শুনতে পায় না, কিন্তু দুজনেই B-কে পায়
   দুজনেই ভাববে লাইন খালি → B-তে collision
```

## তুলনা ⭐⭐⭐

| | **CSMA/CD** | **CSMA/CA** |
|---|---|---|
| কোথায় | **তারযুক্ত (Ethernet 802.3)** | **বেতার (Wi-Fi 802.11)** |
| কৌশল | Collision **ধরে** | Collision **এড়ায়** |
| কখন কাজ করে | পাঠানোর **সময়** | পাঠানোর **আগে** |
| ব্যবহার করে | Jam signal, Backoff | **RTS/CTS/ACK** |
| দক্ষতা | বেশি | কম (overhead বেশি) |

### অন্যান্য MAC পদ্ধতি
| | |
|---|---|
| **ALOHA** | যখন খুশি পাঠাও · দক্ষতা **18%** |
| **Slotted ALOHA** | নির্দিষ্ট slot-এ · দক্ষতা **37%** |
| **Token Passing** | Token যার কাছে সে পাঠাবে · **collision নেই** (802.5) |
| **Polling** | কেন্দ্রীয় controller জিজ্ঞেস করে |

### 🔁 Revision Box
**CSMA/CD = তারযুক্ত Ethernet**, collision ঘটার পর ধরে, jam signal + backoff। **CSMA/CA = বেতার Wi-Fi**, আগেই এড়ায়, **RTS/CTS/ACK**। বেতারে CD চলে না কারণ **একসাথে পাঠানো-শোনা যায় না** ও **Hidden Terminal Problem**। ALOHA 18%, Slotted ALOHA 37%।

---
---

# 2️⃣ ROUTING PROTOCOLS ⭐⭐⭐

## দুই প্রধান শ্রেণি

| | **Distance Vector** | **Link State** |
|---|---|---|
| জানে | শুধু **প্রতিবেশীর** কাছ থেকে দূরত্ব | **পুরো network-এর মানচিত্র** |
| Algorithm | **Bellman-Ford** | **Dijkstra** ⭐ |
| Update পাঠায় | পুরো routing table, **প্রতিবেশীকে** | শুধু পরিবর্তন, **সবাইকে** (flooding) |
| Convergence | ধীর | **দ্রুত** |
| উদাহরণ | **RIP**, IGRP | **OSPF**, IS-IS |
| সমস্যা | **Count-to-infinity** | বেশি CPU ও memory |

⭐ **মনে রাখো: RIP → Bellman-Ford · OSPF → Dijkstra** — তোমার Algorithm ফাইলের সাথে সরাসরি মিলে যায়

## প্রধান Protocol গুলো

| Protocol | ধরন | Metric | সীমা |
|---|---|---|---|
| **RIP v1/v2** | Distance Vector | **Hop count** | সর্বোচ্চ **15 hop** (16 = অসীম) |
| **OSPF** | **Link State** | **Cost** (bandwidth-ভিত্তিক) | সীমা নেই, **area** ব্যবহার করে |
| **EIGRP** | Hybrid (Cisco) | Bandwidth + Delay | Cisco-নির্দিষ্ট |
| **BGP** | Path Vector | Path attribute | **Internet-এর মূল protocol** ⭐ |

## IGP vs EGP ⭐
- **IGP** (Interior Gateway Protocol) — **এক** organization-এর ভিতরে → **RIP, OSPF, EIGRP**
- **EGP** (Exterior Gateway Protocol) — **ভিন্ন** organization-এর মাঝে → **BGP**

## Static vs Dynamic Routing
| **Static** | **Dynamic** |
|---|---|
| হাতে বসানো | নিজে শেখে |
| ছোট network | বড় network |
| নিরাপদ, overhead নেই | পরিবর্তনে নিজে মানিয়ে নেয় |

⚠️ **RIP v1 classful (VLSM সমর্থন করে না)** · **RIP v2, OSPF, EIGRP classless (VLSM চলে)** ⭐
— এটাই Q4-এর সাথে সরাসরি যুক্ত: VLSM চালাতে **classless routing protocol** লাগে

### 🔁 Revision Box
**Distance Vector (RIP) = Bellman-Ford**, hop count, **সর্বোচ্চ 15 hop**, ধীর। **Link State (OSPF) = Dijkstra**, cost metric, দ্রুত convergence। **BGP = Internet-এর routing (EGP)**, বাকিরা IGP। **RIP v1 classful, বাকিরা classless — VLSM চালাতে classless লাগে**।

---
---

# 3️⃣ FLOW ও CONGESTION CONTROL ⭐⭐

## পার্থক্যটা আগে বুঝে নাও ⭐⭐⭐

| | **Flow Control** | **Congestion Control** |
|---|---|---|
| সমস্যা | **Receiver** সামলাতে পারছে না | **Network** ভিড়ে ঠাসা |
| কার মধ্যে | Sender ↔ Receiver | পুরো network |
| Layer | Data Link + Transport | **Transport (TCP)** |
| পদ্ধতি | Stop-and-Wait, Sliding Window | Slow Start, AIMD |

**সহজ কথায়:** Flow control = "তুমি এত দ্রুত নিতে পারছ না" · Congestion control = "রাস্তায় জ্যাম"

## Flow Control পদ্ধতি

### Stop-and-Wait
একটা frame পাঠাও → ACK-এর জন্য অপেক্ষা করো → পরেরটা পাঠাও
✅ সহজ ❌ **খুব ধীর** (একবারে একটাই)

### Sliding Window ⭐
একসাথে **একাধিক frame** পাঠাও, ACK আসতে থাকলে window সামনে সরে

| | **Go-Back-N** | **Selective Repeat** |
|---|---|---|
| ভুল হলে | **ভুলটা থেকে সব আবার** পাঠায় | **শুধু ভুলটাই** পাঠায় |
| Receiver buffer | লাগে না | **লাগে** |
| জটিলতা | কম | বেশি |
| দক্ষতা | কম | **বেশি** |

## TCP Congestion Control ⭐
```
১. Slow Start          — window দ্বিগুণ হারে বাড়ে (exponential)
২. Congestion Avoidance — threshold-এর পর ১ করে বাড়ে (linear)
৩. Congestion Detection — packet হারালে window কমাও
```
**AIMD** = Additive Increase, Multiplicative Decrease
(ধীরে বাড়াও, দ্রুত কমাও)

### 🔁 Revision Box
**Flow control = receiver-কে বাঁচানো** (Stop-and-Wait, Sliding Window)। **Congestion control = network-কে বাঁচানো** (Slow Start, AIMD)। **Go-Back-N = ভুল থেকে সব আবার**, **Selective Repeat = শুধু ভুলটা**। TCP: Slow Start → Congestion Avoidance।

---
---

# 4️⃣ VLAN ও STP ⭐⭐

## VLAN (Virtual LAN)

### Definition
A **VLAN** logically divides a **single physical switch** into **multiple broadcast domains**, so devices can be grouped by function rather than by location.

### কেন দরকার
```
একটা Switch-এ HR, Sales, IT — সবাই যুক্ত
সমস্যা: সবাই একই broadcast domain-এ, সবাই সবার traffic দেখে

VLAN দিয়ে ভাগ করলে:
  VLAN 10 = HR      ┐
  VLAN 20 = Sales   ├─ একই switch, কিন্তু আলাদা network
  VLAN 30 = IT      ┘
```

### Key Points ⭐
1. **প্রতিটি VLAN = আলাদা broadcast domain**
2. **VLAN-এর মধ্যে যোগাযোগ করতে Router বা Layer-3 Switch লাগে** ⭐ (Inter-VLAN Routing)
3. **Trunk port** = একাধিক VLAN-এর traffic বহন করে · **Access port** = একটাই VLAN
4. **802.1Q** = VLAN tagging-এর standard ⭐
5. **VTP** (VLAN Trunking Protocol) = একটা switch-এ VLAN বানালে বাকিদের জানিয়ে দেয় (Cisco)

## STP (Spanning Tree Protocol) ⭐

### সমস্যা
Switch-এর মধ্যে **loop** থাকলে **Broadcast Storm** হয় — একই frame অসীমবার ঘুরতে থাকে, network অচল হয়ে যায়।

### সমাধান
**STP (IEEE 802.1D)** loop-মুক্ত পথ বের করে, বাড়তি link গুলো **block** করে রাখে। মূল link নষ্ট হলে block করা link **চালু** করে দেয়।

### ধাপ
1. **Root Bridge** নির্বাচন (সবচেয়ে ছোট Bridge ID যার)
2. প্রতিটি switch-এ **Root Port** ঠিক করা (root-এর দিকে সবচেয়ে কম cost)
3. প্রতিটি segment-এ **Designated Port** ঠিক করা
4. বাকি port **Blocked**

⭐ STP আসলে graph-এ **Spanning Tree** বের করছে — তোমার Algorithm ফাইলের **Prim/Kruskal**-এর ধারণাটাই

### 🔁 Revision Box
**VLAN** = এক physical switch → একাধিক **broadcast domain**, **802.1Q** tagging, VLAN-এর মধ্যে কথা বলতে **Router লাগে**। **Trunk = অনেক VLAN, Access = একটা**। **STP (802.1D)** = switch loop ও **Broadcast Storm** ঠেকায়, **Root Bridge** নির্বাচন করে বাড়তি link **block** করে।

---
---

# 5️⃣ SHANNON ও NYQUIST ⭐⭐

> সূত্র দুটো — সংখ্যা বসিয়ে হিসাব চাইতে পারে

## Nyquist (শব্দহীন / Noiseless Channel)
```
C = 2 × B × log₂(L)

C = সর্বোচ্চ data rate (bps)
B = Bandwidth (Hz)
L = signal level সংখ্যা
```

**উদাহরণ:** B = 3000 Hz, L = 2
```
C = 2 × 3000 × log₂(2) = 2 × 3000 × 1 = 6000 bps
```

## Shannon (শব্দযুক্ত / Noisy Channel) ⭐
```
C = B × log₂(1 + S/N)

S/N = Signal-to-Noise ratio (অনুপাত, dB নয়)
```

**উদাহরণ:** B = 3000 Hz, S/N = 3
```
C = 3000 × log₂(1 + 3) = 3000 × log₂(4) = 3000 × 2 = 6000 bps
```

## dB থেকে রূপান্তর ⭐
```
SNR(dB) = 10 × log₁₀(S/N)
```
SNR = 30 dB হলে → `S/N = 10³ = 1000`

## পার্থক্য
| **Nyquist** | **Shannon** |
|---|---|
| **শব্দহীন** channel | **শব্দযুক্ত** channel |
| Signal **level** দরকার | **Noise** দরকার |
| তাত্ত্বিক আদর্শ | বাস্তব সীমা |

⭐ দুটোই বের করে **সর্বোচ্চ তাত্ত্বিক data rate** — বাস্তবে এর চেয়ে কম পাওয়া যায়

### 🔁 Revision Box
**Nyquist (noiseless): C = 2B log₂L** · **Shannon (noisy): C = B log₂(1 + S/N)** · **SNR(dB) = 10 log₁₀(S/N)**।

---
---

# 6️⃣ LINE CODING ও MODULATION ⭐⭐

## Line Coding (Digital → Digital)

| পদ্ধতি | কীভাবে |
|---|---|
| **NRZ** (Non-Return to Zero) | 1 = উঁচু, 0 = নিচু · সমস্যা: **synchronization হারায়** |
| **NRZ-I** | **1 এলে voltage উল্টায়**, 0 হলে একই থাকে |
| **Manchester** ⭐ | প্রতি bit-এর **মাঝখানে transition** · 1 = নিচু→উঁচু, 0 = উঁচু→নিচু |
| **Differential Manchester** | মাঝে সবসময় transition · **0 হলে শুরুতেও** transition |
| **Bipolar/AMI** | 0 = শূন্য voltage, 1 = পালাক্রমে +/− |

⭐ **Manchester-এর সুবিধা:** প্রতি bit-এ transition থাকায় **clock নিজেই বেরিয়ে আসে** (self-synchronizing)
⚠️ **অসুবিধা:** দ্বিগুণ bandwidth লাগে

## Modulation (Digital → Analog) ⭐

| পদ্ধতি | কী বদলায় |
|---|---|
| **ASK** (Amplitude Shift Keying) | **বিস্তার** (amplitude) |
| **FSK** (Frequency Shift Keying) | **কম্পাঙ্ক** (frequency) |
| **PSK** (Phase Shift Keying) | **দশা** (phase) |
| **QAM** | **বিস্তার + দশা একসাথে** ⭐ সবচেয়ে দক্ষ |

**Analog → Digital:** **PCM** (Pulse Code Modulation) — Sampling → Quantization → Encoding
⭐ **Sampling Theorem:** sampling rate ≥ **2 × সর্বোচ্চ frequency**

### 🔁 Revision Box
**NRZ** = সহজ কিন্তু sync হারায় · **Manchester** = মাঝে transition, **self-synchronizing**, দ্বিগুণ bandwidth। Modulation: **ASK (amplitude) · FSK (frequency) · PSK (phase) · QAM (দুটোই, সবচেয়ে দক্ষ)**। **PCM** = analog→digital (Sample→Quantize→Encode), rate ≥ **2 × f max**।

---
---

# 7️⃣ বাকি টুকিটাকি 🔵

## Framing (Data Link)
| পদ্ধতি | কীভাবে |
|---|---|
| Character count | শুরুতে দৈর্ঘ্য লিখে দেওয়া |
| **Byte stuffing** | Flag byte-এর আগে escape byte বসানো |
| **Bit stuffing** | পরপর পাঁচটা 1-এর পর একটা 0 ঢোকানো ⭐ |

## WAN Protocols
| | |
|---|---|
| **PPP** | Point-to-Point Protocol · authentication (PAP/CHAP) সহ |
| **HDLC** | Cisco-র default WAN encapsulation |
| **Frame Relay** | Packet-switched WAN, **DLCI** দিয়ে চিহ্নিত |
| **ISDN** | Digital telephone network (B ও D channel) |
| **MPLS** | Label দিয়ে দ্রুত forwarding |

## Network Security
| | |
|---|---|
| **Firewall** | নিয়ম অনুযায়ী traffic ছাঁকে |
| **VPN** | Public network-এ encrypted tunnel |
| **IPsec** | Network layer-এ নিরাপত্তা (IPv6-এ অন্তর্নির্মিত) |
| **SSL/TLS** | Transport/Presentation layer-এ (HTTPS) |
| **Symmetric** | একই key (AES, DES) · দ্রুত |
| **Asymmetric** | Public + Private key (RSA) · ধীর কিন্তু নিরাপদ |
| আক্রমণ | DoS/DDoS · Man-in-the-Middle · Phishing · Spoofing |

## Network Management
**SNMP** (Simple Network Management Protocol) — device পর্যবেক্ষণ
**ping** (ICMP echo) · **traceroute** (পথ দেখা) · **ipconfig/ifconfig** · **netstat**

---
---

# ★ SUPPLEMENT REVISION — ২০টা তথ্য

1. **CSMA/CD = তারযুক্ত** (collision ধরে) · **CSMA/CA = বেতার** (এড়ায়)
2. বেতারে CD চলে না — **Hidden Terminal Problem**
3. CSMA/CA ব্যবহার করে **RTS/CTS/ACK**
4. **ALOHA 18%, Slotted ALOHA 37%**
5. **RIP = Distance Vector = Bellman-Ford**, সর্বোচ্চ **15 hop**
6. **OSPF = Link State = Dijkstra**, cost metric
7. **BGP = Internet-এর routing (EGP)**, বাকিরা IGP
8. **RIP v1 classful — VLSM চলে না**; v2/OSPF/EIGRP classless
9. **Flow control = receiver বাঁচায়** · **Congestion control = network বাঁচায়**
10. **Go-Back-N = সব আবার** · **Selective Repeat = শুধু ভুলটা**
11. TCP: **Slow Start → Congestion Avoidance**, **AIMD**
12. **VLAN = আলাদা broadcast domain**, tagging **802.1Q**
13. **VLAN-এর মধ্যে কথা বলতে Router লাগে**
14. **STP (802.1D)** = switch loop ও **Broadcast Storm** ঠেকায়
15. STP-তে **Root Bridge** নির্বাচন হয়
16. **Nyquist: C = 2B log₂L** (noiseless)
17. **Shannon: C = B log₂(1 + S/N)** (noisy)
18. **SNR(dB) = 10 log₁₀(S/N)**
19. **Manchester = self-synchronizing**, দ্বিগুণ bandwidth
20. **ASK amplitude · FSK frequency · PSK phase · QAM দুটোই**

---

> **এটা কি অবশ্যই পড়তে হবে?**
> Sample paper-এর ৪টা প্রশ্ন মূল ফাইলেই কভার হয়েছে। এই supplement **বীমা** — অন্য প্রশ্ন এলে যেন খালি না যায়।
> **সময় কম থাকলে শুধু ১, ২, ৩ নম্বর module** (CSMA · Routing Protocol · Flow/Congestion) — এই তিনটাই সবচেয়ে বেশি আসে।
