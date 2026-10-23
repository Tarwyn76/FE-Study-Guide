# Reference and Appendix Completeness Report

## References

The release reference structure is now complete at the **bibliographic/provenance level**:

- Layer 1 + Layer 2: unified core register covering **01-01 through 02-70**.
- Layer 3 Chemical: corrected register covering **03-01 through 03-13**.
- Layer 3 Civil: supplied register covering **03-14 through 03-30**.
- Layer 3 ECE: supplied register covering **03-31 through 03-47**.
- Layer 3 Environmental: supplied register covering **03-48 through 03-61**.
- Layer 3 Industrial & Systems: supplied register covering **03-62 through 03-75**.
- Layer 3 Mechanical: supplied register covering **03-76 through 03-90**.
- Layer 3 Other Disciplines: supplied register covering **03-91 through 03-95**.

Latest source audit: **1,375** records; **991 ok** and **384 split_resolved**; **0 unresolved source splits**.

### Reference limitations to preserve

These are verification-level caveats, not missing bibliography:

- Chemical textbook page/chapter locators derived from uploaded indexes should not be represented as sentence-level verification until the underlying pages are inspected.
- Civil AWWA M32 locations identified from a preview/TOC remain locator-level only.
- Standard-level citations without inspected full text remain standard-level citations.

### Chemical register corrections made

- Loh et al. metadata reconciled to *Process Integration and Optimization for Sustainability*, **7**(5), 989–1002 (2023), DOI 10.1007/s41660-022-00288-6.
- IEC Part 4 identified as **IEC TR 61511-4:2020**.
- The obsolete note about `handbook_status: mixed` was replaced with the current audited `in_handbook` + `split_required: true` treatment.

## Appendices generated

1. `appendices/formula-index.md`
   - source: **5,996** audited display formulas;
   - indexed: **1,323** canonical/reusable relations;
   - worked-example arithmetic and boxed numeric substitutions removed.

2. `appendices/notation-master.md`
   - based on the frozen notation contract;
   - includes Handbook-alignment rules, collision rules, structural conventions, reserved subscripts, unit-presentation rules, and verified constants;
   - includes **488** distinct chapter-local notation rows available in current Library snapshots.

3. `appendices/unit-tables.md`
   - SI base and common derived units;
   - common USCS units;
   - metric prefixes;
   - landmark conversions;
   - temperature relations;
   - lbm/lbf and `g_c`;
   - universal gas constant forms;
   - verified constants;
   - **48** chapter-supplied SI/USCS notation rows.

## Remaining integration task

The three appendix files are generated. The remaining repository task is to add them to the guide's build order/table of contents if the build system does not discover appendix files automatically.
