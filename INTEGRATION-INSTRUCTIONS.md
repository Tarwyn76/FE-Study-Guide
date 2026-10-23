# Integration Instructions

Copy these three files into the repository `tools/` directory:

- `technical_audit_exams.py`
- `audit_routes.py`
- `run_release_audit.py`

Keep the existing:

- `technical_audit_all_layers_fixed_v7.py`
- `check_exam_blueprints.py`
- `check_tier_review_blueprints.py`
- `check_item_prereqs.py`

During development:

```powershell
python .\tools\technical_audit_exams.py "E:\Documents\GitHub\FE-Study-Guide" --allow-incomplete
python .\tools\audit_routes.py "E:\Documents\GitHub\FE-Study-Guide" --allow-incomplete
python .\tools\run_release_audit.py "E:\Documents\GitHub\FE-Study-Guide" --development
```

For final release gating:

```powershell
python .\tools\run_release_audit.py "E:\Documents\GitHub\FE-Study-Guide"
```

The strict release run requires all 10 tier exams, 14 practice exams, and seven route files.
