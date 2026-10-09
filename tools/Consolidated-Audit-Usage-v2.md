# Consolidated FE Technical Audit v2 — Usage

This version audits Layers 1, 2, and 3 and fixes the principal false positives found in the first all-layer run.

## Important v2 changes

- Recognizes Layer 1 Worked Examples that use `Given`, `Find`, `Approach`, `Fast approach`, `Verification`, and `Check` instead of only `Problem` / `Solution`.
- Recognizes early Layer 2 `Worked Example — Model Check` blocks without reporting parser-format differences as missing-problem errors.
- Treats percent and common engineering-prefix displays correctly in simple arithmetic checks (for example `0.40 = 40%`, seconds to milliseconds, volts to millivolts).
- Recursively discovers artwork under the configured PNG/SVG directories **and their parent `figures` directory**.
- Accepts artwork filenames with descriptive suffixes, e.g. `FIG-01-14-003-cofactor-expansion.png`, not only `FIG-01-14-003.png`.
- Supports `FIG-01-*`, `FIG-02-*`, and `FIG-03-*`.

## Run all layers

```powershell
python .\tools\technical_audit_all_layers.py --layers 1,2,3
```

## Layer-specific runs

```powershell
python .\tools\technical_audit_all_layers.py --layers 1
python .\tools\technical_audit_all_layers.py --layers 2
python .\tools\technical_audit_all_layers.py --layers 3
```

## Artwork

The default requirement remains both PNG and SVG. The recursive scanner checks the configured `figures\png` and `figures\svg` locations and also searches their parent `figures` tree for nested/batched artwork or filenames containing a descriptive suffix.

## Regression check

v2 was regression-tested against the current Layer 3 staging repository. It preserved the Layer 3 audit result exactly while removing format/parser false positives from representative Layer 1 and Layer 2 chapters.
