#!/usr/bin/env python3
from pathlib import Path
import math,re,yaml
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"appendices"/"practice-exams"; OUT.mkdir(parents=True,exist_ok=True)
LEDGER=ROOT/"meta"/"ledger.yaml"; BPS=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text())["blueprints"]
led=yaml.safe_load(LEDGER.read_text()); concepts=led["concepts"]; have={c.get("id") for c in concepts if isinstance(c,dict)}
# Register OTH integration atoms if absent.
for p in sorted((ROOT/"layer-3-tracks"/"other").glob("03-*.md")):
    txt=p.read_text(); fm=re.search(r"^---\n(.*?)\n---",txt,re.S)
    if not fm: continue
    meta=yaml.safe_load(fm.group(1)); ch=str(meta["chapter"]); cids=list(meta.get("ledger_ids") or [])
    objs=[]; m=re.search(r"## Learning Objectives\n(.*?)(?:\n---|\n## )",txt,re.S)
    if m:
        for line in m.group(1).splitlines():
            mm=re.search(r"\*\*\d+\.\d+\*\*\s+Explain and apply \*\*(.*?)\*\*",line)
            if mm: objs.append(mm.group(1).strip())
    for i,cid in enumerate(cids):
        if cid not in have:
            concepts.append({"id":cid,"chapter":ch,"layer":3,"track":"other_disciplines","title":objs[i] if i<len(objs) else f"Other Disciplines integration concept {i+1}"})
            have.add(cid)
LEDGER.write_text(yaml.safe_dump(led,sort_keys=False,allow_unicode=True,width=120))
BY={}
for c in concepts:
    if c.get("chapter") and c.get("id"): BY.setdefault(str(c["chapter"]),[]).append(c["id"])
def ids(*chs):
    out=[]
    for ch in chs: out+=BY.get(ch,[])
    if not out: raise RuntimeError(chs)
    return out
AREA={
"Mathematics":ids("01-01","01-02","01-04","01-16","01-19"),
"Probability and Statistics":ids("01-28","01-29","01-30","01-31"),
"Chemistry":ids("01-22","01-23","01-24","01-25","01-26"),
"Instrumentation and Controls":ids("02-66","02-67","02-68","02-69","02-70"),
"Engineering Ethics and Societal Impacts":ids("02-01","02-02","03-94","03-95"),
"Safety, Health, and Environment":ids("02-03","03-94","03-95"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Statics":ids("02-11","02-12","02-13","02-14"),
"Dynamics":ids("02-16","02-17","02-18","02-19"),
"Strength of Materials":ids("02-22","02-23","02-24","02-25","02-26"),
"Materials":ids("02-27","02-28","02-29","02-30"),
"Fluid Mechanics":ids("02-41","02-43","02-44","02-45","02-46"),
"Basic Electrical Engineering":ids("02-59","02-60","02-61","02-62","02-63","02-64"),
"Thermodynamics and Heat Transfer":ids("02-47","02-49","02-50","02-51","02-52","02-53","02-54","02-55","02-56","02-57","02-58"),
}
def cid(a,i): return AREA[a][i%len(AREA[a])]
def fmt(x):
    if isinstance(x,int): return str(x)
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"
def mc(a,i,p,c,ds,sol):
    vals=[str(c)]+[str(x) for x in ds]
    # make choices unique and rotate
    out=[]; seen=set()
    for v in vals:
        q=v
        while q in seen:q+=" alternative"
        seen.add(q);out.append(q)
    r=(i+2)%4; out=out[r:]+out[:r]; ans="ABCD"[out.index(str(c))]
    return {"knowledge_area":a,"question_type":"multiple-choice","requires_concepts":[cid(a,i)],"prompt":p,"choices":out,"answer":ans,"solution":f"**{ans}.** {sol}"}

def base(a,i):
    t=i%6
    if a=="Mathematics":
        rows=[("For y=3x²+2x, find dy/dx at x=2.","14",["8","12","18"],"dy/dx=6x+2=14."),
              ("Evaluate ∫_0^3 2x dx.","9",["6","12","18"],"Integral=x², so the value is 9."),
              ("Solve 4x+3=23.","5",["4","6","20"],"4x=20, so x=5."),
              ("Find the determinant of [[2,1],[3,4]].","5",["8","11","-5"],"det=2(4)-1(3)=5."),
              ("A line through (2,3) and (6,15) has slope","3",["2","4","12"],"m=(15-3)/(6-2)=3."),
              ("Evaluate log10(10000).","4",["3","10","100"],"10^4=10000, so log10(10000)=4.")]
    elif a=="Probability and Statistics":
        rows=[("A normal observation has x=70, μ=60, σ=5. Find z.","2",["1","5","10"],"z=(70-60)/5=2."),
              ("For independent events A and B, P(A∩B) equals","P(A)P(B)",["P(A)+P(B)","P(A)-P(B)","1-P(A)"],"Independence gives P(A∩B)=P(A)P(B)."),
              ("For n=100 and population σ=20, the standard error is","2",["0.2","10","20"],"SE=σ/√n=20/10=2."),
              ("A success probability is 0.8. Probability of 3 independent successes is","0.512",["0.200","0.600","0.800"],"P=0.8^3=0.512."),
              ("Which distribution models successes in a fixed number of Bernoulli trials?","binomial",["normal","exponential","uniform"],"The binomial distribution applies."),
              ("Increasing sample size generally makes a confidence interval","narrower",["wider","unchanged","invalid"],"Larger n reduces standard error.")]
    elif a=="Chemistry":
        rows=[("For [H+]=1×10^-6 M, pH is","6",["1","8","14"],"pH=-log10(10^-6)=6."),
              ("At 25°C, if pH=9, pOH is","5",["9","14","23"],"pH+pOH=14, so pOH=5."),
              ("Oxidation corresponds to","loss of electrons",["gain of electrons","gain of protons only","no oxidation-state change"],"Oxidation is electron loss."),
              ("If ion product exceeds Ksp, the solution is driven toward","precipitation",["complete vaporization","infinite solubility","no reaction"],"Ion product>Ksp indicates supersaturation."),
              ("A buffer resists changes primarily in","pH",["density","viscosity","mass"],"A buffer limits pH change after modest acid/base addition."),
              ("Henry's law relates dissolved concentration to","gas partial pressure",["solid density","surface roughness","current"],"Henry's law couples gas partial pressure and dissolved concentration.")]
    elif a=="Instrumentation and Controls":
        rows=[("Accuracy is closeness to","the true or accepted value",["repeatability only","range only","resolution only"],"Accuracy describes correctness."),
              ("Precision is primarily","repeatability of measurements",["closeness to truth only","sensor range","calibration interval"],"Precision describes scatter/repeatability."),
              ("A first-order sensor reaches about 63.2% of a step after","one time constant",["two time constants","half a period","zero time"],"1-e^-1=0.632."),
              ("Negative feedback generally tends to","reduce error and improve regulation",["guarantee instability","remove sensing","increase uncertainty"],"Feedback acts on the error signal."),
              ("A strain gauge responds to strain by changing","electrical resistance",["mass","density","pressure only"],"Gauge factor relates resistance change to strain."),
              ("Increasing a stable first-order time constant makes response","slower",["faster","instantaneous","necessarily oscillatory"],"Larger τ slows the exponential response.")]
    elif a=="Engineering Ethics and Societal Impacts":
        rows=[("A credible safety hazard is discovered. The first professional obligation is to","protect health, safety, and welfare",["protect schedule","conceal the hazard","wait for failure"],"Public welfare is paramount."),
              ("A material conflict of interest should be","disclosed",["hidden","ignored","shifted to a vendor"],"Material conflicts require disclosure."),
              ("Work outside one's competence should be","declined or supported by qualified expertise",["approved anyway","copied from unrelated work","performed without review"],"Engineers must practice within competence."),
              ("A material released-design error should be","corrected and communicated",["concealed","ignored","deleted from records"],"Material errors affecting decisions must be addressed."),
              ("Societal impacts of an engineering decision should be","considered alongside technical and economic effects",["ignored","treated as zero","evaluated only after failure"],"Engineering decisions can have broader public consequences."),
              ("A defensible engineering recommendation should clearly state","assumptions, evidence, and material limitations",["only the conclusion","no uncertainty","only favorable data"],"Traceability and disclosure support sound judgment.")]
    elif a=="Safety, Health, and Environment":
        rows=[("The hierarchy of controls generally prefers","elimination or substitution before PPE",["PPE before elimination always","warnings only","no controls"],"Source controls are generally more reliable."),
              ("Risk is commonly evaluated using","likelihood and consequence",["cost only","schedule only","temperature only"],"Risk combines probability/frequency with severity."),
              ("A confined-space atmosphere should be evaluated for","oxygen, toxic, and flammable hazards",["color only","noise only","lighting only"],"Atmospheric hazards are primary confined-space concerns."),
              ("A safety factor is used primarily to","provide margin between capacity and demand",["eliminate uncertainty completely","increase demand","remove inspection"],"Safety factors provide design margin."),
              ("Environmental source reduction is preferred because it","prevents waste before treatment or disposal",["increases waste","eliminates all regulation","always costs more"],"Prevention occurs upstream of control/disposal."),
              ("An incident investigation should focus on","root and contributing causes",["blame only","schedule recovery only","concealment"],"Corrective action depends on understanding causal factors.")]
    elif a=="Engineering Economics":
        rows=[("A future cost of $20,000 occurs in 5 years at 6%. Present worth is",f"${fmt(20000/1.06**5)}",[f"${fmt(20000)}",f"${fmt(20000*1.06**5)}",f"${fmt(20000/(1+.06*5))}"],f"P=20000/(1.06)^5=${fmt(20000/1.06**5)}."),
              ("A $60,000 project saves $15,000/year ignoring time value. Simple payback is","4 years",["2 years","5 years","15 years"],"60000/15000=4 years."),
              ("For equal-service alternatives, present-worth analysis generally chooses","greatest net present worth",["highest first cost","longest life only","lowest salvage"],"Use a common economic basis and choose greatest net PW."),
              ("Fixed cost is $40,000 and contribution margin is $10/unit. Break-even volume is","4000 units",["400 units","40 units","40000 units"],"Q=F/(p-v)=40000/10=4000 units."),
              ("Depreciation represents","allocation of asset cost over useful life",["cash revenue","loan principal only","salvage paid annually"],"Depreciation allocates capital cost."),
              ("Future worth of $10,000 at 5% for 4 years is",f"${fmt(10000*1.05**4)}",[f"${fmt(10000)}",f"${fmt(10000/1.05**4)}",f"${fmt(10000*(1+.05*4))}"],f"F=P(1+i)^n=${fmt(10000*1.05**4)}.")]
    elif a=="Statics":
        rows=[("A 100 N force acts 2 m perpendicular to a pivot. Moment is","200 N·m",["50 N·m","100 N·m","202 N·m"],"M=Fd=100×2=200 N·m."),
              ("A centered 10 kN load on a simply supported beam gives each vertical reaction","5 kN",["2.5 kN","10 kN","20 kN"],"By symmetry and equilibrium, each reaction is 5 kN."),
              ("Planar static equilibrium requires","ΣFx=0, ΣFy=0, ΣM=0",["ΣFx=1 only","ΣM=velocity","energy=0 only"],"These are the three independent planar equilibrium equations."),
              ("A 3-4-5 cable carries 100 N. The component along side 4 is","80 N",["60 N","100 N","125 N"],"100(4/5)=80 N."),
              ("The centroid of a rectangle is at","its geometric center",["one corner","one-third width only","outside the shape"],"Symmetry places it at the center."),
              ("At impending sliding, maximum static friction is","μsN",["N/μs","μs/N","zero"],"Fmax=μsN.")]
    elif a=="Dynamics":
        rows=[("Velocity changes from 0 to 20 m/s in 5 s uniformly. Acceleration is","4 m/s²",["2 m/s²","5 m/s²","100 m/s²"],"a=Δv/Δt=20/5=4 m/s²."),
              ("A 2 kg mass accelerates at 3 m/s². Net force is","6 N",["1.5 N","5 N","9 N"],"F=ma=2×3=6 N."),
              ("A wheel rotates at 10 rad/s with radius 0.5 m. Rim speed is","5 m/s",["10 m/s","20 m/s","0.05 m/s"],"v=rω=0.5×10=5 m/s."),
              ("Impulse equals change in","linear momentum",["temperature","mass","spring constant"],"J=Δ(mv)."),
              ("Kinetic energy of 4 kg moving at 3 m/s is","18 J",["6 J","12 J","36 J"],"KE=mv²/2=4×9/2=18 J."),
              ("For constant acceleration, displacement follows","x=x0+v0t+½at²",["x=at only","x=v/t","x=a/t²"],"This is the standard constant-acceleration kinematic relation.")]
    elif a=="Strength of Materials":
        rows=[("A 20 kN axial load acts on 200 mm². Normal stress is","100 MPa",["10 MPa","40 MPa","400 MPa"],"σ=P/A=20000/(200×10^-6)=100 MPa."),
              ("Linear elastic uniaxial loading follows","σ=Eε",["σ=ε/E","E=σε²","σ=E/ε"],"Hooke's law is σ=Eε."),
              ("Bending normal stress varies","linearly with distance from the neutral axis",["uniformly across depth","with time only","independently of moment"],"σ=My/I."),
              ("Circular-shaft torsional shear stress is proportional to","radius",["temperature","length only","inverse torque"],"τ=Tr/J."),
              ("Stress concentration factor equals","peak local stress divided by nominal stress",["nominal divided by peak","strain/area","load/length"],"Kt=σmax/σnom."),
              ("Fatigue can occur at stresses","below static yield under repeated cycling",["only above ultimate strength","only at zero cycles","independent of cycles"],"Repeated loading can cause fatigue below yield.")]
    elif a=="Materials":
        rows=[("Young's modulus measures","elastic stiffness",["density only","thermal conductivity","hardness only"],"E is the elastic stress-strain slope."),
              ("A ductile material shows","substantial plastic deformation before fracture",["zero strain before fracture","zero toughness","perfect brittleness"],"Ductility is capacity for plastic deformation."),
              ("Annealing commonly","relieves residual stress and reduces hardness",["increases all residual stress","removes atoms","creates only brittle phases"],"Annealing promotes recovery/recrystallization."),
              ("Casting forms parts by","solidifying material in a mold",["removing chips only","threading only","bonding sheet only"],"Molten material fills a mold and solidifies."),
              ("Machining is primarily","subtractive manufacturing",["additive only","heat treatment only","joining only"],"Machining removes material."),
              ("Material selection should consider","properties, environment, manufacturability, and cost",["color only","supplier name only","density alone"],"Selection balances multiple requirements.")]
    elif a=="Fluid Mechanics":
        Q=math.pi*.2**2/4*3
        rows=[("Flow at 3 m/s in a 0.2 m diameter pipe has Q",f"{fmt(Q)} m³/s",[f"{fmt(Q*2)} m³/s",f"{fmt(.6)} m³/s",f"{fmt(Q/2)} m³/s"],f"Q=VA={fmt(Q)} m³/s."),
              ("Reynolds number compares","inertial and viscous effects",["pressure and temperature","heat and mass","voltage and current"],"Re=ρVD/μ."),
              ("Steady incompressible continuity enforces","mass-flow conservation",["temperature conservation only","zero pressure","zero velocity"],"Mass flow entering equals mass flow leaving."),
              ("Bernoulli's equation relates pressure, velocity, and","elevation head",["electrical charge","yield strength","entropy only"],"The mechanical-energy terms include p/γ, V²/2g, and z."),
              ("Darcy-Weisbach head loss contains","f(L/D)V²/(2g)",["V only","1/L","D² only"],"That is the standard pipe-friction form."),
              ("Hydrostatic pressure change is","ρgΔh",["μV/D","kAΔT/L","I²R"],"Hydrostatic balance gives Δp=ρgΔh.")]
    elif a=="Basic Electrical Engineering":
        rows=[("24 V across 12 Ω produces current","2 A",["0.5 A","12 A","288 A"],"I=V/R=24/12=2 A."),
              ("A 10 Ω resistor carrying 3 A dissipates","90 W",["30 W","3.33 W","300 W"],"P=I²R=3²×10=90 W."),
              ("Two 6 Ω resistors in parallel have equivalent resistance","3 Ω",["6 Ω","12 Ω","1 Ω"],"Req=6 Ω/2=3 Ω."),
              ("For sinusoidal voltage and current in phase, power factor is","1",["0","0.5","-1"],"Power factor=cos0=1."),
              ("An ideal transformer steps 120 V to 24 V. Np/Ns is","5",["0.2","24","144"],"Np/Ns=Vp/Vs=120/24=5."),
              ("Magnetic flux density is measured in","tesla",["ohm","watt","coulomb"],"The SI unit is tesla.")]
    else:
        rows=[("For an ideal gas, PV equals","nRT",["mcΔT","kAΔT/L","I²R"],"The ideal-gas equation is PV=nRT."),
              ("A closed-system first-law balance expresses","energy conservation",["mass creation","entropy destruction","charge neutrality only"],"The first law is conservation of energy."),
              ("Heat-engine efficiency is","net work output divided by heat input",["heat rejected/work","mass flow/pressure","temperature/volume"],"η=Wnet/Qin."),
              ("Steady one-dimensional plane-wall conduction follows","Fourier's law",["Ohm's law only","Hooke's law","Pascal's law"],"q=-kA dT/dx."),
              ("Convective heat transfer is commonly written","q=hA(Ts-T∞)",["q=kA/L only","q=mcΔT only","q=I²R"],"Newton's law of cooling gives q=hAΔT."),
              ("Entropy generation for a real irreversible process is","nonnegative",["always negative","always zero","equal to enthalpy"],"The second law requires Sgen≥0.")]
    return rows[t]

GEN=list(AREA)
def context(form,n):
    if form=="A":
        sites=["utility project","manufacturing cell","test laboratory","facility upgrade","field installation","process skid","energy system","service operation"]
        phases=["design review","technical assessment","verification check","operations review","failure investigation","planning study"]
        return f"During a {phases[(n//8)%len(phases)]} for a {sites[n%len(sites)]},"
    sites=["pilot facility","remote equipment package","production support system","building retrofit","prototype assembly","water-energy project","instrumented process","maintenance program"]
    phases=["independent cross-domain review","separate validation exercise","alternate design study","fresh operating case","new risk assessment","independent calculation audit"]
    return f"An engineer is conducting an {phases[(n//8)%len(phases)]} for a {sites[n%len(sites)]}. In that distinct scenario,"

def build(form):
    bp=next(x for x in BPS if x["discipline"]=="other-disciplines" and x["exam"]==form)
    items=[]; serial=1; off=0 if form=="A" else 31
    for ar in bp["areas"]:
        a=ar["name"]
        for j in range(int(ar["allocated"])):
            p,c,ds,sol=base(a,j+off); stem=context(form,serial)+" "+p[0].lower()+p[1:]
            q=mc(a,j+off,stem,c,ds,sol);q["id"]=f"OTH-{form}-Q{serial:03d}";items.append(q);serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"other-disciplines","exam":form,"question_count":110,
            "appointment_minutes":355,"working_time_minutes":320,"blueprint_source":"meta/exam-blueprints.yaml","items":items}
def md(ex):
    L=[f"# FE Other Disciplines Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ","","## Questions",""]
    for n,q in enumerate(ex["items"],1): L += [f"### {n}","",q["prompt"],""]+[f"{c}) {v}" for c,v in zip("ABCD",q["choices"])]+[""]
    L += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1): L += [f"### {n} — {q['answer']}","",q["solution"],"",f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(L)+"\n"
for form in ("A","B"):
    ex=build(form)
    (OUT/f"other-disciplines-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=120))
    (OUT/f"other-disciplines-practice-{form.lower()}.md").write_text(md(ex))
    print(form,len(ex["items"]))
