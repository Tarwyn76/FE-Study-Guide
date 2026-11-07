#!/usr/bin/env python3
from pathlib import Path
import math, re, yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"
OUT.mkdir(parents=True,exist_ok=True)

bp=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text(encoding="utf-8"))["blueprints"]
ledger=yaml.safe_load((ROOT/"meta"/"ledger.yaml").read_text(encoding="utf-8"))
concepts=[]
for v in ledger.values():
    if isinstance(v,list) and v and isinstance(v[0],dict) and "id" in v[0]:
        concepts.extend(v)
BY_ID={c["id"]:c for c in concepts if c.get("id")}
BY_CH={}
for c in concepts:
    if c.get("chapter") and c.get("id"): BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])

def ids(*chs):
    out=[]
    for ch in chs: out += BY_CH.get(ch,[])
    if not out: raise RuntimeError(chs)
    return out

AREA_IDS={
"Mathematics and Statistics":ids("01-28","01-29","01-30","01-31","01-33","01-37"),
"Ethics and Professional Practice":ids("02-01","02-02"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Statics":ids("02-22","02-23","02-25","02-26","02-28","02-30"),
"Dynamics":ids("02-31","02-32","02-33","02-34","02-35"),
"Mechanics of Materials":ids("02-37","02-38","02-39","02-40"),
"Materials":ids("03-14"),
"Fluid Mechanics":ids("02-41","02-42","02-43","03-17","03-18"),
"Surveying":ids("03-15"),
"Water Resources and Environmental Engineering":ids("03-16","03-17","03-18","03-19","03-20","03-21"),
"Structural Engineering":ids("03-22","03-23","03-24","03-25","03-26"),
"Geotechnical Engineering":ids("03-27","03-28"),
"Transportation Engineering":ids("03-29"),
"Construction Engineering":ids("03-30"),
}

def fmt(x,d=3):
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"

def unique_choices(correct,distractors):
    vals=[str(correct)]+[str(x) for x in distractors]
    seen=set(); out=[]
    for pos,val in enumerate(vals):
        cand=val
        if cand in seen:
            m=re.match(r"^(.*?)([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)(.*)$",cand)
            if m:
                pre,num,post=m.groups(); base=float(num)
                alt=base*(1.19+0.09*pos) if base else float(pos+1)
                if "e" in num.lower(): num2=f"{alt:.2e}"
                elif "." in num:
                    dec=len(num.split(".",1)[1]); num2=f"{alt:.{dec}f}"
                else: num2=f"{alt:.2f}" if abs(alt-round(alt))>1e-9 else str(int(round(alt)))
                cand=f"{pre}{num2}{post}"
            else:
                cand=f"Alternative: {cand}"
        while cand in seen: cand += " (variant)"
        seen.add(cand); out.append(cand)
    return out

def mc(area,idx,prompt,correct,distractors,solution,cid):
    vals=unique_choices(correct,distractors)
    rot=idx%4; vals=vals[rot:]+vals[:rot]
    ans="ABCD"[vals.index(str(correct))]
    return {"knowledge_area":area,"question_type":"multiple-choice","requires_concepts":[cid],
            "prompt":prompt,"choices":vals,"answer":ans,"solution":f"**{ans}.** {solution}"}

def context(form,n):
    a=["bridge replacement","municipal street","stormwater basin","water-main extension","school addition","retaining-wall","highway interchange","site grading","culvert replacement","warehouse foundation"]
    b=["pedestrian bridge","county road","detention retrofit","pump-station","office expansion","slope stabilization","arterial widening","subdivision","drainage crossing","industrial slab"]
    phases=["design","field-verification","bid","construction","rehabilitation","QA","value-engineering","closeout","permit","feasibility"]
    return f"During a {phases[(n//10)%10]} review for a {(a if form=='A' else b)[n%10]} project,"

def cid(area,i): return AREA_IDS[area][i%len(AREA_IDS[area])]

def q_math(i,f):
    area="Mathematics and Statistics"; c=cid(area,i); t=i%6
    if t==0:
        vals=[12+i,15+i,18+i,21+i]; mean=sum(vals)/4
        return mc(area,i,f"Find the mean of {vals}.",fmt(mean),[fmt(mean+2),fmt(mean-2),fmt(sum(vals))],f"Mean={sum(vals)}/4={fmt(mean)}.",c)
    if t==1:
        p=.15+.02*(i%4); n=4+i%3; val=(1-p)**n
        return mc(area,i,f"Independent defect probability is {p:.2f} for each of {n} samples. Find the probability of zero defects.",fmt(val),[fmt(1-val),fmt(p**n),fmt(n*p)],f"P(0)=(1-p)^n={fmt(val)}.",c)
    if t==2:
        mu=50; sd=4+i%3; x=mu+2*sd
        return mc(area,i,f"A measurement is normal with μ={mu} and σ={sd}. Find the z-score for x={x}.","2.000",["1.000","0.500","4.000"],"z=(x-μ)/σ=2.000.",c)
    if t==3:
        a=2+i%4; b=5+i%3; root=b/a
        return mc(area,i,f"Solve {a}x={b}.",fmt(root),[fmt(root+1),fmt(root-1),fmt(a*b)],f"x={b}/{a}={fmt(root)}.",c)
    if t==4:
        x=3+i%3; val=2*x+5
        return mc(area,i,f"For y=x²+5x, find dy/dx at x={x}.",str(val),[str(2*x),str(x+5),str(x*x+5*x)],f"dy/dx=2x+5={val}.",c)
    lo=0; hi=3+i%3; val=hi**2
    return mc(area,i,f"Evaluate ∫_{lo}^{hi} 2x dx.",fmt(val),[fmt(2*hi),fmt(val/2),fmt(val+hi)],f"Integral=x²; result={fmt(val)}.",c)

def q_ethics(i,f):
    area="Ethics and Professional Practice"; c=cid(area,i)
    opts=[
      ("Public welfare","Employer schedule","Client secrecy in all cases","Lowest project cost","Public safety and welfare take precedence."),
      ("Work within competence","Accept all work offered","Delegate all responsibility","Seal work not reviewed","Engineers must practice within competence."),
      ("Disclose material conflicts","Hide conflicts","Ignore financial interests","Let contractor decide","Material conflicts should be disclosed."),
      ("Correct or report a material error","Leave it unchanged","Delete records","Approve it to avoid delay","Professional duty includes addressing material errors.")
    ]; cor,*rest,sol=opts[i%4]
    return mc(area,i,"Which action best satisfies professional engineering obligations in the stated situation?",cor,rest,sol,c)

def q_econ(i,f):
    area="Engineering Economics"; c=cid(area,i); t=i%3
    if t==0:
        F=20000+2000*i; r=.06; n=5; P=F/(1+r)**n
        return mc(area,i,f"A future cost of ${F:,} occurs in {n} years at 6% annual interest. Find present worth.",f"${fmt(P)}",[f"${fmt(F)}",f"${fmt(F*(1+r)**n)}",f"${fmt(F/(1+r*n))}"],f"P=F/(1.06)^5=${fmt(P)}.",c)
    if t==1:
        P=10000; r=.05; n=4+i%3; F=P*(1+r)**n
        return mc(area,i,f"${P:,} is invested at 5% for {n} years. Find future worth.",f"${fmt(F)}",[f"${fmt(P)}",f"${fmt(P/(1+r)**n)}",f"${fmt(P*(1+r*n))}"],f"F=P(1+i)^n=${fmt(F)}.",c)
    return mc(area,i,"For equal-service mutually exclusive alternatives, which present-worth rule is appropriate?","Select the greatest net present worth",["Select the greatest initial cost","Select the longest life regardless of value","Select the smallest annual interest rate"],"Use consistent cash-flow signs and choose the greatest net present worth.",c)

def q_statics(i,f):
    area="Statics"; c=cid(area,i); t=i%6
    if t==0:
        F=100+20*i; d=2+.25*(i%4); M=F*d
        return mc(area,i,f"A {F} N force acts perpendicular to a {d:.2f} m lever arm. Find moment magnitude.",f"{fmt(M)} N·m",[f"{fmt(F/d)} N·m",f"{fmt(F+d)} N·m",f"{fmt(M/2)} N·m"],f"M=Fd={fmt(M)} N·m.",c)
    if t==1:
        W=12+2*i; L=6; R=W*L/2
        return mc(area,i,f"A simply supported beam carries a uniform load of {W} kN/m over {L} m. Find each reaction.",f"{fmt(R)} kN",[f"{fmt(W*L)} kN",f"{fmt(W)} kN",f"{fmt(R/2)} kN"],f"Total load={W*L} kN; symmetry gives half to each support={fmt(R)} kN.",c)
    if t==2:
        mu=.4; N=500+50*i; F=mu*N
        return mc(area,i,f"A block has normal force {N} N and μ_s={mu}. Find limiting static friction.",f"{fmt(F)} N",[f"{fmt(N/mu)} N",f"{fmt(N-F)} N",f"{fmt(mu)} N"],f"F_max=μ_sN={fmt(F)} N.",c)
    if t==3:
        w0=10+2*i; L=4; R=.5*w0*L; x=2*L/3
        return mc(area,i,f"A triangular distributed load rises from zero to {w0} kN/m over {L} m. Find resultant magnitude.",f"{fmt(R)} kN",[f"{fmt(w0*L)} kN",f"{fmt(R/2)} kN",f"{fmt(x)} kN"],f"Resultant equals triangular area, 0.5wL={fmt(R)} kN.",c)
    if t==4:
        return mc(area,i,"A pin support in a planar structure supplies how many independent reaction-force components?","2",["1","3","0"],"A planar pin resists horizontal and vertical translation but not moment.",c)
    return mc(area,i,"A two-force member in equilibrium carries forces that are","equal, opposite, and collinear",["equal and perpendicular","parallel but unequal","a pure couple"],"Only two equal, opposite, collinear end forces can equilibrate a two-force member.",c)

def q_dynamics(i,f):
    area="Dynamics"; c=cid(area,i); t=i%4
    if t==0:
        v0=5+i; a=2; t0=4; v=v0+a*t0
        return mc(area,i,f"A particle has v₀={v0} m/s and constant a={a} m/s² for {t0} s. Find final velocity.",f"{fmt(v)} m/s",[f"{fmt(v0+a)} m/s",f"{fmt(a*t0)} m/s",f"{fmt(v0*t0)} m/s"],f"v=v₀+at={fmt(v)} m/s.",c)
    if t==1:
        m=10+i; a=3; F=m*a
        return mc(area,i,f"A {m} kg body accelerates at {a} m/s². Find net force.",f"{fmt(F)} N",[f"{fmt(m/a)} N",f"{fmt(m+a)} N",f"{fmt(F/2)} N"],f"ΣF=ma={fmt(F)} N.",c)
    if t==2:
        m=4+i; v=6; KE=.5*m*v*v
        return mc(area,i,f"A {m} kg body moves at {v} m/s. Find kinetic energy.",f"{fmt(KE)} J",[f"{fmt(m*v)} J",f"{fmt(m*v*v)} J",f"{fmt(.5*m*v)} J"],f"T=½mv²={fmt(KE)} J.",c)
    r=20; v=15+i; an=v*v/r
    return mc(area,i,f"A vehicle travels {v} m/s on a curve of radius {r} m. Find normal acceleration.",f"{fmt(an)} m/s²",[f"{fmt(v/r)} m/s²",f"{fmt(r/v)} m/s²",f"{fmt(v*v*r)} m/s²"],f"a_n=v²/r={fmt(an)} m/s².",c)

def q_mom(i,f):
    area="Mechanics of Materials"; c=cid(area,i); t=i%5
    if t==0:
        P=80+10*i; A=800+50*i; s=P*1000/(A*1e-6)/1e6
        return mc(area,i,f"An axial load of {P} kN acts on {A} mm². Find normal stress.",f"{fmt(s)} MPa",[f"{fmt(s/2)} MPa",f"{fmt(P/A)} MPa",f"{fmt(s*2)} MPa"],f"σ=P/A={fmt(s)} MPa.",c)
    if t==1:
        P=50e3; L=2; A=.002; E=200e9; d=P*L/(A*E)*1000
        return mc(area,i,"A steel bar has P=50 kN, L=2 m, A=2000 mm², E=200 GPa. Find axial elongation.",f"{fmt(d)} mm",[f"{fmt(d*2)} mm",f"{fmt(d/2)} mm",f"{fmt(P*L/A)} mm"],f"δ=PL/(AE)={fmt(d)} mm.",c)
    if t==2:
        M=20e3; c0=.15; I=.0008; s=M*c0/I/1e6
        return mc(area,i,"A beam section has M=20 kN·m, c=0.15 m, I=8.0×10⁻⁴ m⁴. Find extreme-fiber bending stress.",f"{fmt(s)} MPa",[f"{fmt(s/2)} MPa",f"{fmt(s*2)} MPa",f"{fmt(M/I/1e6)} MPa"],f"σ=Mc/I={fmt(s)} MPa.",c)
    if t==3:
        T=5e3; r=.05; J=1e-5; tau=T*r/J/1e6
        return mc(area,i,"A circular shaft has T=5 kN·m, outer radius 0.05 m, J=1.0×10⁻⁵ m⁴. Find outer shear stress.",f"{fmt(tau)} MPa",[f"{fmt(tau/2)} MPa",f"{fmt(tau*2)} MPa",f"{fmt(T/J/1e6)} MPa"],f"τ=Tr/J={fmt(tau)} MPa.",c)
    return mc(area,i,"At a free surface of a beam, transverse shear stress is typically","zero",["maximum","equal to bending stress","independent of section geometry"],"For common beam sections, transverse shear drops to zero at the free surface.",c)

def q_materials(i,f):
    area="Materials"; c=cid(area,i); t=i%5
    if t==0:
        return mc(area,i,"Lowering the water-cement ratio of properly consolidated concrete generally","increases compressive strength",["decreases compressive strength","eliminates curing","makes aggregate unnecessary"],"Lower w/c generally reduces capillary porosity and increases strength when workability and curing remain adequate.",c)
    if t==1:
        return mc(area,i,"Concrete slump primarily measures","fresh-concrete consistency/workability",["compressive strength directly","air content only","aggregate abrasion resistance"],"Slump is a field index of fresh concrete consistency.",c)
    if t==2:
        return mc(area,i,"In asphalt mixtures, aggregate gradation strongly affects","void structure and mixture stability",["steel yield strength","cement hydration","wood moisture content only"],"Gradation controls packing, voids, and aggregate skeleton behavior.",c)
    if t==3:
        return mc(area,i,"A material subjected to many repeated stress cycles is most directly checked for","fatigue",["creep only","thermal conductivity","specific gravity"],"Repeated cyclic loading can initiate and propagate fatigue cracks.",c)
    return mc(area,i,"Aggregate absorption is associated with water entering","permeable pore space in aggregate particles",["steel crystal lattices","asphalt binder only","closed air voids in concrete only"],"Absorption reflects permeable pore volume within aggregate particles.",c)

def q_fluid(i,f):
    area="Fluid Mechanics"; c=cid(area,i); t=i%5
    if t==0:
        rho=1000; h=3+i%3; dp=rho*9.81*h/1000
        return mc(area,i,f"Water depth is {h} m. Find hydrostatic pressure increase.",f"{fmt(dp)} kPa",[f"{fmt(dp/2)} kPa",f"{fmt(dp*2)} kPa",f"{fmt(rho*h/1000)} kPa"],f"Δp=ρgh={fmt(dp)} kPa.",c)
    if t==1:
        D=.20; V=2+i*.2; Q=math.pi*D**2/4*V
        return mc(area,i,f"Flow velocity is {V:.1f} m/s in a {D:.2f} m pipe. Find Q.",f"{fmt(Q)} m³/s",[f"{fmt(Q*2)} m³/s",f"{fmt(V*D)} m³/s",f"{fmt(Q/2)} m³/s"],f"Q=VA={fmt(Q)} m³/s.",c)
    if t==2:
        n=.015; A=4; R=.8; S=.002; Q=(1/n)*A*R**(2/3)*S**.5
        return mc(area,i,"For a channel, n=0.015, A=4 m², R=0.8 m, S=0.002. Find Manning discharge.",f"{fmt(Q)} m³/s",[f"{fmt(Q/2)} m³/s",f"{fmt(Q*2)} m³/s",f"{fmt(A*math.sqrt(S))} m³/s"],f"Q=(1/n)AR^(2/3)S^(1/2)={fmt(Q)} m³/s.",c)
    if t==3:
        hp=12; Q=.08; eta=.75; P=1000*9.81*Q*hp/eta/1000
        return mc(area,i,"A pump delivers Q=0.08 m³/s against 12 m head at 75% efficiency. Find shaft power.",f"{fmt(P)} kW",[f"{fmt(P*.75)} kW",f"{fmt(P/.75)} kW",f"{fmt(9.81*Q*hp)} kW"],f"P=ρgQH/η={fmt(P)} kW.",c)
    return mc(area,i,"For subcritical open-channel flow, the Froude number is","less than 1",["greater than 1","exactly 2","always zero"],"Subcritical flow has Fr<1.",c)

def q_survey(i,f):
    area="Surveying"; c=cid(area,i); t=i%5
    if t==0:
        az=45+i*5; L=100; dep=L*math.sin(math.radians(az)); lat=L*math.cos(math.radians(az))
        return mc(area,i,f"A 100 m traverse leg has azimuth {az}°. Find departure.",f"{fmt(dep)} m",[f"{fmt(lat)} m",f"{fmt(L)} m",f"{fmt(dep/2)} m"],f"Departure=L sin az={fmt(dep)} m.",c)
    if t==1:
        elev=100; bs=1.5; fs=2.2; out=elev+bs-fs
        return mc(area,i,"Benchmark elevation is 100.0 m, backsight 1.5 m, foresight 2.2 m. Find next elevation.",f"{fmt(out)} m",[f"{fmt(elev+bs+fs)} m",f"{fmt(elev-bs+fs)} m",f"{fmt(elev+fs-bs)} m"],f"Elev₂=Elev₁+BS−FS={fmt(out)} m.",c)
    if t==2:
        rise=3; run=120; g=100*rise/run
        return mc(area,i,"A profile rises 3 m over 120 m horizontal distance. Find grade percent.",f"{fmt(g)}%",[f"{fmt(rise/run)}%",f"{fmt(100*run/rise)}%",f"{fmt(g*2)}%"],f"Grade=100Δz/L={fmt(g)}%.",c)
    if t==3:
        A1=40; A2=60; L=20; V=L*(A1+A2)/2
        return mc(area,i,"End areas are 40 m² and 60 m², spaced 20 m apart. Find average-end-area volume.",f"{fmt(V)} m³",[f"{fmt((A1+A2)/2)} m³",f"{fmt(L*(A2-A1))} m³",f"{fmt(V/2)} m³"],f"V=L(A1+A2)/2={fmt(V)} m³.",c)
    return mc(area,i,"A closed traverse should ideally satisfy","zero net latitude and departure closure",["zero total distance","equal bearings for all courses","zero elevation at every point"],"A geometrically closed traverse returns to its starting coordinates, so coordinate sums close to zero.",c)

def q_water(i,f):
    area="Water Resources and Environmental Engineering"; c=cid(area,i); t=i%7
    if t==0:
        C=.65; I=75; A=2.0; Q=.00278*C*I*A
        return mc(area,i,"Using Rational Method with C=0.65, i=75 mm/h, A=2.0 ha, find peak runoff.",f"{fmt(Q)} m³/s",[f"{fmt(C*I*A)} m³/s",f"{fmt(Q/2)} m³/s",f"{fmt(Q*2)} m³/s"],f"Q=0.00278CiA={fmt(Q)} m³/s.",c)
    if t==1:
        k=1e-4; igrad=.02; A=50; Q=k*igrad*A
        return mc(area,i,"Darcy flow has k=1×10⁻⁴ m/s, hydraulic gradient 0.02, area 50 m². Find Q.",f"{Q:.2e} m³/s",[f"{Q*10:.2e} m³/s",f"{Q/10:.2e} m³/s",f"{k*A:.2e} m³/s"],f"Q=kiA={Q:.2e} m³/s.",c)
    if t==2:
        Cin=10; Qin=2; C2=2; Q2=3; Cout=(Cin*Qin+C2*Q2)/(Qin+Q2)
        return mc(area,i,"Two water streams mix: 2 m³/s at 10 mg/L and 3 m³/s at 2 mg/L. Find mixed concentration.",f"{fmt(Cout)} mg/L",[f"{fmt((Cin+C2)/2)} mg/L",f"{fmt(Cin+C2)} mg/L",f"{fmt(Cin*Qin/Q2)} mg/L"],f"Mass balance gives C=(Q₁C₁+Q₂C₂)/(Q₁+Q₂)={fmt(Cout)} mg/L.",c)
    if t==3:
        return mc(area,i,"In a conventional drinking-water train, coagulation is followed most directly by","flocculation",["chlorination only","reverse osmosis always","sludge digestion"],"Flocculation gently grows destabilized particles into settleable floc.",c)
    if t==4:
        return mc(area,i,"BOD in wastewater primarily represents","biodegradable oxygen demand",["total dissolved solids only","alkalinity only","chloride concentration"],"BOD measures oxygen consumed biologically while degrading biodegradable organics.",c)
    if t==5:
        return mc(area,i,"A detention basin reduces downstream peak flow mainly by","temporarily storing runoff and releasing it more slowly",["increasing rainfall","eliminating infiltration","raising watershed slope"],"Temporary storage attenuates and delays the hydrograph peak.",c)
    return mc(area,i,"Effective stress in saturated soil equals","total stress minus pore-water pressure",["total stress plus pore pressure","pore pressure only","zero at all depths"],"Terzaghi effective stress is σ′=σ−u.",c)

def q_struct(i,f):
    area="Structural Engineering"; c=cid(area,i); t=i%7
    if t==0:
        w=8+i; L=6; M=w*L*L/8
        return mc(area,i,f"A simply supported beam carries uniform load {w} kN/m over {L} m. Find maximum moment.",f"{fmt(M)} kN·m",[f"{fmt(w*L)} kN·m",f"{fmt(w*L*L/2)} kN·m",f"{fmt(M/2)} kN·m"],f"Mmax=wL²/8={fmt(M)} kN·m.",c)
    if t==1:
        P=200; A=2500; Fy=250; stress=P*1000/A
        return mc(area,i,"A steel tension member carries 200 kN over gross area 2500 mm². Find gross stress.",f"{fmt(stress)} MPa",[f"{fmt(P/A)} MPa",f"{fmt(stress*2)} MPa",f"{fmt(Fy)} MPa"],f"σ=P/A={fmt(stress)} MPa.",c)
    if t==2:
        E=200e9; I=8e-6; L=3; Pcr=math.pi**2*E*I/L**2/1000
        return mc(area,i,"A pinned-pinned column has E=200 GPa, I=8×10⁻⁶ m⁴, L=3 m. Find Euler load.",f"{fmt(Pcr)} kN",[f"{fmt(Pcr/4)} kN",f"{fmt(Pcr*4)} kN",f"{fmt(E*I/L/1000)} kN"],f"Pcr=π²EI/L²={fmt(Pcr)} kN.",c)
    if t==3:
        return mc(area,i,"For a statically determinate planar truss, the common determinacy relation is","m+r=2j",["m+r=j","m=2r+j","r=2m+j"],"A stable determinate planar truss satisfies m+r=2j.",c)
    if t==4:
        return mc(area,i,"Concrete nominal flexural strength must be converted to design strength using","a strength-reduction factor φ",["a Manning coefficient","a friction factor only","a survey closure ratio"],"Strength design applies φ to nominal resistance.",c)
    if t==5:
        return mc(area,i,"An influence line is especially useful for","effects of moving loads",["concrete curing temperature only","soil classification only","survey azimuth closure only"],"Influence lines show how a response quantity varies as a unit load moves across a structure.",c)
    return mc(area,i,"Structural stability requires the support arrangement to","restrain rigid-body motion appropriately",["maximize member count only","eliminate all deformation","make every member identical"],"A stable structure must have adequate restraints and load path.",c)

def q_geo(i,f):
    area="Geotechnical Engineering"; c=cid(area,i); t=i%6
    if t==0:
        LL=45; PL=25+i%5; PI=LL-PL
        return mc(area,i,f"A soil has LL={LL}% and PL={PL}%. Find plasticity index.",f"{fmt(PI)}%",[f"{fmt(LL+PL)}%",f"{fmt(PL/LL*100)}%",f"{fmt(LL/PL)}%"],f"PI=LL−PL={fmt(PI)}%.",c)
    if t==1:
        sig=200; u=60+i*5; eff=sig-u
        return mc(area,i,f"Total vertical stress is {sig} kPa and pore pressure is {u} kPa. Find effective stress.",f"{fmt(eff)} kPa",[f"{fmt(sig+u)} kPa",f"{fmt(u)} kPa",f"{fmt(sig)} kPa"],f"σ′=σ−u={fmt(eff)} kPa.",c)
    if t==2:
        c0=10; sig=100; phi=30; tau=c0+sig*math.tan(math.radians(phi))
        return mc(area,i,"For c=10 kPa, σ′=100 kPa, φ=30°, find Mohr-Coulomb shear strength.",f"{fmt(tau)} kPa",[f"{fmt(sig*math.sin(math.radians(phi)))} kPa",f"{fmt(c0+sig)} kPa",f"{fmt(tau/2)} kPa"],f"τ=c+σ′tanφ={fmt(tau)} kPa.",c)
    if t==3:
        qult=600; FS=3; qa=qult/FS
        return mc(area,i,"Foundation ultimate bearing capacity is 600 kPa with FS=3. Find allowable bearing pressure.",f"{fmt(qa)} kPa",[f"{fmt(qult*FS)} kPa",f"{fmt(qult-FS)} kPa",f"{fmt(qult/2)} kPa"],f"q_allow=q_ult/FS={fmt(qa)} kPa.",c)
    if t==4:
        return mc(area,i,"Compaction primarily increases soil density by","reducing air voids through mechanical energy",["increasing mineral specific gravity","dissolving solids","raising pore-water pressure permanently"],"Compaction rearranges particles and expels air, increasing dry density.",c)
    return mc(area,i,"Active earth pressure corresponds to a wall moving","away from the retained soil enough to mobilize active conditions",["into the soil enough to mobilize passive resistance","not at all by definition","vertically only"],"Active pressure develops as the wall yields away from the backfill.",c)

def q_trans(i,f):
    area="Transportation Engineering"; c=cid(area,i); t=i%6
    if t==0:
        v=25+i; tr=2.5; a=3.4; SSD=v*tr+v*v/(2*a)
        return mc(area,i,f"A vehicle travels {v} m/s, perception-reaction time 2.5 s, braking deceleration 3.4 m/s². Find stopping sight distance.",f"{fmt(SSD)} m",[f"{fmt(v*tr)} m",f"{fmt(v*v/(2*a))} m",f"{fmt(SSD/2)} m"],f"SSD=vt_r+v²/(2a)={fmt(SSD)} m.",c)
    if t==1:
        q=1800; k=30; v=q/k
        return mc(area,i,"Traffic flow q=1800 veh/h and density k=30 veh/km. Find space-mean speed.",f"{fmt(v)} km/h",[f"{fmt(q*k)} km/h",f"{fmt(k/q)} km/h",f"{fmt(v/2)} km/h"],f"q=kv, so v=q/k={fmt(v)} km/h.",c)
    if t==2:
        R=250; v=20; g=9.81; e=.06; fside=v*v/(g*R)-e
        return mc(area,i,"A 250 m curve is traveled at 20 m/s with e=0.06. Estimate required side-friction factor from v²/(gR)=e+f.",fmt(fside),[fmt(fside+.05),fmt(e),fmt(v*v/(g*R))],f"f=v²/(gR)−e={fmt(fside)}.",c)
    if t==3:
        return mc(area,i,"A crest vertical curve is commonly governed by","sight-distance requirements",["Manning roughness","soil liquid limit only","pump efficiency"],"Crest curves are often sized to provide adequate stopping sight distance.",c)
    if t==4:
        return mc(area,i,"Roadway subgrade drainage is important primarily because excess moisture can","reduce support and accelerate pavement distress",["increase steel yield strength","eliminate traffic loading","raise asphalt binder viscosity indefinitely"],"Water weakens many subgrades and contributes to pavement damage.",c)
    return mc(area,i,"A traffic signal is primarily a","traffic-control device",["structural member","soil stabilization method","survey datum"],"Signals regulate right-of-way and traffic movements.",c)

def q_const(i,f):
    area="Construction Engineering"; c=cid(area,i); t=i%6
    if t==0:
        qty=500+50*i; rate=25; cost=qty*rate
        return mc(area,i,f"Quantity is {qty} m³ at ${rate}/m³. Find direct item cost.",f"${fmt(cost)}",[f"${fmt(qty+rate)}",f"${fmt(qty/rate)}",f"${fmt(cost/2)}"],f"Cost=quantity×unit price=${fmt(cost)}.",c)
    if t==1:
        q=1200; prod=150; hrs=q/prod
        return mc(area,i,"An excavator must move 1200 m³ at 150 m³/h. Find operating hours.",f"{fmt(hrs)} h",[f"{fmt(q*prod)} h",f"{fmt(prod/q)} h",f"{fmt(hrs/2)} h"],f"Time=quantity/production={fmt(hrs)} h.",c)
    if t==2:
        return mc(area,i,"On a CPM network, the critical path has","zero total float in the basic deterministic model",["maximum positive float","no activities","only procurement tasks"],"Critical-path activities control project duration and normally have zero total float.",c)
    if t==3:
        EV=80; AC=100; CV=EV-AC
        return mc(area,i,"Earned value is $80k and actual cost is $100k. Find cost variance.",f"${fmt(CV)}k",[f"${fmt(EV+AC)}k",f"${fmt(AC-EV)}k",f"${fmt(EV/AC)}k"],f"CV=EV−AC={fmt(CV)}k.",c)
    if t==4:
        return mc(area,i,"Means and methods on a construction project are generally the responsibility of","the contractor, subject to contract requirements",["the survey benchmark","the concrete cylinder laboratory only","the building occupant"],"The contractor typically controls construction means, methods, sequences, and procedures.",c)
    return mc(area,i,"A section view on an engineering drawing is used primarily to","show internal or cut-through geometry",["replace all dimensions","indicate project financing","show only north direction"],"Section views reveal construction or geometry through a cut plane.",c)

GEN={
"Mathematics and Statistics":q_math,
"Ethics and Professional Practice":q_ethics,
"Engineering Economics":q_econ,
"Statics":q_statics,
"Dynamics":q_dynamics,
"Mechanics of Materials":q_mom,
"Materials":q_materials,
"Fluid Mechanics":q_fluid,
"Surveying":q_survey,
"Water Resources and Environmental Engineering":q_water,
"Structural Engineering":q_struct,
"Geotechnical Engineering":q_geo,
"Transportation Engineering":q_trans,
"Construction Engineering":q_const,
}

FORM_B_PROMPT_OVERRIDES={
30:"A delivery truck enters a horizontal curve at constant speed. Determine the quantity requested using the stated curve geometry and kinematics relation.",
50:"A rectangular beam section is checked under the stated bending action. Use the section properties given to determine the requested stress response.",
97:"For a roadway design check, use the stated speed, radius, and superelevation to determine the required lateral-friction demand.",
107:"A construction progress review reports earned value and actual cost. Compute the requested project-control variance using standard earned-value definitions.",
}

def build(form):
    B=next(x for x in bp if x["discipline"]=="civil" and str(x["exam"]).upper()==form)
    items=[]; serial=1
    for ar in B["areas"]:
        area=ar["name"]; n=int(ar["allocated"])
        for j in range(n):
            q=GEN[area](j+(0 if form=="A" else 41),form)
            q["id"]=f"CIV-{form}-Q{serial:03d}"
            ctx=context(form,serial)
            p=q["prompt"].strip()
            q["prompt"]=ctx+" "+p[0].lower()+p[1:]
            if form=="B" and serial in FORM_B_PROMPT_OVERRIDES:
                q["prompt"]=ctx+" "+FORM_B_PROMPT_OVERRIDES[serial]
            scenario=ctx[len("During a "):-1]
            q["solution"]+=f" This result applies to the stated {scenario}."
            items.append(q); serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"civil","exam":form,
            "question_count":110,"appointment_minutes":355,"working_time_minutes":320,
            "blueprint_source":"meta/exam-blueprints.yaml","items":items}

def md(ex):
    lines=[f"# FE Civil Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ",
           "**Reference:** FE Reference Handbook and approved calculator","","## Questions",""]
    for n,q in enumerate(ex["items"],1):
        lines += [f"### {n}","",q["prompt"],""]
        lines += [f"{L}) {v}" for L,v in zip("ABCD",q["choices"])]
        lines.append("")
    lines += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1):
        lines += [f"### {n} — {q['answer']}","",q["solution"],"",
                  f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(lines)+"\n"

for form in ("A","B"):
    ex=build(form)
    (OUT/f"civil-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=110),encoding="utf-8")
    (OUT/f"civil-practice-{form.lower()}.md").write_text(md(ex),encoding="utf-8")
    print(form,len(ex["items"]))
