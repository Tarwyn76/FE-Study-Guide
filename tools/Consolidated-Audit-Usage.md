# Consolidated FE Technical Audit — Usage

The consolidated audit supports Layers 1, 2, and 3 using the same ledger, figure manifest, PNG directory, and SVG directory.

## Default: audit all layers

From the repository root:

```powershell
python .\tools\technical_audit_all_layers.py
```

The default is equivalent to:

```powershell
python .\tools\technical_audit_all_layers.py --layers 1,2,3
```

## Audit selected layers

Layers 1 and 2 only:

```powershell
python .\tools\technical_audit_all_layers.py --layers 1,2
```

Layer 3 only:

```powershell
python .\tools\technical_audit_all_layers.py --layers 3
```

The expected chapter inventory is derived from `meta/ledger.yaml`, rather than hard-coded chapter counts.

## Chapter discovery

By default, the program recursively scans the repository for Markdown files named:

- `01-##-*.md`
- `02-##-*.md`
- `03-##-*.md`

It excludes tooling, generated validation output, figures, metadata, references, archives/backups, virtual environments, and dependency folders.

If the repository contains archived or alternate manuscripts outside those exclusions, restrict scanning with one or more `--chapter-root` arguments:

```powershell
python .\tools\technical_audit_all_layers.py --layers 1,2,3 `
  --chapter-root .\layer-1 `
  --chapter-root .\layer-2 `
  --chapter-root .\layer-3-tracks
```

`--chapter-root` may be repeated.

## Artwork

Default artwork locations:

```text
figures\png\FIG-LL-CC-NNN.png
figures\svg\FIG-LL-CC-NNN.svg
```

where `LL` is `01`, `02`, or `03`.

Default artwork requirement is `both`. Alternatives:

```powershell
--artwork-mode png
--artwork-mode svg
--artwork-mode either
--artwork-mode both
```

The audit distinguishes missing artwork, incomplete PNG/SVG pairs, generated-but-not-QA-verified artwork, and artwork marked verified in the manifest.

## Output

Default consolidated output:

```text
tools\validation\technical-audit\
```

The CSV/Markdown report names remain compatible with the Layer-3 audit reports.

## Validation

The consolidated script was regression-tested against the current Layer-3 staging repository with `--layers 3`. Its issue counts matched technical audit v6 exactly.
