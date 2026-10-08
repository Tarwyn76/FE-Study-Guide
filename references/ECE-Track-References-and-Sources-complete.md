# Electrical & Computer Track — References and Source Reconciliation

This register supports Layer 3 Chapters 03-31 through 03-47. The FE Reference Handbook remains the exam reference. External references are used for specification-required learned/application content and technical verification. Unless a source is later supplied and inspected directly, external references are cited at the publication/standard level without page-level claims.

## Chapter reference map

| Chapter | Subject | Recommended external reference(s) |
|---|---|---|
| 03-31 | Semiconductor Materials, Energy Bands, Doping, and p-n Junctions | SZE_NG |
| 03-32 | Diodes, Rectifiers, Thyristors, and Device Models | SEDRA |
| 03-33 | BJT and MOSFET Biasing and Small-Signal Models | SEDRA |
| 03-34 | Single-Stage, Differential, and Operational Amplifiers | SEDRA, WEBSTER_EREN, IEEE1451 |
| 03-35 | Power Electronics — Rectifiers, Converters, Inverters, and Switching | ERICKSON |
| 03-36 | Power Systems — Transmission, Distribution, Losses, and Voltage Regulation | GLOVER |
| 03-37 | Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations | GRIFFITHS |
| 03-38 | Electromagnetic Waves and Transmission Lines | POZAR |
| 03-39 | Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models | OPPENHEIM, DORF |
| 03-40 | Communications — AM, FM, PM, PCM, Bandwidth, and Noise | PROAKIS |
| 03-41 | Multiplexing and Digital Communications | PROAKIS |
| 03-42 | Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization | HARRIS |
| 03-43 | Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs | HARRIS |
| 03-44 | Computer Systems — Microprocessors, Memory, and Interfacing | PATTERSON |
| 03-45 | Computer Networks — Routing, Switching, Topologies, and TCP/IP | KUROSE, RFC1812, IEEE8021Q |
| 03-46 | Cybersecurity — Security Triad, Firewalls, Detection, Scanning, and Vulnerability Testing | NIST80094, NIST80053, NIST800115 |
| 03-47 | Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing | CLRS, ISO29119 |

## Split-required atom reconciliation

| Concept ID | Concept | External support | Verification level |
|---|---|---|---|
| ECE-3-031-05 | Drift, diffusion, and junction formation | SZE_NG | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-032-02 | Diode operating point and load-line analysis | SEDRA | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-033-02 | BJT load line and Q-point selection | SEDRA | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-034-01 | Common-emitter gain, inversion, and small-signal loading | SEDRA | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-034-07 | Instrumentation chain, sensors, and data-acquisition interfaces | WEBSTER_EREN, IEEE1451 | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-035-01 | Power-switching devices and idealized switching states | ERICKSON | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-035-05 | Inductor current ripple and capacitor voltage ripple | ERICKSON | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-036-03 | Transmission/distribution voltage drop and losses | GLOVER | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-036-04 | Power factor correction and reactive compensation | GLOVER | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-038-06 | Matched lines, power transfer, and termination | POZAR | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-039-04 | Transfer functions, poles, zeros, and frequency response | DORF | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-041-05 | Forward error correction and redundancy | PROAKIS | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-044-01 | Processor datapath, control, and instruction execution | PATTERSON | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-045-04 | Routing, switching, and forwarding decisions | KUROSE, RFC1812, IEEE8021Q | Web-verified bibliographic/standard citation; no page-level claim |
| ECE-3-046-04 | Endpoint and network detection/prevention | NIST80094, NIST80053 | Web-verified bibliographic/standard citation; no page-level claim |

## Bibliography and source scope

### SZE_NG

Sze, S. M., & Ng, K. K. (2006). *Physics of Semiconductor Devices* (3rd ed.). Wiley. Print ISBN 978-0-471-14323-9. DOI: 10.1002/0470068329.

**Supporting scope:** Semiconductor carrier transport, p-n junction physics, depletion regions, and semiconductor devices.

**Authoritative/publisher page:** https://onlinelibrary.wiley.com/doi/book/10.1002/0470068329

### SEDRA

Sedra, A. S., Smith, K. C., Carusone, T. C., & Gaudet, V. (2020). *Microelectronic Circuits* (8th ed.). Oxford University Press. ISBN 978-0-19-085346-4.

**Supporting scope:** Diodes, BJT/MOSFET bias, small-signal models, single-stage amplifiers, differential amplifiers, and op amps.

**Authoritative/publisher page:** https://books.google.com/books?id=nxarxAEACAAJ

### WEBSTER_EREN

Webster, J. G., & Eren, H. (Eds.). (2014). *Measurement, Instrumentation, and Sensors Handbook* (2nd ed.). CRC Press.

**Supporting scope:** Measurement chains, sensors, instrumentation, signal conditioning, and data acquisition.

**Authoritative/publisher page:** https://www.routledge.com/Measurement-Instrumentation-and-Sensors-Handbook-Electromagnetic-Op/Eren-Webster/p/book/9781439848913

### IEEE1451

IEEE. (2024). *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Common Functions, Communication Protocols, and Transducer Electronic Data Sheet (TEDS) Formats* (IEEE Std 1451.0-2024).

**Supporting scope:** Standardized smart-transducer interfaces, services, communications, and TEDS.

**Authoritative/publisher page:** https://standards.ieee.org/ieee/1451.0/11001/

### ERICKSON

Erickson, R. W., & Maksimović, D. (2020). *Fundamentals of Power Electronics* (3rd ed.). Springer. Hardcover ISBN 978-3-030-43879-1. DOI: 10.1007/978-3-030-43881-4.

**Supporting scope:** Power-switching devices, converter steady-state models, ripple, switching losses, and efficiency.

**Authoritative/publisher page:** https://link.springer.com/book/10.1007/978-3-030-43881-4

### GLOVER

Glover, J. D., Sarma, M. S., Overbye, T. J., & Birchfield, A. B. (2022). *Power System Analysis & Design* (7th ed.). Cengage Learning. ISBN 978-0-357-67619-6.

**Supporting scope:** Transmission/distribution modeling, voltage drop, losses, three-phase power, reactive power, and compensation.

**Authoritative/publisher page:** https://books.google.com/books?id=ouqPzgEACAAJ

### GRIFFITHS

Griffiths, D. J. (2023). *Introduction to Electrodynamics* (5th ed.). Cambridge University Press. ISBN 978-1-009-39775-9. DOI: 10.1017/9781009397735.

**Supporting scope:** Electrostatics, magnetostatics, induction, Maxwell equations, and electromagnetic waves.

**Authoritative/publisher page:** https://www.cambridge.org/highereducation/books/introduction-to-electrodynamics/FD23E188E2BDCDB40199CFE3386EC08F

### POZAR

Pozar, D. M. (2011). *Microwave Engineering* (4th ed.). Wiley. ISBN 978-0-470-63155-3.

**Supporting scope:** Transmission lines, characteristic impedance, reflection, standing waves, matching, and impedance transformation.

**Authoritative/publisher page:** https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553

### OPPENHEIM

Oppenheim, A. V., Willsky, A. S., & Nawab, S. H. (1996). *Signals and Systems* (2nd ed.). Prentice Hall/Pearson. ISBN 978-0-13-814757-0.

**Supporting scope:** LTI systems, convolution, Fourier methods, sampling, transform models, and discrete-time systems.

**Authoritative/publisher page:** https://www.pearson.com/en-us/subject-catalog/p/signals-and-systems/P200000003155/9780136169390

### DORF

Dorf, R. C., & Bishop, R. H. (2021). *Modern Control Systems* (14th ed.). Pearson.

**Supporting scope:** Transfer functions, poles, zeros, frequency response, Bode methods, and feedback-system interpretation.

**Authoritative/publisher page:** https://www.pearson.com/en-us/subject-catalog/p/modern-control-systems/P200000003484/9780137307098

### PROAKIS

Proakis, J. G., & Salehi, M. (2008). *Digital Communications* (5th ed.). McGraw-Hill. ISBN 978-0-07-295716-7.

**Supporting scope:** Digital modulation, bandwidth, coding, detection, error control, and digital communication systems.

**Authoritative/publisher page:** https://search.worldcat.org/title/1006307680

### HARRIS

Harris, S. L., & Harris, D. (2021). *Digital Design and Computer Architecture, RISC-V Edition*. Morgan Kaufmann. ISBN 978-0-12-820064-3.

**Supporting scope:** Combinational/sequential logic, timing, finite-state machines, programmable logic, and digital-system organization.

**Authoritative/publisher page:** https://www.sciencedirect.com/book/9780128200643/digital-design-and-computer-architecture

### PATTERSON

Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware/Software Interface* (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-12-820331-6.

**Supporting scope:** Processor datapaths, control, instruction execution, memory hierarchy, cache organization, I/O, and parallelism.

**Authoritative/publisher page:** https://shop.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6

### KUROSE

Kurose, J. F., & Ross, K. W. (2025). *Computer Networking: A Top-Down Approach* (9th ed.). Pearson. Print ISBN 978-0-13-542933-4.

**Supporting scope:** Layered networking, routing and forwarding, IP addressing, transport behavior, LANs, and network delay.

**Authoritative/publisher page:** https://www.pearson.com/en-us/subject-catalog/p/computer-networking/P200000013385

### RFC1812

Baker, F. (Ed.). (1995). *Requirements for IP Version 4 Routers* (RFC 1812). Internet Engineering Task Force / RFC Editor.

**Supporting scope:** IPv4 router forwarding behavior and forwarding decisions.

**Authoritative/publisher page:** https://www.rfc-editor.org/info/rfc1812/

### IEEE8021Q

IEEE. (2022). *IEEE Standard for Local and Metropolitan Area Networks—Bridges and Bridged Networks* (IEEE Std 802.1Q-2022).

**Supporting scope:** MAC bridges, bridged networks, switching, and VLAN operation.

**Authoritative/publisher page:** https://standards.ieee.org/ieee/802.1Q/10323/

### NIST80094

Scarfone, K., & Mell, P. (2007). *Guide to Intrusion Detection and Prevention Systems (IDPS)* (NIST SP 800-94). National Institute of Standards and Technology. DOI: 10.6028/NIST.SP.800-94.

**Supporting scope:** Network-based and host-based intrusion detection/prevention technologies and deployment.

**Authoritative/publisher page:** https://csrc.nist.gov/pubs/sp/800/94/final

### NIST80053

National Institute of Standards and Technology. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST SP 800-53 Rev. 5). DOI: 10.6028/NIST.SP.800-53r5.

**Supporting scope:** Security controls including system monitoring and detection.

**Authoritative/publisher page:** https://www.nist.gov/publications/security-and-privacy-controls-information-systems-and-organizations

### NIST800115

Scarfone, K., Souppaya, M., Cody, A., & Orebaugh, A. (2008). *Technical Guide to Information Security Testing and Assessment* (NIST SP 800-115). National Institute of Standards and Technology. DOI: 10.6028/NIST.SP.800-115.

**Supporting scope:** Security testing, vulnerability scanning, penetration testing, planning, authorization, and assessment.

**Authoritative/publisher page:** https://csrc.nist.gov/pubs/sp/800/115/final

### CLRS

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. ISBN 978-0-262-04630-5.

**Supporting scope:** Algorithms, asymptotic complexity, searching, sorting, data structures, trees, and graph algorithms.

**Authoritative/publisher page:** https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

### ISO29119

ISO/IEC/IEEE. (2022). *Software and systems engineering—Software testing—Part 1: General concepts* (ISO/IEC/IEEE 29119-1:2022).

**Supporting scope:** General concepts and terminology for software testing.

**Authoritative/publisher page:** https://www.iso.org/standard/81291.html

## Source-boundary rule

- **FE-Handbook-supported** — directly supported by the FE Reference Handbook location recorded in the ledger.
- **Externally supported** — required by the FE Electrical and Computer specification but not fully developed in the Handbook.
- **Guide synthesis** — explanatory linkage, worked examples, study workflow, and teaching structure created for the supplemental guide.

A split-required atom remains `split_required: true`; that field records mixed-source scope. It is resolved when its Handbook basis, external support, and guide-synthesis boundary are explicit.
