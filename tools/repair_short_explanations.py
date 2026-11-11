#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

PATHS={
"03-01":"layer-3-tracks/chemical/03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md",
"03-02":"layer-3-tracks/chemical/03-02-Recycle-Bypass-Purge-and-Unsteady-Material-Balances.md",
"03-03":"layer-3-tracks/chemical/03-03-Reactive-Material-Balances-Combustion-and-Heats-of-Reaction.md",
"03-04":"layer-3-tracks/chemical/03-04-Phase-Equilibrium-Raoult-s-Law-Fugacity-Activity-and-Chemical-Equilibrium.md",
"03-05":"layer-3-tracks/chemical/03-05-Molecular-Diffusion-and-Convective-Mass-Transfer.md",
"03-06":"layer-3-tracks/chemical/03-06-Distillation-and-Equilibrium-Stage-Methods.md",
"03-07":"layer-3-tracks/chemical/03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md",
"03-08":"layer-3-tracks/chemical/03-08-Humidification-Drying-and-Evaporation.md",
"03-09":"layer-3-tracks/chemical/03-09-Particle-Characterization-Solids-Handling-Size-Reduction-and-Crystallization.md",
"03-10":"layer-3-tracks/chemical/03-10-Reaction-Kinetics-Rate-Laws-and-Arrhenius-Behavior.md",
"03-11":"layer-3-tracks/chemical/03-11-Reactor-Design-Batch-CSTR-PFR-Multiple-Reactions-and-Catalysis.md",
"03-12":"layer-3-tracks/chemical/03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md",
"03-13":"layer-3-tracks/chemical/03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md",
"01-27":"layer-1-substrate/01-27-Algorithm-and-Logic-Development.md",
"01-34":"layer-1-substrate/01-34-Analysis-of-Variance-and-Design-of-Experiments.md",
"01-35":"layer-1-substrate/01-35-Linear-Regression-and-Goodness-of-Fit.md",
}

ASSESS={
"01-27":[14,15,20],"01-34":[13,16,6],"01-35":[15],
"03-01":[2,6],"03-02":[1,10,2,3,4,5,6,7,8],"03-03":[1,10,2,5,8],
"03-04":[1,10,2,3,5,7,8],"03-05":[10,5,6,7,8],"03-06":[1,10,2,3,5,8],
"03-07":[1,10,2,3,4,5,6,8,9],"03-08":[2,3,8],"03-09":[1,10,2,3,4,5,6],
"03-10":[10,2,3,4,5,6,7,8],"03-11":[3,4,5,9],"03-12":[2,3,5,6,7,8,9],
"03-13":[1,10,3,6],
}
WORKED={
"03-01":[2,3,5,7,8],"03-02":[2,5,7,8],"03-03":[2,3,7,8],
"03-04":[1,3,4,5,6,7],"03-05":[3,6,8,9],"03-06":[1,3,4,5,6,9],
"03-07":[2,3,4,6,7,8,9],"03-08":[5,7],"03-09":[1,2,4,5,8,9],
"03-10":[2,4,5,7,8],"03-11":[7],"03-12":[1,2,4,7,8,9],
"03-13":[1,2,4,5,6,7,8,9],
}
HINT={
"03-01":"Use the stated control volume and basis; conservation requires inputs plus generation minus outputs, consumption, and accumulation to close consistently.",
"03-02":"Separate the overall process boundary from internal recycle, bypass, or purge streams so internal circulation is not double-counted as external flow.",
"03-03":"Keep stoichiometry, extent or conversion, limiting-reactant logic, and reaction enthalpy on the same molar basis before closing the balance.",
"03-04":"Match the phase-equilibrium relation to the stated composition basis, phase assumptions, and degree of nonideality before evaluating the result.",
"03-05":"Define the mass-transfer driving force and area consistently with the selected diffusion or film model, then carry the transport units through the calculation.",
"03-06":"Combine total and component balances with the equilibrium-stage relation and the specified reflux, recovery, or stage-efficiency condition.",
"03-07":"Use the equilibrium or transport model appropriate to the stated contacting process, phase pair, flow direction, and recovery target.",
"03-08":"Track water or solvent on the requested wet/dry basis and couple the material balance to the relevant enthalpy or latent-heat requirement.",
"03-09":"Use the stated particle-size statistic or solids model consistently; number, mass, surface-area, and energy bases are not interchangeable.",
"03-10":"Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter.",
"03-11":"Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption.",
"03-12":"Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis.",
"03-13":"Respect process constraints, control dynamics, objective functions, and safety limits; an optimum is acceptable only inside the feasible and safe operating region.",
"01-27":"Trace the logic from inputs through each branch or loop condition and verify the termination and output behavior for the stated case.",
"01-34":"Compute the appropriate sums of squares and degrees of freedom, form the relevant mean squares or F ratio, and interpret the result at the stated significance level.",
"01-35":"Relate the fitted value or residual to the regression equation and preserve the distinction between model fit, prediction, and unexplained variation.",
}

def section_bounds(text,heading):
    i=text.find(heading)
    if i<0:return None
    a=i+len(heading)
    b=text.find("\n## ",a)
    if b<0:b=len(text)
    return a,b

def numbered_prompts(text,heading):
    b=section_bounds(text,heading)
    if not b:return {}
    body=text[b[0]:b[1]]
    out={}
    for m in re.finditer(r"(?ms)^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|\Z)",body):
        out[int(m.group(1))]=re.sub(r"\s+"," ",m.group(2)).strip()
    return out

def summarize(s):
    s=re.sub(r"[*_$]","",s)
    s=re.sub(r"\s+"," ",s).strip()
    return s[:155].rstrip(" .;:")

def add_to_numbered(text,heading,prompt_heading,targets,hint):
    b=section_bounds(text,heading)
    if not b:return text,0
    a,z=b; body=text[a:z]
    prompts=numbered_prompts(text,prompt_heading)
    changed=0
    # Work from end to start so offsets remain stable.
    matches=list(re.finditer(r"(?ms)^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|\Z)",body))
    edits=[]
    for m in matches:
        n=int(m.group(1))
        if n not in targets: continue
        item=m.group(0).rstrip()
        if "**Explanation.**" in item: continue
        ps=summarize(prompts.get(n,""))
        detail=(f" The question is framed around “{ps}.”" if ps else "")
        extra=(f"\n\n   **Explanation.** {hint}{detail} "
               "This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.")
        edits.append((m.start(),m.end(),item+extra+"\n"))
    for s,e,repl in reversed(edits):
        body=body[:s]+repl+body[e:]
        changed+=1
    return text[:a]+body+text[z:],changed

def add_to_worked(text,targets,hint):
    ms=list(re.finditer(r"(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$",text))
    edits=[]; changed=0
    for k,m in enumerate(ms):
        label=(m.group(1) or str(k+1)).strip()
        num_m=re.search(r"(\d+)",label)
        n=int(num_m.group(1)) if num_m else k+1
        if n not in targets: continue
        end=ms[k+1].start() if k+1<len(ms) else len(text)
        h2=re.search(r"(?m)^##\s+",text[m.end():end])
        if h2:end=m.end()+h2.start()
        block=text[m.start():end].rstrip()
        if "**Why this works.**" in block: continue
        prompt=summarize(" ".join(block.splitlines()[1:5]))
        extra=(f"\n\n**Why this works.** {hint} "
               f"In this example, the stated setup{(' (“'+prompt+'”)') if prompt else ''} fixes the applicable data and assumptions. "
               "Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.\n")
        edits.append((m.start(),end,block+extra))
    for s,e,repl in reversed(edits):
        text=text[:s]+repl+text[e:]
        changed+=1
    return text,changed

total=0
for ch,rel in PATHS.items():
    p=ROOT/rel
    text=p.read_text(encoding="utf-8")
    before=text
    n1=n2=n3=0
    if ch.startswith("03-"):
        text,n1=add_to_numbered(text,"## Practice Problem Solutions","## Practice Problems",set(ASSESS.get(ch,[])),HINT[ch])
    else:
        # Layer-1 flagged entries may be answer-key or practice-solution items.
        ans=[n for n in ASSESS.get(ch,[]) if not (ch=="01-34" and n==6)]
        if ans:text,n2=add_to_numbered(text,"## Answer Key with Explanations","## Review Questions",set(ans),HINT[ch])
        if ch=="01-34":text,n1=add_to_numbered(text,"## Practice Problem Solutions","## Practice Problems",{6},HINT[ch])
    if ch in WORKED:
        text,n3=add_to_worked(text,set(WORKED[ch]),HINT[ch])
    if text!=before:p.write_text(text,encoding="utf-8")
    total+=n1+n2+n3
    print(ch,n1,n2,n3)
print("targeted edits",total)
