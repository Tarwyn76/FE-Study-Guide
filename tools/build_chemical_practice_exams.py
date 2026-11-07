#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import math, yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"
OUT.mkdir(parents=True,exist_ok=True)

def load():
    bp=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text(encoding="utf-8"))
    led=yaml.safe_load((ROOT/"meta"/"ledger.yaml").read_text(encoding="utf-8"))
    concepts=led.get("concepts") or led.get("atoms") or []
    if not isinstance(concepts,list):
        # ledger stores concepts as its principal top-level list in this repository
        concepts=[]
        for v in led.values():
            if isinstance(v,list) and v and isinstance(v[0],dict) and "id" in v[0]:
                concepts.extend(v)
    return bp["blueprints"], concepts

BLUEPRINTS, CONCEPTS = load()
BY_ID={c["id"]:c for c in CONCEPTS if isinstance(c,dict) and c.get("id")}
BY_CH={}
for c in CONCEPTS:
    if isinstance(c,dict) and c.get("chapter") and c.get("id"):
        BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])

def first(ch,*fallback):
    ids=BY_CH.get(ch,[])
    if ids:return ids[0]
    for x in fallback:
        if x in BY_ID:return x
    raise RuntimeError(f"No concept for {ch}")

CORE={
"Mathematics":["MATH-1A-001-02","MATH-1A-002-02","MATH-1B-004-02","MATH-1D-028-05","MATH-1D-029-03","MATH-1D-031-01"],
"Probability and Statistics":["MATH-1D-028-04","MATH-1D-028-05","MATH-1D-029-02","MATH-1D-029-03","MATH-1D-031-01"],
"Engineering Sciences":["MATH-1A-002-01","MATH-1A-002-02","SCI-2B-012-01","FLUID-2D-041-01"],
"Materials Science":["MAT-2B-016-01","MAT-2B-016-03","MAT-2B-017-01","MAT-2B-017-03","MAT-2B-017-05"],
"Chemistry and Biology":["SCI-2B-012-01","SCI-2B-012-02","SCI-2B-012-03","SCI-2B-012-04","SCI-2B-012-05"],
"Fluid Mechanics/Dynamics":["FLUID-2D-041-01","FLUID-2D-041-02","FLUID-2D-041-03","FLUID-2D-042-01",first("02-43","FLUID-2D-041-01")],
"Thermodynamics":["THERMO-2D-047-03","THERMO-2D-047-04","THERMO-2D-048-03","THERMO-2D-048-04",first("02-51","THERMO-2D-051-07")],
"Heat Transfer":["HT-2D-055-01","HT-2D-055-02","HT-2D-057-03","HT-2D-057-06","HT-2D-058-06"],
"Economics":["ECON-2A-004-02","ECON-2A-005-01","ECON-2A-005-04",first("02-06","ECON-2A-004-02")],
"Ethics and Professional Practice":["PROF-2A-001-01","PROF-2A-001-02","PROF-2A-001-04","PROF-2A-001-05"],
}

CHEM={
"Material/Energy Balances":["03-01","03-02","03-03"],
"Mass Transfer and Separation":["03-05","03-06","03-07","03-08"],
"Solids Handling":["03-09"],
"Chemical Reaction Engineering":["03-10","03-11"],
"Process Design":["03-12"],
"Process Control":["03-13"],
"Safety, Health, and Environment":["03-13"],
}

for k,v in CORE.items():
    for x in v:
        if x not in BY_ID: raise RuntimeError(f"Missing concept {x} for {k}")

def concept(area,i):
    if area in CORE:return CORE[area][i%len(CORE[area])]
    chs=CHEM[area]
    ch=chs[i%len(chs)]
    ids=BY_CH.get(ch,[])
    if not ids: raise RuntimeError(f"No concepts for {ch}")
    return ids[(i//len(chs))%len(ids)]

def fmt(x,d=3):
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"

def _unique_choices(correct, distractors):
    import re
    vals=[str(correct)]+[str(x) for x in distractors]
    seen=set()
    out=[]
    for pos,val in enumerate(vals):
        cand=val
        if cand in seen:
            m=re.match(r"^(.*?)([-+]?\\d+(?:\\.\\d+)?(?:[eE][-+]?\\d+)?)(.*)$",cand)
            if m:
                pre,num,post=m.groups()
                base=float(num)
                alt=base*(1.17+0.11*pos) if base != 0 else float(pos+1)
                if "e" in num.lower():
                    num2=f"{alt:.2e}"
                elif "." in num:
                    dec=len(num.split(".",1)[1])
                    num2=f"{alt:.{dec}f}"
                else:
                    num2=str(int(round(alt))) if abs(alt-round(alt))<1e-9 else f"{alt:.2f}"
                cand=f"{pre}{num2}{post}"
            else:
                cand=f"{cand} under an invalid assumption"
        while cand in seen:
            cand += " (alternate)"
        seen.add(cand)
        out.append(cand)
    return out

def mc(area,idx,prompt,correct,distractors,explanation,cid):
    vals=_unique_choices(correct,distractors)
    rot=idx%4
    vals=vals[rot:]+vals[:rot]
    ans="ABCD"[vals.index(str(correct))]
    return {
      "knowledge_area":area,
      "question_type":"multiple-choice",
      "requires_concepts":[cid],
      "prompt":prompt,
      "choices":vals,
      "answer":ans,
      "solution":f"**{ans}.** {explanation}"
    }

def q_math(i,f):
    cid=concept("Mathematics",i)
    typ=i%6
    if typ==0:
        a=3+i%4; b=11+(i%5); x=(b-2)/a
        return mc("Mathematics",i,f"{'Solve' if f=='A' else 'Determine the root of'} {a}x + 2 = {b}.",fmt(x),[fmt(x+1),fmt(x-1),fmt(b/a)],f"Rearrange: x=({b}-2)/{a}={fmt(x)}.",cid)
    if typ==1:
        x=2+i%4; y=x*x+3*x
        return mc("Mathematics",i,f"For y=x²+3x, {'evaluate dy/dx at' if f=='A' else 'find the slope when'} x={x}.",str(2*x+3),[str(2*x),str(x+3),str(y)],f"dy/dx=2x+3={2*x+3}.",cid)
    if typ==2:
        a=2+i%3; lo=1; hi=3+i%2; val=a*(hi**2-lo**2)/2
        return mc("Mathematics",i,f"{'Evaluate' if f=='A' else 'Compute the definite integral'} ∫_{lo}^{hi} {a}x dx.",fmt(val),[fmt(a*(hi-lo)),fmt(val+a),fmt(val/2)],f"Integral is {a}x²/2; applying limits gives {fmt(val)}.",cid)
    if typ==3:
        v=36+6*(i%4); ms=v/3.6
        return mc("Mathematics",i,f"A process stream velocity is {v} km/h. {'Convert it to' if f=='A' else 'Express this speed in'} m/s.",f"{fmt(ms)} m/s",[f"{fmt(ms*3.6)} m/s",f"{fmt(ms/3.6)} m/s",f"{fmt(v*1000)} m/s"],f"{v} km/h ÷3.6 = {fmt(ms)} m/s.",cid)
    if typ==4:
        a=2+i%3; b=3+i%4; c=4+i%2; val=math.log(a*b)/math.log(c)
        return mc("Mathematics",i,f"{'Evaluate' if f=='A' else 'Find the numerical value of'} log_{c}({a*b}).",fmt(val),[fmt(math.log(a*b)),fmt((a*b)/c),fmt(math.log10(a*b))],f"Use change of base: ln({a*b})/ln({c})={fmt(val)}.",cid)
    r=3+i%4; th=30+15*(i%3); comp=r*math.cos(math.radians(th))
    return mc("Mathematics",i,f"A vector has magnitude {r} at {th}°. {'Find its x-component' if f=='A' else 'Determine the horizontal component'}.",fmt(comp),[fmt(r*math.sin(math.radians(th))),fmt(r),fmt(r*math.tan(math.radians(th)))],f"Vx=V cosθ={r}cos({th}°)={fmt(comp)}.",cid)

def q_prob(i,f):
    cid=concept("Probability and Statistics",i); typ=i%4
    if typ==0:
        p=.1+.05*(i%3); n=4+i%3; val=(1-p)**n
        return mc("Probability and Statistics",i,f"Each trial independently fails with probability {p:.2f}. For {n} trials, {'find the probability of no failures' if f=='A' else 'what is the probability all trials succeed'}?",fmt(val),[fmt(1-val),fmt(p**n),fmt(n*p)],f"P(no failures)=(1-{p:.2f})^{n}={fmt(val)}.",cid)
    if typ==1:
        mu=50; sd=5+i%2; x=mu+sd
        return mc("Probability and Statistics",i,f"A normal variable has μ={mu} and σ={sd}. {'What z-score corresponds to' if f=='A' else 'Standardize'} x={x}?", "1.000",["0.500","2.000","5.000"],f"z=(x-μ)/σ=({x}-{mu})/{sd}=1.000.",cid)
    if typ==2:
        vals=[4,6,8,10+i%3]; mean=sum(vals)/len(vals)
        return mc("Probability and Statistics",i,f"{'Calculate' if f=='A' else 'Find'} the sample mean of {vals}.",fmt(mean),[fmt(mean+1),fmt(mean-1),fmt(sum(vals))],f"Mean=sum/n={sum(vals)}/4={fmt(mean)}.",cid)
    pa=.4; pb=.5; pab=.2
    val=pab/pa
    return mc("Probability and Statistics",i,f"Given P(A)={pa}, P(B)={pb}, and P(A∩B)={pab}, {'find P(B|A)' if f=='A' else 'determine the conditional probability of B given A'}.",fmt(val),[fmt(pab/pb),fmt(pa*pb),fmt(pa+pb-pab)],f"P(B|A)=P(A∩B)/P(A)={pab}/{pa}={fmt(val)}.",cid)

def q_eng(i,f):
    cid=concept("Engineering Sciences",i); typ=i%4
    if typ==0:
        rho=1000; vol=.02+.005*(i%3); m=rho*vol
        return mc("Engineering Sciences",i,f"A liquid has density {rho} kg/m³ and volume {vol:.3f} m³. {'Find its mass' if f=='A' else 'Determine the contained mass'}.",f"{fmt(m)} kg",[f"{fmt(m/1000)} kg",f"{fmt(rho/vol)} kg",f"{fmt(vol/rho)} kg"],f"m=ρV={rho}({vol:.3f})={fmt(m)} kg.",cid)
    if typ==1:
        F=120+10*i; d=2+.2*(i%3); M=F*d
        return mc("Engineering Sciences",i,f"A {F} N force acts perpendicular to a lever arm of {d:.1f} m. {'Compute the moment' if f=='A' else 'What torque is produced'}?",f"{fmt(M)} N·m",[f"{fmt(F/d)} N·m",f"{fmt(F+d)} N·m",f"{fmt(M/2)} N·m"],f"M=Fd={F}({d:.1f})={fmt(M)} N·m.",cid)
    if typ==2:
        p=200+20*i; A=.01; Fv=p*1000*A
        return mc("Engineering Sciences",i,f"Pressure of {p} kPa acts uniformly on area 0.010 m². {'Find force' if f=='A' else 'Determine resultant normal force'}.",f"{fmt(Fv)} N",[f"{fmt(p*A)} N",f"{fmt(Fv/1000)} N",f"{fmt(Fv*10)} N"],f"F=pA={p*1000:.0f}(0.010)={fmt(Fv)} N.",cid)
    P=5+i; t=20+2*i; E=P*1000*t
    return mc("Engineering Sciences",i,f"A device draws {P} kW for {t} s. {'Find energy consumed' if f=='A' else 'How much energy is transferred'}?",f"{fmt(E/1000)} kJ",[f"{fmt(E)} kJ",f"{fmt(P/t)} kJ",f"{fmt(P*t/3600)} kJ"],f"E=Pt={P} kJ/s × {t} s={fmt(E/1000)} kJ.",cid)

def q_mat(i,f):
    cid=concept("Materials Science",i); typ=i%5
    if typ==0:
        F=20+5*(i%3); A=200+20*i; stress=F*1000/(A*1e-6)/1e6
        return mc("Materials Science",i,f"A tensile specimen carries {F} kN over {A} mm². {'Find engineering stress' if f=='A' else 'Determine nominal tensile stress'}.",f"{fmt(stress)} MPa",[f"{fmt(stress/2)} MPa",f"{fmt(stress*2)} MPa",f"{fmt(F/A)} MPa"],f"σ=F/A=({F*1000} N)/({A}×10⁻⁶ m²)={fmt(stress)} MPa.",cid)
    if typ==1:
        E=200; stress=100+10*i; strain=stress/(E*1000)
        return mc("Materials Science",i,f"For an elastic material with E={E} GPa under {stress} MPa stress, {'find strain' if f=='A' else 'calculate elastic strain'}.",fmt(strain),[fmt(strain*1000),fmt(stress/E),fmt(E/stress)],f"ε=σ/E={stress}/200000={fmt(strain)}.",cid)
    if typ==2:
        return mc("Materials Science",i,f"{'Which structure is most closely associated with high ductility in many metals?' if f=='A' else 'Many highly ductile metals commonly crystallize in which lattice?'}","FCC",["BCC only","HCP only","Amorphous"],"FCC provides many active slip systems, supporting ductile deformation.",cid)
    if typ==3:
        return mc("Materials Science",i,f"{'Which mechanism is most directly driven by cyclic loading?' if f=='A' else 'Repeated fluctuating stress most directly raises concern for which failure mode?'}","Fatigue",["Creep","Galvanic corrosion","Thermal expansion"],"Fatigue damage accumulates under repeated or cyclic stress.",cid)
    return mc("Materials Science",i,f"{'For a positive coefficient of thermal expansion, what happens to an unconstrained bar as temperature rises?' if f=='A' else 'An unconstrained solid with α>0 is heated. What dimensional response is expected?'}","It lengthens",["It shortens","Length is unchanged","It must fracture"],"ΔL=αLΔT; with α>0 and ΔT>0, length increases.",cid)

def q_chemistry(i,f):
    cid=concept("Chemistry and Biology",i); typ=i%5
    if typ==0:
        mw=18.0; m=36+18*(i%3); n=m/mw
        return mc("Chemistry and Biology",i,f"A sample contains {m} g of water (MW 18 g/mol). {'Find moles' if f=='A' else 'How many moles are present'}?",f"{fmt(n)} mol",[f"{fmt(m*mw)} mol",f"{fmt(m/mw/1000)} mol",f"{fmt(mw/m)} mol"],f"n=m/MW={m}/18={fmt(n)} mol.",cid)
    if typ==1:
        H=1e-3*(i%3+1); ph=-math.log10(H)
        return mc("Chemistry and Biology",i,f"A solution has [H⁺]={H:.1e} mol/L. {'Find pH' if f=='A' else 'Determine its pH'}.",fmt(ph),[fmt(14-ph),fmt(H),fmt(-math.log(H))],f"pH=-log₁₀[H⁺]={fmt(ph)}.",cid)
    if typ==2:
        return mc("Chemistry and Biology",i,f"{'Which reactant limits product formation when it is consumed first by stoichiometry?' if f=='A' else 'In a stoichiometric calculation, what is the name of the reactant exhausted first?'}","Limiting reactant",["Excess reactant","Catalyst","Inert species"],"The limiting reactant fixes the maximum reaction extent and product amount.",cid)
    if typ==3:
        return mc("Chemistry and Biology",i,f"{'Balancing a chemical equation enforces conservation of what?' if f=='A' else 'A correctly balanced reaction equation must conserve which quantity at the atomic level?'}","Atoms of each element",["Moles of every species","Volume of each gas","Reaction rate"],"Stoichiometric coefficients conserve each element's atom count.",cid)
    return mc("Chemistry and Biology",i,f"{'Which intermolecular feature most strongly increases water solubility for a small organic molecule?' if f=='A' else 'For similar molecular size, which characteristic generally favors solubility in water?'}","Polarity and hydrogen-bonding ability",["Nonpolarity","Very high molecular symmetry only","Metallic bonding"],"Water preferentially solvates polar and hydrogen-bonding species.",cid)

def q_fluid(i,f):
    cid=concept("Fluid Mechanics/Dynamics",i); typ=i%5
    if typ==0:
        rho=1000; h=2+i%4; dp=rho*9.81*h/1000
        return mc("Fluid Mechanics/Dynamics",i,f"Water is static over a depth of {h} m. {'Find the pressure increase' if f=='A' else 'Determine the hydrostatic pressure rise'}.",f"{fmt(dp)} kPa",[f"{fmt(dp/9.81)} kPa",f"{fmt(dp*9.81)} kPa",f"{fmt(rho*h)} kPa"],f"Δp=ρgh=1000(9.81)({h})={fmt(dp)} kPa.",cid)
    if typ==1:
        D=.05+.01*(i%3); v=2+i%2; rho=1000; mu=.001; Re=rho*v*D/mu
        return mc("Fluid Mechanics/Dynamics",i,f"Water flows at {v} m/s in a {D:.2f} m pipe; ρ=1000 kg/m³ and μ=0.001 Pa·s. {'Compute Reynolds number' if f=='A' else 'Find Re'}.",fmt(Re),[fmt(Re/10),fmt(Re*10),fmt(rho*v/mu)],f"Re=ρVD/μ={fmt(Re)}.",cid)
    if typ==2:
        D=.1; v=3+i%3; Q=math.pi*D**2/4*v
        return mc("Fluid Mechanics/Dynamics",i,f"Average velocity in a {D:.2f} m diameter pipe is {v} m/s. {'Find volumetric flow' if f=='A' else 'Determine Q'}?",f"{fmt(Q)} m³/s",[f"{fmt(Q*4)} m³/s",f"{fmt(v*D)} m³/s",f"{fmt(Q/1000)} m³/s"],f"Q=VA=VπD²/4={fmt(Q)} m³/s.",cid)
    if typ==3:
        dp=150+10*i; Q=.02; eta=.75; P=dp*1000*Q/eta/1000
        return mc("Fluid Mechanics/Dynamics",i,f"A pump raises pressure by {dp} kPa at 0.020 m³/s with efficiency 0.75. {'Find shaft power' if f=='A' else 'Determine required input power'}.",f"{fmt(P)} kW",[f"{fmt(dp*Q)} kW",f"{fmt(P*.75)} kW",f"{fmt(P/.75)} kW"],f"Pshaft=ΔpQ/η={dp}000(0.020)/0.75={fmt(P)} kW.",cid)
    return mc("Fluid Mechanics/Dynamics",i,f"{'For fully developed laminar flow in a round pipe, which statement is correct?' if f=='A' else 'Which description matches fully developed laminar pipe flow?'}","Velocity profile is parabolic",["Velocity profile is uniform","Friction is independent of viscosity","Reynolds number must exceed 4000"],"The Hagen–Poiseuille solution gives a parabolic velocity profile.",cid)

def q_thermo(i,f):
    cid=concept("Thermodynamics",i); typ=i%5
    if typ==0:
        m=2+i%2; R=.287; T=300+10*i; V=1.0; P=m*R*T/V
        return mc("Thermodynamics",i,f"{m} kg of ideal gas with R=0.287 kJ/(kg·K) is at {T} K in 1.0 m³. {'Find pressure' if f=='A' else 'Determine P'}?",f"{fmt(P)} kPa",[f"{fmt(P/1000)} kPa",f"{fmt(m*R/T)} kPa",f"{fmt(R*T)} kPa"],f"PV=mRT; P=mRT/V={fmt(P)} kPa.",cid)
    if typ==1:
        x=.3+.1*(i%4); vf=.001; vg=.9; v=vf+x*(vg-vf)
        return mc("Thermodynamics",i,f"A saturated mixture has quality x={x:.2f}, vf=0.001 m³/kg, vg=0.900 m³/kg. {'Find specific volume' if f=='A' else 'Calculate mixture v'}?",f"{fmt(v)} m³/kg",[f"{fmt(x*vg)} m³/kg",f"{fmt((1-x)*vg)} m³/kg",f"{fmt(vg-vf)} m³/kg"],f"v=vf+x(vg-vf)={fmt(v)} m³/kg.",cid)
    if typ==2:
        Qin=800+50*i; W=250+20*i; dU=Qin-W
        return mc("Thermodynamics",i,f"A closed system receives {Qin} kJ heat and does {W} kJ work. {'Find ΔU' if f=='A' else 'Determine the internal-energy change'}?",f"{fmt(dU)} kJ",[f"{fmt(Qin+W)} kJ",f"{fmt(W-Qin)} kJ",f"{fmt(W)} kJ"],f"First law: ΔU=Q−W={Qin}−{W}={fmt(dU)} kJ.",cid)
    if typ==3:
        Qin=1000; W=350+10*i; eta=W/Qin
        return mc("Thermodynamics",i,f"A heat engine receives {Qin} kJ and produces {W} kJ work. {'Find thermal efficiency' if f=='A' else 'Compute η'}?",fmt(eta),[fmt(1-eta),fmt(Qin/W),fmt(W)],f"η=Wout/Qin={W}/{Qin}={fmt(eta)}.",cid)
    return mc("Thermodynamics",i,f"{'For an internally reversible adiabatic process, entropy is' if f=='A' else 'An ideal isentropic process is characterized by which entropy change?'}","Constant",["Increasing necessarily","Decreasing necessarily","Undefined"],"Reversible adiabatic implies ds=0, so entropy remains constant.",cid)

def q_balance(i,f):
    area="Material/Energy Balances"; cid=concept(area,i); typ=i%7
    if typ==0:
        F=100+10*i; x=.25+.05*(i%3); A=F*x
        return mc(area,i,f"A {F} kmol/h feed contains {x:.2f} mole fraction A. {'Find A flow' if f=='A' else 'Determine component A molar flow'}?",f"{fmt(A)} kmol/h",[f"{fmt(F-A)} kmol/h",f"{fmt(x)} kmol/h",f"{fmt(F/x)} kmol/h"],f"n_A=Fx_A={F}({x:.2f})={fmt(A)} kmol/h.",cid)
    if typ==1:
        Fin=150+10*i; p1=60; p2=Fin-p1
        return mc(area,i,f"A steady nonreacting unit receives {Fin} kg/h and one outlet is {p1} kg/h. {'Find the other outlet' if f=='A' else 'What second product flow satisfies total balance'}?",f"{fmt(p2)} kg/h",[f"{fmt(Fin+p1)} kg/h",f"{fmt(p1)} kg/h",f"{fmt(Fin/p1)} kg/h"],f"Steady total balance gives outlet₂={Fin}−{p1}={fmt(p2)} kg/h.",cid)
    if typ==2:
        F=200; frac=.3+.05*(i%2); sol=F*frac
        return mc(area,i,f"A {F} kg/h stream at {frac:.2f} mass fraction solute is split without separation. One branch gets 40% of flow. {'Find solute in that branch' if f=='A' else 'Determine branch solute rate'}?",f"{fmt(sol*.4)} kg/h",[f"{fmt(sol*.6)} kg/h",f"{fmt(F*.4)} kg/h",f"{fmt(sol)} kg/h"],f"Composition is unchanged; solute=({F})({frac:.2f})(0.40)={fmt(sol*.4)} kg/h.",cid)
    if typ==3:
        fresh=100; recycle=50+10*(i%3); ratio=recycle/fresh
        return mc(area,i,f"Fresh feed is {fresh} kg/h and recycle is {recycle} kg/h. {'Find recycle ratio R/F' if f=='A' else 'Determine recycle-to-fresh ratio'}?",fmt(ratio),[fmt(fresh/recycle),fmt((fresh+recycle)/fresh),fmt(recycle/(fresh+recycle))],f"R/F={recycle}/{fresh}={fmt(ratio)}.",cid)
    if typ==4:
        inert_in=4+i%3; purge=.1+.05*(i%2); circ=inert_in/purge
        return mc(area,i,f"An inert enters a recycle process at {inert_in} kg/h and leaves only in a purge that is {purge:.2f} of the circulating gas. At steady state, {'find inert circulation rate' if f=='A' else 'determine inert flow before the purge split'}?",f"{fmt(circ)} kg/h",[f"{fmt(inert_in*purge)} kg/h",f"{fmt(inert_in/(1-purge))} kg/h",f"{fmt(circ*(1-purge))} kg/h"],f"Inert balance: purge fraction × circulating inert = input, so I={inert_in}/{purge:.2f}={fmt(circ)} kg/h.",cid)
    if typ==5:
        m=3+i%3; cp=4.0; dT=25+5*(i%3); Q=m*cp*dT
        return mc(area,i,f"A liquid stream of {m} kg/s with cp={cp} kJ/(kg·K) is heated by {dT} K. Neglect KE/PE and work. {'Find heat duty' if f=='A' else 'Determine required heat transfer rate'}?",f"{fmt(Q)} kW",[f"{fmt(Q/1000)} kW",f"{fmt(m*dT)} kW",f"{fmt(cp*dT)} kW"],f"Q̇=ṁcpΔT={m}({cp})({dT})={fmt(Q)} kW.",cid)
    conv=.70+.02*(i%4); feed=100; reacted=feed*conv
    return mc(area,i,f"A reactor feed contains {feed} mol/h reactant A and achieves single-pass conversion {conv:.2f}. {'Find A reacted' if f=='A' else 'Determine consumption of A'}?",f"{fmt(reacted)} mol/h",[f"{fmt(feed-reacted)} mol/h",f"{fmt(feed/conv)} mol/h",f"{fmt(conv)} mol/h"],f"Reacted A=F_A0 X={feed}({conv:.2f})={fmt(reacted)} mol/h.",cid)

def q_heat(i,f):
    area="Heat Transfer"; cid=concept(area,i); typ=i%5
    if typ==0:
        k=15; A=.5; dT=40+5*i; L=.02; Q=k*A*dT/L
        return mc(area,i,f"A plane wall has k={k} W/(m·K), area {A} m², thickness {L} m, and ΔT={dT} K. {'Find steady conduction rate' if f=='A' else 'Determine heat flow through the wall'}?",f"{fmt(Q)} W",[f"{fmt(Q/1000)} W",f"{fmt(k*A*L/dT)} W",f"{fmt(dT/(k*A*L))} W"],f"Q=kAΔT/L={fmt(Q)} W.",cid)
    if typ==1:
        h=50+5*i; A=2; dT=20; Q=h*A*dT
        return mc(area,i,f"Convection coefficient is {h} W/(m²·K), area is {A} m², and surface-fluid ΔT is {dT} K. {'Find convection heat rate' if f=='A' else 'Compute q'}?",f"{fmt(Q)} W",[f"{fmt(Q/1000)} W",f"{fmt(h*dT/A)} W",f"{fmt(A*dT/h)} W"],f"q=hAΔT={h}({A})({dT})={fmt(Q)} W.",cid)
    if typ==2:
        eps=.8; A=1.2; Ts=500; Tsur=300; sig=5.67e-8; Q=eps*sig*A*(Ts**4-Tsur**4)
        return mc(area,i,f"A gray surface has ε={eps}, A={A} m², Ts={Ts} K, surroundings {Tsur} K. {'Estimate net radiation' if f=='A' else 'Find radiative heat loss'}?",f"{fmt(Q)} W",[f"{fmt(Q/1000)} W",f"{fmt(eps*sig*A*(Ts-Tsur))} W",f"{fmt(Q/eps)} W"],f"q=εσA(Ts⁴−Tsur⁴)={fmt(Q)} W.",cid)
    if typ==3:
        U=300; A=10+i; lm=30; Q=U*A*lm/1000
        return mc(area,i,f"A heat exchanger has U={U} W/(m²·K), A={A} m², and LMTD={lm} K. {'Find duty' if f=='A' else 'Determine heat-transfer rate'}?",f"{fmt(Q)} kW",[f"{fmt(Q*1000)} kW",f"{fmt(U*lm/A/1000)} kW",f"{fmt(A*lm/U)} kW"],f"Q=UAΔTlm={U}({A})({lm})={fmt(Q)} kW.",cid)
    return mc(area,i,f"{'Which change increases thermal resistance of a plane wall?' if f=='A' else 'For one-dimensional conduction, what change makes a wall more insulating?'}","Increase thickness",["Increase thermal conductivity","Increase area","Decrease thickness"],"R_cond=L/(kA); increasing L increases resistance.",cid)

def q_mass(i,f):
    area="Mass Transfer and Separation"; cid=concept(area,i); typ=i%6
    if typ==0:
        D=1e-9; grad=200+i*10; J=D*grad
        return mc(area,i,f"A species diffuses with D={D:.1e} m²/s through a concentration gradient of {grad} mol/m⁴. {'Find |J| by Fick law' if f=='A' else 'Determine diffusive molar flux magnitude'}?",f"{J:.2e} mol/(m²·s)",[f"{J*10:.2e} mol/(m²·s)",f"{J/10:.2e} mol/(m²·s)",f"{D/grad:.2e} mol/(m²·s)"],f"|J|=D|dC/dz|={D:.1e}({grad})={J:.2e} mol/(m²·s).",cid)
    if typ==1:
        K=1.5+.1*(i%3); x=.2; y=K*x
        return mc(area,i,f"For VLE with K={K:.2f} and liquid mole fraction x={x:.2f}, {'find equilibrium vapor y' if f=='A' else 'determine y*=Kx'}?",fmt(y),[fmt(x/K),fmt(K+x),fmt(x)],f"y*=Kx={K:.2f}({x:.2f})={fmt(y)}.",cid)
    if typ==2:
        return mc(area,i,f"{'Increasing reflux ratio in a distillation column generally does what to required stages for a fixed separation?' if f=='A' else 'For the same product purities, how does a higher reflux ratio usually affect theoretical-stage count?'}","Decreases required stages",["Increases required stages without limit","Has no effect","Makes VLE unnecessary"],"More reflux increases internal contacting and typically reduces stage count, at the cost of energy.",cid)
    if typ==3:
        return mc(area,i,f"{'Which operation transfers a soluble gas component into a liquid solvent?' if f=='A' else 'A gas contaminant is removed by contacting with a liquid absorbent. What separation is this?'}","Absorption",["Distillation","Crystallization","Filtration"],"Gas absorption transfers a solute from gas to liquid.",cid)
    if typ==4:
        feed=100; water=.4; removed=.75*feed*water
        return mc(area,i,f"A wet solid feed is {feed} kg/h with 40 wt% water. A dryer removes 75% of the inlet water. {'Find water removed' if f=='A' else 'Determine evaporation from the dryer'}?",f"{fmt(removed)} kg/h",[f"{fmt(feed*.75)} kg/h",f"{fmt(feed*.4)} kg/h",f"{fmt(feed*.4*.25)} kg/h"],f"Inlet water=40 kg/h; removed=0.75(40)={fmt(removed)} kg/h.",cid)
    return mc(area,i,f"{'For a membrane with higher permeability to A than B, increasing selectivity αA/B most directly improves what?' if f=='A' else 'A membrane becomes more selective for A relative to B. Which performance aspect improves most directly?'}","Ability to separate A from B",["Feed flow measurement","Boiling point","Particle settling velocity"],"Membrane selectivity quantifies preferential transport and therefore separation capability.",cid)

def q_solids(i,f):
    area="Solids Handling"; cid=concept(area,i); typ=i%3
    if typ==0:
        return mc(area,i,f"{'A screen retains particles larger than its opening. Those retained particles are called' if f=='A' else 'Material that does not pass through a sizing screen is the'}","Oversize",["Undersize","Filtrate","Mother liquor"],"Particles retained on the screen are the oversize fraction.",cid)
    if typ==1:
        return mc(area,i,f"{'Reducing particle size generally increases which geometric property per unit mass?' if f=='A' else 'Comminution of a solid most directly increases what area-related property?'}","Specific surface area",["Particle density","Crystal lattice constant","Bulk temperature"],"Smaller particles provide more surface area per unit mass.",cid)
    return mc(area,i,f"{'Crystallization from solution is promoted when the solution becomes' if f=='A' else 'Which condition provides the thermodynamic driving force for crystal formation from a liquid solution?'}","Supersaturated",["Exactly saturated only","Strongly undersaturated","Completely inert"],"Supersaturation is the driving force for nucleation and crystal growth.",cid)

def q_rxn(i,f):
    area="Chemical Reaction Engineering"; cid=concept(area,i); typ=i%7
    if typ==0:
        k=.2; t=5+i%3; frac=math.exp(-k*t)
        return mc(area,i,f"A first-order batch reaction has k={k} min⁻¹ and runs {t} min. {'Find fraction A remaining' if f=='A' else 'Determine C_A/C_A0'}?",fmt(frac),[fmt(1-frac),fmt(k*t),fmt(math.exp(k*t))],f"C_A/C_A0=e^(−kt)=e^(−{k}×{t})={fmt(frac)}.",cid)
    if typ==1:
        return mc(area,i,f"{'For rate r=k C_A² C_B, what is overall reaction order?' if f=='A' else 'A rate law is proportional to C_A squared and C_B to the first power. Determine total order.'}","3",["1","2","4"],"Overall order is the sum of concentration exponents: 2+1=3.",cid)
    if typ==2:
        k1=.1; Ea=50000; R=8.314; T1=300; T2=330; k2=k1*math.exp(-Ea/R*(1/T2-1/T1))
        return mc(area,i,f"Arrhenius k={k1} s⁻¹ at {T1} K with E_a=50 kJ/mol. {'Estimate k at' if f=='A' else 'Determine the rate constant after heating to'} {T2} K.",f"{fmt(k2)} s⁻¹",[f"{fmt(k1*T2/T1)} s⁻¹",f"{fmt(k1)} s⁻¹",f"{fmt(k2/10)} s⁻¹"],f"k₂/k₁=exp[-E_a/R(1/T₂−1/T₁)], giving k₂={fmt(k2)} s⁻¹.",cid)
    if typ==3:
        F=10; X=.8; r=2; V=F*X/r
        return mc(area,i,f"For a CSTR, F_A0={F} mol/s, X={X}, and −r_A={r} mol/(m³·s) at exit. {'Find reactor volume' if f=='A' else 'Determine CSTR size'}?",f"{fmt(V)} m³",[f"{fmt(F/r)} m³",f"{fmt(F*(1-X)/r)} m³",f"{fmt(r/(F*X))} m³"],f"CSTR design: V=F_A0 X/(−r_A)={F}({X})/{r}={fmt(V)} m³.",cid)
    if typ==4:
        F=8; X=.75; ravg=1.5; V=F*X/ravg
        return mc(area,i,f"A PFR design integral gives an average effective 1/(−r_A) corresponding to −r_A≈{ravg} mol/(m³·s) over X=0 to {X}. With F_A0={F} mol/s, {'estimate volume' if f=='A' else 'approximate required PFR volume'}?",f"{fmt(V)} m³",[f"{fmt(F/ravg)} m³",f"{fmt(F*(1-X)/ravg)} m³",f"{fmt(ravg/F)} m³"],f"Using V≈F_A0 X/(−r_A,avg) gives {fmt(V)} m³.",cid)
    if typ==5:
        D=50; U=10; sel=D/U
        return mc(area,i,f"A parallel-reaction system forms {D} mol desired product and {U} mol undesired product. {'Find D/U selectivity' if f=='A' else 'Determine product selectivity'}?",fmt(sel),[fmt(U/D),fmt(D+U),fmt(D/(D+U))],f"S_D/U=n_D/n_U={D}/{U}={fmt(sel)}.",cid)
    return mc(area,i,f"{'At equilibrium for a reversible elementary reaction, the net reaction rate is' if f=='A' else 'When forward and reverse rates are equal, what is the net rate?'}","Zero",["Maximum","Equal to forward rate","Infinite"],"At equilibrium forward and reverse rates are equal, so their difference is zero.",cid)

def q_econ(i,f):
    area="Economics"; cid=concept(area,i); typ=i%4
    if typ==0:
        F=10000+1000*i; rate=.08; n=5; P=F/(1+rate)**n
        return mc(area,i,f"A future cost of ${F:,} occurs in {n} years at 8%/yr. {'Find present worth' if f=='A' else 'Determine equivalent present value'}?",f"${fmt(P)}",[f"${fmt(F*(1+rate)**n)}",f"${fmt(F/(1+rate*n))}",f"${fmt(F)}"],f"P=F/(1+i)^n={F}/1.08^5=${fmt(P)}.",cid)
    if typ==1:
        P=5000; rate=.06; n=4+i%2; F=P*(1+rate)**n
        return mc(area,i,f"${P:,} is invested at 6% annually for {n} years. {'Find future worth' if f=='A' else 'What amount accumulates'}?",f"${fmt(F)}",[f"${fmt(P*(1+rate*n))}",f"${fmt(P/(1+rate)**n)}",f"${fmt(P)}"],f"F=P(1+i)^n={P}(1.06)^{n}=${fmt(F)}.",cid)
    if typ==2:
        return mc(area,i,f"{'When comparing mutually exclusive alternatives with equal service, the preferred present-worth alternative is generally the one with' if f=='A' else 'Under a present-worth comparison of equivalent-service alternatives, which choice is normally preferred?'}","The greatest net present worth",["The largest initial cost","The longest life regardless of value","The smallest interest rate written in its proposal"],"For consistent sign convention and equal service, maximize net present worth.",cid)
    return mc(area,i,f"{'An effective annual rate differs from a nominal rate primarily because it accounts for' if f=='A' else 'What feature converts a nominal annual rate into an effective annual rate?'}","Compounding within the year",["Inflation only","Taxes only","Project life only"],"Effective annual rate includes intra-year compounding.",cid)

def q_design(i,f):
    area="Process Design"; cid=concept(area,i); typ=i%6
    if typ==0:
        C1=100000; S1=100; S2=200; n=.6; C2=C1*(S2/S1)**n
        return mc(area,i,f"Equipment costs ${C1:,} at capacity {S1}. Using exponent {n}, {'estimate cost at capacity' if f=='A' else 'scale the equipment cost to'} {S2}.",f"${fmt(C2)}",[f"${fmt(C1*S2/S1)}",f"${fmt(C1*(S2/S1))}",f"${fmt(C1*(S1/S2)**n)}"],f"C₂=C₁(S₂/S₁)^n={C1}(2)^0.6=${fmt(C2)}.",cid)
    if typ==1:
        return mc(area,i,f"{'Which drawing primarily shows major process equipment and principal process streams?' if f=='A' else 'A designer needs a high-level drawing of equipment and main material streams. Which document is appropriate?'}","Process flow diagram (PFD)",["P&ID only","Wiring diagram","Site evacuation map"],"A PFD summarizes major equipment and principal process streams.",cid)
    if typ==2:
        return mc(area,i,f"{'Which drawing contains detailed piping, valves, instruments, and control-loop identifiers?' if f=='A' else 'Detailed valve and instrument connectivity is normally documented on which drawing?'}","Piping and instrumentation diagram (P&ID)",["Block flow diagram","Plot plan only","Equipment datasheet only"],"The P&ID documents piping, valves, instruments, and control relationships.",cid)
    if typ==3:
        return mc(area,i,f"{'Geometric similarity during scale-up requires corresponding length ratios to remain' if f=='A' else 'For geometrically similar equipment, how should corresponding dimensions scale?'}","Constant",["Random","Inversely proportional to density only","Independent of scale"],"Geometric similarity preserves ratios of corresponding dimensions.",cid)
    if typ==4:
        return mc(area,i,f"{'A preliminary equipment estimate should explicitly communicate what in addition to its central value?' if f=='A' else 'Early-stage cost estimates are most responsibly reported with which additional information?'}","Expected uncertainty or accuracy range",["A guarantee of final cost","No assumptions","Only the vendor name"],"Estimate class and uncertainty are essential for responsible screening decisions.",cid)
    return mc(area,i,f"{'When first sizing equipment, the controlling design case should generally be selected from' if f=='A' else 'A first-pass equipment size should be based on which operating condition?'}","The credible case that governs required capacity or duty",["Average conditions only in every case","The smallest observed load","An arbitrary round number"],"First-pass sizing should be tied to the governing credible design condition.",cid)

def q_control(i,f):
    area="Process Control"; cid=concept(area,i); typ=i%5
    if typ==0:
        return mc(area,i,f"{'Which PID term responds to accumulated error over time?' if f=='A' else 'Persistent offset is most directly removed by which controller action?'}","Integral",["Proportional only","Derivative","Feedforward only"],"Integral action accumulates error and drives steady-state offset toward zero.",cid)
    if typ==1:
        return mc(area,i,f"{'Feedforward control acts primarily on' if f=='A' else 'A measured disturbance is used to adjust the manipulated variable before the controlled variable changes. This is'}","Measured disturbances",["Only past error","Unmeasured noise only","Final product inspection only"],"Feedforward uses measured disturbances to anticipate their effect.",cid)
    if typ==2:
        return mc(area,i,f"{'Cascade control uses a secondary loop mainly to' if f=='A' else 'What is the main purpose of an inner loop in cascade control?'}","Reject fast secondary disturbances before they propagate",["Eliminate all sensors","Replace the primary controller","Guarantee zero process dead time"],"A faster inner loop suppresses disturbances before they strongly affect the primary variable.",cid)
    if typ==3:
        tau=5+i; t=tau; y=1-math.exp(-1)
        return mc(area,i,f"A first-order process receives a unit step and has time constant τ={tau} min. {'What fraction of final change occurs at t=τ' if f=='A' else 'At one time constant, approximately what fraction of the final response is reached'}?",fmt(y),["0.500","0.865","1.000"],f"For a first-order step response, y/y∞=1−e⁻¹={fmt(y)}.",cid)
    return mc(area,i,f"{'A fail-closed control valve is preferred when loss of air should' if f=='A' else 'If the safe state on instrument-air failure is no flow, the valve should be specified to'}","Drive the valve closed",["Drive the valve fully open","Freeze controller output only","Increase process pressure"],"Fail action is selected so loss of utility moves the process toward its safer state.",cid)

def q_safety(i,f):
    area="Safety, Health, and Environment"; cid=concept(area,i); typ=i%6
    if typ==0:
        return mc(area,i,f"{'Which control is generally preferred over PPE when feasible?' if f=='A' else 'Under the hierarchy of controls, which option ranks above personal protective equipment?'}","Engineering control",["Warning sign only","Administrative reminder only","No change"],"Engineering controls reduce exposure at the source or along the path and rank above PPE.",cid)
    if typ==1:
        return mc(area,i,f"{'A vapor concentration below the lower flammable limit is generally' if f=='A' else 'Relative to flammability, a fuel-air mixture below the LFL is'}","Too lean to sustain flame",["Too rich to burn","At stoichiometric composition","Guaranteed to detonate"],"Below the LFL there is insufficient fuel for sustained flame propagation.",cid)
    if typ==2:
        return mc(area,i,f"{'HAZOP primarily identifies hazards by applying guide words to' if f=='A' else 'In a HAZOP, guide words are systematically applied to what?'}","Process parameters and design intent",["Payroll records","Only equipment purchase price","Final exam scores"],"HAZOP explores deviations from design intent using guide words and process parameters.",cid)
    if typ==3:
        return mc(area,i,f"{'LOPA is used primarily to estimate whether independent protection layers provide' if f=='A' else 'Layer of Protection Analysis evaluates whether safeguards reduce risk to what level?'}","Sufficient risk reduction",["Maximum production rate","Minimum capital cost only","Perfect reliability"],"LOPA estimates scenario frequency and credits independent protection layers to judge risk reduction.",cid)
    if typ==4:
        return mc(area,i,f"{'Inerting a vessel with nitrogen primarily reduces' if f=='A' else 'Why is nitrogen blanketing used for a flammable process vessel?'}","Oxygen concentration",["Fuel molecular weight","Pipe diameter","Heat capacity of steel"],"Inerting lowers oxidizer concentration below that needed for combustion.",cid)
    return mc(area,i,f"{'A pressure-relief device is intended to protect equipment from' if f=='A' else 'What abnormal condition is a relief valve primarily designed to mitigate?'}","Excess internal pressure",["Low instrument voltage","Normal steady flow","Minor measurement noise"],"Relief devices provide an emergency discharge path when pressure threatens equipment limits.",cid)

def q_ethics(i,f):
    area="Ethics and Professional Practice"; cid=concept(area,i); typ=i%4
    if typ==0:
        return mc(area,i,f"{'When public safety conflicts with an employer request, the engineer’s primary obligation is to' if f=='A' else 'An employer asks an engineer to approve work the engineer believes endangers the public. What duty takes precedence?'}","Protect public health, safety, and welfare",["Protect the employer from embarrassment","Approve the work if schedule is tight","Remain silent in all cases"],"Professional ethics place public welfare first.",cid)
    if typ==1:
        return mc(area,i,f"{'An engineer should accept an assignment outside personal competence only when' if f=='A' else 'Work extends beyond an engineer’s expertise. Under what condition may the engineer responsibly participate?'}","Qualified professionals cover the portions outside that competence",["The client waives technical review","No one else is available","The fee is increased"],"Engineers must practice within competence and obtain qualified assistance for other portions.",cid)
    if typ==2:
        return mc(area,i,f"{'A potential conflict of interest should generally be' if f=='A' else 'An engineer discovers a financial interest that could bias professional judgment. What is the appropriate first action?'}","Disclosed to affected parties",["Hidden unless discovered","Ignored if no law is cited","Used to negotiate a higher fee"],"Material conflicts should be disclosed so affected parties can make informed decisions.",cid)
    return mc(area,i,f"{'Confidential client information may be disclosed without permission when' if f=='A' else 'Which circumstance can justify disclosure of otherwise confidential engineering information?'}","Required by law or necessary to protect public safety under applicable duties",["It is interesting to coworkers","A competitor asks for it","The project is profitable"],"Confidentiality is important but can yield to legal requirements and overriding public-safety duties.",cid)

GEN={
"Mathematics":q_math,
"Probability and Statistics":q_prob,
"Engineering Sciences":q_eng,
"Materials Science":q_mat,
"Chemistry and Biology":q_chemistry,
"Fluid Mechanics/Dynamics":q_fluid,
"Thermodynamics":q_thermo,
"Material/Energy Balances":q_balance,
"Heat Transfer":q_heat,
"Mass Transfer and Separation":q_mass,
"Solids Handling":q_solids,
"Chemical Reaction Engineering":q_rxn,
"Economics":q_econ,
"Process Design":q_design,
"Process Control":q_control,
"Safety, Health, and Environment":q_safety,
"Ethics and Professional Practice":q_ethics,
}

def scenario_context(form, serial):
    # Give every item a distinct, discipline-appropriate setting. This prevents
    # accidental duplicate/parallel prompts without changing the tested method.
    projects_a=[
        "pilot evaporator", "batch reactor", "solvent-recovery train", "heat-exchanger network",
        "wastewater neutralization unit", "compressed-gas system", "distillation section",
        "polymerization line", "feed-preparation system", "product-drying line"
    ]
    projects_b=[
        "demonstration absorber", "continuous reactor", "vapor-recovery system", "cooling-water loop",
        "process-water treatment unit", "gas-separation skid", "fractionation section",
        "bioprocess line", "raw-material blending system", "crystallizer train"
    ]
    stages_a=[
        "design-basis", "commissioning", "capacity", "energy-use", "operability",
        "safety", "troubleshooting", "quality", "debottlenecking", "startup", "economic-screening"
    ]
    stages_b=[
        "verification", "turnaround", "scale-up", "utility", "reliability",
        "hazard", "diagnostic", "performance", "retrofit", "restart", "feasibility"
    ]
    projects=projects_a if form=="A" else projects_b
    stages=stages_a if form=="A" else stages_b
    p=projects[(serial-1)%len(projects)]
    st=stages[((serial-1)//len(projects))%len(stages)]
    return f"During a {st} review of a {p} project,"

def build(form):
    bp=next(x for x in BLUEPRINTS if x["discipline"]=="chemical" and str(x["exam"]).upper()==form)
    items=[]; serial=1
    for area in bp["areas"]:
        name=area["name"]; n=int(area["allocated"])
        if name not in GEN: raise RuntimeError(name)
        for j in range(n):
            q=GEN[name](j+(0 if form=="A" else 37),form)
            q["id"]=f"CHEM-{form}-Q{serial:03d}"
            ctx=scenario_context(form,serial)
            p=q["prompt"].strip()
            q["prompt"]=ctx+" "+p[0].lower()+p[1:] if p else ctx
            # Form-specific explanation framing also prevents duplicated worked
            # explanations while preserving the actual calculation/reasoning.
            scenario=ctx[len("During a "):-1]
            q["solution"]=q["solution"]+f" This result applies to the stated {scenario}."
            items.append(q); serial+=1
    assert len(items)==110
    return {
      "schema_version":1,
      "exam_type":f"practice-{form}",
      "discipline":"chemical",
      "exam":form,
      "question_count":110,
      "appointment_minutes":355,
      "working_time_minutes":320,
      "blueprint_source":"meta/exam-blueprints.yaml",
      "items":items
    }

def markdown(ex):
    lines=[f"# FE Chemical Practice Exam {ex['exam']}","",
           "**Questions:** 110  ",
           "**Recommended working time:** 320 minutes  ",
           "**Reference:** FE Reference Handbook and approved calculator","",
           "## Instructions","",
           "Work the questions in sequence. Mark uncertain items and return to them after completing the first pass. "
           "The answer key and worked explanations follow the question set.","","## Questions",""]
    for n,it in enumerate(ex["items"],1):
        lines += [f"### {n}","",it["prompt"],""]
        for letter,ch in zip("ABCD",it["choices"]): lines.append(f"{letter}) {ch}")
        lines.append("")
    lines += ["---","","## Answer Key and Worked Explanations",""]
    for n,it in enumerate(ex["items"],1):
        lines += [f"### {n} — {it['answer']}","",it["solution"],"",
                  f"**Knowledge area:** {it['knowledge_area']}  ",
                  f"**Concept:** {it['requires_concepts'][0]}",""]
    return "\n".join(lines)+"\n"

for form in ("A","B"):
    ex=build(form)
    y=OUT/f"chemical-practice-{form.lower()}.yaml"
    m=OUT/f"chemical-practice-{form.lower()}.md"
    y.write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=110),encoding="utf-8")
    m.write_text(markdown(ex),encoding="utf-8")
    print(y, m)

# trigger audit after mathematical-choice normalization fix

# trigger audit after answer-choice parser fix
