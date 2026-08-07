# CSE 260 — DIGITAL LOGIC DESIGN
## Short Master Viva Notes
### প্রতিটি syllabus topic: 1–5 lines | English Answer + বাংলা ব্যাখ্যা

---

# 1. Digital System
**English:** A digital system processes information using discrete values, commonly binary 0 and 1. Computers and many communication/information systems are digital systems.  
**বাংলা:** Digital system continuous value-এর বদলে discrete value, সাধারণত 0 ও 1, ব্যবহার করে data process করে।

# 2. Binary Number System
**English:** The binary system uses base 2 and has only two digits: 0 and 1. Digital circuits use binary representation because electronic states can represent two logical levels.  
**বাংলা:** Binary-তে শুধু 0 ও 1 থাকে এবং digital circuit-এর ON/OFF বা HIGH/LOW state দিয়ে সহজে represent করা যায়।

# 3. Bit
**English:** A bit is the smallest unit of digital information and can have a value of 0 or 1.  
**বাংলা:** Bit হলো digital data-এর সবচেয়ে ছোট unit।

# 4. Logic Level
**English:** A logic level represents a binary state using a voltage range, typically interpreted as LOW/0 or HIGH/1.  
**বাংলা:** Circuit-এর voltage range থেকে 0 বা 1 logical state determine করা হয়।

---

# BOOLEAN ALGEBRA

# 5. Boolean Algebra
**English:** Boolean algebra is a mathematical system for manipulating binary variables using logical operations such as AND, OR, and NOT.  
**বাংলা:** 0/1 variable নিয়ে logical operation ও expression simplify করার mathematical system হলো Boolean algebra।

# 6. Boolean Variable
**English:** A Boolean variable can have only two values: 0 or 1.  
**বাংলা:** Boolean variable-এর value শুধু 0 অথবা 1 হতে পারে।

# 7. Boolean Expression
**English:** A Boolean expression combines Boolean variables and logical operators to represent a logical function.  
**বাংলা:** Variable ও logic operator দিয়ে তৈরি expression যা একটি logical function represent করে।

# 8. AND Operation
**English:** AND produces 1 only when all inputs are 1. For two inputs, Y = A·B.  
**বাংলা:** সব input 1 হলেই output 1।

# 9. OR Operation
**English:** OR produces 1 when at least one input is 1. Y = A + B.  
**বাংলা:** যেকোনো একটি input 1 হলেই output 1।

# 10. NOT Operation
**English:** NOT complements its input: Y = A̅. If A=1, Y=0; if A=0, Y=1.  
**বাংলা:** Input-এর opposite output দেয়।

# 11. De Morgan's Laws
**English:** (A·B)̅ = A̅ + B̅ and (A+B)̅ = A̅·B̅.  
**বাংলা:** AND/OR complement করার সময় operation পরিবর্তন হয় এবং প্রতিটি variable complement হয়।

# 12. Identity Laws
**English:** A + 0 = A and A·1 = A.  
**বাংলা:** OR-এর সাথে 0 এবং AND-এর সাথে 1 দিলে original value থাকে।

# 13. Null/Dominance Laws
**English:** A + 1 = 1 and A·0 = 0.  
**বাংলা:** OR-এ 1 এবং AND-এ 0 থাকলে result fixed হয়ে যায়।

# 14. Idempotent Laws
**English:** A + A = A and A·A = A.  
**বাংলা:** একই variable নিজেকেই OR/AND করলে value পরিবর্তন হয় না।

# 15. Complement Laws
**English:** A + A̅ = 1 and A·A̅ = 0.  
**বাংলা:** কোনো variable ও তার complement OR করলে 1, AND করলে 0।

# 16. Absorption Laws
**English:** A + A·B = A and A(A+B)=A.  
**বাংলা:** Extra term eliminate করে Boolean expression simplify করা যায়।

---

# LOGIC GATES

# 17. Logic Gate
**English:** A logic gate is a digital circuit that performs a Boolean operation on one or more inputs to produce an output.  
**বাংলা:** Logic gate input-এর ওপর logical operation করে output দেয়।

# 18. AND Gate
**English:** Output is 1 only when all inputs are 1.  
**বাংলা:** সব input 1 → output 1।

# 19. OR Gate
**English:** Output is 1 when at least one input is 1.  
**বাংলা:** কমপক্ষে একটি input 1 → output 1।

# 20. NOT Gate
**English:** Output is the complement of the input.  
**বাংলা:** Input উল্টে দেয়।

# 21. NAND Gate
**English:** NAND is NOT-AND: Y = (A·B)̅. It is a universal gate.  
**বাংলা:** AND-এর output complement করে; NAND দিয়ে সব basic gate তৈরি করা যায়।

# 22. NOR Gate
**English:** NOR is NOT-OR: Y = (A+B)̅. It is also a universal gate.  
**বাংলা:** OR-এর output complement করে; NOR-ও universal gate।

# 23. XOR Gate
**English:** XOR outputs 1 when its inputs are different. For two inputs, Y=A⊕B=A̅B+AB̅.  
**বাংলা:** দুই input আলাদা হলে 1, same হলে 0।

# 24. XNOR Gate
**English:** XNOR outputs 1 when its inputs are equal. It is the complement of XOR.  
**বাংলা:** দুই input same হলে 1, different হলে 0।

# 25. Universal Gates
**English:** NAND and NOR are universal gates because any Boolean function can be implemented using only NANDs or only NORs.  
**বাংলা:** শুধু NAND অথবা শুধু NOR দিয়েও যেকোনো Boolean circuit বানানো যায়।

---

# COMBINATIONAL LOGIC

# 26. Combinational Circuit
**English:** A combinational circuit's output depends only on the current input values and has no stored state.  
**বাংলা:** Current input-এর ওপর output depend করে; previous state memory হিসেবে থাকে না।

# 27. Sequential Circuit
**English:** A sequential circuit's output depends on current inputs and stored previous state. It uses memory elements such as flip-flops.  
**বাংলা:** Current input + previous state-এর ওপর output depend করে এবং memory থাকে।

# 28. Combinational vs Sequential
**English:** Combinational → no memory, output depends on present inputs. Sequential → memory, output depends on present inputs and past state.  
**বাংলা:** Combinational-এর memory নেই; Sequential-এর memory/state থাকে।

# 29. Half Adder
**English:** A Half Adder adds two 1-bit inputs. Sum = A⊕B and Carry = A·B.  
**বাংলা:** দুইটি 1-bit যোগ করে Sum ও Carry দেয়।

# 30. Full Adder
**English:** A Full Adder adds A, B, and Carry-in. Sum = A⊕B⊕Cin; Cout = AB + ACin + BCin.  
**বাংলা:** দুই bit-এর সাথে আগের carry-ও add করে।

# 31. Half Subtractor
**English:** A Half Subtractor subtracts one bit from another. Difference = A⊕B and Borrow = A̅B.  
**বাংলা:** দুই bit subtraction করে Difference ও Borrow দেয়।

# 32. Full Subtractor
**English:** A Full Subtractor subtracts B and Borrow-in from A and produces Difference and Borrow-out.  
**বাংলা:** Borrow-in সহ bit subtraction করে।

# 33. Ripple Carry Adder
**English:** A ripple-carry adder connects full adders so carry propagates from one stage to the next.  
**বাংলা:** এক stage-এর carry পরের stage-এ যাওয়ার কারণে delay accumulate হতে পারে।

# 34. Decoder
**English:** A decoder converts n input lines into up to 2ⁿ output lines, usually activating one output for each input combination.  
**বাংলা:** n input থেকে সর্বোচ্চ 2ⁿ output line তৈরি করে।

# 35. Encoder
**English:** An encoder performs the reverse conceptual operation of a decoder, converting an active input into a binary code.  
**বাংলা:** Active input line-কে binary code-এ convert করে।

# 36. Priority Encoder
**English:** A priority encoder assigns priority when multiple inputs are active and produces the code of the highest-priority input.  
**বাংলা:** একাধিক input 1 হলে priority অনুযায়ী একটি input select করে।

# 37. Multiplexer (MUX)
**English:** A multiplexer selects one of multiple input signals and sends it to a single output using select lines.  
**বাংলা:** অনেক input-এর মধ্যে একটি select করে output-এ পাঠায়।

# 38. MUX Selection Rule
**English:** A MUX with n select lines can select one of 2ⁿ input lines.  
**বাংলা:** n select line → 2ⁿ input choose করা যায়।

# 39. Demultiplexer (DEMUX)
**English:** A demultiplexer routes one input signal to one of multiple output lines according to select inputs.  
**বাংলা:** একটি input-কে select অনুযায়ী multiple output-এর একটিতে পাঠায়।

# 40. Comparator
**English:** A digital comparator compares binary values and indicates relationships such as A>B, A=B, or A<B.  
**বাংলা:** দুই binary number compare করে বড়, ছোট বা equal কিনা দেখায়।

---

# FLIP-FLOPS

# 41. Flip-Flop
**English:** A flip-flop is a bistable sequential circuit that stores one bit of information.  
**বাংলা:** একটি flip-flop 1 bit state store করতে পারে।

# 42. SR Flip-Flop
**English:** SR means Set-Reset. It has inputs S and R and is used to set or reset the stored state; the exact invalid condition depends on implementation.  
**বাংলা:** S দিয়ে set এবং R দিয়ে reset করা হয়; basic SR latch/flip-flop-এ forbidden state থাকতে পারে।

# 43. D Flip-Flop
**English:** A D flip-flop stores the value of D at the active clock edge. It is commonly used for registers and storage.  
**বাংলা:** Clock edge-এ D-এর value store করে।

# 44. JK Flip-Flop
**English:** JK is an improved SR-type flip-flop. When J=K=1 at the active clock event, the output toggles.  
**বাংলা:** J=K=1 হলে output toggle করে।

# 45. T Flip-Flop
**English:** A T flip-flop toggles when T=1 and holds its state when T=0.  
**বাংলা:** T=1 হলে state change/toggle, T=0 হলে hold।

# 46. Clock
**English:** A clock is a periodic digital signal used to coordinate state changes in synchronous sequential circuits.  
**বাংলা:** Sequential circuit-এর state change synchronize করার timing signal হলো clock।

# 47. Edge Triggering
**English:** An edge-triggered flip-flop changes state at a specified clock transition, usually the rising or falling edge.  
**বাংলা:** Clock-এর নির্দিষ্ট edge-এ state update হয়।

# 48. Setup Time
**English:** Setup time is the minimum time input data must be stable before the active clock edge.  
**বাংলা:** Clock edge-এর আগে data input নির্দিষ্ট সময় stable থাকতে হয়।

# 49. Hold Time
**English:** Hold time is the minimum time input data must remain stable after the active clock edge.  
**বাংলা:** Clock edge-এর পরও input কিছু সময় stable রাখতে হয়।

# 50. Race-Around Condition
**English:** In a level-triggered JK flip-flop, when J=K=1 and the clock pulse is too long, repeated toggling can occur during one clock pulse.  
**বাংলা:** JK-তে J=K=1 এবং clock pulse দীর্ঘ হলে এক clock-এর মধ্যে multiple toggle হতে পারে।

---

# REGISTERS

# 51. Register
**English:** A register is a group of flip-flops used to store multiple bits of binary information.  
**বাংলা:** একাধিক flip-flop একসাথে ব্যবহার করে multiple bit data store করা হয়।

# 52. Shift Register
**English:** A shift register moves stored bits left or right on clock events.  
**বাংলা:** Clock-এর সাথে stored bitগুলো left/right shift করে।

# 53. SISO
**English:** Serial-In Serial-Out shift register accepts data serially and outputs it serially.  
**বাংলা:** Data serially ঢোকে এবং serially বের হয়।

# 54. SIPO
**English:** Serial-In Parallel-Out accepts data serially and makes the stored bits available in parallel.  
**বাংলা:** Serial input নিয়ে parallel output দেয়।

# 55. PISO
**English:** Parallel-In Serial-Out loads multiple bits in parallel and shifts them out serially.  
**বাংলা:** একসাথে multiple bit load করে পরে serially output দেয়।

# 56. PIPO
**English:** Parallel-In Parallel-Out loads and outputs multiple bits in parallel.  
**বাংলা:** Parallelভাবে data load ও output হয়।

---

# COUNTERS

# 57. Counter
**English:** A counter is a sequential circuit that progresses through a prescribed sequence of states in response to clock pulses.  
**বাংলা:** Clock pulse-এর সাথে নির্দিষ্ট state sequence follow করে।

# 58. Asynchronous Counter
**English:** In an asynchronous/ripple counter, only the first flip-flop receives the external clock and later stages are triggered by preceding stages.  
**বাংলা:** সব flip-flop একই clock সরাসরি পায় না; ripple effect-এর কারণে delay হয়।

# 59. Synchronous Counter
**English:** In a synchronous counter, all relevant flip-flops receive the clock simultaneously and combinational logic determines their next states.  
**বাংলা:** সব flip-flop একই clock signal পায়, তাই ripple delay কম।

# 60. Asynchronous vs Synchronous Counter
**English:** Asynchronous → ripple clocking, simpler but slower due to propagation delay. Synchronous → common clock, generally faster and more controlled.  
**বাংলা:** Ripple counter সহজ কিন্তু delay বেশি; synchronous counter দ্রুততর।

# 61. Modulus (MOD) of Counter
**English:** The modulus is the number of distinct states through which a counter cycles before repeating.  
**বাংলা:** Counter repeat করার আগে যতগুলো distinct state নেয় সেটাই MOD।

# 62. MOD-n Counter
**English:** A MOD-n counter has n distinct states. The required number of flip-flops is at least ⌈log₂n⌉.  
**বাংলা:** MOD-n counter-এর জন্য minimum flip-flop = ceil(log₂n)।

# 63. Up Counter
**English:** An up counter progresses through states in increasing numerical order.  
**বাংলা:** Count 0,1,2,3... এভাবে বাড়ে।

# 64. Down Counter
**English:** A down counter progresses through states in decreasing numerical order.  
**বাংলা:** Count উল্টো দিকে কমে।

---

# SEQUENTIAL CIRCUITS

# 65. State
**English:** A state represents the stored information of a sequential circuit at a particular time.  
**বাংলা:** নির্দিষ্ট সময়ে circuit-এর stored condition/state হলো state।

# 66. Present State
**English:** Present state is the current stored state before the next state transition.  
**বাংলা:** Current clock event-এর আগে circuit যে state-এ আছে।

# 67. Next State
**English:** Next state is the state the circuit will enter after the relevant input and clock transition.  
**বাংলা:** পরবর্তী clock transition-এর পরে যে state হবে।

# 68. State Table
**English:** A state table lists present states, inputs, next states, and outputs for a sequential circuit.  
**বাংলা:** Current state + input থেকে next state/output কী হবে তা table-এ দেখায়।

# 69. State Diagram
**English:** A state diagram represents states as nodes and transitions as directed edges labeled by input/output information.  
**বাংলা:** Circle/node দিয়ে state এবং arrow দিয়ে transition দেখানো হয়।

# 70. Sequential Circuit Analysis
**English:** Sequential circuit analysis determines the circuit's behavior by deriving its next-state and output relationships from the existing circuit.  
**বাংলা:** Given circuit থেকে state transition ও output behavior বের করাই analysis।

# 71. Sequential Circuit Design
**English:** Sequential circuit design starts from a required behavior and develops states, transitions, logic equations, and flip-flop implementation.  
**বাংলা:** Requirement থেকে state → state table/diagram → equations → flip-flop circuit design করা হয়।

# 72. State Reduction
**English:** State reduction removes equivalent states while preserving the required input-output behavior.  
**বাংলা:** একই behavior দেওয়া equivalent state combine করে circuit simplify করা যায়।

# 73. State Assignment
**English:** State assignment assigns binary codes to symbolic states for implementation using flip-flops.  
**বাংলা:** প্রতিটি symbolic state-কে binary code দেওয়া হয়।

# 74. Mealy Machine
**English:** In a Mealy machine, output depends on both present state and current input.  
**বাংলা:** Output = present state + current input-এর function।

# 75. Moore Machine
**English:** In a Moore machine, output depends only on the present state.  
**বাংলা:** Output শুধু present state-এর ওপর depend করে।

# 76. Mealy vs Moore
**English:** Mealy output depends on state and input; Moore output depends only on state. Moore outputs are generally less directly sensitive to input changes.  
**বাংলা:** Mealy-তে input directly output-কে affect করতে পারে; Moore-তে state-এর মাধ্যমে output আসে।

---

# ADDERS

# 77. Adder
**English:** An adder is a combinational circuit that performs binary addition.  
**বাংলা:** Binary number যোগ করার digital circuit হলো adder।

# 78. Half Adder vs Full Adder
**English:** Half Adder adds two bits; Full Adder adds two bits plus carry-in.  
**বাংলা:** Full Adder-এর অতিরিক্ত Carry-in থাকে।

# 79. Carry
**English:** Carry is the output bit generated when a binary addition exceeds the capacity of the current bit position.  
**বাংলা:** একটি bit position-এর addition থেকে পরের position-এ যে extra bit যায় সেটাই carry।

---

# SIMPLE COMPUTER ARCHITECTURE

# 80. Computer Architecture
**English:** Computer architecture describes the organization and functional behavior of a computer system, including processor, memory, and I/O.  
**বাংলা:** Computer-এর CPU, memory, input/output এবং তাদের interaction-এর overall organization হলো architecture।

# 81. CPU
**English:** The Central Processing Unit executes instructions and coordinates computation; it includes components such as the ALU and control unit.  
**বাংলা:** CPU instruction execute করে এবং system operation control করে।

# 82. ALU
**English:** The Arithmetic Logic Unit performs arithmetic and logical operations.  
**বাংলা:** Addition, subtraction, AND, OR, comparison ইত্যাদি operation ALU করে।

# 83. Control Unit
**English:** The control unit generates/control signals that coordinate instruction execution and data movement.  
**বাংলা:** Computer-এর বিভিন্ন component কখন কী কাজ করবে তা control signals দিয়ে coordinate করে।

# 84. Register in CPU
**English:** CPU registers are small, fast storage locations used to hold operands, addresses, instructions, or intermediate results.  
**বাংলা:** CPU-এর ভিতরের খুব দ্রুত temporary storage হলো register।

# 85. Memory
**English:** Memory stores instructions and data needed by the computer. Main memory is commonly implemented using RAM and related technologies.  
**বাংলা:** Program instruction ও data temporarily/permanently store করার জন্য memory ব্যবহৃত হয়।

# 86. Input/Output (I/O)
**English:** I/O mechanisms allow a computer to communicate with external devices and systems.  
**বাংলা:** Computer-এর বাইরে device/system-এর সাথে data আদান-প্রদান I/O-এর মাধ্যমে হয়।

# 87. Instruction
**English:** An instruction is a binary-coded command that specifies an operation for the processor to perform.  
**বাংলা:** CPU কী operation করবে তা instruction specify করে।

# 88. Instruction Cycle
**English:** The instruction cycle generally involves fetching an instruction, decoding it, and executing it.  
**বাংলা:** CPU সাধারণভাবে instruction fetch → decode → execute করে।

---

# IMPORTANT TRUTH TABLES

## AND
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## OR
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

## XOR
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## XNOR
| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

# MUST-MEMORIZE FORMULAS

- **Half Adder:** S = A ⊕ B, C = AB
- **Full Adder:** S = A ⊕ B ⊕ Cin
- **Full Adder Carry:** Cout = AB + ACin + BCin
- **Half Subtractor:** D = A ⊕ B, Borrow = A̅B
- **MUX:** n select lines → 2ⁿ inputs
- **Decoder:** n inputs → up to 2ⁿ outputs
- **MOD-n counter:** minimum flip-flops = ⌈log₂n⌉
- **XOR:** A⊕B = A̅B + AB̅
- **XNOR:** A⊙B = AB + A̅B̅

---

# IMPORTANT DIFFERENCES

## Combinational vs Sequential
**Combinational:** No memory; output depends on present inputs.  
**Sequential:** Has state/memory; output depends on present inputs and previous state.  
**বাংলা:** Memory থাকলে সাধারণত sequential circuit।

## Latch vs Flip-Flop
**Latch:** Level-sensitive.  
**Flip-Flop:** Commonly edge-triggered.  
**বাংলা:** Latch level অনুযায়ী এবং flip-flop সাধারণত clock edge অনুযায়ী state change করে।

## Synchronous vs Asynchronous Counter
**Synchronous:** Common clock to flip-flops.  
**Asynchronous:** Ripple triggering between stages.  
**বাংলা:** Synchronous দ্রুততর; asynchronous-এ propagation delay বেশি।

## Encoder vs Decoder
**Encoder:** 2ⁿ inputs → n-bit code conceptually.  
**Decoder:** n inputs → up to 2ⁿ outputs.  
**বাংলা:** Encoder code বানায়; Decoder code decode করে।

## MUX vs DEMUX
**MUX:** Many inputs → one output.  
**DEMUX:** One input → one of many outputs.  
**বাংলা:** MUX data select করে; DEMUX data route করে।

## Half Adder vs Full Adder
**Half:** 2 inputs, no Cin.  
**Full:** 2 input bits + Cin.  
**বাংলা:** Full Adder previous carry handle করে।

## XOR vs XNOR
**XOR:** Different inputs → 1.  
**XNOR:** Same inputs → 1.  
**বাংলা:** XOR = difference detector; XNOR = equality detector।

## Mealy vs Moore
**Mealy:** Output = state + input.  
**Moore:** Output = state only.  
**বাংলা:** Mealy output input change-এর সাথে directly change করতে পারে।

---

# LAST-MINUTE VIVA — 20 MUST KNOW

1. **What is Boolean algebra?** A mathematical system for manipulating binary variables and logical operations.
2. **Which are universal gates?** NAND and NOR.
3. **What does XOR do?** Outputs 1 when inputs are different.
4. **What does XNOR do?** Outputs 1 when inputs are equal.
5. **What is a combinational circuit?** Output depends only on present inputs.
6. **What is a sequential circuit?** Output depends on present inputs and stored state.
7. **What is a flip-flop?** A one-bit bistable storage element.
8. **What is a register?** A group of flip-flops used to store multiple bits.
9. **What is a MUX?** Selects one of many inputs to one output.
10. **What is a decoder?** Converts n input bits into up to 2ⁿ output lines.
11. **What is an encoder?** Converts an active input into a binary code.
12. **What is a Half Adder?** Adds two bits and produces Sum and Carry.
13. **What is a Full Adder?** Adds two bits and Carry-in.
14. **What is an asynchronous counter?** A ripple counter where stages are triggered successively.
15. **What is a synchronous counter?** All relevant flip-flops receive the same clock.
16. **What is MOD-n?** A counter with n distinct states.
17. **What is a D flip-flop?** Stores D at the active clock edge.
18. **What is a JK flip-flop?** A flip-flop where J=K=1 causes toggle at the active clock event.
19. **Mealy vs Moore?** Mealy output depends on state+input; Moore output depends on state.
20. **Basic CPU components?** ALU, control unit, registers, memory, and I/O-related components.

---

# CSE 260 SYLLABUS COVERAGE CHECKLIST

- [x] Digital systems
- [x] Computer systems
- [x] Communication systems
- [x] Information systems
- [x] Boolean algebra
- [x] Digital logic gates
- [x] Combinational logic circuits
- [x] Decoders
- [x] Encoders
- [x] Multiplexers
- [x] Asynchronous counters
- [x] Synchronous counters
- [x] Registers
- [x] Flip-flops
- [x] Adders
- [x] Sequential circuit analysis
- [x] Sequential circuit design
- [x] Simple computer architecture
- [x] Digital logic lab concepts

---

# EXAM PRIORITY

### Must Memorize
**Boolean laws, De Morgan's laws, all basic gate functions/truth tables, NAND/NOR as universal gates, Half/Full Adder formulas, MUX/Decoder relationships, flip-flop behavior, counter differences, MOD-n formula, Mealy vs Moore, basic CPU components.**

### Must Practice
**Truth tables → Boolean simplification → gate implementation → Half/Full Adder → MUX/Decoder/Encoder problems → flip-flop excitation/state tables → counter sequence → basic sequential circuit analysis/design.**
