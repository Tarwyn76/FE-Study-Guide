#!/usr/bin/env python3
from pathlib import Path
import math,re,yaml
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"; OUT.mkdir(parents=True,exist_ok=True)
LEDGER=ROOT/"meta"/"ledger.yaml"
BPS=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text())["blueprints"]

# Register Mechanical concept IDs from canonical chapter front matter/objectives when absent.
led=yaml.safe_load(LEDGER.read_text()); concepts=led["concepts"]
have={c.get("id") for c in concepts if isinstance(c,dict)}
for p in sorted((ROOT/"layer-3-tracks"/"mechanical").glob("03-*.md")):
    txt=p.read_text()
    fm=re.search(r"^---\n(.*?)\n---",txt,re.S)
    if not fm: continue
    meta=yaml.safe_load(fm.group(1)); ch=str(meta["chapter"]); ids=list(meta.get("ledger_ids") or [])
    objs=[]
    m=re.search(r"## Learning Objectives\n(.*?)(?:\n---|\n## )",txt,re.S)
    if m:
        for line in m.group(1).splitlines():
            mm=re.search(r"\*\*\d+\.\d+\*\*\s+Explain and apply \*\*(.*?)\*\*",line)
            if mm: objs.append(mm.group(1).strip())
    for i,cid in enumerate(ids):
        if cid in have: continue
        concepts.append({"id":cid,"chapter":ch,"layer":3,"track":"mechanical",
                         "title":objs[i] if i<len(objs) else f"Mechanical concept {i+1}"})
        have.add(cid)
LEDGER.write_text(yaml.safe_dump(led,sort_keys=False,allow_unicode=True,width=120))

BY_CH={}
for c in concepts:
    if c.get("chapter") and c.get("id"): BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])
def ids(*chs):
    out=[]
    for ch in chs: out += BY_CH.get(ch,[])
    if not out: raise RuntimeError(chs)
    return out
AREA_IDS={
"Mathematics":ids("01-01","01-02","01-04","01-16","01-19"),
"Probability and Statistics":ids("01-28","01-29","01-30","01-31"),
"Ethics and Professional Practice":ids("02-01","02-02"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Electricity and Magnetism":ids("02-59","02-60","02-61","02-62","02-63","02-64"),
"Statics":ids("02-11","02-12","02-13","02-14"),
"Dynamics, Kinematics, and Vibrations":ids("02-16","02-17","02-18","02-19","03-76","03-77"),
"Mechanics of Materials":ids("02-22","02-23","02-24","02-25","02-26","03-78","03-85"),
"Material Properties and Processing":ids("02-27","02-28","02-29","02-30","03-79"),
"Fluid Mechanics":ids("02-41","02-43","02-44","02-45","02-46","03-80","03-81"),
"Thermodynamics":ids("02-47","02-49","02-50","02-51","02-52","03-82","03-83"),
"Heat Transfer":ids("02-53","02-54","02-55","02-56","02-57","02-58"),
"Measurements, Instrumentation, and Controls":ids("02-66","02-67","02-68","02-69","02-70"),
"Mechanical Design and Analysis":ids("03-84","03-85","03-86","03-87","03-88","03-89","03-90"),
}
def cid(a,i): return AREA_IDS[a][i%len(AREA_IDS[a])]
def fmt(x):
    if isinstance(x,int): return str(x)
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"
def mc(a,i,p,c,ds,sol):
    vals=[str(c)]+[str(x) for x in ds]; seen=[]; out=[]
    for v in vals:
        q=v
        while q in seen:q+=" alt"
        seen.append(q);out.append(q)
    r=(i*2+1)%4; out=out[r:]+out[:r]
    ans="ABCD"[out.index(str(c))]
    return {"knowledge_area":a,"question_type":"multiple-choice","requires_concepts":[cid(a,i)],
            "prompt":p,"choices":out,"answer":ans,"solution":f"**{ans}.** {sol}"}

def q_math(i):
    t=i%6
    if t==0:
        x=2+i%4; y=4*x+3
        return (f"For y=2x²+3x, find dy/dx at x={x}.",str(y),[str(2*x+3),str(4*x),str(y+4)],f"dy/dx=4x+3={y}.")
    if t==1:
        h=2+i%3; v=h*h
        return (f"Evaluate ∫_0^{h} 2x dx.",fmt(v),[fmt(v/2),fmt(2*h),fmt(v+h)],f"Integral=x², giving {fmt(v)}.")
    if t==2:return ("Solve 5x-7=18.","5",["2.2","11","25"],"5x=25, so x=5.")
    if t==3:return ("For matrix [[3,2],[1,5]], find the determinant.","13",["17","7","15"],"det=3(5)-2(1)=13.")
    if t==4:return ("If f(t)=6e^(0.5t), find df/dt.","3e^(0.5t)",["6.5e^(0.5t)","0.5e^(0.5t)","6e^(3t)"],"Differentiate: 6(0.5)e^(0.5t).")
    return ("A line through (1,4) and (5,16) has slope","3",["2","4","12"],"m=(16-4)/(5-1)=3.")

def q_prob(i):
    t=i%6
    if t==0:return ("A dimension is normally distributed with mean 20 mm and σ=2 mm. The z-score at 24 mm is","2",["1","4","12"],"z=(24-20)/2=2.")
    if t==1:return ("For independent events A and B, P(A∩B) equals","P(A)P(B)",["P(A)+P(B)","P(A)-P(B)","1-P(A)"],"Independence gives the product rule.")
    if t==2:return ("A sample of n=64 has population σ=8. The standard error of the mean is","1",["0.125","8","64"],"SE=σ/√n=8/8=1.")
    if t==3:return ("A component fails with probability 0.05 independently. Probability 4 components all survive is",fmt(.95**4),[fmt(1-.95**4),fmt(.05**4),fmt(.8)],f"P=0.95^4={fmt(.95**4)}.")
    if t==4:return ("Which distribution models counts of successes in a fixed number of independent Bernoulli trials?","binomial",["normal only","exponential","uniform"],"The binomial distribution applies.")
    return ("Increasing sample size, all else equal, generally makes a confidence interval","narrower",["wider","unchanged always","invalid"],"Standard error falls as sample size rises.")

def q_ethics(i):
    rows=[
      ("A design calculation reveals a credible hazard to users. The engineer should first","protect health, safety, and welfare",["protect schedule","hide the calculation","wait for failure"],"Public safety is paramount."),
      ("An engineer has a financial interest in a supplier under evaluation. The engineer should","disclose the conflict",["conceal it","select the supplier automatically","destroy bid records"],"Material conflicts require disclosure."),
      ("A request is outside an engineer's competence. The proper response is to","obtain qualified assistance or decline",["approve anyway","copy an unrelated design","avoid review"],"Practice must remain within competence."),
      ("A released drawing contains a material error. The engineer should","correct it and notify affected parties",["ignore it","delete records","conceal it"],"Material errors must be addressed.")
    ];return rows[i%4]

def q_econ(i):
    t=i%5
    if t==0:
        F=40000+1000*(i%5); P=F/(1.06**5)
        return (f"A future overhaul costs ${F:,} in 5 years. At 6%, find present worth.",f"${fmt(P)}",[f"${fmt(F)}",f"${fmt(F*1.06**5)}",f"${fmt(F/(1+.06*5))}"],f"P=F/(1.06)^5=${fmt(P)}.")
    if t==1:return ("A machine costs $90,000 and saves $18,000 per year ignoring time value. Simple payback is","5 years",["2 years","4 years","18 years"],"90000/18000=5 years.")
    if t==2:return ("For equal-service mutually exclusive alternatives, present-worth analysis generally selects","greatest net present worth",["largest first cost","longest life only","lowest salvage value"],"Use consistent assumptions and select greatest net PW.")
    if t==3:return ("Fixed cost is $50,000 and contribution margin is $10/unit. Break-even volume is","5000 units",["500 units","50 units","50000 units"],"Q=F/(p-v)=50000/10.")
    return ("Depreciation primarily represents","allocation of asset cost over its useful life",["cash revenue","loan principal only","salvage paid annually"],"Depreciation allocates capital cost for accounting/tax purposes.")

def q_elec(i):
    t=i%6
    if t==0:return ("A 24 V source is applied across a 12 Ω resistor. Current is","2 A",["0.5 A","12 A","288 A"],"I=V/R=2 A.")
    if t==1:return ("A 10 Ω resistor carries 3 A. Power dissipated is","90 W",["30 W","3.33 W","300 W"],"P=I²R=9×10=90 W.")
    if t==2:return ("Two 6 Ω resistors in parallel have equivalent resistance","3 Ω",["6 Ω","12 Ω","1 Ω"],"Equal parallel resistors halve.")
    if t==3:return ("For sinusoidal voltage and current in phase, power factor is","1",["0","0.5","-1"],"Phase angle zero gives cosφ=1.")
    if t==4:return ("A transformer ideally steps 120 V down to 24 V. Turns ratio Np/Ns is","5",["0.2","24","144"],"Np/Ns=Vp/Vs=120/24=5.")
    return ("Magnetic flux density B is measured in","tesla",["ohm","watt","coulomb per second"],"Tesla is the SI unit of magnetic flux density.")

def q_statics(i):
    t=i%6
    if t==0:return ("A 100 N force acts 2 m perpendicular to a pivot. Moment magnitude is","200 N·m",["50 N·m","100 N·m","202 N·m"],"M=Fd=200 N·m.")
    if t==1:return ("A simply supported beam carries a centered 10 kN point load. Each vertical reaction is","5 kN",["10 kN","2.5 kN","20 kN"],"Symmetry and ΣFy=0 give 5 kN each.")
    if t==2:return ("For a body in planar static equilibrium, the required equations include","ΣFx=0, ΣFy=0, and ΣM=0",["ΣFx=1 only","ΣM=velocity","energy=0 only"],"These are the three independent planar equilibrium equations.")
    if t==3:return ("A 3-4-5 cable carries 100 N tension. Its horizontal component corresponding to side 4 is","80 N",["60 N","100 N","125 N"],"Fx=100(4/5)=80 N.")
    if t==4:return ("The centroid of a rectangle lies at","its geometric center",["one corner","one-third of width only","outside the rectangle"],"Symmetry places the centroid at the center.")
    return ("For impending sliding with coefficient of static friction μs, maximum friction is","μs N",["N/μs","μs/N","zero"],"Fmax=μsN.")

def q_dyn(i):
    t=i%8
    if t==0:return ("A particle accelerates uniformly from 0 to 20 m/s in 5 s. Acceleration is","4 m/s²",["2 m/s²","5 m/s²","100 m/s²"],"a=Δv/Δt=4 m/s².")
    if t==1:return ("A 2 kg mass accelerates at 3 m/s². Net force is","6 N",["1.5 N","5 N","9 N"],"F=ma=6 N.")
    if t==2:return ("A wheel rotates at 10 rad/s with radius 0.5 m. Rim speed is","5 m/s",["10 m/s","20 m/s","0.05 m/s"],"v=rω=5 m/s.")
    if t==3:return ("For constant angular acceleration α, angular velocity follows","ω=ω0+αt",["ω=α/t","ω=t/α","ω=ω0αt²"],"Rotational kinematics parallels linear motion.")
    if t==4:return ("A spring-mass system with k=200 N/m and m=2 kg has undamped natural frequency",fmt(math.sqrt(100))+" rad/s",[fmt(math.sqrt(200)),fmt(100),fmt(5)],"ωn=√(k/m)=10 rad/s.")
    if t==5:return ("Resonance occurs when forcing frequency is near","the system natural frequency",["zero always","twice mass","static deflection only"],"Dynamic amplification peaks near natural frequency.")
    if t==6:return ("Impulse equals the change in","linear momentum",["temperature","mass","spring constant"],"J=Δ(mv).")
    return ("Kinetic energy of a 4 kg mass moving at 3 m/s is","18 J",["6 J","12 J","36 J"],"KE=mv²/2=18 J.")

def q_mom(i):
    t=i%8
    if t==0:return ("A bar carries 20 kN axial tension over 200 mm² area. Normal stress is","100 MPa",["10 MPa","40 MPa","400 MPa"],"σ=P/A=20000/(200e-6)=100 MPa.")
    if t==1:return ("For linear elastic uniaxial loading, Hooke's law is","σ=Eε",["σ=ε/E","E=σε²","σ=E/ε"],"Stress is modulus times strain.")
    if t==2:return ("For pure bending, normal stress magnitude varies","linearly with distance from the neutral axis",["uniformly across depth","quadratically with time","independently of moment"],"σ=My/I.")
    if t==3:return ("A circular shaft in torsion has shear stress proportional to","radius from the center",["temperature only","shaft length only","inverse torque"],"τ=Tr/J.")
    if t==4:return ("A stress concentration factor is defined as","peak local stress divided by nominal stress",["nominal divided by peak","strain divided by area","load divided by length"],"Kt=σmax/σnom.")
    if t==5:return ("For ductile materials under multiaxial static loading, a common failure criterion is","von Mises distortion-energy theory",["Snell's law","Bernoulli equation","Fourier law"],"Von Mises is widely used for ductile yielding.")
    if t==6:return ("Fatigue failure can occur at stresses","below static yield strength under repeated cycling",["only above ultimate strength","only at zero cycles","independent of load cycles"],"Repeated loading can cause fatigue below yield.")
    return ("For a thin-walled cylindrical pressure vessel, hoop stress is approximately","twice the longitudinal stress",["half longitudinal stress","equal to zero","four times wall thickness"],"σh=pr/t and σL=pr/(2t).")

def q_mat(i):
    t=i%7
    if t==0:return ("Young's modulus measures material","elastic stiffness",["density only","thermal conductivity only","hardness only"],"E is the slope of elastic stress-strain response.")
    if t==1:return ("A ductile material typically exhibits","substantial plastic deformation before fracture",["no strain before fracture","zero toughness","perfect brittleness"],"Ductility is capacity for plastic deformation.")
    if t==2:return ("Quenching steel generally aims to produce a","harder microstructure",["softer polymer","lower carbon content automatically","nonmetallic phase only"],"Rapid cooling can form hard martensitic structures.")
    if t==3:return ("Annealing commonly reduces hardness and","relieves residual stress",["increases all residual stress","eliminates atoms","creates only brittle phases"],"Annealing promotes recovery/recrystallization and stress relief.")
    if t==4:return ("Casting is especially useful for producing","complex shapes from molten material",["only flat sheet","only threaded joints","only heat-treated wire"],"Molten material fills a mold cavity.")
    if t==5:return ("Machining is a","subtractive manufacturing process",["additive process only","heat-treatment process only","joining process only"],"Material is removed to create geometry.")
    return ("A factor important in material selection is","strength, stiffness, environment, manufacturability, and cost",["color only","supplier name only","density alone always"],"Selection balances multiple performance constraints.")

def q_fluid(i):
    t=i%8
    if t==0:
        D=.2;V=3;Q=math.pi*D**2/4*V
        return ("Water flows at 3 m/s in a 0.2 m diameter pipe. Flow rate is",f"{fmt(Q)} m³/s",[f"{fmt(Q*2)} m³/s",f"{fmt(V*D)} m³/s",f"{fmt(Q/2)} m³/s"],f"Q=VA={fmt(Q)} m³/s.")
    if t==1:return ("Reynolds number characterizes the ratio of","inertial to viscous effects",["pressure to temperature","heat to mass","voltage to current"],"Re=ρVD/μ.")
    if t==2:return ("For incompressible steady flow, continuity requires","mass flow rate conservation",["temperature conservation only","zero pressure","zero velocity"],"Mass entering equals mass leaving.")
    if t==3:return ("Bernoulli's equation relates pressure, velocity, and","elevation head",["electrical charge","yield strength","entropy generation only"],"Mechanical energy terms include p/γ, V²/2g, and z.")
    if t==4:return ("Darcy-Weisbach pipe head loss is proportional to","f(L/D)V²/(2g)",["V only","1/L","D² only"],"That is the standard Darcy-Weisbach form.")
    if t==5:return ("Drag force on a body in external flow scales with","½ρV²CdA",["ρV only","μA/V only","g/V²"],"Dynamic pressure times coefficient and area gives drag.")
    if t==6:return ("Mach number is the ratio of flow speed to","local speed of sound",["viscosity","density","gravity"],"M=V/a.")
    return ("Across a normal shock in supersonic flow, Mach number generally","decreases to a subsonic value",["increases without limit","remains exactly unchanged","becomes zero always"],"A normal shock decelerates supersonic flow to subsonic.")

def q_thermo(i):
    t=i%8
    if t==0:return ("For an ideal gas, PV equals","nRT",["mcΔT","kAΔT/L","I²R"],"Ideal-gas equation: PV=nRT.")
    if t==1:return ("For a closed system, first-law energy balance is based on","energy conservation",["mass creation","entropy destruction","charge neutrality only"],"Energy cannot be created or destroyed.")
    if t==2:return ("A heat engine thermal efficiency is","net work output divided by heat input",["heat rejected divided by work","mass flow divided by pressure","temperature divided by volume"],"η=Wnet/Qin.")
    if t==3:return ("A refrigerator COP is","desired cooling effect divided by required work input",["work divided by heat rejected","pressure ratio only","temperature difference only"],"COP_R=QL/W.")
    if t==4:return ("Entropy generation for a real irreversible process is","nonnegative",["always negative","always zero","equal to enthalpy"],"The second law requires Sgen≥0.")
    if t==5:return ("For an ideal constant-pressure heating process, sensible heat is commonly estimated with","Q=mc_pΔT",["Q=m/ΔT","Q=kA/L only","Q=IV"],"Enthalpy change for ideal sensible heating uses cp.")
    if t==6:return ("Stoichiometric combustion means","exact theoretical oxidizer for complete combustion",["no oxygen supplied","infinite excess air","fuel never reacts"],"Stoichiometric conditions match theoretical oxygen demand.")
    return ("Relative humidity compares actual water-vapor partial pressure with","saturation vapor pressure at the same temperature",["total pressure only","dry-bulb temperature only","density of liquid water"],"RH=pv/pg at the same T.")

def q_heat(i):
    t=i%7
    if t==0:return ("One-dimensional steady conduction through a plane wall follows","Fourier's law",["Ohm's law only","Hooke's law","Pascal's law"],"q=-kA dT/dx.")
    if t==1:
        q=20*2*30
        return ("A wall has U=20 W/m²-K, area 2 m², and ΔT=30 K. Heat transfer rate is","1200 W",["300 W","600 W","2400 W"],"Q=UAΔT=1200 W.")
    if t==2:return ("Convective heat transfer is commonly written","q=hA(Ts-T∞)",["q=kA/L only","q=mcΔT/t only","q=I²R"],"Newton's law of cooling.")
    if t==3:return ("Thermal radiation from a surface depends strongly on","absolute temperature to the fourth power",["temperature squared only","pressure only","mass flow only"],"Stefan-Boltzmann relation contains T⁴.")
    if t==4:return ("Adding insulation to a plane wall generally","increases thermal resistance",["reduces resistance to zero","has no thermal effect","creates heat"],"R=L/(kA) increases with thickness.")
    if t==5:return ("For resistances in series, total thermal resistance is","the sum of individual resistances",["their product only","the smallest resistance","zero"],"Series thermal resistances add.")
    return ("A heat exchanger effectiveness compares actual heat transfer to","the maximum thermodynamically possible heat transfer",["pump work only","pressure drop only","area only"],"ε=q/qmax.")

def q_meas(i):
    t=i%6
    if t==0:return ("Accuracy refers to closeness to","the true or accepted value",["repeatability only","sample size only","resolution only"],"Accuracy concerns correctness.")
    if t==1:return ("Precision refers primarily to","repeatability of measurements",["closeness to truth only","sensor range only","calibration date only"],"Precision is scatter/repeatability.")
    if t==2:return ("A first-order sensor reaches about 63.2% of a step change after","one time constant",["half a time constant","two periods","zero time"],"First-order response is 1-e^-1.")
    if t==3:return ("A strain gauge changes","electrical resistance with strain",["mass with pressure","temperature only","magnetic flux only"],"Gauge factor relates ΔR/R to strain.")
    if t==4:return ("Negative feedback in a control loop generally tends to","reduce error and improve regulation",["guarantee instability","remove sensing","increase open-loop uncertainty"],"Feedback acts on the error signal.")
    return ("For a stable first-order system, increasing the time constant makes the response","slower",["faster","instantaneous","oscillatory necessarily"],"Larger τ slows exponential response.")

def q_design(i):
    t=i%9
    if t==0:return ("A helical compression spring with greater wire diameter, all else equal, is generally","stiffer",["less stiff","unchanged","unable to carry load"],"Spring rate rises strongly with wire diameter.")
    if t==1:return ("Rolling-element bearing life rating generally decreases as applied load","increases",["decreases","becomes zero","is unrelated"],"Bearing life varies inversely with a power of load.")
    if t==2:return ("A keyed shaft connection is used primarily to","transmit torque between shaft and hub",["seal pressure only","measure temperature","reduce fluid drag"],"The key prevents relative rotation.")
    if t==3:return ("A gear pair primarily changes","speed and torque according to gear ratio",["mass","material modulus","fluid density"],"Gear ratio relates angular speed and torque.")
    if t==4:return ("For a threaded fastener joint, preload is applied primarily to","clamp the joint members together",["reduce all friction to zero","eliminate threads","increase hole diameter"],"Proper preload maintains joint compression.")
    if t==5:return ("A hydraulic actuator converts fluid pressure into","force and motion",["electrical resistance only","heat transfer only","chemical reaction"],"Pressure acting on piston area produces force.")
    if t==6:return ("A clearance fit means","the hole is always larger than the mating shaft within limits",["shaft always larger","zero tolerance","parts are welded"],"Clearance remains positive.")
    if t==7:return ("A factor of safety is generally the ratio of","allowable or failure capacity to applied demand",["demand to capacity always","cost to time","speed to torque"],"FoS compares capacity margin to demand.")
    return ("A design for manufacturability review seeks to","meet function while simplifying reliable economical production",["maximize part count","ignore process capability","eliminate tolerances"],"DFM reduces unnecessary complexity and production risk.")

GEN={"Mathematics":q_math,"Probability and Statistics":q_prob,"Ethics and Professional Practice":q_ethics,
"Engineering Economics":q_econ,"Electricity and Magnetism":q_elec,"Statics":q_statics,
"Dynamics, Kinematics, and Vibrations":q_dyn,"Mechanics of Materials":q_mom,
"Material Properties and Processing":q_mat,"Fluid Mechanics":q_fluid,"Thermodynamics":q_thermo,
"Heat Transfer":q_heat,"Measurements, Instrumentation, and Controls":q_meas,
"Mechanical Design and Analysis":q_design}

def context(form,n):
    if form=="A":
        systems=["pump skid","shaft assembly","HVAC unit","machine frame","gearbox","pressure vessel","test stand","fan system"]
        phases=["design review","performance check","prototype evaluation","failure analysis","commissioning review","verification test"]
        return f"During a {phases[(n//8)%len(phases)]} of a {systems[n%len(systems)]},"
    systems=["compressor package","robotic fixture","thermal loop","rotating machine","drive train","piping module","instrumented rig","air-handling assembly"]
    phases=["separate redesign study","independent calculation check","new validation exercise","alternate operating case","fresh reliability assessment","independent test review"]
    return f"A mechanical engineer is conducting a {phases[(n//8)%len(phases)]} for a {systems[n%len(systems)]}. In that separate case,"

def build(form):
    bp=next(x for x in BPS if x["discipline"]=="mechanical" and x["exam"]==form)
    items=[]; serial=1; offset=0 if form=="A" else 47
    for ar in bp["areas"]:
        a=ar["name"]
        for j in range(int(ar["allocated"])):
            p,c,ds,sol=GEN[a](j+offset)
            stem=context(form,serial)+" "+p[0].lower()+p[1:]
            q=mc(a,j+offset,stem,c,ds,sol); q["id"]=f"MEC-{form}-Q{serial:03d}"
            items.append(q);serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"mechanical","exam":form,
            "question_count":110,"appointment_minutes":355,"working_time_minutes":320,
            "blueprint_source":"meta/exam-blueprints.yaml","items":items}
def md(ex):
    L=[f"# FE Mechanical Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ","","## Questions",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n}","",q["prompt"],""]+[f"{c}) {v}" for c,v in zip("ABCD",q["choices"])]+[""]
    L += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n} — {q['answer']}","",q["solution"],"",f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(L)+"\n"
for form in ("A","B"):
    ex=build(form)
    (OUT/f"mechanical-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=120))
    (OUT/f"mechanical-practice-{form.lower()}.md").write_text(md(ex))
    print(form,len(ex["items"]))
