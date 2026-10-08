# Civil Track References and Source Reconciliation

This register reconciles the 34 Civil `split_required` concept atoms. Supplied source files receive page/section-level references where the supplied material supports them. All other references are cited at the publication/standard level only, as requested; no page or clause location is asserted for those sources.

## Verification levels

- **uploaded-content-verified** — the supplied file contains the cited substantive material and a page/section location is recorded.
- **uploaded-preview-TOC-verified** — the supplied preview establishes the chapter/page range, but the complete cited chapter content is not present in the preview.
- **standard-citation-no-page** — bibliographic/standard citation assigned without a page or clause claim.

## Atom-to-source mapping

| Concept ID | Concept | External source support | Verification |
|---|---|---|---|
| CIV-3-014-01 | Concrete mix proportions, water-cement ratio, and strength | ACI211 | uploaded-content-verified |
| CIV-3-014-02 | Asphalt binder, aggregate gradation, and volumetrics | MS2 | uploaded-content-verified |
| CIV-3-014-03 | Aggregate gradation, specific gravity, absorption, and durability | MS2, ASTM_AGG | uploaded-content-verified, standard-citation-no-page |
| CIV-3-014-04 | Concrete testing — slump, cylinders, air, and unit weight | ACI211, ASTM_CONC | uploaded-content-verified, standard-citation-no-page |
| CIV-3-014-05 | Asphalt, aggregate, and wood test methods | MS2, WOOD, ASTM_MAT | uploaded-content-verified, uploaded-content-verified, standard-citation-no-page |
| CIV-3-014-06 | Physical and mechanical properties of metals and wood | WOOD, ASTM_MAT | uploaded-content-verified, standard-citation-no-page |
| CIV-3-015-03 | Coordinate systems and horizontal positioning | GHILANI | standard-citation-no-page |
| CIV-3-015-06 | Area computations from coordinates and offsets | GHILANI | standard-citation-no-page |
| CIV-3-016-02 | Rainfall intensity, duration, frequency, and design storms | HEC22 | uploaded-content-verified |
| CIV-3-016-03 | Infiltration, abstraction, and effective rainfall | HEC22, HECHMS | uploaded-content-verified, standard-citation-no-page |
| CIV-3-017-07 | Channel controls, normal depth, and gradually varied flow | HECRAS | standard-citation-no-page |
| CIV-3-018-04 | Network continuity and loop energy balance | M32 | uploaded-preview-TOC-verified |
| CIV-3-018-06 | Water distribution storage, pressure, and service constraints | M32, M42 | uploaded-preview-TOC-verified, uploaded-content-verified |
| CIV-3-018-07 | Gravity collection systems and sewer flow concepts | WEF_FD5 | standard-citation-no-page |
| CIV-3-019-01 | Flood-frequency concepts and design-event selection | B17C | standard-citation-no-page |
| CIV-3-019-02 | Reservoir and detention continuity | HEC22, HECHMS | uploaded-content-verified, standard-citation-no-page |
| CIV-3-019-04 | Stormwater detention sizing and outlet control | HEC22 | uploaded-content-verified |
| CIV-3-019-06 | Dams, freeboard, and flood-control operating concepts | DS13 | uploaded-content-verified |
| CIV-3-020-04 | Unconfined aquifers and water-table concepts | FITTS | standard-citation-no-page |
| CIV-3-020-06 | Multiple wells, superposition, and interference | FITTS | standard-citation-no-page |
| CIV-3-020-07 | Seepage, effective stress, and groundwater-structure interaction | FITTS, DAS_GEO | standard-citation-no-page, standard-citation-no-page |
| CIV-3-021-01 | Water-quality concentration, loading, and mass balance | DAVIS | standard-citation-no-page |
| CIV-3-021-02 | Basic water chemistry — pH, alkalinity, hardness, and equilibrium concepts | DAVIS | standard-citation-no-page |
| CIV-3-021-04 | Drinking-water treatment train | DAVIS | standard-citation-no-page |
| CIV-3-021-06 | Wastewater biological treatment and oxygen demand | METCALF | standard-citation-no-page |
| CIV-3-022-07 | Load combinations and design-demand organization | ASCE7 | standard-citation-no-page |
| CIV-3-024-03 | Inelastic versus elastic column behavior | HIBBELER_MOM | standard-citation-no-page |
| CIV-3-024-04 | Compatibility in indeterminate structures | HIBBELER_SA | standard-citation-no-page |
| CIV-3-025-05 | Beam shear and serviceability | AISC | standard-citation-no-page |
| CIV-3-026-04 | Reinforced concrete beam shear | ACI318 | standard-citation-no-page |
| CIV-3-026-07 | Beam-column interaction and eccentric loading | ACI318 | standard-citation-no-page |
| CIV-3-028-03 | Retaining-wall stability checks | DAS_FOUND | standard-citation-no-page |
| CIV-3-028-06 | Consolidation and settlement | DAS_GEO, DAS_FOUND | standard-citation-no-page, standard-citation-no-page |
| CIV-3-028-07 | Slope stability and stabilization | DAS_GEO | standard-citation-no-page |

## Source details

### ACI211

ACI Committee 211. (2022). *Selecting Proportions for Normal-Density and High-Density Concrete—Guide* (ACI PRC-211.1-22). American Concrete Institute. ISBN 978-1-64195-186-9.

**Verification:** `uploaded-content-verified`

**Location/status:** Chapter 3 pp. 4–5 (w/cm, strength, durability); §4.7 p. 8; Chapter 5 pp. 13–14; Chapters 8–9 pp. 21–28.

### MS2

Asphalt Institute. (2014). *Asphalt Mix Design Methods* (MS-2, 7th ed.). Asphalt Institute. ISBN 978-1-934154-70-0.

**Verification:** `uploaded-content-verified`

**Location/status:** pp. 12–14 (volumetric characteristics); p. 24 (aggregate gradation); pp. 34–45 (laboratory mixture testing); pp. 46–61 (specific gravities, absorption, and volumetric properties).

### ASTM_AGG

ASTM International. *ASTM C136/C136M, Standard Test Method for Sieve Analysis of Fine and Coarse Aggregates*; *ASTM C127, Standard Test Method for Relative Density (Specific Gravity) and Absorption of Coarse Aggregate*; *ASTM C128, Standard Test Method for Relative Density (Specific Gravity) and Absorption of Fine Aggregate*; and *ASTM C88/C88M, Standard Test Method for Soundness of Aggregates by Use of Sodium Sulfate or Magnesium Sulfate*.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim; cited at standard level per user instruction.

### ASTM_CONC

ASTM International. *ASTM C143/C143M, Standard Test Method for Slump of Hydraulic-Cement Concrete*; *ASTM C39/C39M, Standard Test Method for Compressive Strength of Cylindrical Concrete Specimens*; *ASTM C231/C231M* and *ASTM C173/C173M* for air content; and *ASTM C138/C138M* for density (unit weight), yield, and gravimetric air content.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim; cited at standard level per user instruction.

### WOOD

Forest Products Laboratory. (2021). *Wood Handbook—Wood as an Engineering Material*. General Technical Report FPL-GTR-282. U.S. Department of Agriculture, Forest Service, Forest Products Laboratory.

**Verification:** `uploaded-content-verified`

**Location/status:** Chapter 4, pp. 4-1–4-22 (physical/moisture properties); Chapter 5, pp. 5-1–5-44 (mechanical properties); p. 5-26 notes ASTM D143-based test procedures.

### ASTM_MAT

ASTM International. *ASTM D143, Standard Test Methods for Small Clear Specimens of Timber*; and *ASTM E8/E8M, Standard Test Methods for Tension Testing of Metallic Materials*.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim; cited at standard level per user instruction.

### GHILANI

Ghilani, C. D. (2022). *Elementary Surveying: An Introduction to Geomatics* (16th ed.). Pearson. ISBN 978-0-13-682282-0.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### HEC22

Kilgore, R., Atayee, A. T., & Herrmann, G. R. (2024). *Urban Drainage Design* (Hydraulic Engineering Circular No. 22, 4th ed., FHWA-HIF-24-006). Federal Highway Administration.

**Verification:** `uploaded-content-verified`

**Location/status:** Chapter 4, pp. 21–24 for rainfall/IDF/design-storm and runoff concepts; Chapter 10, pp. 182–229 for detention, stage-storage/stage-discharge, routing, and outlet control.

### HECHMS

U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-HMS Technical Reference Manual* (CPD-74B), current online edition.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### HECRAS

U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-RAS Hydraulic Reference Manual*, Version 6.6.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### M32

Robinson, L., Edwards, J. A., & Willnow, L. D. (2012). *Computer Modeling of Water Distribution Systems* (AWWA Manual M32, 3rd ed.). American Water Works Association. ISBN 978-1-58321-864-8.

**Verification:** `uploaded-preview-TOC-verified`

**Location/status:** Uploaded preview confirms Chapter 5, pp. 103–123 (steady-state simulation/system design criteria) and Chapter 6, pp. 125–146 (extended-period simulation); the preview does not contain the complete chapter text.

### M42

American Water Works Association. (1998). *Steel Water-Storage Tanks* (AWWA Manual M42, 1st ed.). American Water Works Association. ISBN 0-89867-977-X.

**Verification:** `uploaded-content-verified`

**Location/status:** Chapter 5, pp. 53–56 (storage sizing, peak demand, fire flow, operating levels); Chapter 8, pp. 85–86 (operation, pressure, controls).

### WEF_FD5

Water Environment Federation & American Society of Civil Engineers. (2007). *Gravity Sanitary Sewer Design and Construction* (MOP FD-5, 2nd ed.). Water Environment Federation.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### B17C

England, J. F., Jr., Cohn, T. A., Faber, B. A., Stedinger, J. R., Thomas, W. O., Jr., Veilleux, A. G., Kiang, J. E., & Mason, R. R., Jr. (2018). *Guidelines for Determining Flood Flow Frequency—Bulletin 17C* (ver. 1.1, May 2019). U.S. Geological Survey Techniques and Methods, Book 4, Chapter B5. https://doi.org/10.3133/tm4B5

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### DS13

U.S. Bureau of Reclamation. (2021). *Design Standards No. 13: Embankment Dams, Chapter 6—Freeboard* (DS-13(6)-2.1, Phase 4 Final). U.S. Department of the Interior.

**Verification:** `uploaded-content-verified`

**Location/status:** Chapter 6, pp. 6-1–6-22; especially §§6.2.1–6.2.3 for minimum, normal, and intermediate freeboard and §6.5 for other freeboard factors.

### FITTS

Fitts, C. R. (2022). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### DAS_GEO

Das, B. M. (2022). *Principles of Geotechnical Engineering* (10th ed.). Cengage. ISBN 978-0-357-42047-8.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### DAVIS

Davis, M. L. (2020). *Water and Wastewater Engineering: Design Principles and Practice* (2nd ed.). McGraw Hill. ISBN 978-1-260-13227-4.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### METCALF

Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw Hill. ISBN 978-0-07-340118-8.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### ASCE7

American Society of Civil Engineers. (2022). *Minimum Design Loads and Associated Criteria for Buildings and Other Structures* (ASCE/SEI 7-22). ASCE.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### HIBBELER_MOM

Hibbeler, R. C. (2023). *Mechanics of Materials* (11th ed.). Pearson. ISBN 978-0-13-760561-3.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### HIBBELER_SA

Hibbeler, R. C. (2024). *Structural Analysis* (11th ed.). Pearson. ISBN 978-0-13-802625-7.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### AISC

American Institute of Steel Construction. (2022). *Specification for Structural Steel Buildings* (ANSI/AISC 360-22). AISC. See also *Steel Construction Manual*, 16th ed. (2023).

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### ACI318

ACI Committee 318. (2025). *Building Code for Structural Concrete—Code Requirements and Commentary* (ACI CODE-318-25). American Concrete Institute.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

### DAS_FOUND

Das, B. M. (2024). *Principles of Foundation Engineering* (10th ed.). Cengage. ISBN 978-0-357-68465-8.

**Verification:** `standard-citation-no-page`

**Location/status:** No page-level claim.

## Release-use rule

For `uploaded-content-verified` sources, the recorded page/section locations may be used as source-location references for the supported Civil concepts. For `uploaded-preview-TOC-verified` sources, the page range is a TOC-confirmed locator rather than a claim that every statement was checked on that page. For `standard-citation-no-page` sources, cite the publication/standard as a whole unless a later source upload permits page/clause verification.