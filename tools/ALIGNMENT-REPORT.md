# Verifier Alignment Report

Basis: `Technical-Audit-Worked-Examples(20261023-182522).csv`

- Technical-audit worked-example rows: **1788**
- Aligned numeric-result candidates using the technical audit's intent rule: **436**
- Default verifier scope: **Layers 1-3**
- Layer 0: excluded unless `--include-layer0` is supplied

The previous verifier reported 1,175 numeric candidates because it treated
numeric context/units as enough to require verification.  The aligned rule
requires both numeric content and a prompt that actually requests a numeric
result.

Expected result on the unchanged local repository:
- worked examples: approximately **1,788**
- numeric-result candidates: approximately **436**
- tagged candidates: **0** until VERIFY metadata is added
