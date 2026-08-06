# 🌐 NETWORKING — সম্পূর্ণ নোট
### CSE 320 / 421 / 490 — BRAC MSc CSE Admission

> **এই এক file-ই যথেষ্ট।** প্রতিটা হিসাবের **ধাপ + dry run** আছে — process মনে না থাকলেও এখান থেকে করতে পারবে।
> **Sample paper-এ ৪টা প্রশ্ন এখান থেকে** (Q1 IPv6, Q2 802.11b, Q3 OSI/TCP-IP, Q4 VLSM/CIDR) — সবচেয়ে বেশি নম্বরের বিষয়।

---

## 📑 সূচি

| Module | বিষয় | Dry Run আছে? |
|---|---|---|
| 1 | Network Basics · LAN/MAN/WAN · Topology | — |
| 2 | **OSI & TCP/IP Model** ⭐ | ✅ |
| 3 | Transmission · Media · Multiplexing | — |
| 4 | **Error Detection (Parity, Checksum, CRC)** | ✅ CRC |
| 5 | **IP Addressing · Binary Conversion** ⭐ | ✅ |
| 6 | **SUBNETTING** ⭐⭐⭐ | ✅ ৪টা |
| 7 | **CIDR & VLSM** ⭐⭐⭐ | ✅ |
| 8 | **IPv6** ⭐ | ✅ |
| 9 | **TCP/UDP · Handshake · Ports** | ✅ |
| 10 | Devices · Protocols (DNS, DHCP, NAT) | — |
| 11 | **Wireless (802.11)** ⭐ | — |
| 12 | Final Revision + MCQ Traps | — |

---
---

# MODULE 1 — NETWORK BASICS

## Topic 1: Computer Network

### Definition (English)
A **Computer Network** is a collection of **interconnected devices** that can **share data and resources** using communication protocols.

⭐ **Keywords:** Interconnected · Share Data · Protocol

### Concept (বাংলায়)
দুই বা তার বেশি device তার/বেতার দিয়ে যুক্ত হয়ে data আদান-প্রদান করলেই সেটা network।
**সুবিধা:** Resource sharing (printer, file) · Communication · Centralized data · খরচ কম

## Topic 2: Network Types ⭐

| Type | পূর্ণরূপ | পরিসর | উদাহরণ |
|---|---|---|---|
| **PAN** | Personal Area Network | ~10 m | Bluetooth, hotspot |
| **LAN** | Local Area Network | একটা building/campus | অফিস, ল্যাব |
| **MAN** | Metropolitan Area Network | একটা শহর | Cable TV, city Wi-Fi |
| **WAN** | Wide Area Network | দেশ/বিশ্ব | **Internet** ⭐ |

**LAN vs WAN:**
| | LAN | WAN |
|---|---|---|
| পরিসর | ছোট | **বিশাল** |
| গতি | **বেশি** (1 Gbps+) | কম |
| খরচ | কম | বেশি |
| Error rate | কম | **বেশি** |
| মালিকানা | ব্যক্তিগত | সাধারণত সরকারি/ISP |

## Topic 3: Topology ⭐

| Topology | গঠন | সুবিধা | অসুবিধা |
|---|---|---|---|
| **Bus** | একটা মূল তারে সব যুক্ত | সস্তা, সহজ | মূল তার ছিঁড়লে **পুরো network বন্ধ** |
| **Star** | সবাই একটা **hub/switch**-এ যুক্ত | সহজ ব্যবস্থাপনা, একটা নষ্ট হলে বাকিরা ঠিক | **Hub নষ্ট হলে সব বন্ধ** |
| **Ring** | বৃত্তাকার, data এক দিকে ঘোরে | সংঘর্ষ নেই | একটা node নষ্ট হলে সমস্যা |
| **Mesh** | প্রত্যেকে প্রত্যেকের সাথে | সবচেয়ে **নির্ভরযোগ্য** | **খুব ব্যয়বহুল** |
| **Hybrid** | মিশ্রণ | নমনীয় | জটিল |

**Formula ⭐:** Full Mesh-এ n নোডের জন্য **link সংখ্যা = n(n − 1) / 2**
*উদাহরণ:* 5 নোড → 5×4/2 = **10 link**

⭐ **বাস্তবে সবচেয়ে বেশি ব্যবহৃত = Star** (আধুনিক Ethernet LAN)

### 🔁 Revision Box
Network = interconnected device + data sharing। **PAN < LAN < MAN < WAN**; Internet = WAN। Topology: **Bus** (এক তার), **Star** (hub-কেন্দ্রিক, সবচেয়ে প্রচলিত), **Ring** (বৃত্ত), **Mesh** (সবার সাথে সবাই, link = **n(n−1)/2**)।

---
---

# MODULE 2 — OSI & TCP/IP MODEL ⭐⭐⭐

> **Sample paper Q3 এখান থেকে।** এই module-টা মুখস্থ করতেই হবে।

## Topic 1: OSI Model

### Definition (English)
The **OSI (Open Systems Interconnection)** model is a **7-layer** conceptual framework developed by **ISO** that standardizes how data moves through a network.

⭐ **Keywords:** 7 Layers · ISO · Conceptual/Reference model

### ৭টি Layer ⭐⭐⭐ (উপর থেকে নিচে)

| # | Layer | কাজ | **PDU** | উদাহরণ |
|---|---|---|---|---|
| **7** | **Application** | User-এর সাথে সরাসরি যোগাযোগ | Data | HTTP, FTP, SMTP, DNS |
| **6** | **Presentation** | **Encryption, Compression, Translation** | Data | SSL/TLS, JPEG, ASCII |
| **5** | **Session** | Session তৈরি, রক্ষণ, সমাপ্তি | Data | NetBIOS, RPC |
| **4** | **Transport** | **End-to-end delivery, নির্ভরযোগ্যতা** | **Segment** | **TCP, UDP** |
| **3** | **Network** | **Routing, Logical addressing (IP)** | **Packet** | **IP, ICMP**, Router |
| **2** | **Data Link** | **Framing, MAC address, Error detection** | **Frame** | Ethernet, Switch |
| **1** | **Physical** | Bit → বৈদ্যুতিক/আলোক সংকেত | **Bit** | Cable, Hub, Repeater |

### মুখস্থ করার Mnemonic ⭐
**উপর → নিচ (7→1):**
> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
> (Application, Presentation, Session, Transport, Network, Data Link, Physical)

**নিচ → উপর (1→7):**
> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

### PDU মনে রাখার ছড়া ⭐
> **Data → Segment → Packet → Frame → Bit**
> (উপর থেকে নিচে নামার সময় নাম বদলায়)

## Topic 2: TCP/IP Model

### Definition (English)
The **TCP/IP model** is a **4-layer** practical model that forms the foundation of the **Internet**.

### ৪টি Layer ⭐

| # | TCP/IP Layer | OSI-এর কোন layer মেলে |
|---|---|---|
| **4** | **Application** | Application + Presentation + Session (7,6,5) |
| **3** | **Transport** | Transport (4) |
| **2** | **Internet** | Network (3) |
| **1** | **Network Access / Link** | Data Link + Physical (2,1) |

⚠️ কিছু বইয়ে **5-layer TCP/IP** দেখানো হয় (Physical ও Data Link আলাদা করে)। প্রশ্নে সাধারণত **4** ধরাই নিরাপদ।

### OSI vs TCP/IP ⭐⭐⭐

| Feature | **OSI** | **TCP/IP** |
|---|---|---|
| Layer সংখ্যা | **7** | **4** |
| তৈরি | **ISO** | DARPA / US DoD |
| ধরন | **Theoretical / Reference** | **Practical / Implemented** |
| ব্যবহার | শেখার জন্য | **বাস্তব Internet** |
| Layer স্বাধীনতা | কড়াভাবে আলাদা | কিছু layer মিলিত |

### 🔍 DRY RUN — একটা Email পাঠালে কী হয়

তুমি Gmail-এ "Send" চাপলে —

```
📤 পাঠানোর সময় (উপর → নিচ, Encapsulation)

Layer 7 Application   : Email text তৈরি (SMTP protocol)          → Data
Layer 6 Presentation  : Encrypt + compress করা                    → Data
Layer 5 Session       : Server-এর সাথে session খোলা               → Data
Layer 4 Transport     : Data-কে টুকরো করে port নম্বর যোগ (TCP)    → Segment
Layer 3 Network       : Source ও Destination IP যোগ               → Packet
Layer 2 Data Link     : MAC address যোগ + error check (FCS)       → Frame
Layer 1 Physical      : বৈদ্যুতিক/আলোক সংকেতে রূপান্তর            → Bit

        ~~~~~~ তার/বেতার দিয়ে যাত্রা ~~~~~~

📥 পাওয়ার সময় (নিচ → উপর, Decapsulation)
Layer 1 → 7 : প্রতিটি layer নিজের header খুলে উপরে পাঠায়
              শেষে receiver email পড়ে
```

⭐ প্রতিটি layer নিজের **header যোগ করে** — এটাকে বলে **Encapsulation**। উল্টোটা **Decapsulation**।

### ⚠️ Common MCQ Traps
- **Encryption হয় Presentation layer-এ** (Application-এ নয়) ⭐
- **Routing হয় Network layer-এ**; **Switching হয় Data Link-এ**
- **Router = Layer 3**, **Switch = Layer 2**, **Hub = Layer 1** ⭐⭐⭐
- **TCP/UDP = Transport (Layer 4)**, **IP = Network (Layer 3)**
- **MAC address = Layer 2**, **IP address = Layer 3**

### 🔁 Revision Box
**OSI = 7 layer (ISO, theoretical)**, **TCP/IP = 4 layer (practical, Internet)**। উপর→নিচ: **A**pplication, **P**resentation, **S**ession, **T**ransport, **N**etwork, **D**ata Link, **P**hysical। PDU: **Data → Segment → Packet → Frame → Bit**। **Hub=L1, Switch=L2, Router=L3**। Encryption = **Presentation**।

---
---

# MODULE 3 — TRANSMISSION & MEDIA

## Topic 1: Transmission Mode ⭐

| Mode | দিক | উদাহরণ |
|---|---|---|
| **Simplex** | এক দিকে **শুধু** | Keyboard, Monitor, TV সম্প্রচার |
| **Half-Duplex** | দুই দিকে, কিন্তু **একসাথে নয়** | **Walkie-talkie** |
| **Full-Duplex** | দুই দিকে **একসাথে** | **টেলিফোন**, আধুনিক Ethernet |

## Topic 2: Transmission Media ⭐

### Guided (তারযুক্ত)
| Media | গতি | বৈশিষ্ট্য |
|---|---|---|
| **Twisted Pair** (UTP/STP) | ~1 Gbps | সবচেয়ে সস্তা ও প্রচলিত (Cat5e, Cat6) |
| **Coaxial Cable** | ~10-100 Mbps | Cable TV, twisted pair-এর চেয়ে ভালো shield |
| **Optical Fiber** | **Tbps** | **সবচেয়ে দ্রুত**, আলো ব্যবহার করে, **EMI-মুক্ত**, ব্যয়বহুল ⭐ |

### Unguided (বেতার)
Radio wave · Microwave · Infrared · Satellite

⭐ **MCQ:** সবচেয়ে **দ্রুত ও নিরাপদ** media = **Optical Fiber** (তড়িৎচুম্বকীয় হস্তক্ষেপ হয় না, tap করা কঠিন)

## Topic 3: Bandwidth, Throughput, Latency ⭐

| Term | অর্থ | উপমা |
|---|---|---|
| **Bandwidth** | তাত্ত্বিক **সর্বোচ্চ** ধারণক্ষমতা | রাস্তার প্রশস্ততা |
| **Throughput** | **বাস্তবে** যতটা পাওয়া যায় | আসলে কত গাড়ি গেল |
| **Latency** | এক প্রান্ত থেকে অন্য প্রান্তে যেতে **সময়** | যাত্রার সময় |
| **Jitter** | Latency-র **ওঠানামা** | সময়ের অনিয়ম |

⚠️ **Throughput সবসময় Bandwidth-এর চেয়ে কম বা সমান।**

## Topic 4: Multiplexing ⭐

**Definition:** Combining multiple signals over a **single shared medium**.

| Type | কীভাবে ভাগ করে |
|---|---|
| **FDM** (Frequency Division) | ভিন্ন **frequency** — যেমন FM রেডিও |
| **TDM** (Time Division) | ভিন্ন **সময়ের ভাগ (time slot)** |
| **WDM** (Wavelength Division) | ভিন্ন **আলোর তরঙ্গদৈর্ঘ্য** — Optical fiber-এ |
| **CDM** (Code Division) | ভিন্ন **code** — মোবাইল নেটওয়ার্কে |

## Topic 5: Switching ⭐

| Type | কীভাবে |
|---|---|
| **Circuit Switching** | আগে একটা **নির্দিষ্ট পথ** ঠিক করে, তারপর data যায় — টেলিফোন |
| **Packet Switching** | Data টুকরো করে, প্রতিটা টুকরো **আলাদা পথে** যেতে পারে — **Internet** ⭐ |
| **Message Switching** | পুরো message store করে তারপর forward |

### 🔁 Revision Box
**Simplex** (এক দিকে) · **Half-duplex** (walkie-talkie) · **Full-duplex** (টেলিফোন)। Media: Twisted Pair (সস্তা) < Coaxial < **Optical Fiber (দ্রুততম, EMI-মুক্ত)**। **Bandwidth = তাত্ত্বিক, Throughput = বাস্তব**। Multiplexing: **FDM (frequency), TDM (time), WDM (wavelength)**। **Internet = Packet Switching**।

---
---

# MODULE 4 — ERROR DETECTION ⭐

## Topic 1: তিন পদ্ধতি

| পদ্ধতি | কীভাবে | শক্তি |
|---|---|---|
| **Parity Bit** | 1-এর সংখ্যা জোড়/বিজোড় করতে একটা bit যোগ | দুর্বল (২টা ভুল ধরতে পারে না) |
| **Checksum** | সব অংশ যোগ করে complement পাঠানো | মাঝারি |
| **CRC** (Cyclic Redundancy Check) | Binary division-এর remainder পাঠানো | **সবচেয়ে শক্তিশালী** ⭐ |

## 🔍 DRY RUN — Even Parity

Data = `1011001` → 1-এর সংখ্যা = **4** (জোড়)
Even parity মানে মোট 1 জোড় থাকতে হবে → ইতিমধ্যেই জোড় → **parity bit = 0**
পাঠানো হবে: `10110010`

Data = `1011000` → 1-এর সংখ্যা = **3** (বিজোড়)
জোড় করতে **parity bit = 1** → পাঠানো হবে: `10110001`

## 🔍 DRY RUN — CRC ⭐⭐

**Data = `1101`, Divisor (generator) = `1011`**

### Steps
1. Divisor-এর দৈর্ঘ্য = 4 → শেষে **(4−1) = 3টা শূন্য** যোগ করো
2. **XOR division** চালাও (বিয়োগ নয়, XOR)
3. যে **remainder** থাকে সেটাই **CRC**
4. মূল data + CRC পাঠাও

```
Data + 3 zeros = 1101000
Divisor        = 1011

  1101000
  1011↓↓↓        ← XOR
  -------
  0110000
   1100          ← পরের bit নামালাম
   1011          ← XOR
   ----
   0111
   1110          ← পরের bit নামালাম
   1011          ← XOR
   ----
   0101
   1010          ← পরের bit নামালাম
   1011          ← XOR
   ----
   0001

Remainder (CRC) = 001
পাঠানো হবে: 1101 + 001 = 1101001
```

### Receiver যাচাই করবে
পাওয়া `1101001` কে একই divisor `1011` দিয়ে ভাগ করবে →
**Remainder = 000** হলে **কোনো ভুল নেই** ✅
Remainder ≠ 0 হলে **ভুল আছে** ❌

### 🔁 Revision Box
**Parity** = 1-এর সংখ্যা জোড়/বিজোড় করা, দুর্বল। **Checksum** = যোগফলের complement। **CRC** = binary XOR division-এর remainder, **সবচেয়ে শক্তিশালী**। CRC-তে divisor-এর দৈর্ঘ্য n হলে **n−1টা শূন্য** যোগ করতে হয়। Receiver-এ remainder **0 = ঠিক আছে**।

---
---

# MODULE 5 — IP ADDRESSING ⭐⭐⭐

## Topic 1: IPv4

### Definition (English)
An **IPv4 address** is a **32-bit** logical address written as **four decimal octets** separated by dots (dotted-decimal notation).

⭐ **Keywords:** 32 bit · 4 octet · Dotted decimal · Layer 3

### গঠন
```
192  .  168  .   1   .   10
 ↓       ↓       ↓       ↓
8 bit  8 bit   8 bit   8 bit   =  32 bit
```
প্রতিটি octet-এর মান **0 থেকে 255** (কারণ 2⁸ = 256টি সম্ভাবনা)

**মোট ঠিকানা = 2³² ≈ 4.3 বিলিয়ন**

## 🔍 DRY RUN — Decimal → Binary ⭐⭐

**নিয়ম:** প্রতিটি octet-এর জন্য এই মানগুলো মনে রাখো:
```
128  64  32  16  8  4  2  1
```
বাম থেকে শুরু করে যেটা বসে সেখানে **1**, না বসলে **0**।

**উদাহরণ: 192 → binary**
```
128  64  32  16  8  4  2  1
 ?   ?   ?   ?   ?  ?  ?  ?

128 ≤ 192 ✅ → 1, বাকি 192−128 = 64
 64 ≤ 64  ✅ → 1, বাকি 64−64 = 0
বাকি সব 0

ফলাফল: 1 1 0 0 0 0 0 0  →  11000000 ✅
```

**উদাহরণ: 168 → binary**
```
128 ≤ 168 ✅ → 1, বাকি 40
 64 > 40  ❌ → 0
 32 ≤ 40  ✅ → 1, বাকি 8
 16 > 8   ❌ → 0
  8 ≤ 8   ✅ → 1, বাকি 0
বাকি সব 0

ফলাফল: 10101000 ✅
```

**পুরো IP: 192.168.1.10**
```
192 → 11000000
168 → 10101000
  1 → 00000001
 10 → 00001010

192.168.1.10 = 11000000.10101000.00000001.00001010
```

## 🔍 DRY RUN — Binary → Decimal

`11000000` → কোথায় কোথায় 1 আছে, সেগুলো যোগ করো
```
128  64  32  16  8  4  2  1
 1   1   0   0   0  0  0  0

128 + 64 = 192 ✅
```

`11111111` → 128+64+32+16+8+4+2+1 = **255** (সর্বোচ্চ)

## Topic 2: IP Address Classes ⭐⭐⭐

| Class | প্রথম octet | Default Mask | CIDR | Network/Host bit | ব্যবহার |
|---|---|---|---|---|---|
| **A** | **1 – 126** | 255.0.0.0 | **/8** | 8 / 24 | বিশাল network |
| **B** | **128 – 191** | 255.255.0.0 | **/16** | 16 / 16 | মাঝারি |
| **C** | **192 – 223** | 255.255.255.0 | **/24** | 24 / 8 | ছোট (LAN) |
| **D** | **224 – 239** | — | — | — | **Multicast** |
| **E** | **240 – 255** | — | — | — | **Experimental** |

### ⚠️ বিশেষ ঠিকানা (MCQ favourite)
| ঠিকানা | অর্থ |
|---|---|
| **127.0.0.0 – 127.255.255.255** | **Loopback** (127.0.0.1 = localhost) ⭐ |
| **0.0.0.0** | এই network / অনির্দিষ্ট |
| **255.255.255.255** | **Limited broadcast** |
| **169.254.x.x** | APIPA (DHCP ব্যর্থ হলে নিজে নেয়) |

⚠️ **Class A-তে 127 নেই** কারণ ওটা loopback-এর জন্য সংরক্ষিত — এজন্যই range 1–126, 1–127 নয় ⭐

## Topic 3: Private IP Ranges ⭐⭐

| Class | Range | CIDR |
|---|---|---|
| **A** | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| **B** | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| **C** | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

⭐ Private IP **Internet-এ সরাসরি চলে না** — **NAT** দিয়ে public IP-তে রূপান্তর করতে হয়।
তোমার বাসার Wi-Fi router প্রায় নিশ্চিতভাবে **192.168.x.x** দেয়।

## Topic 4: MAC vs IP Address ⭐

| | **MAC Address** | **IP Address** |
|---|---|---|
| Layer | **2 (Data Link)** | **3 (Network)** |
| আকার | **48 bit** (6 জোড়া hex) | 32 bit (IPv4) |
| উদাহরণ | `00:1A:2B:3C:4D:5E` | `192.168.1.10` |
| ধরন | **Physical**, স্থায়ী (NIC-এ পোড়ানো) | **Logical**, পরিবর্তনযোগ্য |
| পরিসর | শুধু local network-এ | পুরো Internet-এ |
| কে দেয় | প্রস্তুতকারক | ISP / Admin |

⭐ **ARP** = IP → MAC বের করে · **RARP** = MAC → IP

### 🔁 Revision Box
**IPv4 = 32 bit, 4 octet (0–255)**, মোট ~4.3 বিলিয়ন। Class **A (1–126, /8)**, **B (128–191, /16)**, **C (192–223, /24)**, **D multicast**, **E experimental**। **127 = loopback**। Private: **10.x, 172.16–31.x, 192.168.x**। **MAC = 48 bit, Layer 2, স্থায়ী**; **IP = 32 bit, Layer 3, পরিবর্তনযোগ্য**। **ARP: IP → MAC**।

---
---

# MODULE 6 — SUBNETTING ⭐⭐⭐

> **সবচেয়ে গুরুত্বপূর্ণ module।** এখানে ৪টা dry run আছে — প্রতিটা নিজে হাতে করো।

## Topic 1: মূল ধারণা

### Definition (English)
**Subnetting** is the process of dividing a large network into **smaller logical sub-networks** by borrowing bits from the **host portion**.

### কেন দরকার? (বাংলায়)
একটা Class C network-এ 254টা host। কিন্তু তোমার ৪টা বিভাগে ৫০ জন করে দরকার।
পুরোটা একসাথে রাখলে —
- **Broadcast traffic** সবার কাছে যাবে (network ধীর হবে)
- **নিরাপত্তা** থাকবে না (HR-এর data Sales দেখতে পাবে)
- IP **অপচয়** হবে

Subnetting করলে প্রতিটা বিভাগ আলাদা network পাবে।

## Topic 2: আবশ্যিক সূত্র ⭐⭐⭐

```
Host bit = n  →  ব্যবহারযোগ্য host সংখ্যা = 2ⁿ − 2
Borrow করা bit = m  →  Subnet সংখ্যা = 2ᵐ
Block Size = 256 − (mask-এর ঐ octet)
```

⚠️ **−2 কেন?** প্রতিটি subnet-এ দুটো ঠিকানা ব্যবহার করা যায় না:
- **প্রথমটা = Network address** (subnet-এর পরিচয়)
- **শেষটা = Broadcast address** (সবার কাছে পাঠানোর জন্য)

## Topic 3: Subnet Mask Cheat Sheet ⭐⭐⭐ (মুখস্থ করে ফেলো)

| CIDR | Subnet Mask | Block Size | Host bit | ব্যবহারযোগ্য Host |
|---|---|---|---|---|
| **/24** | 255.255.255.**0** | 256 | 8 | **254** |
| **/25** | 255.255.255.**128** | 128 | 7 | **126** |
| **/26** | 255.255.255.**192** | 64 | 6 | **62** |
| **/27** | 255.255.255.**224** | 32 | 5 | **30** |
| **/28** | 255.255.255.**240** | 16 | 4 | **14** |
| **/29** | 255.255.255.**248** | 8 | 3 | **6** |
| **/30** | 255.255.255.**252** | 4 | 2 | **2** |
| /31 | 255.255.255.254 | 2 | 1 | 0 (point-to-point) |
| /32 | 255.255.255.255 | 1 | 0 | 1 (একক host) |

⭐ **Block Size = 256 − mask octet** — এটাই সবচেয়ে কাজের shortcut
*যেমন /26 → mask 192 → block = 256 − 192 = **64***

---

## 🔍 DRY RUN 1 — Network ও Broadcast Address বের করা ⭐⭐⭐

**প্রশ্ন:** IP = `192.168.1.100`, Mask = `255.255.255.192` (/26)
Network address, Broadcast address ও Host range বের করো।

### পদ্ধতি ১: Binary AND (নিখুঁত পদ্ধতি)

```
ধাপ 1: শেষ octet binary-তে লেখো
  IP-র শেষ octet   100 = 01100100
  Mask-এর শেষ octet 192 = 11000000

ধাপ 2: AND operation (দুটোই 1 হলে 1, নাহলে 0)
  01100100
  11000000
  --------  AND
  01000000  =  64

ধাপ 3: Network Address = 192.168.1.64  ✅
```

### পদ্ধতি ২: Block Size (দ্রুত পদ্ধতি) ⭐

```
ধাপ 1: Block size = 256 − 192 = 64

ধাপ 2: 64-এর গুণিতক লেখো
  0, 64, 128, 192, (256)

ধাপ 3: 100 কোন দুই গুণিতকের মাঝে?
  64 ≤ 100 < 128
  → Network Address = 192.168.1.64  ✅

ধাপ 4: Broadcast = পরের block-এর ঠিক আগেরটা
  → 128 − 1 = 127
  → Broadcast Address = 192.168.1.127  ✅

ধাপ 5: Host range = Network+1 থেকে Broadcast−1
  → 192.168.1.65 থেকে 192.168.1.126  ✅
```

### ✅ চূড়ান্ত উত্তর
| | ঠিকানা |
|---|---|
| **Network Address** | 192.168.1.**64** |
| **First usable host** | 192.168.1.**65** |
| **Last usable host** | 192.168.1.**126** |
| **Broadcast Address** | 192.168.1.**127** |
| **মোট usable host** | 2⁶ − 2 = **62** |

---

## 🔍 DRY RUN 2 — একটা Network-কে ৪ ভাগ করা ⭐⭐⭐

**প্রশ্ন:** `192.168.1.0/24` কে **৪টি সমান subnet**-এ ভাগ করো।

```
ধাপ 1: কত bit ধার নিতে হবে?
  Subnet সংখ্যা = 2ᵐ ≥ 4
  2² = 4 ✅  →  m = 2 bit ধার নিতে হবে

ধাপ 2: নতুন CIDR
  /24 + 2 = /26
  Subnet Mask = 255.255.255.192

ধাপ 3: Block size = 256 − 192 = 64

ধাপ 4: প্রতিটি subnet-এ host = 2⁶ − 2 = 62

ধাপ 5: Subnet গুলো লেখো (64 করে বাড়াও)
```

| Subnet | Network | First Host | Last Host | Broadcast |
|---|---|---|---|---|
| **1** | 192.168.1.**0** | .1 | .62 | .**63** |
| **2** | 192.168.1.**64** | .65 | .126 | .**127** |
| **3** | 192.168.1.**128** | .129 | .190 | .**191** |
| **4** | 192.168.1.**192** | .193 | .254 | .**255** |

**যাচাই:** 4 subnet × 62 host = 248 usable + 8টা (network/broadcast) = 256 ✅

---

## 🔍 DRY RUN 3 — প্রয়োজন থেকে Mask বের করা ⭐⭐

**প্রশ্ন:** প্রতিটি subnet-এ **অন্তত ৩০টি host** দরকার। কোন mask নেবে?

```
ধাপ 1: 2ⁿ − 2 ≥ 30 হতে হবে
  n=4 → 2⁴−2 = 14  ❌ (কম পড়ে)
  n=5 → 2⁵−2 = 30  ✅ (ঠিক ঠিক হয়)

ধাপ 2: Host bit = 5, তাই Network bit = 32 − 5 = 27
  → CIDR = /27

ধাপ 3: Mask
  /27 মানে প্রথম 27টা bit 1:
  11111111.11111111.11111111.11100000
  শেষ octet: 128+64+32 = 224
  → Subnet Mask = 255.255.255.224  ✅

ধাপ 4: Block size = 256 − 224 = 32
  → Subnet: .0, .32, .64, .96, .128, .160, .192, .224  (মোট 8টা)
```

**উত্তর: /27, mask 255.255.255.224, প্রতি subnet-এ 30 host, মোট 8টা subnet**

---

## 🔍 DRY RUN 4 — একটা IP কোন subnet-এ আছে?

**প্রশ্ন:** `172.16.45.200/28` — Network address কী?

```
ধাপ 1: /28 → mask 255.255.255.240
ধাপ 2: Block size = 256 − 240 = 16
ধাপ 3: 16-এর গুণিতক: 0,16,32,...,192, 208, 224...
        200 কোথায়? →  192 ≤ 200 < 208
ধাপ 4: Network = 172.16.45.192
       Broadcast = 208 − 1 = 172.16.45.207
       Host range = .193 থেকে .206  (মোট 14টা = 2⁴−2) ✅
```

### 🔁 Revision Box
**Host = 2ⁿ − 2**, **Subnet = 2ᵐ**, **Block size = 256 − mask octet**। Network address = block-এর শুরু, Broadcast = পরের block-এর ঠিক আগে। মুখস্থ: **/26=192=64 block=62 host**, **/27=224=32 block=30 host**, **/28=240=16 block=14 host**, **/30=252=4 block=2 host**।

---
---

# MODULE 7 — CIDR & VLSM ⭐⭐⭐

> **Sample paper Q4 এখান থেকে।**

## Topic 1: CIDR

### Definition (English)
**CIDR (Classless Inter-Domain Routing)** is an IP addressing method that **eliminates rigid class boundaries**, allowing subnet masks of any length, written as a **slash notation** (e.g. /26).

⭐ **Keywords:** Classless · Slash notation · Route Aggregation

### কেন এসেছে? (বাংলায়)
পুরনো **Classful** পদ্ধতিতে শুধু /8, /16, /24 — তিনটাই বিকল্প ছিল।

সমস্যা: তোমার ৩০০টা host দরকার।
- Class C (254) → **কম পড়ে** ❌
- Class B (65,534) → **65,000+ IP অপচয়** ❌

**CIDR এই সমস্যার সমাধান** — /23 নিলে 510টা host, ঠিক ঠিক মিলে যায় ✅

### CIDR-এর দুই সুবিধা
1. **IP অপচয় কমে** — প্রয়োজনমতো আকার নেওয়া যায়
2. **Route Aggregation / Supernetting** — অনেক ছোট network একটা entry-তে মিলিয়ে routing table ছোট রাখা ⭐

### 🔍 DRY RUN — Route Aggregation
```
চারটা আলাদা network:
  192.168.0.0/24
  192.168.1.0/24
  192.168.2.0/24
  192.168.3.0/24

Router-এ ৪টা আলাদা entry রাখার বদলে —
একসাথে লেখা যায়:  192.168.0.0/22   ✅

কারণ: /24 থেকে 2 bit কমালে (/22) 4টা network কভার হয় (2² = 4)
```

## Topic 2: VLSM ⭐⭐⭐

### Definition (English)
**VLSM (Variable Length Subnet Mask)** allows subnets of **different sizes** within the same network, assigning each subnet only as many addresses as it actually needs.

⭐ **Keywords:** Variable size · Efficient utilization · Subnet of a subnet

### কেন দরকার? (বাংলায়)
সাধারণ subnetting-এ সব subnet **সমান আকারের** হয়।

কিন্তু বাস্তবে —
- Sales বিভাগে **৫০ জন**
- HR বিভাগে **২৫ জন**
- IT বিভাগে **১০ জন**
- দুই router-এর মাঝের link-এ **২টা** IP

সবাইকে ৬২টা করে দিলে বিশাল অপচয়। **VLSM প্রত্যেককে ঠিক যতটা দরকার ততটাই দেয়।** ⭐

### VLSM-এর সোনালি নিয়ম ⭐
> **সবচেয়ে বড় চাহিদা আগে, সবচেয়ে ছোট শেষে।**
> (বড় থেকে ছোট ক্রমে বরাদ্দ করো — নাহলে জায়গা টুকরো হয়ে যাবে)

---

## 🔍 DRY RUN — সম্পূর্ণ VLSM Design ⭐⭐⭐

**প্রশ্ন:** `192.168.1.0/24` থেকে নিচের চাহিদা মেটাও —

| বিভাগ | প্রয়োজনীয় Host |
|---|---|
| Sales | 50 |
| HR | 25 |
| IT | 10 |
| Router link | 2 |

### ধাপ 1: বড় থেকে ছোট সাজাও
`50 → 25 → 10 → 2` ✅ (ইতিমধ্যেই সাজানো)

### ধাপ 2: প্রতিটির জন্য mask বের করো
```
Sales (50):  2ⁿ−2 ≥ 50  →  2⁶−2 = 62 ✅  →  n=6  →  /26,  block 64
HR    (25):  2ⁿ−2 ≥ 25  →  2⁵−2 = 30 ✅  →  n=5  →  /27,  block 32
IT    (10):  2ⁿ−2 ≥ 10  →  2⁴−2 = 14 ✅  →  n=4  →  /28,  block 16
Link   (2):  2ⁿ−2 ≥ 2   →  2²−2 = 2  ✅  →  n=2  →  /30,  block 4
```

### ধাপ 3: ক্রমানুসারে বরাদ্দ করো

```
শুরু: 192.168.1.0

Sales /26  → block 64 → দখল করবে 0 থেকে 63
HR    /27  → block 32 → পরের খালি জায়গা 64 → দখল 64 থেকে 95
IT    /28  → block 16 → পরের খালি জায়গা 96 → দখল 96 থেকে 111
Link  /30  → block 4  → পরের খালি জায়গা 112 → দখল 112 থেকে 115
```

### ✅ চূড়ান্ত VLSM Table

| বিভাগ | Network | CIDR | Mask | Host Range | Broadcast | Host |
|---|---|---|---|---|---|---|
| **Sales** | 192.168.1.**0** | /26 | 255.255.255.192 | .1 – .62 | .63 | 62 |
| **HR** | 192.168.1.**64** | /27 | 255.255.255.224 | .65 – .94 | .95 | 30 |
| **IT** | 192.168.1.**96** | /28 | 255.255.255.240 | .97 – .110 | .111 | 14 |
| **Link** | 192.168.1.**112** | /30 | 255.255.255.252 | .113 – .114 | .115 | 2 |

**বাকি রইল:** 192.168.1.116 – 255 (ভবিষ্যতের জন্য) ✅

⭐ **তুলনা:** সাধারণ subnetting-এ সবাইকে /26 দিলে ৪টা subnet-এ পুরো ২৫৬ শেষ, কিছুই বাকি থাকত না। **VLSM-এ ১৪০টা ঠিকানা বেঁচে গেল।**

### CIDR vs VLSM ⭐

| | **CIDR** | **VLSM** |
|---|---|---|
| কী | Classless addressing পদ্ধতি | **এক network-এ ভিন্ন আকারের subnet** |
| উদ্দেশ্য | Class-এর সীমা ভাঙা, route aggregation | Subnet-এর ভিতরে আবার subnet, অপচয় রোধ |
| দিক | বাইরের দিকে (**Supernetting**) | ভিতরের দিকে (**Subnetting**) |
| সম্পর্ক | VLSM কাজ করতে **CIDR লাগে** | CIDR-এর একটা প্রয়োগ |

### 🔁 Revision Box
**CIDR** = Classless Inter-Domain Routing — class-এর সীমা নেই, **/notation**, **route aggregation** করে routing table ছোট রাখে। **VLSM** = Variable Length Subnet Mask — এক network-এ **ভিন্ন আকারের subnet**, প্রয়োজনমতো বরাদ্দ। নিয়ম: **বড় চাহিদা আগে, ছোট পরে**। VLSM চালাতে CIDR-সমর্থিত routing protocol (OSPF, EIGRP, RIPv2) লাগে।

---
---

# MODULE 8 — IPv6 ⭐⭐⭐

> **Sample paper Q1 এখান থেকে।**

## Topic 1: IPv6

### Definition (English)
**IPv6** is a **128-bit** IP addressing scheme written as **eight groups of four hexadecimal digits** separated by colons, developed to replace IPv4's limited address space.

⭐ **Keywords:** 128 bit · Hexadecimal · Colon-separated · 8 groups

### গঠন
```
2001 : 0db8 : 85a3 : 0000 : 0000 : 8a2e : 0370 : 7334
 ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓
16bit  16bit  16bit  16bit  16bit  16bit  16bit  16bit  = 128 bit
```
- **৮টি group**, প্রতিটিতে **৪টি hex digit**
- প্রতিটি group = **16 bit** (4 hex × 4 bit)
- মোট ঠিকানা = **2¹²⁸ ≈ 3.4 × 10³⁸**

### কেন IPv6?
IPv4-এর 4.3 বিলিয়ন ঠিকানা ফুরিয়ে গেছে (**IPv4 exhaustion**)। মোবাইল, IoT, smart device-এর সংখ্যা বিস্ফোরণের কারণে আরও অনেক ঠিকানা দরকার।

## 🔍 DRY RUN — IPv6 সংক্ষিপ্ত করা ⭐⭐⭐

### দুটো নিয়ম
1. প্রতিটি group-এর **শুরুর শূন্য (leading zeros) বাদ** দেওয়া যায়
2. **পরপর সব-শূন্য group** গুলোকে **`::`** দিয়ে বদলানো যায় — কিন্তু **পুরো ঠিকানায় মাত্র একবার** ⚠️

### উদাহরণ
```
মূল ঠিকানা:
2001:0db8:0000:0000:0000:ff00:0042:8329

ধাপ 1 — leading zero বাদ:
  0db8 → db8
  0000 → 0
  0042 → 42
  ফল: 2001:db8:0:0:0:ff00:42:8329

ধাপ 2 — পরপর শূন্য group গুলো :: দিয়ে বদলাও
  0:0:0  →  ::
  ফল: 2001:db8::ff00:42:8329   ✅ চূড়ান্ত
```

### আরেকটা
```
মূল:      0000:0000:0000:0000:0000:0000:0000:0001
সংক্ষেপ:  ::1        ←  IPv6-এর loopback (IPv4-এর 127.0.0.1-এর সমতুল্য) ⭐
```

### ⚠️ ভুল উদাহরণ (Trap)
```
2001:0:0:1:0:0:0:1

ভুল ❌:  2001::1::1        ← দুইবার :: ব্যবহার করা যাবে না!
সঠিক ✅: 2001:0:0:1::1     ← বড় শূন্য-অংশটায় :: বসাও
```

## Topic 2: IPv4 vs IPv6 ⭐⭐⭐

| Feature | **IPv4** | **IPv6** |
|---|---|---|
| **আকার** | **32 bit** | **128 bit** |
| **লেখা হয়** | Dotted **decimal** | Colon-separated **hexadecimal** |
| **অংশ** | 4 octet | **8 group** |
| **মোট ঠিকানা** | ~4.3 × 10⁹ | **~3.4 × 10³⁸** |
| Header | পরিবর্তনশীল (20–60 byte) | **স্থির 40 byte** (দ্রুত) |
| **Broadcast** | ✅ আছে | ❌ **নেই** (Multicast/Anycast আছে) ⭐ |
| Security (IPsec) | ঐচ্ছিক | **অন্তর্নির্মিত** |
| Configuration | Manual / DHCP | **Auto-configuration (SLAAC)** |
| Checksum (header-এ) | ✅ আছে | ❌ নেই |
| NAT | দরকার হয় | সাধারণত **দরকার নেই** |

⚠️ **সবচেয়ে বড় trap: IPv6-এ Broadcast নেই।** Unicast, Multicast, **Anycast** — এই তিনটা আছে।

## Topic 3: IPv6 Address Types
| Type | অর্থ |
|---|---|
| **Unicast** | একটি নির্দিষ্ট interface |
| **Multicast** | একদল interface (সবাই পাবে) |
| **Anycast** | একদলের **সবচেয়ে কাছেরটি** পাবে ⭐ (IPv6-এ নতুন) |

### 🔁 Revision Box
**IPv6 = 128 bit**, ৮টি group × ৪টি hex digit, colon-separated।
উদাহরণ: `2001:0db8:85a3:0000:0000:8a2e:0370:7334` → সংক্ষেপে `2001:db8:85a3::8a2e:370:7334`
নিয়ম: **leading zero বাদ** + **পরপর শূন্য group = `::` (একবারই)**। Loopback = `::1`।
**IPv6-এ Broadcast নেই** — Unicast/Multicast/**Anycast**। Header স্থির **40 byte**, IPsec অন্তর্নির্মিত।

---
---

# MODULE 9 — TRANSPORT LAYER: TCP & UDP ⭐⭐⭐

## Topic 1: TCP vs UDP

### Definitions
- **TCP (Transmission Control Protocol):** A **connection-oriented**, **reliable** protocol that guarantees ordered, error-checked delivery.
- **UDP (User Datagram Protocol):** A **connectionless**, **unreliable** but **fast** protocol with minimal overhead.

### Comparison ⭐⭐⭐

| Feature | **TCP** | **UDP** |
|---|---|---|
| Connection | **Connection-oriented** | **Connectionless** |
| নির্ভরযোগ্যতা | **নির্ভরযোগ্য** (ACK, retransmission) | **অনির্ভরযোগ্য** |
| ক্রম | ✅ ক্রম বজায় রাখে | ❌ রাখে না |
| গতি | ধীর | **দ্রুত** ⭐ |
| Header আকার | **20 byte** | **8 byte** |
| Error checking | ✅ + সংশোধন | ✅ শুধু detect |
| Flow/Congestion control | ✅ আছে | ❌ নেই |
| **উদাহরণ** | HTTP, HTTPS, FTP, SMTP, SSH | **DNS, DHCP, VoIP, Video streaming, Online game** |

⭐ **মনে রাখার উপায়:**
**TCP** = "সব পৌঁছাতেই হবে" (file download — একটা byte হারালেও চলবে না)
**UDP** = "দ্রুত হওয়াটাই আসল" (video call — একটা frame হারালে সমস্যা নেই, থেমে থাকলেই সমস্যা)

## 🔍 DRY RUN — TCP Three-Way Handshake ⭐⭐⭐

**সংযোগ স্থাপন (Connection Establishment):**

```
   Client                                    Server
     │                                          │
     │  1️⃣  SYN  (seq = x)                     │
     │ ────────────────────────────────────────►│
     │      "আমি সংযোগ করতে চাই"                 │
     │                                          │
     │  2️⃣  SYN-ACK  (seq = y, ack = x+1)      │
     │ ◄────────────────────────────────────────│
     │      "ঠিক আছে, আমিও রাজি"                 │
     │                                          │
     │  3️⃣  ACK  (ack = y+1)                    │
     │ ────────────────────────────────────────►│
     │      "নিশ্চিত করলাম"                      │
     │                                          │
     │ ✅ সংযোগ স্থাপিত — এখন data যাবে          │
```

### ধাপগুলো
1. **SYN** — Client synchronize request পাঠায় (নিজের sequence number x সহ)
2. **SYN-ACK** — Server নিজের SYN (y) + Client-এর ACK (x+1) একসাথে পাঠায়
3. **ACK** — Client server-এর SYN স্বীকার করে (y+1)

⭐ **তিন ধাপ কেন?** দুই পক্ষেরই **পাঠানো ও পাওয়া** — দুটোই কাজ করছে কিনা নিশ্চিত হতে।

**সংযোগ বিচ্ছেদ = Four-way handshake:** `FIN → ACK → FIN → ACK`

## Topic 2: Port Numbers ⭐⭐

| Port | Protocol | কাজ |
|---|---|---|
| **20, 21** | **FTP** | File transfer (20=data, 21=control) |
| **22** | **SSH** | নিরাপদ remote login |
| **23** | **Telnet** | অনিরাপদ remote login |
| **25** | **SMTP** | Email পাঠানো |
| **53** | **DNS** | Domain → IP |
| **67, 68** | **DHCP** | স্বয়ংক্রিয় IP বরাদ্দ |
| **80** | **HTTP** | Web |
| **110** | POP3 | Email নামানো |
| **143** | IMAP | Email (server-এ রেখে) |
| **443** | **HTTPS** | নিরাপদ web |
| **3306** | MySQL | Database |

**Port Range:**
- 0–1023 = **Well-known** ports
- 1024–49151 = Registered
- 49152–65535 = Dynamic/Private

⭐ মোট port = **65,536** (2¹⁶, কারণ port number 16 bit)

### 🔁 Revision Box
**TCP = connection-oriented, নির্ভরযোগ্য, 20 byte header, ধীর** (HTTP, FTP, SMTP)। **UDP = connectionless, দ্রুত, 8 byte header** (DNS, DHCP, VoIP, streaming)। **Three-way handshake: SYN → SYN-ACK → ACK**; বিচ্ছেদ = 4-way (FIN/ACK)। Port: **21 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 80 HTTP, 443 HTTPS**। মোট port = 65,536।

---
---

# MODULE 10 — DEVICES & PROTOCOLS

## Topic 1: Network Devices ⭐⭐⭐

| Device | **OSI Layer** | কাজ | Broadcast domain |
|---|---|---|---|
| **Repeater** | **1 Physical** | সংকেত শক্তিশালী করে | ১টাই |
| **Hub** | **1 Physical** | সবার কাছে পাঠায় (বোকা) | ১টাই |
| **Bridge** | **2 Data Link** | দুই LAN জোড়ে, MAC দেখে | ১টাই |
| **Switch** | **2 Data Link** | **MAC দেখে শুধু সঠিক port-এ** পাঠায় ⭐ | ১টাই |
| **Router** | **3 Network** | **IP দেখে ভিন্ন network-এ পাঠায়** ⭐ | **প্রতি port-এ আলাদা** |
| **Gateway** | **সব layer** | ভিন্ন protocol-এর network জোড়ে | আলাদা |

### Hub vs Switch ⭐
| | **Hub** | **Switch** |
|---|---|---|
| পাঠায় | **সবার কাছে** (broadcast) | **শুধু গন্তব্যে** (unicast) |
| Bandwidth | সবাই ভাগ করে | প্রতি port-এ পূর্ণ |
| Collision | **হয়** | **হয় না** (full-duplex) |
| বুদ্ধি | নেই | MAC address table রাখে |

⭐ **Switch = Layer 2 (MAC)**, **Router = Layer 3 (IP)** — এই পার্থক্য নিশ্চিত MCQ।

## Topic 2: গুরুত্বপূর্ণ Protocol ⭐

| Protocol | পূর্ণরূপ | কাজ |
|---|---|---|
| **DNS** | Domain Name System | **Domain নাম → IP** (google.com → 142.250.x.x) |
| **DHCP** | Dynamic Host Configuration Protocol | **স্বয়ংক্রিয়ভাবে IP বরাদ্দ** |
| **NAT** | Network Address Translation | **Private IP ↔ Public IP** রূপান্তর |
| **PAT** | Port Address Translation | অনেক private IP → **একটাই** public IP (port দিয়ে আলাদা) |
| **ARP** | Address Resolution Protocol | **IP → MAC** |
| **RARP** | Reverse ARP | **MAC → IP** |
| **ICMP** | Internet Control Message Protocol | Error report — **ping, traceroute** এটা ব্যবহার করে |
| **HTTP/HTTPS** | HyperText Transfer Protocol (Secure) | Web browsing |
| **FTP** | File Transfer Protocol | File আদান-প্রদান |
| **SMTP/POP3/IMAP** | — | Email পাঠানো / নামানো |

### DHCP-এর ৪ ধাপ ⭐ (**DORA** — মুখস্থ)
```
1. D iscover  →  Client: "কোনো DHCP server আছে?"       (broadcast)
2. O ffer     →  Server: "এই IP-টা নিতে পারো"
3. R equest   →  Client: "ঠিক আছে, ওটাই চাই"
4. A cknowledge → Server: "দিলাম, তোমার হলো"
```

### 🔁 Revision Box
**Hub = L1 (সবাইকে পাঠায়)**, **Switch = L2 (MAC, শুধু গন্তব্যে)**, **Router = L3 (IP, ভিন্ন network)**। **DNS = নাম→IP**, **DHCP = স্বয়ংক্রিয় IP (DORA)**, **NAT = private↔public**, **ARP = IP→MAC**, **ICMP = ping/traceroute**।

---
---

# MODULE 11 — WIRELESS & IEEE STANDARDS ⭐⭐⭐

> **Sample paper Q2 এখান থেকে।**

## Topic 1: IEEE 802.11 (Wi-Fi) ⭐⭐⭐

| Standard | সাল | **Frequency** | **সর্বোচ্চ Bandwidth** | Wi-Fi নাম |
|---|---|---|---|---|
| **802.11** | 1997 | 2.4 GHz | 2 Mbps | — |
| **802.11a** | 1999 | **5 GHz** | **54 Mbps** | — |
| **802.11b** ⭐ | 1999 | **2.4 GHz** | **11 Mbps** | — |
| **802.11g** | 2003 | **2.4 GHz** | **54 Mbps** | — |
| **802.11n** | 2009 | 2.4 / 5 GHz | **600 Mbps** | Wi-Fi 4 |
| **802.11ac** | 2013 | 5 GHz | ~1.3 Gbps+ | Wi-Fi 5 |
| **802.11ax** | 2019 | 2.4 / 5 / 6 GHz | ~9.6 Gbps | Wi-Fi 6 |

⭐⭐⭐ **Q2-এর সরাসরি উত্তর: 802.11b, 2.4 GHz → সর্বোচ্চ 11 Mbps**

### 2.4 GHz vs 5 GHz ⭐
| | **2.4 GHz** | **5 GHz** |
|---|---|---|
| পাল্লা | **বেশি দূর যায়** | কম |
| গতি | কম | **বেশি** |
| দেয়াল ভেদ | ভালো | দুর্বল |
| হস্তক্ষেপ | **বেশি** (microwave, Bluetooth) | কম |

## Topic 2: অন্যান্য IEEE 802 Standard ⭐⭐

| Standard | কী |
|---|---|
| **802.3** | **Ethernet** (তারযুক্ত LAN) ⭐ |
| **802.5** | **Token Ring** |
| **802.11** | **Wi-Fi / WLAN** ⭐ |
| **802.15** | **Bluetooth / WPAN** ⭐ |
| **802.15.4** | Zigbee (IoT) |
| **802.16** | **WiMAX** (broadband wireless) |
| **802.1** | Bridging, VLAN |

⭐ **মুখস্থ:** **3 = Ethernet · 5 = Token Ring · 11 = Wi-Fi · 15 = Bluetooth · 16 = WiMAX**

## Topic 3: Wireless Security
| Protocol | নিরাপত্তা |
|---|---|
| **WEP** | দুর্বল, ভাঙা (ব্যবহার করবে না) |
| **WPA** | মাঝারি |
| **WPA2** | **শক্তিশালী (AES)** — সবচেয়ে প্রচলিত |
| **WPA3** | সর্বাধুনিক |

### Ethernet Standards
| নাম | গতি |
|---|---|
| 10BASE-T | 10 Mbps |
| 100BASE-TX (Fast Ethernet) | 100 Mbps |
| 1000BASE-T (Gigabit) | 1 Gbps |

**নামের অর্থ:** `10BASE-T` → **10** Mbps, **BASE**band, **T**wisted pair

### 🔁 Revision Box
**802.11b = 2.4 GHz = 11 Mbps** ⭐ · 802.11a = 5 GHz = 54 · 802.11g = 2.4 GHz = 54 · 802.11n = 600 Mbps। IEEE: **802.3 Ethernet · 802.5 Token Ring · 802.11 Wi-Fi · 802.15 Bluetooth · 802.16 WiMAX**। **2.4 GHz = দূর যায় কিন্তু ধীর**, **5 GHz = দ্রুত কিন্তু কাছে**। Security: WEP < WPA < **WPA2** < WPA3।

---
---

# ★ FINAL REVISION — শেষ ৩০ মিনিট

## 1. Sample Paper-এর ৪টা প্রশ্নের সরাসরি উত্তর ⭐⭐⭐

**Q1. IPv6-এর দৈর্ঘ্য কত? উদাহরণ দাও।**
> IPv6 হলো **128 bit**। ৮টি group-এ লেখা হয়, প্রতিটি group ৪টি hexadecimal digit, colon দিয়ে আলাদা।
> **উদাহরণ:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
> সংক্ষেপে: `2001:db8:85a3::8a2e:370:7334`

**Q2. IEEE 802.11b (2.4 GHz)-এর সর্বোচ্চ bandwidth কত?**
> **11 Mbps**

**Q3. OSI ও TCP/IP-তে কয়টি layer?**
> **OSI = 7 layer** (Application, Presentation, Session, Transport, Network, Data Link, Physical)
> **TCP/IP = 4 layer** (Application, Transport, Internet, Network Access)

**Q4. VLSM ও CIDR বলতে কী বোঝায়?**
> **VLSM** (Variable Length Subnet Mask) — একই network-এ **ভিন্ন আকারের subnet** বানানোর কৌশল, যাতে প্রতিটি বিভাগ ঠিক যতটা IP দরকার ততটাই পায়, অপচয় না হয়।
> **CIDR** (Classless Inter-Domain Routing) — class-এর কঠোর সীমা বাদ দিয়ে **যেকোনো দৈর্ঘ্যের subnet mask** ব্যবহারের পদ্ধতি, `/24`, `/26` এভাবে লেখা হয়। এটি IP অপচয় কমায় ও **route aggregation** সম্ভব করে।

## 2. আবশ্যিক সূত্র

| সূত্র | কোথায় |
|---|---|
| **Host = 2ⁿ − 2** | Subnetting |
| **Subnet = 2ᵐ** | Subnetting |
| **Block Size = 256 − mask octet** | Subnetting ⭐ |
| Mesh link = **n(n−1)/2** | Topology |
| মোট Port = **2¹⁶ = 65,536** | Transport |
| IPv4 = **2³²** ≈ 4.3 বিলিয়ন | Addressing |
| IPv6 = **2¹²⁸** | Addressing |

## 3. Subnet Cheat Sheet (মুখস্থ) ⭐⭐⭐

| CIDR | Mask (শেষ octet) | Block | Host |
|---|---|---|---|
| /24 | 0 | 256 | 254 |
| /25 | 128 | 128 | 126 |
| **/26** | **192** | **64** | **62** |
| **/27** | **224** | **32** | **30** |
| **/28** | **240** | **16** | **14** |
| /29 | 248 | 8 | 6 |
| **/30** | **252** | **4** | **2** |

## 4. Top 20 MCQ Traps ⭐⭐⭐

1. **OSI = 7, TCP/IP = 4** layer
2. **Encryption = Presentation layer** (Application নয়)
3. **Hub = L1, Switch = L2, Router = L3**
4. **MAC = 48 bit (L2)**, **IP = 32 bit (L3)**
5. **Class A range 1–126** (127 নয় — ওটা loopback)
6. **127.0.0.1 = loopback/localhost**
7. **Private IP: 10.x, 172.16–31.x, 192.168.x**
8. **Host = 2ⁿ − 2** (network ও broadcast বাদ)
9. **Block size = 256 − mask octet**
10. **/26 = 62 host, /27 = 30, /28 = 14, /30 = 2**
11. **IPv6 = 128 bit, hexadecimal** (IPv4-এর মতো decimal নয়)
12. ⚠️ **IPv6-এ Broadcast নেই** — Unicast/Multicast/**Anycast**
13. ⚠️ **`::` একবারই** ব্যবহার করা যায়
14. **TCP = 20 byte header, UDP = 8 byte**
15. **DNS ও DHCP = UDP** ব্যবহার করে (TCP নয়) ⭐
16. **Three-way handshake: SYN → SYN-ACK → ACK**
17. **802.11b = 11 Mbps**, 802.11g = 54 Mbps (দুটোই 2.4 GHz)
18. **802.3 = Ethernet, 802.11 = Wi-Fi, 802.15 = Bluetooth**
19. **ARP = IP→MAC**, RARP = MAC→IP
20. **Internet = Packet Switching** (Circuit নয়)

## 5. দ্রুত সংজ্ঞা (এক লাইনে)

| Term | এক লাইনে |
|---|---|
| **VLSM** | এক network-এ ভিন্ন আকারের subnet, প্রয়োজনমতো IP বরাদ্দ |
| **CIDR** | Classless addressing, /notation, route aggregation |
| **NAT** | Private IP → Public IP রূপান্তর |
| **DNS** | Domain নাম → IP ঠিকানা |
| **DHCP** | স্বয়ংক্রিয়ভাবে IP বরাদ্দ (DORA) |
| **ARP** | IP ঠিকানা → MAC ঠিকানা |
| **Subnetting** | বড় network-কে ছোট ছোট ভাগে ভাঙা |
| **Encapsulation** | প্রতিটি layer নিজের header যোগ করা |
| **Multiplexing** | এক media-তে একাধিক signal পাঠানো |
| **Latency** | এক প্রান্ত থেকে অন্য প্রান্তে যেতে লাগা সময় |

---

# ✍️ নিজে করে দেখো (উত্তর নিচে)

1. `192.168.10.75/28` — Network, Broadcast ও host range কী?
2. `10.0.0.0/8` কে 8টা subnet-এ ভাগ করলে CIDR কত হবে?
3. প্রতিটি subnet-এ 100 host দরকার — কোন mask?
4. `2001:0000:0000:0db8:0000:0000:0000:0001` সংক্ষেপ করো।

<details>
<summary>উত্তর</summary>

**1.** /28 → mask 240 → block 16 → 16-এর গুণিতক: 64, 80
   75 আছে 64 ও 80-এর মাঝে →
   **Network = 192.168.10.64** · **Broadcast = 192.168.10.79** · **Host = .65 – .78** (14টা)

**2.** 2ᵐ ≥ 8 → m = 3 → /8 + 3 = **/11** (mask 255.224.0.0)

**3.** 2ⁿ − 2 ≥ 100 → n = 7 (2⁷−2 = 126) → **/25, mask 255.255.255.128**

**4.** দুটো শূন্য-অংশ আছে (২টা ও ৩টা group)। বড়টায় `::` বসাও →
   **`2001:0:0:db8::1`**

</details>
