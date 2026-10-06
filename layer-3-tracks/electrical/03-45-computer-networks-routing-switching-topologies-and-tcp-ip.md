---
chapter: "03-45"
title: "Computer Networks — Routing, Switching, Topologies, and TCP/IP"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-045-01, ECE-3-045-02, ECE-3-045-03, ECE-3-045-04, ECE-3-045-05, ECE-3-045-06, ECE-3-045-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-45: Computer Networks — Routing, Switching, Topologies, and TCP/IP

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-044-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Computer Networks — Routing, Switching, Topologies, and TCP/IP**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **45.1** Explain and apply **Packet switching, hosts, routers, and link-layer switches**.
* **45.2** Explain and apply **OSI and TCP/IP layered models**.
* **45.3** Explain and apply **IPv4/IPv6 addressing and CIDR**.
* **45.4** Explain and apply **Routing, switching, and forwarding decisions**.
* **45.5** Explain and apply **TCP, UDP, reliability, and transport behavior**.
* **45.6** Explain and apply **LAN configuration, DHCP, SLAAC, and topologies**.
* **45.7** Explain and apply **End-to-end delay, throughput, and bottlenecks**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 45.1 Packet switching, hosts, routers, and link-layer switches

Packet-switched networks divide application data into packets that may traverse shared network infrastructure. Hosts originate/terminate traffic; routers forward between networks; switches forward within links/LANs.

\[\text{message}\rightarrow\text{packets}\rightarrow\text{network}\rightarrow\text{reassembly}\]

![FIG-03-45-001: LAN and WAN diagram showing hosts, switches, routers, links, and packet path.](../figures/FIG-03-45-001-packet-switching-hosts-routers-and-link-layer-switches.png)

### Worked Example 1

**Problem.** A router normally makes forwarding decisions using network-layer addressing.

**Solution.** Use the relation and model in §45.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.2 OSI and TCP/IP layered models

Layering separates functions and interfaces. Encapsulation adds protocol headers as data moves down the stack and removes them on receipt.

\[\text{application}\rightarrow\text{transport}\rightarrow\text{internet/network}\rightarrow\text{link}\]

![FIG-03-45-002: OSI and TCP/IP stacks with encapsulation from application message to segment, packet, and frame.](../figures/FIG-03-45-002-osi-and-tcp-ip-layered-models.png)

### Worked Example 2

**Problem.** A TCP segment is encapsulated inside an IP packet and then a link-layer frame.

**Solution.** Use the relation and model in §45.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.3 IPv4/IPv6 addressing and CIDR

IPv4 uses 32-bit addresses and IPv6 uses 128-bit addresses. CIDR prefix length identifies the network portion without classful assumptions.

\[\text{prefix length}=\text{number of leading network bits}\]

![FIG-03-45-003: IPv4 and IPv6 address formats with CIDR prefix and host/interface portions.](../figures/FIG-03-45-003-ipv4-ipv6-addressing-and-cidr.png)

### Worked Example 3

**Problem.** A /24 IPv4 prefix leaves 8 address bits outside the network prefix.

**Solution.** Use the relation and model in §45.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.4 Routing, switching, and forwarding decisions

Switches use link-layer information to forward frames within a LAN; routers use network-layer routes to move packets between networks. Routing builds/chooses paths; forwarding applies those decisions per packet.

\[\text{destination}\rightarrow\text{lookup}\rightarrow\text{next hop or output port}\]

![FIG-03-45-004: Switch MAC table and router forwarding table applied to a multi-subnet topology.](../figures/FIG-03-45-004-routing-switching-and-forwarding-decisions.png)

### Worked Example 4

**Problem.** Traffic between two IP subnets normally requires a router or Layer-3 forwarding function.

**Solution.** Use the relation and model in §45.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.5 TCP, UDP, reliability, and transport behavior

TCP is connection-oriented and supplies mechanisms for reliable ordered delivery; UDP is connectionless with lower protocol overhead and no delivery guarantee.

\[d_{trans}=\frac{L}{R}\]

![FIG-03-45-005: TCP handshake/reliable byte stream contrasted with UDP datagrams between two hosts.](../figures/FIG-03-45-005-tcp-udp-reliability-and-transport-behavior.png)

### Worked Example 5

**Problem.** Streaming or request/response applications choose transport behavior based on reliability, latency, and application requirements.

**Solution.** Use the relation and model in §45.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.6 LAN configuration, DHCP, SLAAC, and topologies

LANs may use static configuration, DHCP for IPv4-style configuration, or IPv6 autoconfiguration mechanisms. Physical/logical topologies include star, bus, ring, mesh, and tree.

\[\text{device joins network}\rightarrow\text{address/configuration}\rightarrow\text{local forwarding}\]

![FIG-03-45-006: Star, bus, ring, mesh, and tree topology sketches plus DHCP/SLAAC configuration flow.](../figures/FIG-03-45-006-lan-configuration-dhcp-slaac-and-topologies.png)

### Worked Example 6

**Problem.** Modern switched Ethernet LANs are commonly arranged physically as stars around switches.

**Solution.** Use the relation and model in §45.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 45.7 End-to-end delay, throughput, and bottlenecks

Network performance is limited by the slowest relevant resource and by accumulated delays. Packet size, link rate, distance, congestion, and protocol behavior all contribute.

\[d_{total}=d_{proc}+d_{queue}+d_{trans}+d_{prop}\]

![FIG-03-45-007: Packet path with processing, queueing, transmission, and propagation delay annotated at each hop.](../figures/FIG-03-45-007-end-to-end-delay-throughput-and-bottlenecks.png)

### Worked Example 7

**Problem.** On a long high-speed link, propagation delay can dominate even when transmission delay is small.

**Solution.** Use the relation and model in §45.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. Re-select the appropriate piecewise model or system state and solve again. Algebraic consistency does not override the model's validity conditions.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 14; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using packet-switched network outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using network protocol layering outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using IP addressing outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using routing and switching outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using transport protocol behavior outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using local area network topology outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using network performance outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| packet-switched network | Concept developed in §45.1; apply with that section's stated model and conventions. |
| network protocol layering | Concept developed in §45.2; apply with that section's stated model and conventions. |
| IP addressing | Concept developed in §45.3; apply with that section's stated model and conventions. |
| routing and switching | Concept developed in §45.4; apply with that section's stated model and conventions. |
| transport protocol behavior | Concept developed in §45.5; apply with that section's stated model and conventions. |
| local area network topology | Concept developed in §45.6; apply with that section's stated model and conventions. |
| network performance | Concept developed in §45.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **packet-switched network** and identify the governing relation, state variable, or decision it organizes.

2. Define **network protocol layering** and identify the governing relation, state variable, or decision it organizes.

3. Define **IP addressing** and identify the governing relation, state variable, or decision it organizes.

4. Define **routing and switching** and identify the governing relation, state variable, or decision it organizes.

5. Define **transport protocol behavior** and identify the governing relation, state variable, or decision it organizes.

6. Define **local area network topology** and identify the governing relation, state variable, or decision it organizes.

7. Define **network performance** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **packet-switched network**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **network protocol layering**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **IP addressing**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **routing and switching**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **transport protocol behavior**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **local area network topology**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **network performance**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **packet-switched network**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **network protocol layering**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **IP addressing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **routing and switching**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **transport protocol behavior**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **local area network topology**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **network performance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **packet-switched network**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **network protocol layering**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **packet-switched network** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **network protocol layering** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **IP addressing** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **routing and switching** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **transport protocol behavior** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **local area network topology** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **network performance** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **packet-switched network**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **network protocol layering**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **IP addressing**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **routing and switching**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **transport protocol behavior**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **local area network topology**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **network performance**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. The same symbol or equation can represent different physical behavior outside its valid device region, frequency range, timing model, or protocol abstraction.

16. The Handbook is the exam reference; using its definitions prevents hidden differences in constants, RMS/peak values, sign convention, or model form.

17. Algebra can be internally consistent while predicting an impossible device state, voltage, timing relationship, address range, or complexity claim. The physical/logical model must also be satisfied.

18. Limiting cases and order-of-magnitude checks expose sign errors, impossible gains, invalid probabilities, unrealistic timing, and model misuse.

19. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

20. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

21. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

22. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

23. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

24. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

25. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

26. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

27. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.


---

## Practice Problems

1. A router normally makes forwarding decisions using network-layer addressing.

2. A TCP segment is encapsulated inside an IP packet and then a link-layer frame.

3. A /24 IPv4 prefix leaves 8 address bits outside the network prefix.

4. Traffic between two IP subnets normally requires a router or Layer-3 forwarding function.

5. Streaming or request/response applications choose transport behavior based on reliability, latency, and application requirements.

6. Modern switched Ethernet LANs are commonly arranged physically as stars around switches.

7. On a long high-speed link, propagation delay can dominate even when transmission delay is small.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §45.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §45.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §45.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §45.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §45.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §45.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §45.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 14, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 14.

- **packet-switched network:** Packet switching, hosts, routers, and link-layer switches
- **network protocol layering:** OSI and TCP/IP layered models
- **IP addressing:** IPv4/IPv6 addressing and CIDR
- **routing and switching:** Routing, switching, and forwarding decisions
- **transport protocol behavior:** TCP, UDP, reliability, and transport behavior
- **local area network topology:** LAN configuration, DHCP, SLAAC, and topologies
- **network performance:** End-to-end delay, throughput, and bottlenecks

---

## What's Next

**Chapter 03-46: Cybersecurity — Security Triad, Firewalls, Detection, Scanning, and Vulnerability Testing**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
