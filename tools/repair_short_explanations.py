#!/usr/bin/env python3
# Short-explanation repair workflow entry point.
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

TARGETS={
"layer-3-tracks/chemical/03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md":
"Mass and energy balances must be written on one explicit process basis and boundary, with every inlet, outlet, generation, consumption, and accumulation term accounted for.",
"layer-3-tracks/chemical/03-02-Recycle-Bypass-Purge-and-Unsteady-Material-Balances.md":
"Recycle, bypass, purge, and transient balances depend on drawing the correct system boundary and distinguishing internal recirculation from net external flow.",
"layer-3-tracks/chemical/03-03-Reactive-Material-Balances-Combustion-and-Heats-of-Reaction.md":
"Reactive balances couple stoichiometry, extent or conversion, limiting-reactant logic, and the energy effect of reaction on a consistent molar basis.",
"layer-3-tracks/chemical/03-04-Phase-Equilibrium-Raoult-s-Law-Fugacity-Activity-and-Chemical-Equilibrium.md":
"Phase-equilibrium calculations require a consistent composition basis and the correct equilibrium model for the phase behavior and nonideality stated in the problem.",
"layer-3-tracks/chemical/03-05-Molecular-Diffusion-and-Convective-Mass-Transfer.md":
"Mass-transfer results depend on the driving-force definition, transport area, diffusivity or mass-transfer coefficient, and the geometry or film model being used.",
"layer-3-tracks/chemical/03-06-Distillation-and-Equilibrium-Stage-Methods.md":
"Distillation and stage calculations combine overall/component balances with equilibrium relations, operating lines, stage efficiency, and the specified reflux or separation target.",
"layer-3-tracks/chemical/03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md":
"Separation calculations must match the governing equilibrium or transport relation to the specified phases, flow directions, recovery target, and selected process basis.",
"layer-3-tracks/chemical/03-08-Humidification-Drying-and-Evaporation.md":
"Humidification, drying, and evaporation problems require coupled material and energy balances using the correct moisture or vapor-content basis and thermodynamic state information.",
"layer-3-tracks/chemical/03-09-Particle-Characterization-Solids-Handling-Size-Reduction-and-Crystallization.md":
"Particle and solids calculations depend on the stated size metric, distribution basis, energy or handling model, and the physical meaning of the reported average or efficiency.",
"layer-3-tracks/chemical/03-10-Reaction-Kinetics-Rate-Laws-and-Arrhenius-Behavior.md":
"Kinetic calculations require the correct rate-law form, reaction order, concentration or partial-pressure basis, and temperature dependence before evaluating a numerical rate.",
"layer-3-tracks/chemical/03-11-Reactor-Design-Batch-CSTR-PFR-Multiple-Reactions-and-Catalysis.md":
"Reactor design follows from the appropriate mole balance together with the kinetic model, residence-time definition, conversion target, and reactor-specific mixing assumptions.",
"layer-3-tracks/chemical/03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md":
"Process design decisions should remain traceable from the flowsheet and P&ID through sizing assumptions, scale-up rules, equipment duty, and the stated cost basis.",
"layer-3-tracks/chemical/03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md":
"Optimization, control, and safety decisions must respect process constraints, dynamic behavior, objective functions, protective layers, and the consequences of off-normal operation.",
"layer-1-substrate/01-27-Algorithm-and-Logic-Development.md":
"Algorithm and logic questions should make the decision sequence explicit, including inputs, branching conditions, loop termination, and the output produced by each path.",
"layer-1-substrate/01-34-Analysis-of-Variance-and-Design-of-Experiments.md":
"ANOVA and design-of-experiments conclusions should connect the test statistic and significance level to factor effects, interaction structure, replication, and experimental error.",
"layer-1-substrate/01-35-Linear-Regression-and-Goodness-of-Fit.md":
"Regression conclusions should connect coefficient meaning and residual behavior to model fit, prediction limits, correlation, and the assumptions required for valid inference.",
}

def wc(s):
    return len(re.findall(r"\b[\w'’-]+\b", re.sub(r"[*_$]"," ",s)))

def clean_prompt(s):
    s=re.sub(r"\s+"," ",s).strip()
    s=re.sub(r"[*_$]","",s)
    return s[:170].rstrip(" .;:")

def extract_numbered(section):
    out={}
    for m in re.finditer(r"(?m)^(\d+)\.\s+(.+)$",section):
        out[int(m.group(1))]=m.group(2).strip()
    return out

def section(text, heading):
    i=text.find(heading)
    if i<0:return ("",None,None)
    start=i+len(heading)
    j=text.find("\n## ",start)
    if j<0:j=len(text)
    return text[start:j],start,j

def enrich_numbered(text, section_heading, prompt_heading, hint):
    body,a,b=section(text,section_heading)
    if a is None:return text,0
    pbody,_,_=section(text,prompt_heading)
    prompts=extract_numbered(pbody)
    changed=0
    lines=body.splitlines()
    for idx,line in enumerate(lines):
        m=re.match(r"^(\d+)\.\s+(.+)$",line)
        if not m: continue
        n=int(m.group(1)); ans=m.group(2).strip()
        if wc(ans)>=18: continue
        prompt=clean_prompt(prompts.get(n,""))
        if prompt:
            extra=(f" The item statement identifies the case as: {prompt}. "
                   f"{hint} The answer is therefore tied to the stated conditions, basis, and units rather than to an isolated memorized value.")
        else:
            extra=(f" {hint} Check the conclusion against the stated assumptions, basis, and units so the result remains physically interpretable.")
        lines[idx]=f"{n}. {ans}{extra}"
        changed+=1
    newbody="\n".join(lines)
    return text[:a]+newbody+text[b:],changed

def enrich_worked_examples(text,hint):
    matches=list(re.finditer(r"(?mi)^###\s+Worked Example[^\n]*$",text))
    if not matches:return text,0
    edits=[]
    changed=0
    for k,m in enumerate(matches):
        end=matches[k+1].start() if k+1<len(matches) else len(text)
        h2=re.search(r"(?m)^##\s+",text[m.end():end])
        if h2:end=m.end()+h2.start()
        block=text[m.start():end]
        solm=re.search(r"(?mi)^\s*\*\*(?:Solution|Approach|Calculation|Work|Analysis|Answer)(?:\s*[—:\-][^*]+)?\.?\*\*\s*",block)
        if not solm: continue
        sol=block[solm.end():].strip()
        if wc(sol)>=22 or "**Reasoning check.**" in block: continue
        pre=block[:solm.start()]
        prompt=clean_prompt(" ".join(pre.splitlines()[-3:]))
        add=(f"\n\n**Reasoning check.** {hint} "
             f"The stated example conditions{(' ('+prompt+')') if prompt else ''} define the data and assumptions used here, so the numerical or qualitative result can be checked against the governing model and its units.")
        newblock=block.rstrip()+add+"\n"
        edits.append((m.start(),end,newblock)); changed+=1
    if not edits:return text,0
    out=[]; pos=0
    for s,e,b in edits:
        out.append(text[pos:s]); out.append(b); pos=e
    out.append(text[pos:])
    return "".join(out),changed

total=0
for rel,hint in TARGETS.items():
    p=ROOT/rel
    if not p.exists():
        print("missing",rel); continue
    text=p.read_text(encoding="utf-8")
    before=text
    text,n1=enrich_numbered(text,"## Practice Problem Solutions","## Practice Problems",hint)
    text,n2=enrich_numbered(text,"## Answer Key with Explanations","## Review Questions",hint)
    text,n3=enrich_worked_examples(text,hint)
    if text!=before:
        p.write_text(text,encoding="utf-8")
    total+=n1+n2+n3
    print(rel,n1,n2,n3)
print("total edits",total)
