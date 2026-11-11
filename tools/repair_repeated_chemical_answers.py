#!/usr/bin/env python3
# Repeated-answer repair workflow entry point.
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
FILES={
"03-01":"03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md",
"03-02":"03-02-Recycle-Bypass-Purge-and-Unsteady-Material-Balances.md",
"03-03":"03-03-Reactive-Material-Balances-Combustion-and-Heats-of-Reaction.md",
"03-04":"03-04-Phase-Equilibrium-Raoult-s-Law-Fugacity-Activity-and-Chemical-Equilibrium.md",
"03-05":"03-05-Molecular-Diffusion-and-Convective-Mass-Transfer.md",
"03-06":"03-06-Distillation-and-Equilibrium-Stage-Methods.md",
"03-07":"03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md",
"03-08":"03-08-Humidification-Drying-and-Evaporation.md",
"03-09":"03-09-Particle-Characterization-Solids-Handling-Size-Reduction-and-Crystallization.md",
"03-10":"03-10-Reaction-Kinetics-Rate-Laws-and-Arrhenius-Behavior.md",
"03-11":"03-11-Reactor-Design-Batch-CSTR-PFR-Multiple-Reactions-and-Catalysis.md",
"03-12":"03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md",
"03-13":"03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md",
}
CONTEXT={
"03-01":"single-unit and flowsheet balances depend on consistent stream flow rates, compositions, accumulation terms, and energy states",
"03-02":"recycle, bypass, purge, and unsteady systems require a clear distinction between internal circulation and net external flow",
"03-03":"reactive systems couple stoichiometry, extent or conversion, composition, and reaction enthalpy on one molar basis",
"03-04":"phase-equilibrium work depends on composition basis, phase state, equilibrium assumptions, and the selected ideal or nonideal model",
"03-05":"mass-transfer calculations depend on the driving-force definition, area, diffusivity or transfer coefficient, and transport geometry",
"03-06":"distillation calculations depend on column flow rates, compositions, reflux, feed condition, equilibrium stages, and tray efficiency",
"03-07":"absorption, extraction, adsorption, and membrane calculations depend on phase pairing, equilibrium or transport laws, and recovery targets",
"03-08":"humidification, drying, and evaporation require moisture or vapor content on the correct basis plus coupled material and energy balances",
"03-09":"solids calculations depend on particle-size basis, distribution metric, handling or comminution model, and crystallization assumptions",
"03-10":"kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant",
"03-11":"reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model",
"03-12":"process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis",
"03-13":"optimization and control must remain inside process constraints and safety limits while respecting dynamic response and protective layers",
}
FAIL={
"03-01":"mix incompatible flow or composition bases, omit a stream, or assign accumulation to the wrong control volume",
"03-02":"double-count an internal recycle, misplace a purge or bypass, or treat a transient inventory as steady state",
"03-03":"apply stoichiometry on inconsistent molar bases, select the wrong limiting reactant, or attach reaction heat to the wrong extent",
"03-04":"use the wrong liquid/vapor composition basis or apply an ideal relation where activity or fugacity effects matter",
"03-05":"use a concentration difference that does not match the transfer coefficient or pair the wrong area and transport length",
"03-06":"construct operating or q-lines from inconsistent flow definitions or use an equilibrium-stage relation with the wrong feed/reflux condition",
"03-07":"pair the wrong equilibrium relation with the contacting phases or compute recovery on an inconsistent solute-free/total-flow basis",
"03-08":"mix wet-basis and dry-basis moisture quantities or close an energy balance with an inconsistent vapor/solid reference state",
"03-09":"mix number-, mass-, and surface-based particle measures or apply a size-reduction/crystallization relation to the wrong characteristic size",
"03-10":"infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model",
"03-11":"use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition",
"03-12":"size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions",
"03-13":"optimize an infeasible operating point, tune against the wrong dynamic model, or overlook a safety constraint or protection layer",
}

def sec(text,name):
    i=text.find(name)
    if i<0:return None
    a=i+len(name); b=text.find("\n## ",a)
    if b<0:b=len(text)
    return a,b

def blocks(body):
    return list(re.finditer(r"(?ms)^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|\Z)",body))

for ch,fn in FILES.items():
    p=ROOT/"layer-3-tracks"/"chemical"/fn
    text=p.read_text(encoding="utf-8")
    qb=sec(text,"## Review Questions"); ab=sec(text,"## Answer Key with Explanations")
    if not qb or not ab: raise RuntimeError(f"missing sections {ch}")
    questions={int(m.group(1)):re.sub(r"\s+"," ",m.group(2)).strip() for m in blocks(text[qb[0]:qb[1]])}
    body=text[ab[0]:ab[1]]
    edits=[]
    for m in blocks(body):
        n=int(m.group(1))
        if not (8<=n<=18): continue
        q=questions.get(n,"")
        if 8<=n<=14:
            tm=re.search(r"\*\*([^*]+)\*\*",q)
            topic=tm.group(1).strip() if tm else re.sub(r"[?].*","",q).strip()
            ans=(f"Applying **{topic}** before the process basis and system boundary are fixed can {FAIL[ch]}. "
                 f"In this chapter, {CONTEXT[ch]}. Define the basis, boundary, known streams or states, and independent specifications first; then apply the {topic} relation to that defined system.")
        elif n==15:
            ans=(f"Close the material balance first because it establishes the flow rates and compositions that the energy balance must use. "
                 f"For this chapter, {CONTEXT[ch]}; without those material quantities, enthalpy, heat duty, reaction energy, or phase-change terms can be attached to the wrong amount of material.")
        elif n==16:
            ans=(f"A degrees-of-freedom check compares the number of unknowns with the number of independent balances, constitutive relations, equilibrium or rate equations, and specifications. "
                 f"For {ch}, this prevents algebra from starting before the {CONTEXT[ch]} are sufficiently defined and exposes redundant or missing equations.")
        elif n==17:
            ans=(f"Use a relation supplied in the FE problem whenever it defines the model or data for that question. "
                 f"That stated relation controls the calculation even if another correlation is familiar; in {ch}, substituting an unstated model can change the assumptions behind the {CONTEXT[ch]}.")
        else:
            ans=(f"Separate Handbook-supported material from specification-required or externally supported material so the learner knows what may be looked up and what must be understood independently. "
                 f"In {ch}, the distinction matters because the {CONTEXT[ch]} can include methods or assumptions that are required by the exam specification but are not fully tabulated in the Handbook.")
        repl=f"{n}. {ans}\n\n"
        edits.append((m.start(),m.end(),repl))
    for s,e,r in reversed(edits): body=body[:s]+r+body[e:]
    text=text[:ab[0]]+body+text[ab[1]:]
    p.write_text(text,encoding="utf-8")
    print(ch,len(edits))
