#!/usr/bin/env python3
from pathlib import Path
import math,re,yaml
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"; OUT.mkdir(parents=True,exist_ok=True)
BPS=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text())["blueprints"]
LED=yaml.safe_load((ROOT/"meta"/"ledger.yaml").read_text())["concepts"]
BY_CH={}
for c in LED:
    if c.get("chapter") and c.get("id"): BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])
def ids(*chs):
    a=[]
    for ch in chs:a+=BY_CH.get(ch,[])
    if not a: raise RuntimeError(chs)
    return a
AREA_IDS={
"Mathematics":ids("01-01","01-02","01-04","01-16","01-19"),
"Probability and Statistics":ids("01-28","01-29","01-30","01-31"),
"Ethics and Professional Practice":ids("02-01","02-02"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Fundamental Principles":ids("03-48"),
"Environmental Chemistry":ids("03-49"),
"Health Hazards and Risk Assessment":ids("03-50"),
"Fluid Mechanics and Hydraulics":ids("02-41","02-43","02-44","02-45","02-46","03-51"),
"Thermodynamics":ids("02-47","02-49","02-50","02-51","02-52"),
"Surface Water Resources and Hydrology":ids("03-52","03-53"),
"Groundwater, Soils, and Sediments":ids("03-54","03-55"),
"Water and Wastewater":ids("03-56","03-57","03-58","03-59"),
"Air Quality and Control":ids("03-60"),
"Solid and Hazardous Waste":ids("03-61"),
"Energy and Environment":ids("03-61")
}
def cid(a,i): return AREA_IDS[a][i%len(AREA_IDS[a])]
def fmt(x):
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"
def unique(c,ds):
    vals=[str(c)]+[str(x) for x in ds];out=[];seen=set()
    for k,v in enumerate(vals):
        q=v
        if q in seen:
            m=re.match(r"^(.*?)([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)(.*)$",q)
            if m:
                a,n,b=m.groups();x=float(n);y=x*(1.21+.07*k) if x else k+1
                if "e" in n.lower():nn=f"{y:.2e}"
                elif "." in n:nn=f"{y:.{len(n.split('.')[1])}f}"
                else:nn=str(int(round(y))) if abs(y-round(y))<1e-9 else f"{y:.2f}"
                q=a+nn+b
            else:q="Alternative "+q
        while q in seen:q+=" variant"
        seen.add(q);out.append(q)
    return out
def mc(a,i,p,c,ds,sol):
    v=unique(c,ds);r=i%4;v=v[r:]+v[:r];ans="ABCD"[v.index(str(c))]
    return {"knowledge_area":a,"question_type":"multiple-choice","requires_concepts":[cid(a,i)],"prompt":p,"choices":v,"answer":ans,"solution":f"**{ans}.** {sol}"}
def ctx(form,n):
    A=["water-treatment","wastewater","stormwater","groundwater","air-permit","landfill","remediation","watershed","industrial-discharge","reuse"]
    B=["drinking-water","activated-sludge","detention","aquifer","air-control","solid-waste","site-cleanup","river-basin","process-wastewater","reclaimed-water"]
    ph=["design","compliance","operations","sampling","risk","optimization","permit","troubleshooting","planning","verification"]
    return f"During a {ph[(n//10)%10]} review of a {(A if form=='A' else B)[n%10]} system,"

def q_math(i,f):
    a="Mathematics";t=i%5
    if t==0:
        x=2+i%4;y=4*x+3
        return mc(a,i,f"For y=2x²+3x, find dy/dx at x={x}.",str(4*x+3),[str(2*x+3),str(y),str(4*x)],f"dy/dx=4x+3={4*x+3}.")
    if t==1:
        lo=0;hi=2+i%3;v=hi**2
        return mc(a,i,f"Evaluate ∫_0^{hi} 2x dx.",fmt(v),[fmt(v/2),fmt(2*hi),fmt(v+hi)],f"Integral=x², so result={fmt(v)}.")
    if t==2:return mc(a,i,"Solve 3x+5=20.","5",["3","15","25"],"3x=15, so x=5.")
    if t==3:
        z=math.log10(1000);return mc(a,i,"Evaluate log10(1000).",fmt(z),["2.000","10.00","1000"],"10³=1000, so log10(1000)=3.")
    return mc(a,i,"For a 2×2 matrix [[a,b],[c,d]], the determinant is","ad-bc",["ac-bd","ab-cd","a+b+c+d"],"det=ad-bc.")

def q_prob(i,f):
    a="Probability and Statistics";t=i%4
    if t==0:
        p=.1+.02*(i%3);n=5;v=(1-p)**n
        return mc(a,i,f"A sample exceeds a limit with probability {p:.2f}. For {n} independent samples, find probability none exceed.",fmt(v),[fmt(1-v),fmt(p**n),fmt(n*p)],f"P=(1-p)^n={fmt(v)}.")
    if t==1:return mc(a,i,"A normal variable has μ=50 and σ=5. Find z for x=60.","2.000",["1.000","10.00","12.00"],"z=(60-50)/5=2.")
    if t==2:
        vals=[10,12,14,16+i%2];m=sum(vals)/4
        return mc(a,i,f"Find the mean of {vals}.",fmt(m),[fmt(m+2),fmt(m-2),fmt(sum(vals))],f"Mean=sum/4={fmt(m)}.")
    return mc(a,i,"For independent events A and B, P(A∩B) equals","P(A)P(B)",["P(A)+P(B)","P(A)-P(B)","0 always"],"Independence gives the product rule.")

def q_ethics(i,f):
    a="Ethics and Professional Practice";arr=[
    ("protect public health, safety, and welfare",["protect schedule first","conceal known hazards","approve outside competence"],"Public welfare is paramount."),
    ("disclose a material conflict of interest",["hide it","ignore it","shift it to a vendor"],"Material conflicts must be disclosed."),
    ("practice within one's competence",["seal any requested work","avoid peer review","accept every assignment"],"Engineers must work within competence."),
    ("correct or report a material error",["leave it unchanged","delete records","conceal it"],"Material errors affecting decisions must be addressed.")
    ];c,ds,s=arr[i%4];return mc(a,i,"Which action best meets professional engineering obligations?",c,ds,s)

def q_econ(i,f):
    a="Engineering Economics";t=i%3
    if t==0:
        F=20000+1000*i;P=F/1.06**5
        return mc(a,i,f"A future environmental compliance cost of ${F:,} occurs in 5 years at 6%. Find present worth.",f"${fmt(P)}",[f"${fmt(F)}",f"${fmt(F*1.06**5)}",f"${fmt(F/(1+.06*5))}"],f"P=F/(1.06)^5=${fmt(P)}.")
    if t==1:
        P=10000;F=P*1.05**4
        return mc(a,i,"$10,000 invested at 5% for 4 years grows to what future worth?",f"${fmt(F)}",[f"${fmt(P)}",f"${fmt(P/1.05**4)}",f"${fmt(P*(1+.05*4))}"],f"F=P(1+i)^n=${fmt(F)}.")
    return mc(a,i,"For equal-service mutually exclusive alternatives, the present-worth criterion generally selects","the greatest net present worth",["the highest first cost","the longest life regardless of economics","the lowest nominal interest rate"],"Choose the greatest net present worth using consistent assumptions.")

def q_fund(i,f):
    a="Fundamental Principles";t=i%5
    if t==0:
        Q=2;C=15;load=Q*C*86.4
        return mc(a,i,"A stream flow is 2 m³/s at 15 mg/L. Find mass loading in kg/day.",f"{fmt(load)} kg/day",[f"{fmt(Q*C)} kg/day",f"{fmt(load/2)} kg/day",f"{fmt(load*2)} kg/day"],f"Load=Q C ×86.4={fmt(load)} kg/day.")
    if t==1:
        Qin=3;Cin=20;Qout=3;Cout=8;rate=Qin*Cin-Qout*Cout
        return mc(a,i,"At steady state, Q=3 m³/s enters at 20 mg/L and exits at 8 mg/L. Find contaminant removal rate in mg·m³/s per L-equivalent basis.",fmt(rate),[fmt(Qin*Cin),fmt(Qout*Cout),fmt(rate/2)],f"Steady mass balance gives removal=Q(Cin-Cout)={fmt(rate)} in consistent flow-concentration units.")
    if t==2:
        k=.2;t0=5;frac=math.exp(-k*t0)
        return mc(a,i,"A first-order contaminant decays with k=0.2 day⁻¹ for 5 days. Find C/C0.",fmt(frac),[fmt(1-frac),fmt(k*t0),fmt(math.exp(k*t0))],f"C/C0=e^(-kt)={fmt(frac)}.")
    if t==3:return mc(a,i,"A completely mixed flow reactor assumes the effluent concentration is","equal to the reactor concentration",["always zero","equal to influent concentration","independent of mixing"],"Ideal CSTR mixing makes tank and effluent concentrations equal.")
    return mc(a,i,"Residence time for an ideal tank of volume V with flow Q is","V/Q",["Q/V","VQ","1/(VQ)"],"Hydraulic residence time is volume divided by flow.")

def q_chem(i,f):
    a="Environmental Chemistry";t=i%6
    if t==0:
        H=1e-7;pH=-math.log10(H)
        return mc(a,i,"For [H+]=1×10⁻⁷ M, find pH.",fmt(pH),["1.000","14.00","0.000"],"pH=-log10[H+]=7.")
    if t==1:
        pH=9;pOH=14-pH
        return mc(a,i,"At 25°C, if pH=9, find pOH.",fmt(pOH),["9.000","14.00","23.00"],"pH+pOH=14, so pOH=5.")
    if t==2:return mc(a,i,"Henry's law primarily relates dissolved concentration to","gas partial pressure above the liquid",["soil bulk density only","light intensity","viscosity"],"Henry's law couples gas-phase partial pressure and dissolved concentration.")
    if t==3:return mc(a,i,"A large octanol-water partition coefficient generally indicates a compound is relatively","hydrophobic",["highly ionic in all conditions","nonvolatile by definition","insoluble in octanol"],"Large Kow implies preference for organic phases.")
    if t==4:return mc(a,i,"Oxidation corresponds to","loss of electrons",["gain of electrons","gain of neutrons","no change in oxidation state"],"Oxidation is electron loss.")
    return mc(a,i,"If ion product exceeds Ksp, a sparingly soluble salt is thermodynamically driven toward","precipitation",["complete volatilization","no reaction ever","infinite solubility"],"Ion product > Ksp indicates supersaturation.")

def q_risk(i,f):
    a="Health Hazards and Risk Assessment";t=i%4
    if t==0:
        dose=.002;RfD=.001;HQ=dose/RfD
        return mc(a,i,"Average daily dose is 0.002 mg/kg-day and RfD is 0.001 mg/kg-day. Find hazard quotient.",fmt(HQ),["0.500","0.002","1.000"],"HQ=dose/RfD=2.")
    if t==1:
        dose=1e-4;sf=2;R=dose*sf
        return mc(a,i,"Lifetime average daily dose is 1×10⁻⁴ mg/kg-day and slope factor is 2 (mg/kg-day)⁻¹. Estimate cancer risk.",f"{R:.2e}",["2.00e-04","5.00e-05","2.00e+00"],f"Risk=LADD×SF={R:.2e}.")
    if t==2:return mc(a,i,"The exposure pathway that involves breathing a contaminant is","inhalation",["ingestion","dermal absorption only","sedimentation"],"Breathing exposure is inhalation.")
    return mc(a,i,"A hazard quotient below 1 generally suggests","noncancer adverse effects are not expected at the evaluated exposure",["zero risk of every kind","certain carcinogenicity","automatic regulatory compliance"],"HQ<1 is commonly interpreted as below the reference-dose benchmark.")

def q_fluid(i,f):
    a="Fluid Mechanics and Hydraulics";t=i%7
    if t==0:
        h=4;dp=1000*9.81*h/1000
        return mc(a,i,"Find hydrostatic pressure increase 4 m below a water surface.",f"{fmt(dp)} kPa",[f"{fmt(dp/2)} kPa",f"{fmt(dp*2)} kPa","4.000 kPa"],f"Δp=ρgh={fmt(dp)} kPa.")
    if t==1:
        D=.25;V=2;Q=math.pi*D**2/4*V
        return mc(a,i,"Water velocity is 2 m/s in a 0.25 m diameter pipe. Find flow rate.",f"{fmt(Q)} m³/s",[f"{fmt(Q*2)} m³/s",f"{fmt(V*D)} m³/s",f"{fmt(Q/2)} m³/s"],f"Q=VA={fmt(Q)} m³/s.")
    if t==2:
        fD=.02;L=100;D=.2;V=2;hf=fD*L/D*V*V/(2*9.81)
        return mc(a,i,"For f=0.02, L=100 m, D=0.2 m, V=2 m/s, find Darcy-Weisbach head loss.",f"{fmt(hf)} m",[f"{fmt(hf/2)} m",f"{fmt(hf*2)} m",f"{fmt(fD*L/D)} m"],f"hf=f(L/D)V²/(2g)={fmt(hf)} m.")
    if t==3:
        n=.015;A=3;R=.7;S=.002;Q=(1/n)*A*R**(2/3)*S**.5
        return mc(a,i,"For an open channel, n=0.015, A=3 m², R=0.7 m, S=0.002. Find Manning discharge.",f"{fmt(Q)} m³/s",[f"{fmt(Q/2)} m³/s",f"{fmt(Q*2)} m³/s",f"{fmt(A*S)} m³/s"],f"Q=(1/n)AR^(2/3)S^(1/2)={fmt(Q)} m³/s.")
    if t==4:
        Q=.05;H=15;eta=.7;P=1000*9.81*Q*H/eta/1000
        return mc(a,i,"A pump delivers 0.05 m³/s against 15 m head at 70% efficiency. Find shaft power.",f"{fmt(P)} kW",[f"{fmt(P*.7)} kW",f"{fmt(P/.7)} kW",f"{fmt(9.81*Q*H)} kW"],f"P=ρgQH/η={fmt(P)} kW.")
    if t==5:return mc(a,i,"Reynolds number is used primarily to characterize","flow regime",["water pH","chemical dose","radiation risk"],"Re compares inertial and viscous effects.")
    return mc(a,i,"For a Venturi meter, a pressure drop between inlet and throat is related primarily to","velocity increase through the throat",["chemical equilibrium","electrical resistance","soil compaction"],"Continuity and Bernoulli connect reduced area to increased velocity and reduced pressure.")

def q_thermo(i,f):
    a="Thermodynamics";t=i%3
    if t==0:
        m=2;cp=4.18;dT=20;Q=m*cp*dT
        return mc(a,i,"2 kg of water is heated 20°C with cp=4.18 kJ/kg-K. Estimate sensible heat.",f"{fmt(Q)} kJ",[f"{fmt(cp*dT)} kJ",f"{fmt(m*dT)} kJ",f"{fmt(Q/2)} kJ"],f"Q=mc_pΔT={fmt(Q)} kJ.")
    if t==1:return mc(a,i,"For an ideal gas at fixed amount, PV=nRT implies pressure increases with absolute temperature when volume is","constant",["infinite","zero mass","unrelated to temperature"],"At fixed V and n, P is proportional to T.")
    return mc(a,i,"Entropy generation for a real irreversible process is","nonnegative",["always negative","always zero","equal to enthalpy"],"The second law requires S_gen≥0.")

def q_hydro(i,f):
    a="Surface Water Resources and Hydrology";t=i%6
    if t==0:
        C=.7;i0=60;A=1.5;Q=.00278*C*i0*A
        return mc(a,i,"Using Rational Method with C=0.7, i=60 mm/h, A=1.5 ha, find peak runoff.",f"{fmt(Q)} m³/s",[f"{fmt(Q/2)} m³/s",f"{fmt(Q*2)} m³/s",f"{fmt(C*i0*A)} m³/s"],f"Q=0.00278CiA={fmt(Q)} m³/s.")
    if t==1:return mc(a,i,"A detention basin attenuates a storm hydrograph mainly by","temporarily storing runoff and releasing it more slowly",["increasing rainfall","eliminating watershed area","raising soil density"],"Storage delays and reduces the peak outflow.")
    if t==2:return mc(a,i,"The time of concentration is the travel time from","the hydraulically most remote point to the watershed outlet",["the nearest curb inlet only","groundwater table to atmosphere","any random point"],"Tc characterizes the longest relevant runoff travel path.")
    if t==3:return mc(a,i,"Infiltration reduces direct runoff by","transferring water from the surface into the soil",["increasing impervious area","raising rainfall intensity","eliminating evapotranspiration"],"Infiltration removes water from surface runoff.")
    if t==4:return mc(a,i,"A unit hydrograph represents watershed response to","one unit depth of effective rainfall of specified duration",["one unit of groundwater head","one pollutant molecule","one year of evaporation"],"Unit hydrographs scale runoff response to unit excess precipitation.")
    return mc(a,i,"Eutrophication is commonly driven by excess inputs of","nutrients such as nitrogen and phosphorus",["inert sand only","oxygen alone","pure water"],"Nutrient enrichment stimulates excessive biological productivity.")

def q_ground(i,f):
    a="Groundwater, Soils, and Sediments";t=i%6
    if t==0:
        k=1e-4;grad=.03;A=40;Q=k*grad*A
        return mc(a,i,"Darcy flow has k=1×10⁻⁴ m/s, gradient 0.03, area 40 m². Find Q.",f"{Q:.2e} m³/s",[f"{Q*10:.2e} m³/s",f"{Q/10:.2e} m³/s",f"{k*A:.2e} m³/s"],f"Q=kiA={Q:.2e} m³/s.")
    if t==1:return mc(a,i,"Hydraulic gradient is defined as","head loss divided by flow-path length",["flow rate divided by area only","porosity times density","pressure plus temperature"],"i=Δh/L.")
    if t==2:return mc(a,i,"Sorption generally causes a dissolved contaminant plume to move","more slowly than groundwater",["faster than light","at exactly zero velocity","independent of soil"],"Sorption retards solute transport relative to advective groundwater flow.")
    if t==3:return mc(a,i,"A monitoring well network is used primarily to","characterize groundwater levels and contaminant distribution",["increase rainfall","replace all soil samples","measure air emissions only"],"Monitoring wells provide hydraulic and water-quality data.")
    if t==4:return mc(a,i,"Pump-and-treat remediation relies on","extracting contaminated groundwater for treatment",["only capping soil","heating the atmosphere","increasing infiltration intentionally"],"Extraction wells capture groundwater and send it to treatment.")
    return mc(a,i,"Effective porosity controls primarily","the pore space available for groundwater flow",["air stack height","combustion temperature","pump motor voltage"],"Effective porosity excludes isolated pore space.")

def q_water(i,f):
    a="Water and Wastewater";t=i%7
    if t==0:
        Cin=200;Cout=20;eta=(Cin-Cout)/Cin*100
        return mc(a,i,"Influent concentration is 200 mg/L and effluent is 20 mg/L. Find removal efficiency.",f"{fmt(eta)}%",[f"{fmt(Cout/Cin*100)}%",f"{fmt(Cin-Cout)}%",f"{fmt(eta/2)}%"],f"η=(Cin-Cout)/Cin×100={fmt(eta)}%.")
    if t==1:return mc(a,i,"Coagulation is followed most directly by","flocculation",["chlorination only","sludge digestion","reverse osmosis always"],"Flocculation promotes particle collisions after destabilization.")
    if t==2:return mc(a,i,"Primary sedimentation removes contaminants mainly by","gravity settling of settleable solids",["biological nitrification","UV photolysis only","ion exchange"],"Clarifiers remove settleable suspended matter by gravity.")
    if t==3:return mc(a,i,"Activated sludge treatment is primarily a","suspended-growth biological process",["membrane-only process","chemical oxidation only","groundwater process"],"Biomass suspended in aeration basins consumes biodegradable substrate.")
    if t==4:return mc(a,i,"Disinfection is intended primarily to","inactivate pathogenic microorganisms",["increase hardness","add suspended solids","raise BOD"],"Disinfection reduces pathogen viability.")
    if t==5:
        Q=5000;dose=3;kgd=Q*3.785*1000*dose/1e6
        return mc(a,i,"A plant treats 5000 gal/day at a chemical dose of 3 mg/L. Estimate chemical mass in kg/day.",f"{fmt(kgd)} kg/day",[f"{fmt(kgd/2)} kg/day",f"{fmt(kgd*2)} kg/day",f"{fmt(Q*dose/1e6)} kg/day"],f"Convert gallons to liters and multiply by dose: {fmt(kgd)} kg/day.")
    return mc(a,i,"Anaerobic digestion is commonly used to","stabilize sludge and reduce volatile solids",["increase influent BOD","remove grit only","increase dissolved oxygen"],"Anaerobic digestion converts volatile solids and produces biogas.")

def q_air(i,f):
    a="Air Quality and Control";t=i%6
    if t==0:
        ef=.5;rate=100;em=ef*rate
        return mc(a,i,"An emission factor is 0.5 kg/ton and production is 100 ton/day. Find emissions.",f"{fmt(em)} kg/day",[f"{fmt(ef/rate)} kg/day",f"{fmt(rate/ef)} kg/day",f"{fmt(em/2)} kg/day"],f"Emissions=EF×activity={fmt(em)} kg/day.")
    if t==1:return mc(a,i,"A baghouse primarily removes","particulate matter",["dissolved groundwater contaminants","noise","BOD"],"Fabric filters capture suspended particles from gas streams.")
    if t==2:return mc(a,i,"An electrostatic precipitator removes particles primarily by","electrically charging and collecting them",["biological oxidation","gravity drainage only","chlorination"],"ESPs use electric fields to migrate charged particles to collection plates.")
    if t==3:return mc(a,i,"A cyclone separator relies mainly on","inertial and centrifugal separation",["chemical precipitation","adsorption equilibrium only","UV disinfection"],"Cyclones use swirling flow to drive particles toward the wall.")
    if t==4:return mc(a,i,"Gas absorption transfers a pollutant from gas into","a liquid phase",["a solid landfill only","vacuum only","electrical current"],"Absorbers contact contaminated gas with a liquid solvent.")
    return mc(a,i,"Indoor-air concentration at steady state decreases when clean-air ventilation rate","increases",["decreases to zero","is unrelated to concentration","becomes negative"],"Greater clean-air dilution lowers steady-state concentration for fixed generation.")

def q_waste(i,f):
    a="Solid and Hazardous Waste";t=i%5
    if t==0:
        pop=10000;gen=2;mass=pop*gen/1000
        return mc(a,i,"A community of 10,000 people generates 2 kg/person-day. Find waste generation in metric tons/day.",f"{fmt(mass)} metric tons/day",[f"{fmt(pop*gen)} metric tons/day",f"{fmt(mass/2)} metric tons/day",f"{fmt(gen)} metric tons/day"],f"Mass=population×rate/1000={fmt(mass)} metric tons/day.")
    if t==1:return mc(a,i,"A landfill liner system is designed primarily to","limit contaminant migration from leachate",["increase waste combustion","eliminate collection vehicles","raise air emissions"],"Liners reduce seepage of leachate into surrounding soil and groundwater.")
    if t==2:return mc(a,i,"Landfill gas commonly contains substantial","methane and carbon dioxide",["oxygen only","chlorine gas only","nitrogen dioxide only"],"Anaerobic decomposition generates methane and carbon dioxide.")
    if t==3:return mc(a,i,"Hazardous-waste compatibility screening is important to prevent","dangerous reactions during mixing or storage",["all moisture loss","traffic congestion","groundwater recharge"],"Incompatible wastes can react violently or generate toxic gases.")
    return mc(a,i,"Composting is most appropriate for the biodegradable fraction of","organic solid waste",["metals","glass","inert concrete"],"Composting biologically stabilizes organic material.")

def q_energy(i,f):
    a="Energy and Environment";t=i%4
    if t==0:
        E=1000;eta=.9;use=E*eta
        return mc(a,i,"An energy system receives 1000 kWh with 90% conversion efficiency. Find useful output.",f"{fmt(use)} kWh",[f"{fmt(E/eta)} kWh",f"{fmt(E*(1-eta))} kWh",f"{fmt(eta)} kWh"],f"Useful energy=ηEin={fmt(use)} kWh.")
    if t==1:return mc(a,i,"A lifecycle assessment considers environmental burdens across","multiple stages from resource extraction through end of life",["operation only","construction only","disposal only"],"LCA evaluates impacts across the product/system life cycle.")
    if t==2:return mc(a,i,"A carbon footprint is commonly expressed in","CO2-equivalent emissions",["pH units","decibels only","meters of head"],"Different greenhouse gases are normalized to CO2-equivalent.")
    return mc(a,i,"Improving energy efficiency generally reduces environmental burden when it","reduces resource use or emissions per unit service",["always increases fuel use","eliminates all impacts","requires no system boundary"],"Efficiency can lower inputs and associated emissions per useful output.")

GEN={"Mathematics":q_math,"Probability and Statistics":q_prob,"Ethics and Professional Practice":q_ethics,
"Engineering Economics":q_econ,"Fundamental Principles":q_fund,"Environmental Chemistry":q_chem,
"Health Hazards and Risk Assessment":q_risk,"Fluid Mechanics and Hydraulics":q_fluid,"Thermodynamics":q_thermo,
"Surface Water Resources and Hydrology":q_hydro,"Groundwater, Soils, and Sediments":q_ground,
"Water and Wastewater":q_water,"Air Quality and Control":q_air,"Solid and Hazardous Waste":q_waste,
"Energy and Environment":q_energy}

def build(form):
    b=next(x for x in BPS if x["discipline"]=="environmental" and str(x["exam"]).upper()==form)
    items=[];serial=1
    for ar in b["areas"]:
        a=ar["name"]
        for j in range(int(ar["allocated"])):
            q=GEN[a](j+(0 if form=="A" else 47),form);q["id"]=f"ENV-{form}-Q{serial:03d}"
            c=ctx(form,serial);p=q["prompt"];q["prompt"]=c+" "+p[0].lower()+p[1:]
            q["solution"]+=f" This result applies to the stated {c[len('During a '):-1]}."
            items.append(q);serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"environmental","exam":form,
            "question_count":110,"appointment_minutes":355,"working_time_minutes":320,
            "blueprint_source":"meta/exam-blueprints.yaml","items":items}
def md(ex):
    L=[f"# FE Environmental Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ","","## Questions",""]
    for n,q in enumerate(ex["items"],1):L += [f"### {n}","",q["prompt"],""]+[f"{c}) {v}" for c,v in zip("ABCD",q["choices"])]+[""]
    L += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1):L += [f"### {n} — {q['answer']}","",q["solution"],"",f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(L)+"\n"
for form in ("A","B"):
    ex=build(form)
    (OUT/f"environmental-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=110))
    (OUT/f"environmental-practice-{form.lower()}.md").write_text(md(ex))
    print(form,len(ex["items"]))
