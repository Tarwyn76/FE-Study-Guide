# Aligned `verify_examples.py`

This version is aligned with `technical_audit_all_layers_fixed_v7.py`.

## What changed

1. Default scope is now **Layers 1-3**, matching the technical audit.
2. `--include-layer0` is available when orientation examples should also be checked.
3. Worked-example parsing uses the technical audit's heading, prompt-marker, solution-marker, and H2-boundary conventions.
4. A numeric verification candidate must:
   - contain a numeric token in the parsed problem, and
   - pass the same `expects_numeric_result()` intent heuristic used by the technical audit.
5. The normal run still writes:
   - `meta/example-verification-results.csv`
   - `meta/example-verification-summary.md`

## Run

From `tools/`:

```powershell
python .\verify_examples.py
```

Optional Layer 0:

```powershell
python .\verify_examples.py --include-layer0
```

Release gate:

```powershell
python .\verify_examples.py --strict
```

Do not use `--strict` until independent VERIFY metadata has been populated.
