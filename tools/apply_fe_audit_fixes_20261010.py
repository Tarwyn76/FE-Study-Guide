#!/usr/bin/env python3
"""
Apply the FE Supplemental Guide audit fixes identified in the
2026-10-10 16:27:51 technical audit without replacing whole chapter files.

Edits:
  1. 01-37: convert two rollback instructions incorrectly formatted as display math to prose.
  2. 02-01..02-21: replace answer-key items 15-18 with chapter-specific explanations.
  3. 01-02..01-23: normalize Learning Objectives bullets to the audit's expected format.
  4. Correct 27 worked-example unit-review cases with explicit dimensional substitutions
     or explicit dimensionless interpretation.

Usage:
    python apply_fe_audit_fixes_20261010.py E:\\Documents\\GitHub\\FE-Study-Guide

The script searches recursively for the chapter filenames. It refuses to edit when a
target chapter is missing or ambiguous. A .bak file is created beside every edited file.
"""

from __future__ import annotations
import argparse
import re
import shutil
from pathlib import Path

ANSWER_FIXES = {
"02-01":[
"First verify the facts that affect public welfare: who could be harmed, how severe the consequence could be, and whether reliable evidence supports the suspected hazard.",
"A rule can be applied correctly to the wrong ethical issue. The decision must still account for public safety, competence, conflicts of interest, disclosure duties, and the actual facts.",
"A written chronology shows what the engineer knew, when it was known, what warnings were issued, and how responsible parties responded; that record matters when professional conduct is evaluated.",
"Check that the proposed action protects public welfare, stays within the engineer's competence and authority, and is supported by documented facts rather than assumption."
],
"02-02":[
"First verify the governing jurisdiction and the engineer's legal role, because licensure requirements, exemptions, sealing authority, and responsible-charge duties depend on where and how the work is performed.",
"A correctly remembered Model Law rule may not control the case if the jurisdiction adopted different language or if the engineer is not actually the person in responsible charge.",
"Documenting who made technical decisions and when they were reviewed establishes whether responsible charge was genuinely exercised rather than merely claimed afterward.",
"Check the applicable jurisdictional requirement, the engineer's license status and scope, and whether any signing or sealing action reflects genuine responsible charge over the work."
],
"02-03":[
"First verify the controlling contract language and the parties' actual duties, including scope, standard of care, indemnity, ownership, confidentiality, and any notice or limitation provisions.",
"A correct legal or economic rule gives the wrong result when applied to the wrong contract term, duty, jurisdiction, or sequence of events.",
"A timeline connects notice, performance, change orders, alleged breach, damages, and intellectual-property events, helping determine which obligations existed at each stage.",
"Confirm the relevant contract provision, identify the duty and alleged breach, separate facts from assumptions, and check whether the conclusion fits the stated allocation of risk."
],
"02-04":[
"First verify the sign and timing of every cash flow and the interest period, because economic equivalence depends on when each amount occurs as well as its magnitude.",
"A factor formula can be used correctly yet give a wrong answer if the cash-flow direction, compounding period, effective rate, or focal date is mismatched.",
"A cash-flow timeline prevents beginning-of-period and end-of-period amounts from being confused and makes the chosen equivalence date explicit.",
"Check that all cash flows are moved to the same focal date with a rate consistent with the compounding period, then verify the sign and order of magnitude."
],
"02-05":[
"First verify the comparison date, interest rate, number of periods, and whether each amount is a single payment or a uniform series before selecting a present- or future-worth factor.",
"A correct P/F, F/P, P/A, or F/A factor gives the wrong result if the conversion direction or series timing does not match the cash-flow diagram.",
"A timeline shows whether the first payment occurs at time zero or at the end of period one and prevents an off-by-one error in the period count.",
"Reconstruct the equivalent amount in the opposite direction when practical and confirm that the factor, period count, units, and cash-flow signs are internally consistent."
],
"02-06":[
"First verify the analysis period, interest rate, uniform-series timing, and whether a gradient begins with the first payment or one period later.",
"Annual-worth and gradient factors assume specific timing conventions; using the right equation with the wrong series origin or gradient definition produces a systematically shifted result.",
"A labeled cash-flow timeline makes the base annuity and gradient increments visible, preventing the gradient from being applied one period too early or too late.",
"Check that the annual worth reproduces the same present worth over the stated analysis period and that each capital-recovery or gradient factor uses the correct period count."
],
"02-07":[
"First verify the complete cash-flow pattern and the decision criterion, especially whether the problem asks for internal rate of return, another return measure, or comparison with a stated MARR.",
"An IRR equation may be solved correctly but still mislead when cash-flow signs change more than once, multiple roots exist, or mutually exclusive projects require incremental analysis.",
"A timeline exposes sign changes and identifies the periods creating multiple-root or reinvestment issues, making it easier to decide whether ordinary IRR is appropriate.",
"Substitute the computed rate back into the present-worth equation, check for additional roots when sign changes permit them, and compare the relevant rate with the MARR using the proper rule."
],
"02-08":[
"First verify which costs are fixed, which vary with output, what revenue or benefit changes with the decision variable, and whether the comparison is incremental or total.",
"A breakeven or benefit-cost equation can be algebraically correct but decisionally wrong if sunk costs, nonincremental benefits, or inconsistent time bases are included.",
"A timeline or documented cost model shows when costs and benefits occur and prevents annual, present, and one-time amounts from being compared directly.",
"Check that only relevant incremental quantities are included, all alternatives use the same economic basis, and the calculated breakeven or B/C result lies in a physically meaningful range."
],
"02-09":[
"First verify whether monetary values and rates are on a real or nominal basis, then identify the depreciation method, tax rate, recovery period, and replacement assumptions supplied.",
"A correct depreciation or after-tax formula gives the wrong decision if inflation treatment, tax basis, salvage value, or nominal-versus-real interest conventions are mixed.",
"A year-by-year timeline separates depreciation, taxable income, taxes, operating cash flow, salvage, and replacement events so each occurs in the proper period.",
"Check that nominal cash flows use a nominal discount rate or real cash flows use a real rate, verify depreciation and tax effects, and confirm equivalent service in replacement comparisons."
],
"02-10":[
"First verify the feasible alternatives, decision constraints, evaluation criterion, and any probabilities or ranges assigned to uncertain outcomes before calculating a preferred project.",
"A mathematically correct ranking can be wrong when mutually exclusive and independent projects are mixed, constraints are omitted, or expected values are treated as certain outcomes.",
"A decision timeline or tree makes the order of decisions, uncertain events, and information availability explicit, preventing future knowledge from being used prematurely.",
"Check feasibility first, then confirm the ranking uses a consistent economic criterion and test the recommendation against the stated uncertainty and sensitivity assumptions."
],
"02-11":[
"Locate the Handbook definitions and tabulated atomic information used for atomic number, atomic mass, electron configuration, periodic trends, and the principal bonding types.",
"Check that atomic counts and charges are conserved, electron configurations do not exceed orbital capacities, and any predicted trend is consistent with periodic-table position.",
"Use measured or tabulated atomic radii, electronegativities, ionization energies, or material data whenever supplied; those values control over a qualitative periodic-trend expectation.",
"The chapter's use of bonding and periodic trends as a screening tool for likely engineering behavior is an instructional interpretation, not a verbatim Handbook decision rule."
],
"02-12":[
"Locate the Handbook definitions for mole, molar mass, stoichiometric coefficients, limiting reactant, and any reaction-property tables needed for the stated chemical equation.",
"Verify conservation of each element and electric charge, and confirm that mole-to-mass conversions cancel units correctly before accepting the stoichiometric result.",
"Use supplied composition, purity, yield, conversion, or tabulated molar data whenever available instead of substituting an idealized value or remembered trend.",
"The sequence balance first, convert to moles, apply the stoichiometric ratio, then convert to the requested quantity is guide-developed problem-solving structure."
],
"02-13":[
"Locate the Handbook concentration definitions, acid-base relations, pH/pOH equations, and any required dissociation or equilibrium constants before solving the solution problem.",
"Check concentration units, require mole and mass fractions to remain between zero and one, and verify that calculated pH and species concentrations are physically consistent.",
"Use measured composition, density, activity data, or tabulated equilibrium constants when supplied; those values supersede qualitative expectations about acid or base strength.",
"The chapter's recommendation to perform a concentration-basis check before applying an acid-base equation is guide-developed quality control rather than a verbatim Handbook rule."
],
"02-14":[
"Locate the Handbook equilibrium-constant relations, reaction-quotient definitions, electrochemical equations, standard-potential data, and corrosion terminology relevant to the problem.",
"Check that equilibrium expressions use the correct species and exponents, cell-potential signs follow reaction direction, and half-reactions conserve both mass and charge.",
"Use supplied equilibrium constants, activities, standard potentials, polarization data, or measured corrosion rates rather than relying on a qualitative statement that a reaction is favored.",
"Pairing the thermodynamic driving-force calculation with an explicit kinetics or corrosion-environment caution is a guide-developed interpretation."
],
"02-15":[
"Locate the Handbook functional-group definitions, representative organic-property data, biochemical stoichiometry, and any reaction or biological-system relations referenced by the problem.",
"Check elemental and charge balance, confirm molecular formulas and functional groups are chemically possible, and keep concentration or yield quantities within physically meaningful bounds.",
"Use measured partition coefficients, solubilities, reaction yields, biodegradation data, or organism-specific values when provided instead of inferring performance solely from structural trends.",
"Using structural features as a first-pass engineering screening method before consulting property data is guide-developed interpretation rather than a Handbook rule."
],
"02-16":[
"Locate the Handbook definitions and property tables that distinguish metals, ceramics, polymers, composites, crystal structures, and the principal bonding mechanisms.",
"Check that density, modulus, strength, and temperature values use consistent units and fall in a plausible range for the stated material class and structure.",
"Use measured or specified material properties, phase information, or manufacturer data when provided; these values control over broad trends associated with bonding or material class.",
"The structure-bonding-property chain is used as a guide-developed reasoning framework for screening materials, not as a substitute for actual property data."
],
"02-17":[
"Locate the Handbook definitions and tables for strength, stiffness, toughness, hardness, ductility, fatigue, creep, thermal properties, and any material-selection indices used.",
"Check property units and orders of magnitude, distinguish stress from force and modulus from strength, and verify that a selected material satisfies every stated constraint.",
"Use certified material data, design allowables, temperature-dependent properties, or test results whenever supplied instead of relying on typical values for a material family.",
"The staged process of screening constraints first, ranking objectives second, and then considering secondary factors is guide-developed selection strategy."
],
"02-18":[
"Locate the Handbook diffusion relations, phase-diagram definitions, heat-treatment terminology, and any temperature- or composition-dependent data needed for the process.",
"Check diffusion dimensions and temperature units, require phase fractions to remain between zero and one, and verify that the predicted phase path matches composition and temperature.",
"Use the supplied phase diagram, diffusion coefficient, transformation data, or processing specification rather than substituting a generic trend from another material system.",
"Tracing processing history through structure and then to properties is a guide-developed engineering interpretation used to organize the analysis."
],
"02-19":[
"Locate the Handbook safety definitions and any tables relevant to hazard identification, exposure control, hazard communication, PPE, and the hierarchy of controls.",
"Check that exposure quantities use the stated averaging period and units, and verify that the selected control actually addresses the identified hazard.",
"Use measured exposure data, the current safety data sheet, equipment ratings, or applicable exposure limits whenever provided; these control over generalized assumptions about hazard severity.",
"The stepwise review identify the hazard, apply the hierarchy of controls, then evaluate residual risk and PPE is guide-developed workflow."
],
"02-20":[
"Locate the Handbook equations and definitions for fire and explosion limits, electrical hazards, energy isolation, and confined-space conditions that apply to the scenario.",
"Check concentration and energy units, verify calculated values are physically meaningful, and confirm that the proposed control matches the actual hazardous-energy source.",
"Use measured gas concentrations, equipment nameplate data, protective-device ratings, ventilation measurements, and current entry-permit data whenever supplied.",
"Separating ignition, fuel, oxidizer, electrical-energy, and atmospheric hazards before selecting controls is guide-developed diagnostic structure."
],
"02-21":[
"Locate the Handbook toxicology definitions, dose or concentration relations, exposure-limit terminology, risk equations, and chemical-compatibility data applicable to the substance and exposure route.",
"Check dose and concentration units, distinguish acute from time-weighted exposure, and verify that calculated probabilities or risk values remain within valid bounds.",
"Use measured concentrations, toxicological reference values, exposure limits, mixture data, and compatibility charts when available instead of extrapolating from a qualitative hazard label.",
"Separating hazard, exposure, dose-response, risk, and compatibility questions before selecting controls is guide-developed analytical structure."
]
}

UNIT_FIXES = {
("02-37",2):"ε=(1 mm)/(2 m)=0.0005, which is dimensionless.",
("02-45",1):"Re=(2 m/s)(0.05 m)/(1.0e-6 m²/s)=100,000, dimensionless.",
("02-48",2):"x=(2 kg)/(2 kg+6 kg)=0.25, dimensionless.",
("02-49",6):"φ=(2 kPa)/(4 kPa)=0.50=50%, dimensionless.",
("02-54",1):"COP_R=(10 kW)/(2 kW)=5, dimensionless.",
("02-54",3):"COP_R=(270 K)/(300 K-270 K)=9, dimensionless.",
("02-54",4):"COP_R=(400 kJ/kg-250 kJ/kg)/(450 kJ/kg-400 kJ/kg)=3, dimensionless.",
("02-54",5):"Capacity=(105.5 kW)/(3.516 kW per ton)=30.0 tons of refrigeration.",
("02-56",1):"Bi=(20 W/m²)(0.001 m³)/[(50 W/m·K)(0.06 m²)]=0.00667, dimensionless.",
("02-56",6):"Using t=100 s and L=0.02 m in the Fourier-number relation gives Fo=0.9375, dimensionless.",
("02-57",2):"Nu=(120 W/m²)(0.05 m)/(0.6 W/m·K)=10, dimensionless.",
("02-58",6):"ε=(180 kW)/(300 kW)=0.60, dimensionless.",
("02-58",7):"NTU=(6 kW)/(3 kW)=2, dimensionless.",
("02-61",1):"q=(10e-6 F)(12 V)=120e-6 C=120 µC.",
("02-62",3):"Using θ=30 deg, 10∠30°=8.66+j5.00 in rectangular form.",
("02-63",2):"S=(5 kW)/0.60=8.33 kVA.",
("02-63",3):"For P=10 kW, Qc=P[tan(cos^-1 0.70)-tan(cos^-1 0.95)]≈6.92 kVAR.",
("02-63",8):"S=√3(208 V)(15 A)=5.40 kVA.",
("02-64",1):"B=(2.0e-3 H/m)(500 A/m)=1.0 T.",
("02-65",5):"s=(1800 rpm-1746 rpm)/(1800 rpm)=0.030=3.0%, dimensionless.",
("02-65",9):"s=(1000 rpm-970 rpm)/(1000 rpm)=0.030=3.0%, dimensionless.",
("02-67",2):"R=(10000 Ω) exp[3950(1/323.15-1/298.15)]≈3.59 kΩ.",
("02-68",6):"At t=3 s=τ, y=2(1-e^-1)=1.264 output units.",
("02-68",9):"At t=1 s<θ=2 s, the output change is zero because the delayed dynamic response has not started.",
("02-69",6):"With time constant τ=2 s, the DC gain is G(0)=5, dimensionless.",
("02-69",7):"At the -180 deg phase crossing where |G|=0.25, GM=-20log10(0.25)=12.04 dB.",
("02-70",2):"With t=4 s, u_I=K_i e t=0.5·3·4=6 output units."
}

FIGURE_RESTORE_01_02 = {
"## 2.1 Quantity, Dimension, Unit":
"![FIG-01-02-001: Three-tier pyramid showing physical quantity at the base, dimension in the middle, and representative units at the top](../figures/FIG-01-02-001-quantity-dimension-unit.png)",
"## 2.2 The SI System":
"![FIG-01-02-002: Tree connecting SI base units through physical definitions to the derived units newton, pascal, joule, and watt](../figures/FIG-01-02-002-si-derived-units-tree.png)",
"## 2.4 Dimensional Homogeneity":
"![FIG-01-02-003: Dimensional check comparing an incorrect pendulum-period equation with the dimensionally consistent corrected form](../figures/FIG-01-02-003-pendulum-dimensional-check.png)",
"## 2.5 Unit Conversion by Dimensional Analysis":
"![FIG-01-02-004: Three-step factor-label unit-conversion flowchart with a decision branch based on whether the units cancel](../figures/FIG-01-02-004-factor-label-method.png)",
"## 2.6 The Pound Problem":
"""![FIG-01-02-005: Comparison of SI, USCS slug, and USCS lbm-lbf systems, highlighting why the lbm-lbf form requires g_c](../figures/FIG-01-02-005-unit-system-comparison.png)

![FIG-01-02-006: Side-by-side comparison of gravitational acceleration g and the unit-conversion constant g_c](../figures/FIG-01-02-006-g-vs-gc.png)

![FIG-01-02-007: Newton's second law written in SI, USCS slug, and USCS lbm-lbf forms with units annotated](../figures/FIG-01-02-007-newtons-second-law-unit-systems.png)""",
"## 2.7 Temperature Scales":
"""![FIG-01-02-008: Four aligned temperature scales showing absolute zero, water freezing and boiling points, and body temperature](../figures/FIG-01-02-008-temperature-scales.png)

![FIG-01-02-009: Decision flowchart for selecting an absolute temperature scale or converting a temperature difference](../figures/FIG-01-02-009-temperature-scale-selection.png)""",
"## 2.8 Fundamental Constants":
"![FIG-01-02-010: Reference grid showing four common forms of the universal gas constant with their units and uses](../figures/FIG-01-02-010-universal-gas-constant.png)",
}

def find_chapter(root: Path, chapter: str) -> Path:
    matches = [
        p for p in root.rglob(f"{chapter}-*.md")
        if ".bak" not in p.name
        and "FE-Audit-" not in str(p)
    ]
    # Prefer the real repository copy over packaged/exported duplicates.
    matches = [p for p in matches if "FE Supplemental Guide" not in str(p)] or matches
    if len(matches) != 1:
        raise RuntimeError(f"{chapter}: expected exactly one target, found {len(matches)}: {matches}")
    return matches[0]

def backup(path: Path) -> None:
    bak = path.with_suffix(path.suffix + ".bak")
    if not bak.exists():
        shutil.copy2(path, bak)

def update_answer_key(text: str, vals: list[str]) -> str:
    m = re.search(r'(## Answer Key[^\n]*\n)(.*?)(?=\n---|\Z)', text, re.S)
    if not m:
        raise RuntimeError("Answer Key section not found")
    sec = m.group(2)
    for idx, val in enumerate(vals, start=15):
        pat = rf'(?ms)^{idx}\.\s+.*?(?=^\d+\.\s|\Z)'
        if not re.search(pat, sec):
            raise RuntimeError(f"Answer-key item {idx} not found")
        sec = re.sub(pat, f"{idx}. {val}\n", sec, count=1)
    return text[:m.start(2)] + sec + text[m.end(2):]

def fix_learning_objectives(text: str) -> tuple[str,int]:
    m = re.search(r'(## Learning Objectives\s*\n)(.*?)(?=\n---|\n## )', text, re.S)
    if not m:
        return text, 0
    sec = m.group(2)
    new_sec, n = re.subn(
        r'(?m)^(\s*[*-]\s+)(\d+(?:\.\d+)+)\s+',
        r'\1**\2** ',
        sec,
    )
    return text[:m.start(2)] + new_sec + text[m.end(2):], n

def fix_worked_example_prefix(text: str, exnum: int, new_prefix: str) -> str:
    pat = rf'(### Worked Example {exnum}\b.*?\*\*Solution\.\*\*\s*)(.*?)(?=(?:Reasoning:|The governing model here is))'
    m = re.search(pat, text, re.S)
    if not m:
        raise RuntimeError(f"Worked Example {exnum}: expected Solution/Reasoning pattern not found")
    return text[:m.start(2)] + new_prefix + " " + text[m.end(2):]

def restore_01_02_figures(text: str) -> tuple[str,int]:
    restored = 0
    for heading, block in FIGURE_RESTORE_01_02.items():
        ids = sorted(set(re.findall(r"FIG-01-02-\d{3}", block)))
        if all(fid in text for fid in ids):
            continue
        if heading not in text:
            raise RuntimeError(f"01-02 heading not found for figure restoration: {heading}")
        text = text.replace(heading, heading + "\n\n" + block, 1)
        restored += len(ids)
    return text, restored

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    if not root.exists():
        raise SystemExit(f"Repository root not found: {root}")

    changed = set()
    stats = {"formula_boxes":0, "answer_entries":0, "objective_bullets":0, "unit_examples":0, "figures_restored":0}

    # 01-37 formula/prose correction.
    p = find_chapter(root, "01-37")
    text = p.read_text(encoding="utf-8")
    old = """At each chance node:

$$
\\boxed{\\text{replace the node by its expected value}.}
$$

At each decision node:

$$
\\boxed{\\text{replace the node by the preferred branch value}.}
$$"""
    new = """At each chance node, **replace the node by its expected value**.

At each decision node, **replace the node by the preferred branch value**."""
    if old in text:
        backup(p); text = text.replace(old,new); p.write_text(text,encoding="utf-8")
        changed.add(p); stats["formula_boxes"] += 2

    # 02-01..02-21 answer-key cleanup.
    for chapter, vals in ANSWER_FIXES.items():
        p = find_chapter(root, chapter)
        text = p.read_text(encoding="utf-8")
        new_text = update_answer_key(text, vals)
        if new_text != text:
            backup(p); p.write_text(new_text,encoding="utf-8")
            changed.add(p); stats["answer_entries"] += 4

    # Restore the ten Chapter 01-02 figure references that disappeared between
    # the 16:19 and 16:27 audits. Insert only missing references at their original headings.
    p = find_chapter(root, "01-02")
    text = p.read_text(encoding="utf-8")
    new_text, count = restore_01_02_figures(text)
    if count:
        backup(p); p.write_text(new_text,encoding="utf-8")
        changed.add(p); stats["figures_restored"] += count

    # 01-02..01-23 Learning Objectives formatting.
    for n in range(2,24):
        chapter = f"01-{n:02d}"
        p = find_chapter(root, chapter)
        text = p.read_text(encoding="utf-8")
        new_text, count = fix_learning_objectives(text)
        if count:
            backup(p); p.write_text(new_text,encoding="utf-8")
            changed.add(p); stats["objective_bullets"] += count

    # Worked-example unit review corrections.
    for (chapter, exnum), prefix in UNIT_FIXES.items():
        p = find_chapter(root, chapter)
        text = p.read_text(encoding="utf-8")
        new_text = fix_worked_example_prefix(text, exnum, prefix)
        if new_text != text:
            backup(p); p.write_text(new_text,encoding="utf-8")
            changed.add(p); stats["unit_examples"] += 1

    print("FE audit patch complete")
    print(f"  Files changed: {len(changed)}")
    print(f"  Formula/prose boxes corrected: {stats['formula_boxes']}")
    print(f"  Answer-key entries replaced: {stats['answer_entries']}")
    print(f"  Learning-objective bullets reformatted: {stats['objective_bullets']}")
    print(f"  Chapter 01-02 figure references restored: {stats['figures_restored']}")
    print(f"  Worked examples with explicit dimensional handling: {stats['unit_examples']}")
    print("  Backups: <file>.md.bak beside every modified chapter")

if __name__ == "__main__":
    main()
