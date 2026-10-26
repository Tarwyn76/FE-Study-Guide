# Worked Example Verification Summary

- Scope: **Layers 0-3**
- Worked examples found: **3**
- Numeric-result candidates: **2**
- Tagged numeric candidates: **1**
- Independent VERIFY checks: **4**
- VERIFY tags on non-required examples: **0**
- Curated numeric-candidate exclusions: **1**
- Failures: **0**
- Coverage reviews: **0**

## Classification rule

The numeric-candidate rule is aligned to `technical_audit_all_layers_fixed_v7.py`: the parsed problem must contain a numeric token and the prompt must ask for a numeric result. Classification/model-selection/explanation/symbolic tasks that merely contain numbers are not verification-required by this heuristic.

## Interpretation

A coverage review means the example was classified as requiring a numeric result but does not yet have independent machine-readable verification metadata. It is not, by itself, evidence that the worked example is wrong.
