#!/usr/bin/env python3
from pathlib import Path
import math,re,yaml,random
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"; OUT.mkdir(parents=True,exist_ok=True)
LEDGER=ROOT/"meta"/"ledger.yaml"
BPS=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text())["blueprints"]

# Repair missing Industrial & Systems concept registrations from canonical chapter metadata/objectives.
led=yaml.safe_load(LEDGER.read_text())
concepts=led["concepts"]; have={c.get("id") for c in concepts if isinstance(c,dict)}
for p in sorted((ROOT/"layer-3-tracks"/"industrial").glob("03-*.md")):
    txt=p.read_text()
    fm=re.search(r"^---\n(.*?)\n---",txt,re.S)
    if not fm: continue
    meta=yaml.safe_load(fm.group(1))
    ch=str(meta["chapter"]); ids=list(meta.get("ledger_ids") or [])
    objs=[]
    m=re.search(r"## Learning Objectives\n(.*?)(?:\n---|\n## )",txt,re.S)
    if m:
        for line in m.group(1).splitlines():
            mm=re.search(r"\*\*\d+\.\d+\*\*\s+Explain and apply \*\*(.*?)\*\*",line)
            if mm: objs.append(mm.group(1).strip())
    for i,cid in enumerate(ids):
        if cid in have: continue
        concepts.append({"id":cid,"chapter":ch,"layer":3,"track":"industrial_and_systems",
                         "title":objs[i] if i<len(objs) else f"Industrial & Systems concept {i+1}"})
        have.add(cid)
LEDGER.write_text(yaml.safe_dump(led,sort_keys=False,allow_unicode=True,width=120))

BY_CH={}
for c in concepts:
    if c.get("chapter") and c.get("id"): BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])
def ids(*chs):
    out=[]
    for ch in chs: out += BY_CH.get(ch,[])
    if not out: raise RuntimeError(f"No concepts for {chs}")
    return out

AREA_IDS={
"Mathematics":ids("01-01","01-02","01-04","01-16","01-19"),
"Engineering Sciences":ids("03-62","03-69"),
"Ethics and Professional Practice":ids("02-01","02-02"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Probability and Statistics":ids("01-28","01-29","01-30","01-31"),
"Modeling and Quantitative Analysis":ids("03-62","03-63","03-64","03-65"),
"Engineering Management":ids("03-66","03-67"),
"Manufacturing, Service, and Other Production Systems":ids("03-68","03-69","03-70"),
"Facilities and Supply Chain":ids("03-71","03-72"),
"Human Factors, Ergonomics, and Safety":ids("03-73"),
"Work Design":ids("03-73"),
"Quality":ids("03-74"),
"Systems Engineering, Analysis, and Design":ids("03-75"),
}
def cid(a,i): return AREA_IDS[a][i%len(AREA_IDS[a])]
def fmt(x):
    if isinstance(x,int): return str(x)
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"
def unique(vals):
    out=[]; seen=set()
    for v in map(str,vals):
        q=v
        while q in seen:q+=" (alternate)"
        seen.add(q);out.append(q)
    return out
def mc(a,i,p,c,ds,sol):
    vals=unique([c]+ds); r=(i*3+1)%4; vals=vals[r:]+vals[:r]
    ans="ABCD"[vals.index(str(c))]
    return {"knowledge_area":a,"question_type":"multiple-choice","requires_concepts":[cid(a,i)],
            "prompt":p,"choices":vals,"answer":ans,"solution":f"**{ans}.** {sol}"}

def q_math(i):
    t=i%6
    if t==0:
        x=2+i%5; c=3*x*x-4*x+7
        return ("For f(x)=x³-2x²+7x, evaluate f'(x) at x=%d."%x,fmt(c),[fmt(c+6),fmt(c-4),fmt(x*x)],f"f'(x)=3x²-4x+7={c}.")
    if t==1:
        a=3+i%4;b=5+i%3;c=a*b/2
        return (f"A triangular response profile has base {a} and height {b}. Find its area.",fmt(c),[fmt(a*b),fmt(c/2),fmt(a+b)],f"A=bh/2={fmt(c)}.")
    if t==2:return ("For matrix [[2,3],[1,4]], find the determinant.","5",["11","8","-5"],"det=2(4)-3(1)=5.")
    if t==3:return ("Solve ln(x)=2 for x.","e²",["2e","ln 2","e/2"],"Exponentiation gives x=e².")
    if t==4:return ("If y=4e^(0.2t), what is dy/dt?","0.8e^(0.2t)",["4.2e^(0.2t)","0.2e^(0.2t)","4e^(0.8t)"],"Differentiate the exponential: 4(0.2)e^(0.2t).")
    return ("A line passes through (2,5) and (6,17). Find its slope.","3",["2","4","12"],"m=(17-5)/(6-2)=3.")

def q_science(i):
    t=i%6
    if t==0:return ("A workstation processes 48 parts in 6 h. What is average throughput?","8 parts/h",["6 parts/h","42 parts/h","288 parts/h"],"Throughput=48/6=8 parts/h.")
    if t==1:return ("A 20 N force moves an object 4 m in its direction. How much work is done?","80 J",["5 J","24 J","160 J"],"W=Fd=80 J.")
    if t==2:return ("A 2 kW machine operates for 3 h. How much energy does it use?","6 kWh",["0.667 kWh","5 kWh","9 kWh"],"Energy=power×time=6 kWh.")
    if t==3:return ("Which quantity is conserved in a steady-flow material balance with no accumulation or reaction?","mass",["temperature","pressure","cycle time"],"For the stated system, mass in equals mass out.")
    if t==4:return ("A process has 90% availability and 80% performance. Ignoring quality losses, their combined factor is","0.72",["0.85","1.70","0.10"],"0.90×0.80=0.72.")
    return ("Which physical principle best explains why increasing required work at fixed available power increases completion time?","power = work/time",["Hooke's law","ideal gas law","Ohm's law only"],"Rearrange P=W/t to t=W/P.")

def q_ethics(i):
    arr=[
      ("A manager discovers a safety hazard that could injure operators. The first professional obligation is to","protect public and worker safety",["protect schedule","avoid documentation","wait for a customer complaint"],"Safety and welfare take precedence."),
      ("An engineer evaluating a vendor owned by a close relative should","disclose the conflict of interest",["hide the relationship","select the vendor automatically","destroy bid records"],"Material conflicts must be disclosed."),
      ("An engineer asked to approve analysis outside their competence should","obtain qualified assistance or decline",["approve it anyway","copy an old report","remove calculations"],"Engineers practice within competence."),
      ("If a material calculation error is found after release, the engineer should","correct and communicate it promptly",["conceal it","delete the source data","ignore it if inconvenient"],"Material errors must be addressed.")
    ]; return arr[i%4]

def q_econ(i):
    t=i%5
    if t==0:
        F=50000+2000*(i%5); P=F/(1.07**4)
        return (f"A replacement cost of ${F:,} occurs in 4 years. At 7%, find present worth.",f"${fmt(P)}",[f"${fmt(F)}",f"${fmt(F*1.07**4)}",f"${fmt(F/(1+.07*4))}"],f"P=F/(1.07)^4=${fmt(P)}.")
    if t==1:
        A=12000;n=5;i0=.06; P=A*(1-(1+i0)**-n)/i0
        return ("Annual savings are $12,000 for 5 years at 6%. Find present worth.",f"${fmt(P)}",[f"${fmt(A*n)}",f"${fmt(A/i0)}",f"${fmt(P/2)}"],f"P=A(P/A,6%,5)=${fmt(P)}.")
    if t==2:return ("For mutually exclusive alternatives with equal service, the preferred present-worth choice is generally","the alternative with greatest net present worth",["highest first cost","longest life regardless of value","lowest salvage value"],"Use a consistent economic basis and select greatest net PW.")
    if t==3:return ("A project costs $80,000 and returns $20,000 per year with no time-value adjustment. Simple payback is","4 years",["2 years","5 years","16 years"],"80,000/20,000=4 years.")
    return ("If annual fixed cost is $60,000 and contribution margin is $15/unit, break-even volume is","4000 units",["900 units","15 units","60000 units"],"Q=F/(p-v)=60000/15=4000.")

def q_prob(i):
    t=i%7
    if t==0:return ("A defect occurs with probability 0.08 independently. Probability that 5 inspected items are all nondefective is",fmt(.92**5),[fmt(1-.92**5),fmt(.08**5),fmt(5*.08)],f"P=0.92^5={fmt(.92**5)}.")
    if t==1:return ("A normal observation has x=72, mean 60, and standard deviation 6. Its z-score is","2",["1","6","12"],"z=(72-60)/6=2.")
    if t==2:return ("For independent events A and B, P(A∩B) equals","P(A)P(B)",["P(A)+P(B)","P(A)-P(B)","1-P(A)"],"Independence gives the product rule.")
    if t==3:return ("A sample mean is based on n=100 and population σ=20. The standard error is","2",["0.2","10","20"],"SE=σ/√n=20/10=2.")
    if t==4:return ("Which distribution models the count of independent successes in a fixed number of Bernoulli trials?","binomial",["uniform","exponential","normal only"],"The binomial model counts successes in n Bernoulli trials.")
    if t==5:return ("If events arrive as a Poisson process at 3 per hour, the expected count in 2 hours is","6",["1.5","3","9"],"Expected count=λt=3×2=6.")
    return ("A 95% confidence interval becomes narrower, all else equal, when","sample size increases",["sample size decreases","standard deviation increases","confidence level increases"],"Larger n reduces standard error.")

def q_model(i):
    t=i%9
    if t==0:return ("Maximize 5x+4y subject to x+y≤8, x≤5, y≤6, x,y≥0. Which listed feasible point has largest objective?","(5,3)",["(0,6)","(2,6)","(4,4)"],"Objectives: 24,34,36,37; (5,3) is largest.")
    if t==1:return ("In a linear program, a binding constraint at the optimum has","zero slack",["negative probability","infinite slack","no coefficients"],"Binding means the inequality is active as equality.")
    if t==2:return ("An M/M/1 queue has λ=8/h and μ=10/h. Utilization is","0.8",["0.2","1.25","18"],"ρ=λ/μ=0.8.")
    if t==3:return ("For an M/M/1 queue with λ=8/h and μ=10/h, average number in system is","4",["0.8","5","8"],"L=λ/(μ-λ)=8/2=4.")
    if t==4:return ("A two-state Markov chain transition matrix row must sum to","1",["0","2","the state number"],"Outgoing transition probabilities from each state sum to 1.")
    if t==5:return ("Monte Carlo simulation primarily estimates system behavior by","repeated random sampling",["solving only deterministic equations","removing all uncertainty","forcing every input to its mean"],"Monte Carlo propagates uncertainty through repeated random trials.")
    if t==6:return ("A sensitivity analysis is used to","measure how outputs respond to input changes",["guarantee an optimum","eliminate constraints","replace validation"],"Sensitivity quantifies response to parameter changes.")
    if t==7:return ("A regression coefficient for x represents","estimated change in response per unit change in x, holding modeled terms fixed",["the sample size","a probability that must equal 1","the residual sum only"],"That is the standard slope interpretation.")
    return ("A model that matches historical data but fails on new data most likely suffers from","overfitting",["perfect robustness","zero variance","guaranteed validity"],"Overfitting captures noise rather than generalizable structure.")

def q_mgmt(i):
    t=i%7
    if t==0:return ("In CPM, activities on the critical path have total float approximately","zero",["equal to project budget","always negative","equal to duration"],"Critical-path delay directly delays completion when float is zero.")
    if t==1:return ("A project has EV=$80k, PV=$100k. Schedule performance index is","0.80",["1.25","0.20","$20k"],"SPI=EV/PV=0.80.")
    if t==2:return ("A project has EV=$80k and AC=$100k. Cost performance index is","0.80",["1.25","0.20","$20k"],"CPI=EV/AC=0.80.")
    if t==3:return ("A work breakdown structure is primarily used to","decompose project scope into manageable work",["calculate only interest","replace all schedules","eliminate accountability"],"WBS structures deliverables/work packages.")
    if t==4:return ("A moving average forecast generally becomes more responsive to recent changes when","fewer periods are averaged",["more periods are averaged","all observations are discarded","the horizon is infinite"],"Shorter windows react faster.")
    if t==5:return ("Exponential smoothing with a larger α places","more weight on the newest observation",["less weight on newest data","equal weight on all history","zero weight on errors"],"Higher α increases responsiveness.")
    return ("A KPI is most defensible when its numerator, denominator, time basis, and inclusion rules are","explicitly defined",["left implicit","changed after seeing results","different for every viewer"],"Operational definitions make KPIs reproducible.")

def q_prod(i):
    t=i%8
    if t==0:return ("A line produces 240 units in an 8-hour shift. Average production rate is","30 units/h",["8 units/h","240 units/h","1920 units/h"],"240/8=30 units/h.")
    if t==1:return ("Demand is 360 units per 6-hour shift. Required takt time is","1 min/unit",["6 min/unit","60 min/unit","0.1 min/unit"],"360 min/360 units=1 min/unit.")
    if t==2:return ("A bottleneck workstation has capacity 20 units/h while all others exceed 30 units/h. Maximum line throughput is approximately","20 units/h",["30 units/h","50 units/h","unlimited"],"System throughput cannot exceed bottleneck capacity.")
    if t==3:return ("EOQ increases when annual demand increases, all else equal, approximately with","the square root of demand",["the inverse of demand","demand squared","no relation"],"EOQ=√(2DS/H).")
    if t==4:return ("In MRP, dependent demand for a component is derived primarily from","parent-item requirements and the bill of materials",["random weather only","employee seniority","facility rent"],"MRP explodes parent requirements through the BOM.")
    if t==5:return ("Little's Law states","WIP = throughput × flow time",["WIP = setup/time","quality = cost/time","capacity = demand²"],"L=λW.")
    if t==6:return ("A pull system is designed to release work primarily in response to","downstream demand or consumption",["maximum forecast regardless of use","supplier preference","calendar year only"],"Pull limits production to actual downstream need.")
    return ("Line balancing seeks primarily to","distribute task work across stations while meeting precedence and cycle-time constraints",["maximize idle time","ignore precedence","increase WIP intentionally"],"Balanced assignments reduce idle time subject to constraints.")

def q_fac(i):
    t=i%7
    if t==0:return ("A center-of-gravity location method weights candidate coordinates primarily by","shipment or demand volume",["employee age","machine color","interest rate only"],"Flows weight coordinates in the center-of-gravity method.")
    if t==1:return ("Safety stock is held primarily to protect against","demand or lead-time uncertainty",["known average demand only","fixed rent","tax depreciation"],"Safety stock buffers variability.")
    if t==2:return ("Increasing the number of stocking locations generally tends to","increase total safety stock through loss of risk pooling",["eliminate all inventory","guarantee shorter lead time without cost","reduce variability to zero"],"Pooling demand usually lowers aggregate safety stock.")
    if t==3:return ("A product layout is most appropriate for","high-volume standardized flow",["unique one-off projects","very low-volume functional routing","random storage only"],"Product layouts support repetitive flow.")
    if t==4:return ("A process layout groups resources primarily by","similar function or process type",["customer surname","product color","calendar month"],"Functional departments characterize process layouts.")
    if t==5:return ("Cross-docking aims to","move inbound goods rapidly to outbound flow with little storage",["maximize long-term storage","increase handling steps","eliminate transportation"],"Cross-docking reduces storage dwell.")
    return ("Capacity cushion is the difference between","available capacity and expected demand",["price and variable cost","mean and median","inventory and lead time"],"It provides reserve capacity above expected load.")

def q_human(i):
    t=i%6
    if t==0:return ("For repetitive lifting, the preferred ergonomic action is generally to","reduce load, reach, and awkward posture at the source",["rely only on worker motivation","increase reach distance","remove all breaks"],"Engineering controls reduce exposure.")
    if t==1:return ("A control-display mapping is best when it is","consistent with user expectations and spatial relationships",["random each shift","hidden from operators","opposite all natural mappings"],"Compatible mappings reduce error.")
    if t==2:return ("For a normally distributed body dimension, designing an adjustable workstation typically aims to","accommodate a broad percentile range",["fit only the 50th percentile","fit only the smallest person","ignore anthropometry"],"Adjustability serves a wide population.")
    if t==3:return ("A hazard with high severity but low probability should","still be evaluated and controlled based on risk",["be ignored automatically","be treated as impossible","be hidden from records"],"Risk combines likelihood and consequence.")
    if t==4:return ("The hierarchy of controls generally prefers","elimination or substitution before PPE",["PPE before elimination in all cases","warnings only","no controls"],"Source controls are generally more reliable.")
    return ("A well-designed alarm should be","detectable, interpretable, and distinguishable from competing signals",["ambiguous","constantly active","identical to every other alarm"],"Alarm design supports rapid correct response.")

def q_work(i):
    t=i%6
    if t==0:return ("Observed time is 4.0 min and performance rating is 110%. Normal time is","4.4 min",["3.6 min","4.0 min","5.1 min"],"Normal time=observed×rating=4.0×1.10=4.4 min.")
    if t==1:return ("Normal time is 5.0 min with 20% allowance based on normal time. Standard time is","6.0 min",["4.0 min","5.2 min","25 min"],"ST=NT(1+allowance)=5×1.2=6 min.")
    if t==2:return ("A learning curve means unit time generally","decreases as cumulative production experience increases",["increases without bound","is unrelated to experience","becomes zero after two units"],"Learning captures improved performance with repetition.")
    if t==3:return ("Predetermined motion-time systems are used to","estimate task time from defined basic motions",["replace all safety analysis","forecast interest rates","size warehouses only"],"PMTS builds task times from motion elements.")
    if t==4:return ("Method study primarily seeks to","improve how work is performed",["set corporate tax rate","choose bond yields","calculate only inventory"],"Method study analyzes and improves work methods.")
    return ("A work-sampling study estimates","proportions of time spent in activity states",["exact continuous path of every motion","future interest rates","material strength"],"Random observations estimate activity fractions.")

def q_quality(i):
    t=i%8
    if t==0:return ("A process mean is 50, σ=2, and USL=56, LSL=44. Cp is","1.0",["0.5","1.5","3.0"],"Cp=(USL-LSL)/(6σ)=12/12=1.")
    if t==1:return ("A control chart point beyond a control limit is evidence of","potential special-cause variation",["guaranteed customer satisfaction","zero variation","only common cause"],"An out-of-control signal warrants investigation.")
    if t==2:return ("A Pareto chart is used to","rank categories by frequency or impact",["display only time order","calculate regression slope","replace sampling"],"Pareto prioritizes the vital few categories.")
    if t==3:return ("Type I error means","rejecting a true null hypothesis",["failing to reject a false null","accepting every alternative","measuring bias only"],"Type I error is a false positive.")
    if t==4:return ("Increasing sample size in acceptance sampling generally provides","more information about lot quality",["less information","zero inspection effort","certainty with one item"],"Larger samples reduce sampling uncertainty.")
    if t==5:return ("A cause-and-effect diagram is also called a","fishbone or Ishikawa diagram",["Gantt chart","histogram only","PERT network"],"Those are standard names.")
    if t==6:return ("Design of experiments uses randomization primarily to","reduce bias from uncontrolled nuisance effects",["guarantee every factor significant","remove replication","eliminate measurement"],"Randomization protects inference.")
    return ("Cpk differs from Cp because Cpk accounts for","process centering relative to specification limits",["only sample size","only inspection cost","time value of money"],"Cpk reflects both spread and centering.")

def q_systems(i):
    t=i%8
    if t==0:return ("Two independent components in series have reliabilities 0.9 and 0.8. System reliability is","0.72",["0.98","0.85","1.70"],"Series reliability=0.9×0.8=0.72.")
    if t==1:return ("Two independent parallel components each have reliability 0.9. System reliability is","0.99",["0.81","0.90","1.80"],"R=1-(0.1)(0.1)=0.99.")
    if t==2:return ("FMEA risk priority commonly considers severity, occurrence, and","detectability",["interest rate","inventory turns","line slope"],"Traditional RPN uses S×O×D.")
    if t==3:return ("A fault tree begins with","an undesired top event",["a final invoice","a random employee","the lowest component cost"],"Fault-tree analysis works backward from the top event.")
    if t==4:return ("A requirement is most verifiable when it is","specific, measurable, and testable",["vague and subjective","changed during testing","missing acceptance criteria"],"Verification requires objective acceptance criteria.")
    if t==5:return ("A trade study compares alternatives using","defined criteria and weights or decision logic",["unrecorded intuition only","one arbitrary metric","no assumptions"],"Traceable criteria support defensible decisions.")
    if t==6:return ("Life-cycle analysis should consider","costs and impacts across acquisition, operation, support, and retirement",["purchase price only","labor only","first week only"],"Systems decisions span the life cycle.")
    return ("Verification asks whether the system was built correctly to requirements; validation asks whether","the right system was built for stakeholder needs",["the budget is always zero","every component is identical","all risks are removed"],"Validation addresses intended use and stakeholder need.")

GEN={
"Mathematics":q_math,"Engineering Sciences":q_science,"Ethics and Professional Practice":q_ethics,
"Engineering Economics":q_econ,"Probability and Statistics":q_prob,
"Modeling and Quantitative Analysis":q_model,"Engineering Management":q_mgmt,
"Manufacturing, Service, and Other Production Systems":q_prod,"Facilities and Supply Chain":q_fac,
"Human Factors, Ergonomics, and Safety":q_human,"Work Design":q_work,"Quality":q_quality,
"Systems Engineering, Analysis, and Design":q_systems,
}
def context(form,n,a):
    if form=="A":
        sites=["assembly plant","distribution center","hospital service line","repair depot","warehouse","production cell","call center","maintenance operation"]
        phases=["capacity review","improvement study","planning meeting","operations audit","design review","performance analysis"]
        return f"During a {phases[(n//8)%len(phases)]} at a {sites[n%len(sites)]},"
    sites=["electronics factory","regional fulfillment hub","field-service network","packaging line","clinic intake system","spare-parts center","fabrication shop","technical support queue"]
    phases=["separate optimization study","independent verification","new process redesign","risk-based assessment","fresh simulation study","management review"]
    return f"An industrial engineer is conducting a {phases[(n//8)%len(phases)]} for a {sites[n%len(sites)]}. In that independent scenario,"

def build(form):
    bp=next(x for x in BPS if x["discipline"]=="industrial-systems" and x["exam"]==form)
    items=[]; serial=1; offset=0 if form=="A" else 53
    for ar in bp["areas"]:
        a=ar["name"]
        for j in range(int(ar["allocated"])):
            p,c,ds,sol=GEN[a](j+offset)
            stem=context(form,serial,a)+" "+p[0].lower()+p[1:]
            q=mc(a,j+offset,stem,c,ds,sol)
            q["id"]=f"IND-{form}-Q{serial:03d}"
            items.append(q); serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"industrial-systems","exam":form,
            "question_count":110,"appointment_minutes":355,"working_time_minutes":320,
            "blueprint_source":"meta/exam-blueprints.yaml","items":items}
def md(ex):
    L=[f"# FE Industrial & Systems Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ","","## Questions",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n}","",q["prompt"],""]+[f"{c}) {v}" for c,v in zip("ABCD",q["choices"])]+[""]
    L += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n} — {q['answer']}","",q["solution"],"",f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(L)+"\n"

for form in ("A","B"):
    ex=build(form)
    (OUT/f"industrial-systems-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=120))
    (OUT/f"industrial-systems-practice-{form.lower()}.md").write_text(md(ex))
    print(form,len(ex["items"]))
