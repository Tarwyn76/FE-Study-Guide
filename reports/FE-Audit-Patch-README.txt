FE Supplemental Guide — 2026-10-10 16:27 audit patch

Run:
  python apply_fe_audit_fixes_20261010.py E:\Documents\GitHub\FE-Study-Guide

This patch edits the repository in place and creates .bak files beside every changed chapter.

Changes:
- Fixes the 2 formula_suspicious_text warnings in 01-37.
- Replaces 84 generic answer-key entries (15–18 in 02-01 through 02-21)
  with chapter-specific explanations, addressing the 8 remaining warning-level
  repeated-solution groups.
- Reformats 232 Learning Objectives bullets in 01-02 through 01-23 to the
  audit parser's expected format without changing objective wording.
- Adds explicit units/dimensional substitutions to the 27 worked examples
  flagged for solution-unit review.
- Restores FIG-01-02-001 through FIG-01-02-010 at their original chapter
  section placements. These 10 references disappeared between the 16:19 and
  16:27 audits even though their PNG/SVG artwork still exists.

The patch is intentionally surgical: it does not replace whole chapter files,
so previously applied terminology/source-boundary corrections remain intact.
