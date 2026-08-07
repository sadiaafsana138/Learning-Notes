# CSE 320 + CSE 421 + CSE 490
## Short Master Viva Notes
### প্রতিটি syllabus topic: 1–5 lines | English Answer + বাংলা ব্যাখ্যা

---

# CSE 320 — DATA COMMUNICATIONS

## 1. Data Communication
**English:** Data communication is the exchange of data between two or more devices through a transmission medium using agreed communication rules.  
**বাংলা:** দুই বা ততোধিক device-এর মধ্যে medium ও protocol ব্যবহার করে data আদান-প্রদান করাই data communication।

## 2. Purpose of Communication
**English:** Communication enables information sharing, resource sharing, remote access, coordination, and reliable data exchange.  
**বাংলা:** Information/resource share করা, remote access ও reliable data exchange-এর জন্য communication প্রয়োজন।

## 3. Communication System
**English:** A basic communication system includes sender, receiver, message, transmission medium, and protocol.  
**বাংলা:** Sender, receiver, message, medium এবং protocol মিলে communication system তৈরি হয়।

## 4. Transmission Medium
**English:** A transmission medium is the path through which signals travel, such as copper cable, fiber, or wireless radio.  
**বাংলা:** যে physical বা wireless path দিয়ে signal যায় সেটিই transmission medium।

## 5. Analog Signal
**English:** An analog signal varies continuously with time and can take a continuous range of values.  
**বাংলা:** Continuousভাবে পরিবর্তিত signal হলো analog signal।

## 6. Digital Signal
**English:** A digital signal uses discrete levels, commonly representing binary 0 and 1.  
**বাংলা:** Discrete signal, সাধারণত 0 ও 1, ব্যবহার করে digital data transmit করা হয়।

## 7. Bandwidth
**English:** Bandwidth is the frequency range of a communication channel; in networking, it is also commonly used informally for the channel's maximum data-carrying capacity.  
**বাংলা:** Channel-এর frequency range-কে bandwidth বলে; networking-এ এটি data carrying capacity বোঝাতেও ব্যবহৃত হয়।

## 8. Data Rate / Bit Rate
**English:** Bit rate is the number of bits transmitted per second, measured in bps.  
**বাংলা:** প্রতি second-এ যত bit transmit হয় সেটাই bit rate।

## 9. Baud Rate
**English:** Baud rate is the number of signal symbols transmitted per second. A symbol can represent multiple bits in some modulation schemes.  
**বাংলা:** প্রতি second-এ কতটি symbol transmit হয় তা baud rate।

## 10. Noise
**English:** Noise is unwanted electrical or electromagnetic disturbance that can alter or corrupt a transmitted signal.  
**বাংলা:** Unwanted disturbance-এর কারণে signal/data corrupt হতে পারে; এটিই noise।

## 11. Signal-to-Noise Ratio (SNR)
**English:** SNR compares signal power with noise power; higher SNR generally means better signal quality.  
**বাংলা:** Signal কতটা strong compared to noise তা SNR দিয়ে বোঝায়।

## 12. Attenuation
**English:** Attenuation is the loss of signal strength as a signal travels through a medium.  
**বাংলা:** Distance-এর সাথে signal দুর্বল হয়ে যাওয়াকে attenuation বলে।

## 13. Distortion
**English:** Distortion occurs when different frequency components of a signal are altered unequally, changing the signal shape.  
**বাংলা:** Signal-এর বিভিন্ন component unequalভাবে পরিবর্তিত হয়ে original shape বদলে গেলে distortion হয়।

## 14. Modulation
**English:** Modulation varies a carrier signal according to the information signal so data can be transmitted effectively over a communication channel.  
**বাংলা:** Carrier signal-এর কোনো property পরিবর্তন করে information transmit করাই modulation।

## 15. Why Modulation is Needed
**English:** Modulation can enable practical antenna sizes, frequency allocation, long-distance transmission, multiplexing, and better suitability to channel characteristics.  
**বাংলা:** Long-distance transmission, antenna size, channel suitability ও multiple signals share করার জন্য modulation দরকার।

## 16. Carrier Signal
**English:** A carrier is a high-frequency periodic signal whose properties are varied during modulation to carry information.  
**বাংলা:** Information বহন করার জন্য যে high-frequency signal modify করা হয় সেটি carrier।

## 17. Amplitude Modulation (AM)
**English:** In AM, the amplitude of the carrier varies according to the information signal while carrier frequency remains nominally constant.  
**বাংলা:** Carrier-এর amplitude পরিবর্তন করে data/information বহন করা হয়।

## 18. Frequency Modulation (FM)
**English:** In FM, the carrier frequency varies according to the information signal while amplitude remains nominally constant.  
**বাংলা:** Carrier-এর frequency পরিবর্তন করে information বহন করা হয়।

## 19. Phase Modulation (PM)
**English:** In PM, the carrier phase varies according to the information signal.  
**বাংলা:** Carrier-এর phase পরিবর্তনের মাধ্যমে information encode করা হয়।

## 20. ASK
**English:** Amplitude Shift Keying represents digital symbols by changing the carrier amplitude.  
**বাংলা:** Digital data অনুযায়ী carrier amplitude change করা হয়।

## 21. FSK
**English:** Frequency Shift Keying represents digital symbols using different carrier frequencies.  
**বাংলা:** Different frequency দিয়ে different digital symbol represent করা হয়।

## 22. PSK
**English:** Phase Shift Keying represents digital symbols by changing the carrier phase.  
**বাংলা:** Phase পরিবর্তনের মাধ্যমে digital symbol represent করা হয়।

## 23. QAM
**English:** Quadrature Amplitude Modulation varies both amplitude and phase to represent multiple bits per symbol.  
**বাংলা:** Amplitude ও phase দুটোই ব্যবহার করে প্রতি symbol-এ বেশি bit carry করা যায়।

## 24. Encoding
**English:** Encoding maps information/data into a signal or code suitable for storage or transmission.  
**বাংলা:** Data-কে transmission/storage-এর উপযোগী signal/code-এ convert করাই encoding।

## 25. Line Coding
**English:** Line coding represents digital data as digital signal patterns for transmission over a physical link.  
**বাংলা:** Digital data-কে digital signal pattern-এ convert করার পদ্ধতি line coding।

## 26. Multiplexing
**English:** Multiplexing combines multiple signals so they can share a common communication link.  
**বাংলা:** একাধিক signal-কে একই communication channel share করানো হলো multiplexing।

## 27. FDM
**English:** Frequency Division Multiplexing assigns different frequency bands to different signals on the same medium.  
**বাংলা:** Different signal-এর জন্য আলাদা frequency band দেওয়া হয়।

## 28. TDM
**English:** Time Division Multiplexing allows multiple signals to share a channel by assigning different time slots.  
**বাংলা:** Different signal-এর জন্য আলাদা time slot দেওয়া হয়।

## 29. WDM
**English:** Wavelength Division Multiplexing carries multiple optical signals using different wavelengths over the same fiber.  
**বাংলা:** Fiber-এর মধ্যে different wavelength ব্যবহার করে multiple optical signal পাঠানো হয়।

## 30. Error
**English:** A transmission error occurs when received data differs from the transmitted data.  
**বাংলা:** Sender-এর data ও receiver-এর received data mismatch হলে error হয়।

## 31. Error Detection
**English:** Error detection adds redundancy so the receiver can determine whether transmitted data was corrupted.  
**বাংলা:** Extra information ব্যবহার করে data corrupt হয়েছে কিনা detect করা হয়।

## 32. Parity Check
**English:** A parity bit is added so the total number of 1s is even or odd according to the chosen parity rule.  
**বাংলা:** Extra parity bit দিয়ে simple transmission error detect করা হয়।

## 33. Checksum
**English:** A checksum is a computed value derived from data and sent with it so the receiver can detect certain transmission errors.  
**বাংলা:** Data থেকে calculated value পাঠিয়ে received data-এর error detect করা হয়।

## 34. CRC
**English:** Cyclic Redundancy Check treats data as a binary polynomial and uses modulo-2 division to generate a remainder for error detection.  
**বাংলা:** Polynomial/modulo-2 division ব্যবহার করে powerful error detection করা হয়।

## 35. Error Control
**English:** Error control detects and/or corrects transmission errors using techniques such as retransmission, acknowledgments, and error-detecting codes.  
**বাংলা:** Error detect করে retransmission বা correction-এর মাধ্যমে reliable delivery নিশ্চিত করা হয়।

## 36. ARQ
**English:** Automatic Repeat reQuest uses error detection plus feedback so corrupted or lost frames can be retransmitted.  
**বাংলা:** Error হলে receiver feedback দেয় এবং sender frame আবার পাঠায়।

## 37. Stop-and-Wait ARQ
**English:** The sender transmits one frame and waits for an acknowledgment before sending the next frame.  
**বাংলা:** একবারে একটি frame পাঠিয়ে ACK-এর জন্য wait করে।

## 38. Sliding Window
**English:** Sliding-window protocols allow multiple frames to be outstanding before acknowledgments, improving link utilization.  
**বাংলা:** ACK-এর জন্য প্রতিটি frame-এর পরে থেমে না থেকে একাধিক frame পাঠানো যায়।

## 39. Protocol
**English:** A protocol is a set of rules governing communication, including message format, timing, sequencing, and error handling.  
**বাংলা:** Communication-এর rules—format, timing, sequencing, error handling—মিলে protocol।

## 40. Data Transmission Protocol
**English:** A data transmission protocol defines how devices exchange data reliably and interpret transmitted messages.  
**বাংলা:** Device কীভাবে data পাঠাবে, receive করবে ও error handle করবে তা protocol নির্ধারণ করে।

## 41. Protocol Layers
**English:** Layering divides communication functions into manageable levels, where each layer provides services to the layer above it.  
**বাংলা:** বড় communication task-কে আলাদা layer-এ ভাগ করলে design ও troubleshooting সহজ হয়।

## 42. OSI Model
**English:** OSI has seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.  
**বাংলা:** Communication function-এর standard 7-layer conceptual model হলো OSI।

## 43. TCP/IP Model
**English:** The TCP/IP architecture commonly uses Link/Network Access, Internet, Transport, and Application layers.  
**বাংলা:** Internet communication-এর practical protocol architecture হলো TCP/IP model।

## 44. Physical Layer
**English:** The physical layer transmits raw bits over a physical medium and defines electrical, mechanical, and signaling characteristics.  
**বাংলা:** Raw bit-এর actual transmission ও physical signaling handle করে।

## 45. Data Link Layer
**English:** The data link layer provides framing, link-level error detection/control, and media access control on a local link.  
**বাংলা:** Frame, error control ও local medium access handle করে।

## 46. Network Layer
**English:** The network layer handles logical addressing and routing packets between networks.  
**বাংলা:** Different network-এর মধ্যে packet-এর routing ও logical addressing করে।

## 47. Transport Layer
**English:** The transport layer provides end-to-end process communication and may provide reliability, flow control, and congestion control.  
**বাংলা:** End-to-end data delivery ও reliability/flow/congestion control handle করতে পারে।

## 48. Session Layer
**English:** The session layer manages logical communication sessions, including establishment, coordination, and termination in the OSI model.  
**বাংলা:** দুই application-এর communication session establish/manage/terminate করার conceptual layer।

## 49. Presentation Layer
**English:** The presentation layer handles data representation issues such as translation, encryption, and compression in the OSI model.  
**বাংলা:** Data format, encryption ও compression-এর মতো representation কাজ করে।

## 50. Application Layer
**English:** The application layer provides network services directly to applications, such as web, email, and file-transfer services.  
**বাংলা:** User/application-এর সবচেয়ে কাছের network service layer।

## 51. LAN
**English:** A Local Area Network connects devices over a relatively small geographic area such as a room, building, or campus.  
**বাংলা:** ছোট geographic area-এর network হলো LAN।

## 52. WAN
**English:** A Wide Area Network connects networks across large geographic areas, often using carrier or telecommunications infrastructure.  
**বাংলা:** Large geographic area জুড়ে network connect করে WAN।

## 53. Telephony Network
**English:** Telephony networks are communication infrastructures originally designed for voice services and can also support data transmission through suitable technologies.  
**বাংলা:** Telephone infrastructure voice-এর পাশাপাশি বিভিন্ন technology দিয়ে data communication-ও support করতে পারে।

## 54. LAN vs WAN
**English:** LAN covers a smaller area and is usually privately managed; WAN covers larger areas and often uses carrier infrastructure.  
**বাংলা:** LAN ছোট area, WAN বড় area cover করে।

## 55. Fundamental Limits
**English:** Communication channels have theoretical limits on reliable data transmission imposed by bandwidth, noise, and signal conditions.  
**বাংলা:** Channel-এর bandwidth ও noise-এর কারণে reliable data rate-এর theoretical limit থাকে।

## 56. Nyquist Bit Rate
**English:** For a noiseless channel with bandwidth B Hz and L signal levels, the maximum theoretical bit rate is 2B log₂L bps.  
**বাংলা:** Noiseless channel-এর maximum theoretical bit rate নির্ধারণে Nyquist formula ব্যবহৃত হয়।

## 57. Shannon Capacity
**English:** For a noisy channel, Shannon capacity is C = B log₂(1 + S/N) bps.  
**বাংলা:** Noise থাকা channel-এর theoretical maximum reliable data rate Shannon formula দিয়ে পাওয়া যায়।

---

# CSE 421 — COMPUTER NETWORKS

## 58. Computer Network
**English:** A computer network is a collection of interconnected devices that communicate and share data/resources using protocols.  
**বাংলা:** Protocol ব্যবহার করে interconnected device-এর data/resource sharing system হলো computer network।

## 59. Transport Connection
**English:** A transport connection is a logical end-to-end communication relationship between transport endpoints, as in TCP.  
**বাংলা:** Sender ও receiver-এর transport endpoints-এর মধ্যে logical end-to-end connection।

## 60. Session
**English:** A session is a logical communication interaction maintained between applications or endpoints for a period of time.  
**বাংলা:** দুই application-এর মধ্যে নির্দিষ্ট সময়ের logical communication interaction হলো session।

## 61. Protocol Hierarchy
**English:** A protocol hierarchy organizes network protocols into layers, with each layer using services from lower layers and serving higher layers.  
**বাংলা:** Network protocol-গুলো layered structure-এ organize করা হয়।

## 62. Transport Layer Design Issues
**English:** Transport protocols address reliability, sequencing, flow control, multiplexing, connection management, and congestion control.  
**বাংলা:** Reliable end-to-end delivery, sequencing, flow/congestion control ও connection management প্রধান issue।

## 63. Session Layer Design Issues
**English:** Session protocols manage dialog control, synchronization, session establishment, maintenance, and termination in the OSI framework.  
**বাংলা:** Session establish, synchronize ও terminate করার বিষয়গুলো session layer-এর design issue।

## 64. End-to-End Protocol
**English:** An end-to-end protocol provides communication functions between source and destination hosts/processes rather than only one local link.  
**বাংলা:** শুধু এক link নয়, পুরো sender-to-receiver path-এর communication handle করে।

## 65. Message Handling
**English:** Message handling protocols define how messages are formatted, transferred, acknowledged, routed, or delivered to applications.  
**বাংলা:** Message কীভাবে format, transfer ও deliver হবে তা নির্ধারণ করে।

## 66. Terminal Protocol
**English:** Terminal protocols support remote interaction with another computer, allowing a user to operate a remote system through a network.  
**বাংলা:** Network-এর মাধ্যমে remote computer-এ terminal access দেওয়ার protocol।

## 67. File Transfer Protocol
**English:** File transfer protocols provide mechanisms for transferring files between networked systems; FTP is a classic example.  
**বাংলা:** Network-এর মাধ্যমে file upload/download করার protocol।

## 68. TCP
**English:** TCP is a connection-oriented transport protocol that provides reliable, ordered byte-stream delivery with flow and congestion control.  
**বাংলা:** TCP reliable, ordered এবং connection-oriented transport service দেয়।

## 69. UDP
**English:** UDP is a connectionless transport protocol with low overhead; it does not provide TCP-style reliable ordered delivery.  
**বাংলা:** UDP connectionless ও low-overhead; TCP-এর মতো reliability guarantee দেয় না।

## 70. TCP vs UDP
**English:** TCP → connection-oriented, reliable, ordered, more overhead. UDP → connectionless, lightweight, no built-in reliable ordered delivery.  
**বাংলা:** Reliability দরকার হলে TCP; low overhead/real-time-style applications-এ UDP useful হতে পারে।

## 71. Internet Protocol (IP)
**English:** IP provides logical addressing and packet forwarding/routing across interconnected networks.  
**বাংলা:** Network-to-network packet delivery ও logical addressing-এর মূল protocol হলো IP।

## 72. IPv4
**English:** IPv4 uses 32-bit addresses and provides packet delivery across IP networks.  
**বাংলা:** IPv4 address 32-bit।

## 73. IPv6
**English:** IPv6 uses 128-bit addresses and provides a much larger address space with additional protocol improvements.  
**বাংলা:** IPv6 address 128-bit এবং huge address space দেয়।

## 74. End-to-End Data Network
**English:** An end-to-end data network provides communication from a source endpoint to a destination endpoint across intermediate networks and devices.  
**বাংলা:** Source থেকে destination পর্যন্ত intermediate network/device পার হয়ে complete communication path।

## 75. Congestion
**English:** Congestion occurs when offered traffic exceeds the network's ability to process or forward it efficiently, causing delay and packet loss.  
**বাংলা:** Network-এর capacity-এর তুলনায় traffic বেশি হলে congestion হয়।

## 76. Congestion Control
**English:** Congestion control regulates sending behavior to reduce overload and maintain efficient network operation.  
**বাংলা:** Network overload কমাতে sender-এর transmission rate/control adjust করা হয়।

## 77. Flow Control
**English:** Flow control prevents a fast sender from overwhelming a slower receiver.  
**বাংলা:** Sender যেন receiver-এর processing capacity-এর চেয়ে বেশি data না পাঠায় তা নিশ্চিত করে।

## 78. Flow Control vs Congestion Control
**English:** Flow control protects the receiver; congestion control protects the network from overload.  
**বাংলা:** Flow control = receiver protection; congestion control = network protection।

## 79. Wireless Network
**English:** A wireless network communicates through radio or other wireless media instead of a physical wired link.  
**বাংলা:** Cable ছাড়াই wireless medium দিয়ে communication করা হয়।

## 80. Mobile Computing
**English:** Mobile computing enables users/devices to access and process information while moving across locations and networks.  
**বাংলা:** Device/user চলাফেরা করলেও network service/data access করতে পারা।

## 81. High-Speed Network
**English:** High-speed networks provide very high data rates using technologies such as high-capacity fiber, modern Ethernet, and advanced wireless systems.  
**বাংলা:** Very high bandwidth/data rate-এর network হলো high-speed network।

## 82. Concurrent Programming
**English:** Concurrent programming allows multiple computations or processes to make progress during overlapping periods of time.  
**বাংলা:** একাধিক process/thread-এর কাজ overlappingভাবে progress করে।

## 83. Data Link Layer
**English:** The data link layer provides node-to-node delivery over a link, including framing, error handling, and media access functions.  
**বাংলা:** Direct/local link-এর data delivery, framing ও access control করে।

## 84. Framing
**English:** Framing divides a stream of bits into identifiable data units called frames.  
**বাংলা:** Continuous bit stream-কে identifiable frame-এ ভাগ করাই framing।

## 85. Error Control at Data Link
**English:** Data-link error control detects/corrects or retransmits corrupted frames using techniques such as CRC and ARQ.  
**বাংলা:** Frame error detect করে প্রয়োজন হলে retransmission/correction করা হয়।

## 86. MAC
**English:** Media Access Control determines how multiple devices share access to a common communication medium.  
**বাংলা:** Shared medium-এ কে কখন transmit করবে তা MAC mechanism control করে।

## 87. MAC Address
**English:** A MAC address is a link-layer identifier associated with a network interface, commonly represented as a 48-bit address in Ethernet.  
**বাংলা:** Local network/link layer-এ network interface identify করার address।

## 88. Distributed Computation
**English:** Distributed computation divides computation among multiple networked machines that coordinate by exchanging messages.  
**বাংলা:** Multiple networked computer মিলে computation সম্পন্ন করে।

## 89. Distributed System
**English:** A distributed system consists of independent computers that coordinate their actions and appear to users as a coherent system.  
**বাংলা:** Multiple independent computer coordinatedভাবে কাজ করে একটি unified system-এর মতো service দেয়।

## 90. Network Management
**English:** Network management monitors, configures, maintains, and troubleshoots network devices and services.  
**বাংলা:** Network-এর performance, configuration, faults ও operation manage করা।

## 91. Resource Control
**English:** Resource control manages shared network/system resources such as bandwidth, buffers, CPU, storage, and access rights.  
**বাংলা:** Shared resource efficiently ও fairly allocate/control করা।

## 92. Distributed Operating System
**English:** A distributed operating system coordinates resources and processes across multiple connected computers to provide integrated system behavior.  
**বাংলা:** Multiple computer-এর process/resource coordinatedভাবে manage করে।

## 93. Distributed File System
**English:** A distributed file system allows files to be stored and accessed across multiple networked machines while presenting a unified file interface.  
**বাংলা:** Multiple machine-এ file থাকলেও user-এর কাছে unified file system-এর মতো দেখা যায়।

## 94. Caching
**English:** Caching stores frequently or recently used data closer to where it is needed to reduce access time and network traffic.  
**বাংলা:** Frequently used data কাছাকাছি temporary store করে access দ্রুত করা হয়।

## 95. Scheduling
**English:** Scheduling determines the order and allocation of resources for processes/tasks to improve performance and fairness.  
**বাংলা:** কোন process কখন resource পাবে তা scheduling নির্ধারণ করে।

## 96. Process Migration
**English:** Process migration moves a process or its execution state from one machine/node to another in a distributed environment.  
**বাংলা:** Distributed system-এ process এক node থেকে অন্য node-এ move করা।

## 97. Fault Tolerance
**English:** Fault tolerance is the ability of a system to continue providing acceptable service despite component or network failures.  
**বাংলা:** কিছু component fail করলেও system service চালিয়ে যেতে পারা।

## 98. Network Security
**English:** Network security protects communication systems and data from unauthorized access, attacks, alteration, and disruption.  
**বাংলা:** Network ও transmitted data-কে attack/unauthorized access থেকে protect করা।

## 99. Privacy
**English:** Network privacy protects sensitive information from unauthorized observation, collection, or disclosure.  
**বাংলা:** Sensitive information unauthorizedভাবে দেখা/collect/share হওয়া prevent করা।

## 100. Deadlock
**English:** Deadlock occurs when processes are permanently waiting for resources/events that cannot become available because of circular dependencies.  
**বাংলা:** Process-গুলো একে অপরের resource-এর জন্য অপেক্ষা করতে থাকলে deadlock হতে পারে।

## 101. Deadlock Detection
**English:** Deadlock detection identifies whether a set of processes/resources has entered a deadlocked state, often using a wait-for or resource-allocation graph.  
**বাংলা:** Process/resource dependency analyze করে deadlock হয়েছে কিনা detect করা হয়।

## 102. Synchronization
**English:** Synchronization coordinates concurrent processes so shared data and operations occur in a safe and intended order.  
**বাংলা:** Concurrent process-এর কাজকে coordinated রেখে race/inconsistency prevent করা হয়।

## 103. Concurrency Control
**English:** Concurrency control ensures that simultaneous operations on shared data preserve correctness and consistency.  
**বাংলা:** Multiple process একসাথে shared data access করলেও consistency বজায় রাখে।

## 104. Race Condition
**English:** A race condition occurs when the result depends on the timing/order of concurrent operations accessing shared state.  
**বাংলা:** Concurrent operation-এর timing-এর ওপর result depend করলে race condition হতে পারে।

---

# CSE 490 — SPECIAL TOPICS

## 105. Special Topics
**English:** Special Topics is a flexible course for studying a current or contemporary area of Computer Science and Engineering in depth.  
**বাংলা:** CSE-এর current/contemporary কোনো field গভীরভাবে study করার flexible course।

## 106. Contemporary Field
**English:** A contemporary field is a current area of active research, development, or practical interest in CSE.  
**বাংলা:** বর্তমানে research/development-এ গুরুত্বপূর্ণ নতুন বা evolving field।

## 107. Intermediate Undergraduate Background
**English:** The course is designed to be accessible to students with an intermediate undergraduate CSE background.  
**বাংলা:** Advanced research-level prerequisite নয়; undergraduate CSE foundation-এর ওপর topic শেখানো হয়।

## 108. Syllabus Approval
**English:** The syllabus must be approved by the department chair before the course begins.  
**বাংলা:** Course শুরু হওয়ার আগে department chair syllabus approve করেন।

## 109. Detailed Course Description
**English:** A detailed description of the selected topic is provided before the registration period.  
**বাংলা:** Registration-এর আগেই course-এ কী topic পড়ানো হবে তার detailed description দেওয়া হয়।

## 110. Prerequisite
**English:** CSE 490 requires permission of the instructor rather than a fixed technical prerequisite.  
**বাংলা:** Fixed prerequisite নেই; instructor-এর permission প্রয়োজন।

---

# IMPORTANT DIFFERENCES

## Analog vs Digital Signal
**Analog:** Continuous values.  
**Digital:** Discrete values, commonly binary.  
**বাংলা:** Analog continuous; digital discrete।

## Bandwidth vs Bit Rate
**Bandwidth:** Frequency range/capacity concept of a channel.  
**Bit Rate:** Bits transmitted per second.  
**বাংলা:** Bandwidth frequency-related; bit rate data transmission rate।

## Bit Rate vs Baud Rate
**Bit Rate:** Bits/second.  
**Baud Rate:** Symbols/second.  
**বাংলা:** 1 symbol-এ multiple bit থাকলে bit rate > baud rate হতে পারে।

## Modulation vs Encoding
**Modulation:** Changes a carrier's physical property to carry information.  
**Encoding:** Maps data into a suitable signal/code representation.  
**বাংলা:** Modulation carrier-based; encoding data representation-based।

## FDM vs TDM
**FDM:** Different frequency bands.  
**TDM:** Different time slots.  
**বাংলা:** FDM frequency ভাগ করে; TDM time ভাগ করে।

## LAN vs WAN
**LAN:** Small area, usually local/private.  
**WAN:** Large geographic area, often carrier-based.  
**বাংলা:** LAN ছোট; WAN বড় area cover করে।

## TCP vs UDP
**TCP:** Reliable, ordered, connection-oriented.  
**UDP:** Connectionless, lightweight, no TCP-style reliability guarantee.  
**বাংলা:** Reliability দরকার → TCP; low overhead → UDP useful।

## Flow Control vs Congestion Control
**Flow Control:** Protects receiver.  
**Congestion Control:** Protects network.  
**বাংলা:** Receiver overload বনাম network overload।

## OSI vs TCP/IP
**OSI:** Seven-layer reference model.  
**TCP/IP:** Practical Internet protocol architecture with fewer commonly described layers.  
**বাংলা:** OSI বেশি conceptual/reference; TCP/IP Internet-এর practical protocol suite/architecture।

## Framing vs Routing
**Framing:** Creates data-link frames on a link.  
**Routing:** Determines packet paths between networks.  
**বাংলা:** Framing link-level; routing network-level।

## Authentication vs Authorization
**Authentication:** Verifies identity.  
**Authorization:** Determines permissions.  
**বাংলা:** কে? বনাম কী করতে পারবে?

## Synchronization vs Concurrency
**Concurrency:** Multiple computations make overlapping progress.  
**Synchronization:** Coordinates those computations safely.  
**বাংলা:** Concurrency = একসাথে/overlapping কাজ; synchronization = কাজগুলোকে safeভাবে coordinate করা।

## Fault Tolerance vs Security
**Fault Tolerance:** Handles failures and keeps service running.  
**Security:** Protects against unauthorized access/attacks.  
**বাংলা:** Failure survive করা বনাম attack/access protect করা।

---

# MUST-MEMORIZE FORMULAS

- **Nyquist:** `Bit Rate = 2B log₂L`
- **Shannon:** `C = B log₂(1 + S/N)`
- **SNR(dB):** `10 log₁₀(S/N)` for power ratio
- **MUX:** n select lines → 2ⁿ inputs
- **Decoder:** n input lines → up to 2ⁿ outputs
- **IPv4:** 32-bit address
- **IPv6:** 128-bit address

---

# LAST-MINUTE VIVA — 30 MUST KNOW

1. **What is data communication?** Exchange of data between devices through a medium using protocols.
2. **Why is modulation needed?** For practical transmission, frequency allocation, antenna/channel suitability, and multiplexing.
3. **What is noise?** Unwanted disturbance that can corrupt a signal.
4. **What is attenuation?** Loss of signal strength during transmission.
5. **What is bandwidth?** Frequency range of a channel; often also used as a capacity term.
6. **Bit rate vs baud rate?** Bits/sec vs symbols/sec.
7. **What is modulation?** Varying a carrier according to information.
8. **What is multiplexing?** Sharing one communication link among multiple signals.
9. **FDM vs TDM?** Frequency division vs time division.
10. **What is CRC?** Polynomial-based error-detection technique using modulo-2 division.
11. **What is ARQ?** Error-control method using feedback and retransmission.
12. **What is a protocol?** Set of communication rules.
13. **What is LAN?** Network over a relatively small area.
14. **What is WAN?** Network covering a large geographic area.
15. **What is the OSI model?** Seven-layer reference model for network communication.
16. **What does the network layer do?** Logical addressing and routing.
17. **What does the transport layer do?** End-to-end process communication, with reliability/flow/congestion functions depending on protocol.
18. **TCP vs UDP?** TCP reliable/ordered/connection-oriented; UDP lightweight/connectionless.
19. **What is congestion?** Network overload caused by excessive offered traffic.
20. **Flow vs congestion control?** Receiver protection vs network overload protection.
21. **What is framing?** Dividing bit stream into frames.
22. **What is MAC?** Controls access to a shared communication medium.
23. **What is a distributed system?** Networked independent computers coordinating as a coherent system.
24. **What is a distributed file system?** Unified file access over multiple networked machines.
25. **What is caching?** Keeping frequently used data closer for faster access.
26. **What is process migration?** Moving a process/execution state between distributed nodes.
27. **What is fault tolerance?** Continuing service despite failures.
28. **What is deadlock?** Processes permanently waiting due to circular resource dependencies.
29. **What is synchronization?** Coordinating concurrent operations safely.
30. **What is CSE 490?** A flexible course studying a contemporary CSE topic, subject to an approved syllabus and instructor permission.

---

# CSE 320 SYLLABUS CHECKLIST

- [x] Purpose and methods of communication
- [x] Necessity of modulation
- [x] Modulation techniques
- [x] Technical aspects of data communication
- [x] Noise
- [x] Control
- [x] Fundamental limits
- [x] Encoding
- [x] Modulation
- [x] Multiplexing
- [x] Error detection
- [x] Error control
- [x] Data transmission protocols
- [x] Different layers
- [x] LAN
- [x] WAN
- [x] Telephony-linked networks
- [x] CCNA-oriented lab concepts

# CSE 421 SYLLABUS CHECKLIST

- [x] Transport connections
- [x] Sessions
- [x] Protocol hierarchy
- [x] Transport-layer design issues
- [x] Session-layer design issues
- [x] End-to-end protocols
- [x] Message handling protocols
- [x] Terminal protocols
- [x] File transfer protocols
- [x] TCP/IP protocols
- [x] End-to-end data networks
- [x] Congestion control
- [x] Wireless networks
- [x] Mobile computing
- [x] High-speed networks
- [x] Concurrent programming
- [x] Data link layer
- [x] Framing
- [x] Error control
- [x] MAC
- [x] Distributed computation models
- [x] Network management
- [x] Resource control
- [x] Distributed operating systems
- [x] Distributed file systems
- [x] Caching
- [x] Scheduling
- [x] Process migration
- [x] Fault tolerance
- [x] Network security
- [x] Privacy
- [x] Deadlock detection
- [x] Synchronization
- [x] Concurrency control
- [x] CCNA-oriented lab concepts

# CSE 490 SYLLABUS CHECKLIST

- [x] Contemporary CSE field
- [x] Thorough study of current topic
- [x] Intermediate undergraduate accessibility
- [x] Department chair syllabus approval
- [x] Detailed description before registration
- [x] Instructor permission prerequisite

---

# EXAM PRIORITY

### CSE 320 — Must Memorize
**OSI layers, TCP/IP layers, modulation, AM/FM/PM, ASK/FSK/PSK, multiplexing FDM/TDM/WDM, noise/attenuation/distortion, parity/checksum/CRC, ARQ, LAN/WAN, Nyquist, Shannon.**

### CSE 421 — Must Memorize
**TCP vs UDP, transport/session concepts, flow vs congestion control, framing, MAC, data link functions, wireless/mobile/high-speed networks, distributed system concepts, caching, process migration, fault tolerance, deadlock, synchronization, network security.**

### CSE 490 — Must Memorize
**Definition, purpose, contemporary field, syllabus approval, registration description, and instructor permission.**

### Must Practice
**OSI/TCP-IP layer mapping, transmission/modulation questions, Nyquist/Shannon calculations, CRC/parity basics, multiplexing comparisons, TCP/UDP scenarios, flow/congestion control scenarios, framing/MAC concepts, and distributed-system viva questions.**
