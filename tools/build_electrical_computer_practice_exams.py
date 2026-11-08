#!/usr/bin/env python3
from pathlib import Path
import math,re,yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"appendices"/"practice-exams"; OUT.mkdir(parents=True,exist_ok=True)
BPS=yaml.safe_load((ROOT/"meta"/"exam-blueprints.yaml").read_text())["blueprints"]
ledger=yaml.safe_load((ROOT/"meta"/"ledger.yaml").read_text())
concepts=ledger["concepts"]; BY_CH={}
for c in concepts:
    if c.get("chapter") and c.get("id"): BY_CH.setdefault(str(c["chapter"]),[]).append(c["id"])

def ids(*chs):
    a=[]
    for ch in chs:a+=BY_CH.get(ch,[])
    if not a: raise RuntimeError(chs)
    return a

AREA_IDS={
"Mathematics":ids("01-01","01-02","01-04","01-16","01-19","01-23"),
"Probability and Statistics":ids("01-28","01-29","01-30","01-31"),
"Ethics and Professional Practice":ids("02-01","02-02"),
"Engineering Economics":ids("02-04","02-05","02-06"),
"Properties of Electrical Materials":ids("03-31"),
"Circuit Analysis (DC and AC Steady State)":ids("02-59","02-60","02-61","02-62","02-63"),
"Linear Systems":ids("02-69","03-39"),
"Signal Processing":ids("02-68","03-39"),
"Electronics":ids("03-32","03-33","03-34","03-35"),
"Power Systems":ids("02-63","02-64","02-65","03-36"),
"Electromagnetics":ids("02-64","03-37","03-38"),
"Control Systems":ids("02-69","02-70"),
"Communications":ids("03-40","03-41"),
"Computer Networks":ids("03-45","03-46"),
"Digital Systems":ids("03-42","03-43"),
"Computer Systems":ids("03-44"),
"Software Engineering":ids("03-47"),
}
def cid(a,i): return AREA_IDS[a][i%len(AREA_IDS[a])]
def fmt(x):
    if abs(x)>=100:return f"{x:.1f}"
    if abs(x)>=10:return f"{x:.2f}"
    return f"{x:.3f}"
def unique(correct,ds):
    vals=[str(correct)]+[str(x) for x in ds]; out=[];seen=set()
    for k,v in enumerate(vals):
        q=v
        if q in seen:
            m=re.match(r"^(.*?)([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)(.*)$",q)
            if m:
                a,n,b=m.groups(); x=float(n); y=x*(1.23+.08*k) if x else k+1
                if "e" in n.lower(): nn=f"{y:.2e}"
                elif "." in n: nn=f"{y:.{len(n.split('.')[1])}f}"
                else: nn=f"{y:.2f}" if abs(y-round(y))>1e-9 else str(int(round(y)))
                q=a+nn+b
            else:q="Alternative "+q
        while q in seen:q+=" variant"
        seen.add(q);out.append(q)
    return out
def mc(area,i,p,cor,ds,sol):
    vals=unique(cor,ds);r=i%4;vals=vals[r:]+vals[:r];ans="ABCD"[vals.index(str(cor))]
    return {"knowledge_area":area,"question_type":"multiple-choice","requires_concepts":[cid(area,i)],
            "prompt":p,"choices":vals,"answer":ans,"solution":f"**{ans}.** {sol}"}
def ctx(form,n):
    A=["motor-drive","embedded-control","data-acquisition","industrial-network","power-distribution","sensor-interface","RF-link","battery-converter","automation-panel","digital-controller"]
    B=["servo-drive","microcontroller","test-instrument","campus-network","substation","measurement-front-end","telemetry-link","DC-converter","control-cabinet","FPGA-controller"]
    ph=["design","verification","commissioning","fault-analysis","upgrade","validation","integration","performance","safety","prototype"]
    return f"During a {ph[(n//10)%10]} review of a {(A if form=='A' else B)[n%10]} system,"

def q_math(i,f):
    a="Mathematics";t=i%6
    if t==0:
        x=2+i%4; y=3*x*x+2*x
        return mc(a,i,f"For y=3x²+2x, find dy/dx at x={x}.",str(6*x+2),[str(3*x+2),str(y),str(6*x)],f"dy/dx=6x+2={6*x+2}.")
    if t==1:
        re0=3+i%4; im=4; mag=math.hypot(re0,im)
        return mc(a,i,f"Find the magnitude of z={re0}+j{im}.",fmt(mag),[fmt(re0+im),fmt(abs(re0-im)),fmt(re0*im)],f"|z|=sqrt({re0}²+{im}²)={fmt(mag)}.")
    if t==2:
        A=[[2,1],[1,3]];det=5
        return mc(a,i,"Find det([[2,1],[1,3]]).",str(det),["6","4","3"],"det=2(3)-1(1)=5.")
    if t==3:
        lo=0;hi=2+i%3;val=hi**2
        return mc(a,i,f"Evaluate ∫_0^{hi} 2x dx.",fmt(val),[fmt(2*hi),fmt(val/2),fmt(val+hi)],f"Integral=x², so result={fmt(val)}.")
    if t==4:
        w=2*math.pi*(10+i); return mc(a,i,f"Convert f={10+i} Hz to angular frequency.",f"{fmt(w)} rad/s",[f"{fmt(10+i)} rad/s",f"{fmt(w/2)} rad/s",f"{fmt(w*2)} rad/s"],f"ω=2πf={fmt(w)} rad/s.")
    x=math.log(8,2); return mc(a,i,"Evaluate log₂(8).",fmt(x),["2.000","4.000","8.000"],"2³=8, so log₂8=3.")

def q_prob(i,f):
    a="Probability and Statistics";t=i%4
    if t==0:
        p=.1+.02*(i%3);n=5;v=(1-p)**n
        return mc(a,i,f"Independent packet error probability is {p:.2f}. For {n} packets, find probability of no errors.",fmt(v),[fmt(1-v),fmt(p**n),fmt(n*p)],f"P=(1-p)^n={fmt(v)}.")
    if t==1:
        mu=10;sd=2;x=14;return mc(a,i,"A normal variable has μ=10, σ=2. Find z for x=14.","2.000",["1.000","4.000","7.000"],"z=(14-10)/2=2.")
    if t==2:
        vals=[2,4,6,8+i%2];m=sum(vals)/4
        return mc(a,i,f"Find the mean of {vals}.",fmt(m),[fmt(m+1),fmt(m-1),fmt(sum(vals))],f"Mean=sum/4={fmt(m)}.")
    return mc(a,i,"If events A and B are independent, P(A∩B) equals","P(A)P(B)",["P(A)+P(B)","P(A)-P(B)","0 always"],"Independence gives P(A∩B)=P(A)P(B).")

def q_ethics(i,f):
    a="Ethics and Professional Practice";sets=[
    ("protect public health, safety, and welfare",["protect schedule first","conceal material hazards","approve outside competence"],"Public welfare is the engineer's paramount obligation."),
    ("disclose a material conflict of interest",["hide it if profitable","ignore it","transfer it to a vendor"],"Material conflicts must be disclosed to affected parties."),
    ("practice only within competence",["seal any work requested","avoid peer review","accept all assignments"],"Engineers must perform services only in areas of competence."),
    ("correct or report a material technical error",["leave it unchanged","delete records","conceal it from reviewers"],"Material errors that affect safety or decisions must be addressed.")
    ];c,ds,s=sets[i%4];return mc(a,i,"Which action best satisfies professional engineering obligations?",c,ds,s)

def q_econ(i,f):
    a="Engineering Economics";t=i%3
    if t==0:
        F=15000+1000*i;P=F/1.07**5
        return mc(a,i,f"A replacement cost of ${F:,} occurs in 5 years at 7%. Find present worth.",f"${fmt(P)}",[f"${fmt(F)}",f"${fmt(F*1.07**5)}",f"${fmt(F/(1+.07*5))}"],f"P=F/(1.07)^5=${fmt(P)}.")
    if t==1:
        P=10000;F=P*1.06**4
        return mc(a,i,"$10,000 invested at 6% for 4 years grows to what future worth?",f"${fmt(F)}",[f"${fmt(P)}",f"${fmt(P/1.06**4)}",f"${fmt(P*(1+.06*4))}"],f"F=P(1+i)^n=${fmt(F)}.")
    return mc(a,i,"For mutually exclusive equal-service alternatives, the present-worth rule generally selects","the greatest net present worth",["the highest first cost","the longest life regardless of value","the lowest nominal interest rate"],"Use consistent cash-flow signs and maximize net present worth.")

def q_material(i,f):
    a="Properties of Electrical Materials";t=i%4
    if t==0:
        rho=1.7e-8;L=20;A=2e-6;R=rho*L/A
        return mc(a,i,"A conductor has ρ=1.7×10⁻⁸ Ω·m, L=20 m, A=2 mm². Find resistance.",f"{fmt(R)} Ω",[f"{fmt(R*2)} Ω",f"{fmt(R/2)} Ω",f"{fmt(rho*L)} Ω"],f"R=ρL/A={fmt(R)} Ω.")
    if t==1:return mc(a,i,"Doping silicon with a group-V donor creates predominantly","n-type material",["p-type material","intrinsic material","perfect insulator"],"Donors contribute majority electrons, producing n-type material.")
    if t==2:return mc(a,i,"In p-type semiconductor material, the majority carriers are","holes",["electrons","photons","neutrons"],"Acceptor doping creates holes as majority carriers.")
    return mc(a,i,"Increasing semiconductor temperature generally increases intrinsic carrier concentration","strongly",["to exactly zero","only if externally illuminated","without changing conductivity"],"Thermal generation increases intrinsic carrier concentration.")

def q_circuit(i,f):
    a="Circuit Analysis (DC and AC Steady State)";t=i%7
    if t==0:
        V=12+i;R=6;I=V/R
        return mc(a,i,f"A {V} V source is across {R} Ω. Find current.",f"{fmt(I)} A",[f"{fmt(V*R)} A",f"{fmt(R/V)} A",f"{fmt(I/2)} A"],f"I=V/R={fmt(I)} A.")
    if t==1:
        r1=10;r2=20;req=r1*r2/(r1+r2)
        return mc(a,i,"Find equivalent resistance of 10 Ω in parallel with 20 Ω.",f"{fmt(req)} Ω",["30.00 Ω","15.00 Ω","2.000 Ω"],f"Req=R1R2/(R1+R2)={fmt(req)} Ω.")
    if t==2:
        V=10;R1=2;R2=8;vo=V*R2/(R1+R2)
        return mc(a,i,"A 10 V divider has 2 Ω on top and 8 Ω to ground. Find output across 8 Ω.",f"{fmt(vo)} V",["2.000 V","10.00 V","4.000 V"],f"Vo=V R2/(R1+R2)={fmt(vo)} V.")
    if t==3:
        f0=1000;C=1e-6;X=1/(2*math.pi*f0*C)
        return mc(a,i,"At 1 kHz, find |Xc| for C=1 μF.",f"{fmt(X)} Ω",[f"{fmt(2*math.pi*f0*C)} Ω",f"{fmt(X/2)} Ω",f"{fmt(X*2)} Ω"],f"|Xc|=1/(2πfC)={fmt(X)} Ω.")
    if t==4:
        Vrms=120;R=30;P=Vrms**2/R
        return mc(a,i,"A 30 Ω resistor is connected to 120 V rms. Find real power.",f"{fmt(P)} W",[f"{fmt(Vrms/R)} W",f"{fmt(Vrms*R)} W",f"{fmt(P/2)} W"],f"P=V²/R={fmt(P)} W.")
    if t==5:
        tau=10e3*10e-6
        return mc(a,i,"An RC circuit has R=10 kΩ and C=10 μF. Find time constant.",f"{fmt(tau)} s",[f"{fmt(tau*10)} s",f"{fmt(tau/10)} s",f"{fmt(10e3/10e-6)} s"],f"τ=RC={fmt(tau)} s.")
    return mc(a,i,"At series resonance in an ideal RLC circuit, the net reactance is","zero",["maximum inductive","maximum capacitive","equal to resistance"],"At resonance XL=XC, so net reactance cancels.")

def q_linear(i,f):
    a="Linear Systems";t=i%4
    if t==0:return mc(a,i,"For an LTI system, the output corresponding to input x(t) is obtained from impulse response h(t) by","convolution",["differentiation only","division","logic minimization"],"For LTI systems y=x*h.")
    if t==1:
        pole=-5; tau=-1/pole
        return mc(a,i,"A first-order transfer function has pole at s=-5 rad/s. Find time constant.",f"{fmt(tau)} s",[f"{fmt(5)} s",f"{fmt(1/25)} s",f"{fmt(10)} s"],f"τ=1/|p|={fmt(tau)} s.")
    if t==2:return mc(a,i,"A continuous-time LTI system is BIBO stable if all rational transfer-function poles are","in the open left half-plane",["on the positive real axis","at infinity","necessarily zeros"],"For a proper rational continuous-time system, left-half-plane poles imply BIBO stability.")
    return mc(a,i,"Multiplication in the frequency domain corresponds to what operation in time?","convolution",["sampling","integration only","quantization"],"The convolution theorem maps time convolution to frequency multiplication.")

def q_signal(i,f):
    a="Signal Processing";t=i%5
    if t==0:
        fm=4e3;fs=2*fm
        return mc(a,i,"A signal is bandlimited to 4 kHz. What is the Nyquist minimum sampling rate?",f"{fmt(fs/1000)} kHz",["4.000 kHz","6.000 kHz","16.00 kHz"],"Nyquist requires fs≥2fmax=8 kHz.")
    if t==1:return mc(a,i,"Sampling below the Nyquist rate can cause","aliasing",["zero quantization error","perfect reconstruction always","infinite bandwidth"],"Spectral replicas overlap when sampling is too slow, producing aliasing.")
    if t==2:
        bits=12;levels=2**bits
        return mc(a,i,"How many ideal codes does a 12-bit ADC provide?",str(levels),["2048","8192","1200"],"An N-bit ADC has 2^N codes; 2^12=4096.")
    if t==3:return mc(a,i,"An anti-alias filter is placed before an ADC primarily to","attenuate frequencies above the intended Nyquist band",["increase bit depth","create aliasing","replace the sample clock"],"It limits input bandwidth so out-of-band components do not fold into baseband.")
    return mc(a,i,"A low-pass filter primarily passes","low frequencies while attenuating high frequencies",["only DC exactly","high frequencies only","all frequencies equally"],"A low-pass response preserves the lower-frequency band.")

def q_electronics(i,f):
    a="Electronics";t=i%7
    if t==0:
        Vin=5;Vd=.7;R=1e3;I=(Vin-Vd)/R*1000
        return mc(a,i,"A silicon diode with 0.7 V drop is in series with 1 kΩ from a 5 V source. Find current.",f"{fmt(I)} mA",[f"{fmt(Vin/R*1000)} mA",f"{fmt(Vd/R*1000)} mA",f"{fmt((Vin+Vd)/R*1000)} mA"],f"I=(5-0.7)/1k={fmt(I)} mA.")
    if t==1:return mc(a,i,"An ideal op amp under negative feedback has approximately","equal input-terminal voltages",["infinite output voltage","zero open-loop gain","equal input currents to load current"],"Negative feedback drives v+≈v- while input currents are approximately zero.")
    if t==2:
        Rin=10;Rf=50;gain=-Rf/Rin
        return mc(a,i,"An ideal inverting op amp has Rin=10 kΩ and Rf=50 kΩ. Find gain.",fmt(gain),[fmt(-Rin/Rf),fmt(abs(gain)),fmt(1+Rf/Rin)],f"Av=-Rf/Rin={fmt(gain)}.")
    if t==3:return mc(a,i,"An enhancement NMOS is normally off when","VGS is below threshold",["VDS is zero only","gate is always positive","drain current is maximum"],"A channel forms when VGS exceeds threshold.")
    if t==4:
        Vin=24;D=.4;Vo=Vin*D
        return mc(a,i,"An ideal buck converter has Vin=24 V and duty ratio D=0.4. Find average output.",f"{fmt(Vo)} V",[f"{fmt(Vin/D)} V",f"{fmt(Vin*(1-D))} V",f"{fmt(D)} V"],f"Vo=D Vin={fmt(Vo)} V.")
    if t==5:return mc(a,i,"A common-emitter amplifier normally produces an output that is","inverted relative to the input",["always in phase","DC only","independent of bias"],"Common-emitter voltage gain is typically negative.")
    return mc(a,i,"A Zener diode used as a shunt regulator is normally operated in","reverse breakdown",["forward cutoff","zero-bias only","avalanche-free forward saturation"],"Zener regulation uses the approximately constant reverse-breakdown voltage.")

def q_power(i,f):
    a="Power Systems";t=i%6
    if t==0:
        V=480;I=50;pf=.8;P=math.sqrt(3)*V*I*pf/1000
        return mc(a,i,"A balanced 480 V three-phase load draws 50 A at pf=0.8. Find real power.",f"{fmt(P)} kW",[f"{fmt(V*I/1000)} kW",f"{fmt(math.sqrt(3)*V*I/1000)} kW",f"{fmt(P/2)} kW"],f"P=√3 VLI_L pf={fmt(P)} kW.")
    if t==1:
        n1=1000;n2=100;V1=240;V2=V1*n2/n1
        return mc(a,i,"An ideal transformer has N1=1000, N2=100, V1=240 V. Find V2.",f"{fmt(V2)} V",[f"{fmt(V1*n1/n2)} V",f"{fmt(V1)} V",f"{fmt(V1/2)} V"],f"V2/V1=N2/N1, so V2={fmt(V2)} V.")
    if t==2:
        f0=60;poles=4;ns=120*f0/poles
        return mc(a,i,"Find synchronous speed of a 4-pole, 60 Hz AC machine.",f"{fmt(ns)} rpm",["3600.0 rpm","900.0 rpm","60.00 rpm"],f"Ns=120f/P={fmt(ns)} rpm.")
    if t==3:return mc(a,i,"Power-factor correction for an inductive load is commonly achieved by adding","shunt capacitance",["series resistance only","more inductance","a fuse"],"Capacitors supply leading reactive power to offset lagging load VARs.")
    if t==4:
        I=100;R=.05;loss=3*I*I*R/1000
        return mc(a,i,"Each conductor of a balanced three-phase feeder has R=0.05 Ω and carries 100 A. Find total copper loss.",f"{fmt(loss)} kW",[f"{fmt(I*I*R/1000)} kW",f"{fmt(loss*2)} kW",f"{fmt(R*I/1000)} kW"],f"P_loss=3I²R={fmt(loss)} kW.")
    return mc(a,i,"For an induction motor, slip is zero at","synchronous rotor speed",["standstill","maximum torque necessarily","half synchronous speed"],"s=(Ns-Nr)/Ns, so s=0 when Nr=Ns.")

def q_em(i,f):
    a="Electromagnetics";t=i%5
    if t==0:
        c0=3e8;f0=100e6;lam=c0/f0
        return mc(a,i,"Find free-space wavelength at 100 MHz.",f"{fmt(lam)} m",[f"{fmt(c0/f0/2)} m",f"{fmt(f0/c0)} m",f"{fmt(c0*f0)} m"],f"λ=c/f={fmt(lam)} m.")
    if t==1:
        z0=50;zl=100;g=(zl-z0)/(zl+z0)
        return mc(a,i,"A 50 Ω line is terminated in 100 Ω. Find reflection coefficient Γ.",fmt(g),[fmt(-g),fmt(1-g),fmt(zl/z0)],f"Γ=(ZL-Z0)/(ZL+Z0)={fmt(g)}.")
    if t==2:return mc(a,i,"A transmission line is perfectly matched when","ZL=Z0",["ZL=0","ZL is infinite","line length is zero"],"When load equals characteristic impedance, Γ=0.")
    if t==3:return mc(a,i,"Faraday's law relates induced emf to","time-varying magnetic flux",["static electric charge only","resistance only","temperature"],"A changing magnetic flux produces induced emf.")
    return mc(a,i,"Gauss's law for electric fields relates electric flux through a closed surface to","enclosed charge",["external resistance","magnetic reluctance","frequency only"],"Net electric flux is proportional to enclosed charge.")

def q_control(i,f):
    a="Control Systems";t=i%5
    if t==0:
        K=4;G=2;cl=K*G/(1+K*G)
        return mc(a,i,"A unity-feedback loop has forward gain KG=8. Find closed-loop gain.",fmt(cl),[fmt(8),fmt(1/8),fmt(1+8)],f"T=KG/(1+KG)={fmt(cl)}.")
    if t==1:return mc(a,i,"Integral control primarily helps eliminate","steady-state error",["all measurement noise","plant dynamics","sampling requirements"],"Integral action accumulates error and drives constant offset toward zero.")
    if t==2:return mc(a,i,"Derivative action responds to","rate of change of error",["integral of error","constant bias only","reference magnitude only"],"Derivative control is proportional to de/dt.")
    if t==3:return mc(a,i,"A continuous-time closed-loop system is stable when its characteristic roots lie","in the left half-plane",["in the right half-plane","only at the origin","on the positive real axis"],"Negative real parts give decaying natural modes.")
    return mc(a,i,"Increasing phase margin generally corresponds to","greater relative stability and damping",["guaranteed instability","zero bandwidth","infinite steady-state error"],"Adequate phase margin provides robustness and typically more damped response.")

def q_comm(i,f):
    a="Communications";t=i%6
    if t==0:
        fm=5e3;BW=2*fm
        return mc(a,i,"A conventional AM signal has maximum modulating frequency 5 kHz. Find transmission bandwidth.",f"{fmt(BW/1000)} kHz",["5.000 kHz","20.00 kHz","2.500 kHz"],"Conventional AM bandwidth is 2fm=10 kHz.")
    if t==1:
        df=75e3;fm=15e3;bw=2*(df+fm)
        return mc(a,i,"For FM with Δf=75 kHz and fm=15 kHz, estimate Carson bandwidth.",f"{fmt(bw/1000)} kHz",["90.00 kHz","150.0 kHz","75.00 kHz"],"Carson BW≈2(Δf+fm)=180 kHz.")
    if t==2:
        fs=8e3;bits=8;br=fs*bits
        return mc(a,i,"PCM samples at 8 ksample/s with 8 bits/sample. Find raw bit rate.",f"{fmt(br/1000)} kb/s",["8.000 kb/s","16.00 kb/s","128.0 kb/s"],"Rb=fsN=64 kb/s.")
    if t==3:return mc(a,i,"QPSK conveys how many bits per ideal symbol?","2",["1","4","8"],"QPSK has four symbols, so log2(4)=2 bits/symbol.")
    if t==4:return mc(a,i,"TDM separates users primarily by assigning different","time slots",["carrier amplitudes only","IP addresses only","wire gauges"],"Time-division multiplexing interleaves users in time.")
    return mc(a,i,"A CRC is primarily used for","error detection",["encryption","analog modulation","clock generation"],"CRC adds redundancy optimized for detecting transmission errors.")

def q_network(i,f):
    a="Computer Networks";t=i%5
    if t==0:return mc(a,i,"A router forwards packets primarily using","network-layer destination addressing and a routing/forwarding table",["source MAC address only","application filenames","CPU clock speed"],"Routers select next hops from network-layer addressing information.")
    if t==1:return mc(a,i,"TCP differs from UDP because TCP provides","connection-oriented reliable byte-stream service",["broadcast-only delivery","no sequencing","no acknowledgments"],"TCP provides ordered reliable delivery with connection state.")
    if t==2:
        prefix=24;hosts=2**(32-prefix)-2
        return mc(a,i,"How many conventional usable host addresses are in an IPv4 /24 subnet?",str(hosts),["256","128","510"],"A /24 leaves 8 host bits: 2^8-2=254 usable addresses.")
    if t==3:return mc(a,i,"DHCP is commonly used to","automatically supply IP configuration to hosts",["encrypt Ethernet frames","replace DNS permanently","route BGP"],"DHCP leases addresses and related network parameters.")
    return mc(a,i,"Network segmentation improves security primarily by","limiting communication paths and blast radius",["increasing every password length automatically","eliminating all vulnerabilities","removing authentication"],"Segmentation constrains lateral movement and policy scope.")

def q_digital(i,f):
    a="Digital Systems";t=i%6
    if t==0:
        n=13;return mc(a,i,"Convert decimal 13 to binary.","1101",["1011","1110","1001"],"13=8+4+1, so binary 1101.")
    if t==1:return mc(a,i,"By De Morgan's law, NOT(A AND B) equals","(NOT A) OR (NOT B)",["(NOT A) AND (NOT B)","A OR B","A XOR B"],"Complement of a product equals sum of complements.")
    if t==2:return mc(a,i,"A multiplexer selects","one of several inputs to one output",["one input to many outputs only","a clock frequency","analog gain"],"A MUX routes one selected data input to the output.")
    if t==3:return mc(a,i,"A D flip-flop stores","one bit",["one byte","one address bus","an analog voltage continuously"],"A D flip-flop is a single-bit state element.")
    if t==4:
        n=4;states=2**n
        return mc(a,i,"A 4-bit binary counter has how many distinct states?",str(states),["4","8","32"],"2^4=16 states.")
    return mc(a,i,"Setup time specifies how long data must be stable","before the active clock edge",["after power-off","after the hold interval only","during reset only"],"Setup time is the required pre-clock data-stability interval.")

def q_computer(i,f):
    a="Computer Systems";t=i%5
    if t==0:return mc(a,i,"Cache memory is used primarily to","reduce average memory access time",["replace all registers","increase disk latency","perform routing"],"Cache exploits temporal/spatial locality to reduce effective memory latency.")
    if t==1:
        bits=16;locations=2**bits
        return mc(a,i,"A 16-bit address bus can directly select how many distinct addresses?",str(locations),["32768","16384","131072"],"2^16=65,536 addressable locations.")
    if t==2:return mc(a,i,"Memory-mapped I/O means peripherals are accessed using","ordinary address-space reads and writes",["only special network packets","mechanical relays","cache tags exclusively"],"Peripheral registers occupy addresses in the processor's memory map.")
    if t==3:return mc(a,i,"A Harvard architecture distinguishes itself by having","separate instruction and data memories or paths",["no CPU","no registers","only one address"],"Harvard organization separates instruction and data storage/access.")
    return mc(a,i,"A cache miss occurs when requested data","is not present in the cache",["is already in L1","is in a register","has zero value"],"A miss requires fetching the block from a lower memory level.")

def q_software(i,f):
    a="Software Engineering";t=i%5
    if t==0:return mc(a,i,"Binary search on a sorted array has worst-case time complexity","O(log n)",["O(n²)","O(1)","O(n!)"],"Each comparison halves the remaining search interval.")
    if t==1:return mc(a,i,"A stack follows which access discipline?","LIFO",["FIFO","random-only","priority-only"],"Stacks are last-in, first-out.")
    if t==2:return mc(a,i,"Breadth-first graph traversal normally uses a","queue",["stack only","hash function only","compiler"],"BFS processes vertices level by level using a queue.")
    if t==3:return mc(a,i,"A unit test primarily targets","a small isolated software component",["an entire deployed enterprise only","network cabling","hardware solder joints"],"Unit tests verify small units such as functions/classes in isolation.")
    return mc(a,i,"Static analysis examines software","without executing it",["only after deployment","only via packet capture","by changing CPU voltage"],"Static analysis inspects source/bytecode artifacts without running the program.")

GEN={"Mathematics":q_math,"Probability and Statistics":q_prob,"Ethics and Professional Practice":q_ethics,
"Engineering Economics":q_econ,"Properties of Electrical Materials":q_material,
"Circuit Analysis (DC and AC Steady State)":q_circuit,"Linear Systems":q_linear,"Signal Processing":q_signal,
"Electronics":q_electronics,"Power Systems":q_power,"Electromagnetics":q_em,"Control Systems":q_control,
"Communications":q_comm,"Computer Networks":q_network,"Digital Systems":q_digital,
"Computer Systems":q_computer,"Software Engineering":q_software}

FORM_B_OVERRIDES={
27:"A capital-allocation review compares alternatives with different future cash-flow timing. Apply the stated interest rate to determine the requested equivalent-value result before selecting among the options.",
19:"A field engineer must select the ethically appropriate response to a professional-conflict scenario. Which action best satisfies the governing duty?",
20:"A design review identifies a situation involving professional responsibility. Which response is most consistent with engineering ethics?",
24:"A project team must compare alternative investments using equivalent-value methods. Which engineering-economy principle applies to the stated decision?",
31:"A branch-current calculation is required for a resistive network under the stated source and resistance values. Determine the requested current.",
33:"An AC network is operating at the stated frequency with a reactive element. Determine the requested impedance-related quantity.",
36:"A first-order network is switched to a new source condition. Determine the requested transient parameter from the stated component values.",
37:"A sinusoidal steady-state circuit must be checked for resonance behavior. Which condition characterizes the requested operating point?",
38:"A circuit-analysis review requires identifying the appropriate theorem or network reduction for the stated source-load configuration.",
39:"A system engineer is checking whether a linear time-invariant model satisfies the stated response property. Which system concept applies?",
40:"A first-order dynamic model is represented by a single real pole. Determine the associated time-domain parameter from the pole location.",
43:"A sampled-data design is being checked against its highest input frequency. Determine the minimum compliant sampling rate.",
47:"An ADC interface is being reviewed for quantization capability. Determine the number of distinct ideal output codes from the stated resolution.",
56:"A three-phase feeder supplies the stated balanced load. Determine the real power delivered from the line voltage, current, and power factor.",
57:"A transformer design uses the stated primary and secondary turns. Determine the secondary voltage from the ideal turns-ratio relation.",
59:"A feeder-loss check is required for the stated conductor resistance and phase current. Determine the total three-phase copper loss.",
60:"An induction machine is evaluated at a particular rotor speed. Which condition corresponds to zero slip?",
63:"A transmission-line check is required at the stated source frequency. Determine the free-space wavelength.",
66:"A load is connected to a transmission line with the stated characteristic impedance. Determine the load reflection coefficient.",
67:"A termination is selected for a transmission line. Which condition produces a matched line with zero reflection?",
69:"A feedback loop is modeled by the stated forward-path gain and unity feedback. Determine the resulting closed-loop gain.",
70:"A controller is being tuned to remove persistent offset. Which control action most directly addresses that objective?",
78:"A digital communication link is evaluated for symbol efficiency. Determine the number of bits represented by each QPSK symbol.",
87:"An IPv4 subnet is configured with the stated prefix length. Determine the conventional number of usable host addresses.",
104:"A processor memory subsystem is being analyzed for latency reduction. What is the principal purpose of cache memory?",
109:"A software routine searches an ordered array by repeatedly halving the remaining interval. State the corresponding worst-case time complexity.",
}

def build(form):
    b=next(x for x in BPS if x["discipline"]=="electrical-computer" and str(x["exam"]).upper()==form)
    items=[];serial=1
    for ar in b["areas"]:
        area=ar["name"]
        for j in range(int(ar["allocated"])):
            q=GEN[area](j+(0 if form=="A" else 43),form)
            q["id"]=f"ECE-{form}-Q{serial:03d}"
            c=ctx(form,serial); p=q["prompt"];q["prompt"]=c+" "+p[0].lower()+p[1:]
            if form=="B" and serial in FORM_B_OVERRIDES:
                q["prompt"]=c+" "+FORM_B_OVERRIDES[serial]
            q["solution"]+=f" This result applies to the stated {c[len('During a '):-1]}."
            items.append(q);serial+=1
    assert len(items)==110
    return {"schema_version":1,"exam_type":f"practice-{form}","discipline":"electrical-computer","exam":form,
            "question_count":110,"appointment_minutes":355,"working_time_minutes":320,
            "blueprint_source":"meta/exam-blueprints.yaml","items":items}
def md(ex):
    L=[f"# FE Electrical and Computer Practice Exam {ex['exam']}","","**Questions:** 110  ","**Recommended working time:** 320 minutes  ","","## Questions",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n}","",q["prompt"],""]+[f"{c}) {v}" for c,v in zip("ABCD",q["choices"])]+[""]
    L += ["---","","## Answer Key and Worked Explanations",""]
    for n,q in enumerate(ex["items"],1):
        L += [f"### {n} — {q['answer']}","",q["solution"],"",f"**Knowledge area:** {q['knowledge_area']}  ",f"**Concept:** {q['requires_concepts'][0]}",""]
    return "\n".join(L)+"\n"
for form in ("A","B"):
    ex=build(form)
    (OUT/f"electrical-computer-practice-{form.lower()}.yaml").write_text(yaml.safe_dump(ex,sort_keys=False,allow_unicode=True,width=110))
    (OUT/f"electrical-computer-practice-{form.lower()}.md").write_text(md(ex))
    print(form,len(ex["items"]))
