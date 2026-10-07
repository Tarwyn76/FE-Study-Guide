# Chemical Track — References and Source Provenance

## Purpose

This file records source provenance for the Chemical-track material that is either marked `split_required: true` or is specification-required but not directly developed in the FE Reference Handbook.

A `split_required` concept combines material that is directly supported by the FE Reference Handbook with application, synthesis, workflow, or discipline-specific guidance developed in this guide. Other entries may be `not_in_handbook` concepts that require an authoritative external source.

**Provenance policy:** The FE Reference Handbook 10.6 and the FE Chemical specification remain the exam-facing authorities. Perry's, Felder/Rousseau/Bullard, CCPS publications, ANSI/ISA 5.1, and IEC 61511 are supplemental technical authorities used to support material that the FE Handbook does not fully develop. Where the guide combines several sources into a teaching workflow, the result is identified as **guide synthesis based on** those sources rather than being attributed to one source.

## Common sources

### NCEES FE Reference Handbook

National Council of Examiners for Engineering and Surveying (NCEES). *FE Reference Handbook*, Version 10.6.

The page numbers below are printed-page references recorded in `meta/ledger.yaml`.

### FE Chemical specification

NCEES FE Chemical examination specification as reproduced/mapped in the FE Reference Handbook 10.6 Appendix, printed pp. 478–481.

The specification establishes that the listed subjects belong within the FE Chemical route. It is not, by itself, a tutorial or technical derivation source.

### Perry's Chemical Engineers' Handbook, 9th Edition

Green, Don W., and Marylee Z. Southard, eds. *Perry's Chemical Engineers' Handbook*. 9th ed. McGraw-Hill Education, 2019.

ISBN: **9780071834087**

This is the most recent edition identified for the project. Page/section references below use the chapter-page notation shown in the uploaded index, such as `8-14 to 8-16`.

### Elementary Principles of Chemical Processes, 4th Edition

Felder, Richard M., Ronald W. Rousseau, and Lisa G. Bullard. *Elementary Principles of Chemical Processes*. 4th ed. John Wiley & Sons, 2016.

ISBN: **9780470616291**

Page references below use the printed-page numbers shown in the uploaded index.

### Layer of Protection Analysis: Simplified Process Risk Assessment

*Layer of Protection Analysis: Simplified Process Risk Assessment*. Published October 2001.

ISBN: **978-0-8169-0811-0**

Used in this project for Layer of Protection Analysis (LOPA), independent protection layer concepts, and risk-reduction logic in the Chemical process-safety material.

### Guidelines for Inherently Safer Chemical Processes: A Life Cycle Approach, 3rd Edition

*Guidelines for Inherently Safer Chemical Processes: A Life Cycle Approach*. 3rd ed. Published October 2019.

ISBN: **978-1-119-52922-4**

Used in this project for inherently safer design principles and life-cycle application of inherent-safety strategies.

### ANSI/ISA 5.1-2024 — Instrumentation Symbols and Identification

ANSI/ISA 5.1-2024. *Instrumentation Symbols and Identification*.

Used in this project as the primary standards reference for instrumentation identification, P&ID symbols, tag conventions, and related drawing notation.

### IEC 61511 — Functional Safety for the Process Industry Sector

The following IEC 61511 references are used for safety-instrumented-system concepts, the relationship between process control and safety functions, and safety-integrity-level determination:

- **IEC 61511-1:2016** — *Functional safety - Safety instrumented systems for the process industry sector - Part 1: Framework, definitions, system, hardware and application programming requirements*.
- **IEC 61511-2:2016** — *Functional safety - Safety instrumented systems for the process industry sector - Part 2: Guidelines for the application of IEC 61511-1:2016*.
- **IEC 61511-3:2016** — *Functional safety - Safety instrumented systems for the process industry sector - Part 3: Guidance for the determination of the required safety integrity levels*.
- **IEC 61511-3:2020** — *Functional safety - Safety instrumented systems for the process industry sector - Part 4: Explanation and rationale for changes in IEC 61511-1 from Edition 1 to Edition 2*.

**Metadata note:** The project information supplied for Part 4 did not include its publication year or document identifier beyond the Part 4 title; those fields are intentionally not inferred here.

---


## CHE-3-001-07 — Coupled Material-and-Energy Balance Workflow

**Chapter:** 03-01, §1.7  
**Concept:** Coupled Material-and-Energy Balance Workflow

**External source actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Thermodynamics / First Law — Open Systems, printed pp. 147–149.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 8 items A and C.

**Internal dependency**
- `CHE-3-001-06` — Steady Nonreactive Energy Balances.

**Handbook-supported content**
- Steady-flow/open-system first-law framework.
- Enthalpy and control-volume energy-balance relationships used in the calculation.

**Guide-developed content**
- The workflow for solving a coupled material-and-energy problem in a particular order.
- The recommendation to establish the process basis and stream balances before closing the energy balance.

**Additional external sources**
- Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed.:
  - Material balances, pp. 91–173.
  - Multiple-unit processes, pp. 116–122.
  - Energy balances, pp. 360–379.
  - Energy-balance procedures, pp. 372–375.
  - Steady-state open-system energy balances, pp. 362–367.
  - Nonreactive process balances, pp. 402–456.

These references support the sequencing and coupling of material and energy balances beyond the FE Handbook's compact equation set.

---

## CHE-3-007-02 — Stripping as the Reverse Gas-Liquid Operation

**Chapter:** 03-07, §7.2  
**Concept:** Stripping as the Reverse Gas-Liquid Operation

**External source actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Chemical Engineering / Absorption (Packed Columns), printed p. 253.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 10 items C and E.

**Internal dependency**
- `CHE-3-007-01` — Packed-Column Absorption — NTU and HTU.

**Handbook-supported content**
- Packed-column gas-liquid mass-transfer relationships.
- Transfer-unit/film concepts carried over from absorption.

**Guide-developed content**
- Explicitly framing stripping as the reverse-direction gas-liquid operation.
- Application guidance for reversing the desired solute-transfer direction while retaining the same mass-transfer framework.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Stripping equations and gas-liquid stripping treatment, Chapter 14, approximately 14-13 to 14-15.
  - Gas stripping applications, 20-94 to 20-95.
- Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed.:
  - Gas absorption and gas-liquid systems, including absorption and multicomponent gas-liquid equilibrium material.

Perry's is the primary outside source for the stripping-specific application framework.

---

## CHE-3-008-02 — Humidification and Dehumidification Balances

**Chapter:** 03-08, §8.2  
**Concept:** Humidification and Dehumidification Balances

**External source actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Thermodynamics / Psychrometrics, printed pp. 149–150.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 10 item F.

**Internal dependencies**
- `CHE-3-008-01` — Humid-Air Variables for Chemical Operations.
- `THERMO-2D-049-06` — Layer 2 psychrometric-humidity concept.

**Handbook-supported content**
- Psychrometric variables and relations.
- Humidity-ratio and humid-air property relationships.

**Guide-developed content**
- The chemical-process humidifier/dehumidifier material-balance workflow.
- Using dry-air flow as the conserved carrier basis and combining water and energy balances for process calculations.

**Additional external sources**
- Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed.:
  - Dehumidification, p. 284.
  - Humidification, p. 284.
  - Gas-liquid systems, pp. 284–290.
  - Humidity and psychrometric charts, pp. 432–440.
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Humidity and air-water-system material indexed in Chapter 12.

Felder/Rousseau/Bullard is the primary outside source for the process-balance treatment used here.

---

## CHE-3-008-07 — Energy Use and Process Selection

**Chapter:** 03-08, §8.7  
**Concept:** Energy Use and Process Selection

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Thermodynamics / Psychrometrics, printed pp. 149–150.
- Heat Transfer, printed pp. 209–224.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 10 item F.

**Internal dependency**
- `CHE-3-008-06` — Single-Effect Evaporation Balances.

**Handbook-supported content**
- Psychrometric property relations.
- General heat-transfer relations and thermal-resistance concepts.

**Guide-developed content**
- Combining heat and mass transfer to compare process alternatives.
- Process-selection guidance based on energy use, moisture-removal duty, and operating constraints.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Drying and humidification material in Chapter 12.
  - Dryer modeling, design, and scale-up material in Chapter 12.
  - Process-selection and energy-conservation material where indexed for the relevant unit operation.
- Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed.:
  - Nonreactive process balances, pp. 402–456.
  - Phase-change operations, pp. 424–443.
  - Psychrometric charts, pp. 432–440.

These references support the energy-use comparison and the combination of heat- and mass-transfer considerations used in process selection.

---

## CHE-3-012-03 — Equipment Selection and First-Pass Sizing

**Chapter:** 03-12, §12.3  
**Concept:** Equipment Selection and First-Pass Sizing

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- General core engineering sections used for equipment-duty equations, printed pp. 181–224.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 14 items A–E.

**Internal dependency**
- `CHE-3-012-02` — Piping and Instrumentation Diagrams.

**Handbook-supported content**
- Governing engineering relations used for duties and first-pass calculations, including fluid-mechanics and heat-transfer relationships within the cited page range.

**Guide-developed content**
- The general workflow:
  `required duty → governing equation → size → check constraints`.
- Choosing an equipment class from process duty and then applying the appropriate equation as a first-pass sizing method.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Equipment sizing and design material throughout the equipment chapters.
  - Equipment sizing is indexed at 9-11, with equipment-specific selection and design procedures distributed through the handbook.

Perry's is the primary outside reference for first-pass equipment selection and sizing practice.

---

## CHE-3-012-04 — Scale-Up and Similarity

**Chapter:** 03-12, §12.4  
**Concept:** Scale-Up and Similarity

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Fluid Mechanics / dimensionless groups and scaling laws, printed pp. 186–200.
- Chemical Engineering / cost scaling, printed pp. 263–264.
- FE Chemical specification mapping, Appendix pp. 478–481, Area 14 items A–E.

**Internal dependency**
- `CHE-3-012-03` — Equipment Selection and First-Pass Sizing.

**Handbook-supported content**
- Dimensionless groups and fluid-mechanics similarity/scaling relationships.
- Cost-capacity scaling relations.

**Guide-developed content**
- Combining geometric, dynamic, transport, and economic scaling considerations into a general chemical-process scale-up workflow.
- Guidance on deciding which similarity criterion controls a particular scale-up problem.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Mixer scale-up, 18-29 to 18-30.
  - Dryer design/modeling/scale-up material in Chapter 12.
  - Additional operation-specific scale-up entries throughout the handbook.
- Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed.:
  - Dimensional homogeneity, pp. 19–20.
  - Dimensionless groups and quantities, pp. 20–21.

Together these support the guide's use of similarity criteria, dimensionless analysis, and operation-specific scale-up reasoning.

---

## CHE-3-013-03 — Feedback, Feedforward, Cascade, and Ratio Control

**Chapter:** 03-13, §13.3  
**Concept:** Feedback, Feedforward, Cascade, and Ratio Control

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Instrumentation, Measurement, and Control / Feedback Control, printed pp. 231–234.
- FE Chemical specification mapping, Appendix pp. 478–481, Areas 14D–E, 15A–C, and 16C/D/F.

**Internal foundation identified by the chapter**
- Layer 2F control-system relationships.

**Handbook-supported content**
- General feedback-control relationships and control-system fundamentals.

**Guide-developed content**
- Side-by-side selection and interpretation of feedback, feedforward, cascade, and ratio control for chemical-process applications.
- Chemical-process examples used to distinguish the control strategies.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Feedback control, Chapter 8.
  - Feedforward control, Chapter 8.
  - Cascade control, approximately 8-19 to 8-20.
  - Ratio and related process-control strategies within Chapter 8.

Perry's is the primary outside source for selecting and distinguishing chemical-process control strategies.

---

## CHE-3-013-04 — Process Dynamics and Controller Tuning

**Chapter:** 03-13, §13.4  
**Concept:** Process Dynamics and Controller Tuning

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Instrumentation, Measurement, and Control / Dynamic Response and PID, printed pp. 231–234.
- FE Chemical specification mapping, Appendix pp. 478–481, Areas 14D–E, 15A–C, and 16C/D/F.

**Internal dependencies**
- `CHE-3-013-03` — Feedback, Feedforward, Cascade, and Ratio Control.
- `CTRL-2F-069-01` — Layer 2 transfer-function/dynamic-response concept.
- `CTRL-2F-070-04` — Layer 2 PID-control concept.

**Handbook-supported content**
- Dynamic-response and PID-control fundamentals.
- Transfer-function and controller relations inherited through Layer 2.

**Guide-developed content**
- Applying first-order-plus-dead-time and PID ideas specifically to chemical-process loops.
- Tuning interpretation involving actuator limits, process dead time, measurement noise, and safety constraints.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Controller tuning, approximately 8-14 to 8-16.
  - Dynamic response and controller behavior throughout Chapter 8.
  - Autotune and adaptive-control material where indexed.

Perry's directly supports the practical controller-tuning and dynamic-response guidance added beyond the FE Handbook.

---

## CHE-3-013-05 — Control Valves, DCS/PLC, Alarms, and Interlocks

**Chapter:** 03-13, §13.5  
**Concept:** Control Valves, DCS/PLC, Alarms, and Interlocks

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Instrumentation, Measurement, and Control / Control-Loop Hardware, printed pp. 225–234.
- FE Chemical specification mapping, Appendix pp. 478–481, Areas 14D–E, 15A–C, and 16C/D/F.

**Internal dependencies**
- `CHE-3-013-04` — Process Dynamics and Controller Tuning.
- `CTRL-2F-070-07` — Layer 2 control-loop hardware concept.

**Handbook-supported content**
- Sensors, final elements, and general control-loop hardware concepts.

**Guide-developed content**
- Integrating control valves, DCS/PLC functions, alarms, and interlocks into a chemical-process control/protection architecture.
- Distinguishing a regulatory-control function from an interlock/protective action.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Control valves, approximately 8-66 to 8-69.
  - Distributed control and automation material in Chapter 8.
  - Programmable-control material in Chapter 8.
  - Alarms, 8-84 to 8-85.
  - Actuators and final control elements, including 8-68 to 8-69 and 8-74.
- IEC 61511-1:2016:
  - Framework and requirements for safety instrumented systems in the process industry.
  - Used to distinguish ordinary regulatory control from safety-instrumented protective functions where the guide makes that distinction.
- IEC 61511-2:2016:
  - Application guidance for IEC 61511-1.
- IEC 61511-3:2016:
  - Guidance for determining required safety integrity levels.
- IEC 61511-4:2020:
  - Explanatory/rationale material concerning the Edition 1-to-Edition 2 changes in IEC 61511-1.

Perry's remains the principal explanatory process-control source; IEC 61511 is the standards authority when the discussion crosses from ordinary control hardware into safety-instrumented functions.

---

## CHE-3-013-07 — Relief, Inerting, Runaway Reactions, and Protection Layers

**Chapter:** 03-13, §13.7  
**Concept:** Relief, Inerting, Runaway Reactions, and Protection Layers

**External sources actually recorded**
- NCEES, *FE Reference Handbook*, Version 10.6.
- Safety / Safety Systems and Flammability Fundamentals, printed pp. 15–23.
- FE Chemical specification mapping, Appendix pp. 478–481, Areas 14D–E, 15A–C, and 16C/D/F.

**Internal dependencies**
- `CHE-3-013-06` — HAZOP, LOPA, Fault Trees, and Event Trees.
- `SAFE-2B-019-07` — Layer 2 pressure-relief/safety concept.

**Handbook-supported content**
- General safety-system and flammability fundamentals.
- Pressure-relief concepts inherited from the safety prerequisite.

**Guide-developed content**
- Integrating relief, inerting, runaway-reaction awareness, controls, interlocks, containment, and procedures as protection layers.
- Application-level statements about how those layers differ in purpose.

**Additional external sources**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed.:
  - Process safety material in Chapter 23.
  - Runaway reactions, approximately 23-20.
  - HAZOP, approximately 23-24.
  - Inerting/inert-gas hazard-control material in Chapter 23.
  - Pressure-relief systems and relief-device design material beginning around 23-57.
- *Layer of Protection Analysis: Simplified Process Risk Assessment* (October 2001), ISBN 978-0-8169-0811-0:
  - Used for LOPA methodology, independent protection layers, and the relationship between initiating-event likelihood and risk reduction.
- IEC 61511-1:2016, IEC 61511-2:2016, and IEC 61511-3:2016:
  - Used when protection-layer discussion specifically involves safety instrumented systems or safety integrity levels.

Perry's is the primary broad process-safety reference; the LOPA publication and IEC 61511 provide the specialized methodology and functional-safety framework.

---

# Additional Chemical Concepts Covered by the New Sources

## CHE-3-012-02 — Piping and Instrumentation Diagrams

**Chapter:** 03-12, §12.2  
**Concept:** Piping and Instrumentation Diagrams  
**Ledger status:** `not_in_handbook`

**Primary external source**
- ANSI/ISA 5.1-2024, *Instrumentation Symbols and Identification*.

**Supported content**
- Instrument identification.
- P&ID instrumentation symbols and functional identification.
- Tagging and drawing conventions used when the guide presents standardized instrumentation notation.

**Secondary explanatory source**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed., process instrumentation/P&ID material in Chapter 8.

**Source boundary**
- ANSI/ISA 5.1 is the standards authority for symbol and identification conventions.
- The guide may simplify a full industrial P&ID to FE-study scope; such simplification is guide synthesis and should not be represented as the complete ISA standard.

---

## CHE-3-013-02 — Sustainability, Efficiency, and Inherently Safer Design

**Chapter:** 03-13, §13.2  
**Concept:** Sustainability, Efficiency, and Inherently Safer Design  
**Ledger status:** `not_in_handbook`

**Primary external source**
- *Guidelines for Inherently Safer Chemical Processes: A Life Cycle Approach*, 3rd ed., October 2019, ISBN 978-1-119-52922-4.

**Supported content**
- Inherently safer design philosophy.
- Application of inherent-safety strategies over the process life cycle.
- The concepts of reducing or eliminating hazards by design rather than relying solely on add-on protective systems.

**Secondary source**
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed., process-safety material in Chapter 23.

**Source boundary**
- Sustainability and efficiency material that is not specifically part of inherent-safety methodology may require separate support from the FE specification, Perry's, or another engineering-sustainability source.

---

## CHE-3-013-06 — HAZOP, LOPA, Fault Trees, and Event Trees

**Chapter:** 03-13, §13.6  
**Concept:** HAZOP, LOPA, Fault Trees, and Event Trees  
**Ledger status:** `not_in_handbook`

**Primary external sources**
- *Layer of Protection Analysis: Simplified Process Risk Assessment*, October 2001, ISBN 978-0-8169-0811-0.
- Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed., process-hazard-analysis material in Chapter 23, including HAZOP coverage around 23-24.

**Functional-safety supporting sources**
- IEC 61511-1:2016.
- IEC 61511-2:2016.
- IEC 61511-3:2016.
- IEC 61511-4:2020, explanatory/rationale document for Edition 1-to-Edition 2 changes.

**Supported content**
- LOPA methodology and independent protection layers.
- HAZOP as a structured hazard-identification method.
- Relationship between protection layers and safety instrumented functions.
- SIL determination where the guide explicitly introduces that connection.

**Remaining source boundary**
- The supplied references do not, from the metadata alone, establish detailed fault-tree or event-tree methodology. Perry's may support these topics, but the actual referenced pages should be verified before treating it as the direct source. If the chapter develops quantitative fault-tree/event-tree analysis beyond a conceptual FE-level description, a dedicated risk-analysis reference may still be warranted.

---

## CHE-3-013-05 — Control Valves, DCS/PLC, Alarms, and Interlocks

**Chapter:** 03-13, §13.5  
**Concept:** Control Valves, DCS/PLC, Alarms, and Interlocks  
**Ledger status:** `split_required: true`

**Additional standards support**
- IEC 61511-1:2016 for the process-industry SIS framework and system requirements.
- IEC 61511-2:2016 for application guidance.
- IEC 61511-3:2016 for SIL determination guidance.
- IEC 61511-4:2020 for explanatory/rationale context regarding the Edition 2 changes.

**Use in the guide**
- These standards are cited only when the chapter distinguishes a normal control function from a safety instrumented function or discusses SIL/SIS concepts.
- Ordinary DCS, PLC, alarm, sensor, and control-valve descriptions remain primarily supported by Perry's and the FE Handbook control material.

---

## CHE-3-013-07 — Relief, Inerting, Runaway Reactions, and Protection Layers

**Chapter:** 03-13, §13.7  
**Concept:** Relief, Inerting, Runaway Reactions, and Protection Layers  
**Ledger status:** `split_required: true`

**Additional specialized sources**
- *Layer of Protection Analysis: Simplified Process Risk Assessment*, October 2001, ISBN 978-0-8169-0811-0.
- IEC 61511-1:2016.
- IEC 61511-2:2016.
- IEC 61511-3:2016.

**Use in the guide**
- LOPA source: protection-layer independence and risk-reduction logic.
- IEC 61511 source: safety instrumented functions and safety integrity where those are part of the protection-layer discussion.
- Perry's remains the broad source for relief, inerting, runaway-reaction hazards, and process-safety hardware.

---

# Source Coverage Status

The two added chemical-engineering references substantially close the earlier outside-source gap for the ten `split_required` concepts.

- **Elementary Principles of Chemical Processes, 4th ed.** is the principal outside source for coupled material/energy balances and humidification/dehumidification balance workflows.
- **Perry's Chemical Engineers' Handbook, 9th ed.** is the principal broad outside source for stripping, equipment selection/sizing, scale-up, process control, control hardware, and process safety.
- **ANSI/ISA 5.1-2024** is the standards authority used for P&ID instrumentation symbols and identification.
- **Guidelines for Inherently Safer Chemical Processes: A Life Cycle Approach, 3rd ed. (2019)** is the dedicated source for inherently safer process design.
- **Layer of Protection Analysis: Simplified Process Risk Assessment (2001)** is the dedicated source for LOPA and independent protection layer methodology.
- **IEC 61511 Parts 1–3 (2016), plus the supplied Part 4 explanatory/rationale reference**, provide the functional-safety/SIS framework where the Chemical track discusses safety instrumented functions or SILs.
- The **NCEES FE Reference Handbook 10.6** remains the exam-facing source and lookup reference.
- The **FE Chemical specification** remains the route/coverage authority.

## Remaining verification requirement

The uploaded files are indexes, not the full books. The page and chapter ranges above identify the appropriate source locations, but final publication should still verify the actual text on those pages before claiming that a specific sentence, workflow, or example is directly supported.

Where a guide statement synthesizes multiple sources rather than reproducing one source's treatment, label it as **guide synthesis based on** the cited references rather than claiming a single-source derivation.

# Ledger Classification Note

The current records use `handbook_status: mixed`. The schema for `meta/ledger.yaml` defines only:

- `in_handbook`
- `in_handbook_memorize_anyway`
- `not_in_handbook`

For these ten atoms, the cleaner representation is:

```yaml
handbook_status: in_handbook
split_required: true
```

with the `notes` field explicitly stating which portion is Handbook-supported and which portion is guide-developed. This preserves source provenance without introducing an unsupported `mixed` status.
