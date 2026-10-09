# Consolidated FE Technical Audit v3 — Usage

Run all layers from the repository root:

```powershell
python .\tools\technical_audit_all_layers.py --layers 1,2,3
```

## v3 corrections

- Ignores LaTeX array/cases row-spacing commands such as `\\[4pt]`, `\\[2mm]`, and `\\[8pt]` when checking `\[` / `\]` display-math balance.
- Recognizes substantive Layer 1 worked solutions even when the chapter uses headings such as `Hypotheses`, `Statistic`, `Critical value`, or direct calculations instead of a literal `**Solution.**` heading.
- Excludes artwork under directories named `archive`, `archives`, `backup`, or `backups`.
- Recursively recognizes current artwork with descriptive suffixes such as `FIG-01-14-003-cofactor-expansion.png`.
- Continues to support Layers 1, 2, and 3 and `--artwork-mode both|either|png|svg`.

Install the supplied `technical_audit_all_layers_fixed.py` as:

```text
tools\technical_audit_all_layers.py
```

Default report directory:

```text
tools\validation\technical-audit\
```
