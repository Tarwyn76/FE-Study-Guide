# FE Audit Framework — 2026-10-23

This package adds validation for the new exam and route assets without changing the stable manuscript audit.

## Files

- `tools/technical_audit_exams.py` — technical/content audit for tier, practice, and test-out exam YAML.
- `tools/audit_routes.py` — checks the seven route markdown files against chapter front-matter route assignments.
- `tools/run_release_audit.py` — master runner that executes manuscript, blueprint, prerequisite, exam, and route audits.

## Development mode

While the 14 full practice exams and seven routes are unfinished:

```powershell
python .\tools\technical_audit_exams.py "E:\Documents\GitHub\FE-Study-Guide" --allow-incomplete
python .\tools\audit_routes.py "E:\Documents\GitHub\FE-Study-Guide" --allow-incomplete
python .\tools\run_release_audit.py "E:\Documents\GitHub\FE-Study-Guide" --development
```

## Strict release mode

```powershell
python .\tools\run_release_audit.py "E:\Documents\GitHub\FE-Study-Guide"
```

Strict mode requires all 10 tier exams, all 14 practice exams, and all seven route files.

## Exam audit outputs

The exam audit writes timestamped files under `audit-results/exams/`:

- `Exam-Audit-Summary(...).md`
- `Exam-Audit-Issues(...).csv`
- `Exam-Audit-Inventory(...).csv`

The route audit writes analogous files under `audit-results/routes/`.
