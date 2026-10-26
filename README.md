# Applying the Phase-1 figure repairs

This package contains corrected chapter copies, repaired/aliased figure assets, a corrected canonical manifest, and updated QA records.

## Automatic application

Run:

```bash
python tools/apply_figure_repairs.py --root /path/to/FE-Supplemental-Guide --manifest /path/to/figure-manifest.csv
```

`--manifest` is optional. When supplied, that file is replaced with `manifests/figure-manifest-fixed.csv`. The script searches the repository recursively for the corrected chapter filenames and copies the supplied figure files into the shortest existing `figures` directory.

The script is idempotent: rerunning it after a successful application makes no additional changes.

## Manual application

1. Replace the matching files in `chapters/`.
2. Copy all files from `figures/` into the guide's figure asset directory.
3. Replace the canonical manifest with `manifests/figure-manifest-fixed.csv`.
4. Keep the files under `meta/` as QA records; they are not manuscript content.

The original project/library files were not overwritten by creation of this package.
