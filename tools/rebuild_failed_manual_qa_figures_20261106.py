#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle
from matplotlib.lines import Line2D

ROOT=Path(__file__).resolve().parents[1]
PNG=ROOT/"figures/png"; SVG=ROOT/"figures/svg"

C_TEXT="#23313d"; C_BLUE="#235a78"; C_TEAL="#26776f"; C_RED="#b63b2e"; C_FILL="#edf3f6"; C_FILL2="#dcece9"

def save(fig, idx, stem):
    fig.savefig(SVG/f"{idx}_{stem}.svg", bbox_inches="tight", pad_inches=0.18)
    fig.savefig(PNG/f"{idx}_{stem}.png", dpi=300, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)

def support(ax,x,y,roller=False):
    ax.add_patch(Polygon([[x-0.16,y-0.12],[x+0.16,y-0.12],[x,y+0.04]],closed=True,fill=False,ec=C_BLUE,lw=1.4))
    if roller:
        ax.add_patch(Circle((x-0.07,y-0.17),0.025,fill=False,ec=C_BLUE,lw=1))
        ax.add_patch(Circle((x+0.07,y-0.17),0.025,fill=False,ec=C_BLUE,lw=1))

def beam_panel(ax, loadP=True, loadW=True, label=""):
    ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis("off")
    ax.add_patch(Rectangle((0.7,1.1),8.6,0.18,fc=C_FILL2,ec=C_BLUE,lw=1.3))
    support(ax,0.9,1.07); support(ax,9.1,1.07,True)
    if loadP:
        ax.annotate("",xy=(5,1.28),xytext=(5,2.45),arrowprops=dict(arrowstyle="-|>",lw=1.8,color=C_RED))
    if loadW:
        for x in np.linspace(0.9,9.1,9):
            ax.annotate("",xy=(x,1.28),xytext=(x,2.15),arrowprops=dict(arrowstyle="-|>",lw=1.0,color=C_TEAL))
    ax.text(5,0.38,label,ha="center",va="center",fontsize=12,color=C_TEXT)

def save_exact(fig, idx, stem, width_pt, height_pt):
    fig.set_size_inches(width_pt/72.0, height_pt/72.0, forward=True)
    fig.savefig(SVG/f"{idx}_{stem}.svg", format="svg")
    fig.savefig(PNG/f"{idx}_{stem}.png", dpi=300)
    plt.close(fig)

def fig0521():
    fig=plt.figure(figsize=(1030/72,600/72))
    fig.text(.5,.955,"Linear superposition and transformed sections solve compatible elastic problems",
             ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)

    # Compact top row: smaller beam diagrams and reduced gaps.
    a1=fig.add_axes([.045,.665,.265,.205]); beam_panel(a1,True,True,"P + w")
    a2=fig.add_axes([.365,.665,.265,.205]); beam_panel(a2,True,False,"P alone")
    a3=fig.add_axes([.685,.665,.265,.205]); beam_panel(a3,False,True,"w alone")
    fig.text(.337,.745,"=",fontsize=24,color=C_TEXT,ha="center",va="center")
    fig.text(.662,.745,"+",fontsize=24,color=C_TEXT,ha="center",va="center")

    # Reduced-size transformed-section diagrams.
    axL=fig.add_axes([.11,.315,.34,.285]); axL.axis("off"); axL.set_xlim(0,10); axL.set_ylim(0,8)
    axL.text(5,7.35,"BONDED ORIGINAL SECTION",ha="center",fontsize=12.5,fontweight="bold",color=C_TEXT)
    axL.add_patch(Rectangle((3.5,1.85),3.0,1.95,fc=C_FILL,ec=C_BLUE,lw=1.25))
    axL.add_patch(Rectangle((3.5,3.80),3.0,1.95,fc=C_FILL2,ec=C_TEAL,lw=1.25))
    axL.text(5,2.82,"E₁ = 100 GPa",ha="center",va="center",fontsize=11,color=C_TEXT)
    axL.text(5,4.78,"E₂ = 200 GPa",ha="center",va="center",fontsize=11,color=C_TEXT)

    axR=fig.add_axes([.55,.315,.34,.285]); axR.axis("off"); axR.set_xlim(0,10); axR.set_ylim(0,8)
    axR.text(5,7.35,"REFERENCE E₁: WIDTH₂ → n b",ha="center",fontsize=12.5,fontweight="bold",color=C_TEXT)
    axR.add_patch(Rectangle((3.85,1.85),2.3,1.95,fc=C_FILL,ec=C_BLUE,lw=1.25))
    axR.add_patch(Rectangle((2.55,3.80),4.9,1.95,fc=C_FILL2,ec=C_TEAL,lw=1.25))
    axR.plot([2.25,7.75],[4.15,4.15],"--",color=C_RED,lw=1.25)
    axR.text(7.87,4.15,"NA",va="center",fontsize=10.5,color=C_RED)

    # Tight bottom annotation band.
    fig.text(.30,.245,"n = E₂/E₁ = 2",ha="center",fontsize=14,color=C_TEXT)
    fig.text(.69,.245,"Neutral axis from transformed-area centroid",ha="center",fontsize=13,color=C_TEXT)
    fig.text(.5,.115,
             "Superposition requires linear elasticity, small deformation, and unchanged boundary conditions.\n"
             "Transformed-section analysis assumes perfect bonding and common longitudinal strain.",
             ha="center",va="center",fontsize=9.2,color=C_TEXT)

    save_exact(fig,"0521","FIG-02-39-007",1030,600)

def fig0579():
    fig=plt.figure(figsize=(10.8,6.2))
    fig.text(.5,.955,"Quality lines interpolate by vapor mass fraction between saturation limits",
             ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)

    ax=fig.add_axes([.06,.20,.56,.66])
    ax.set_xlim(0,1.05); ax.set_ylim(0,1.05)
    ax.spines[['top','right']].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Specific volume v (schematic)",fontsize=11)
    ax.set_ylabel("Pressure P (schematic)",fontsize=11)

    y=np.linspace(.10,.90,220)
    t=np.clip((y-.10)/.80,0,1)
    # Rounded dome with exact meeting at critical point; no NaNs.
    xf=.12 + .10*(1-np.sqrt(np.clip(1-t,0,1)))
    xg=.90 - .68*(t**.82)
    # Force exact critical-point convergence.
    xcrit=(xf[-1]+xg[-1])/2
    xf[-1]=xcrit; xg[-1]=xcrit

    ax.fill_betweenx(y,xf,xg,color=C_FILL)
    ax.plot(xf,y,color=C_BLUE,lw=1.8)
    ax.plot(xg,y,color=C_BLUE,lw=1.8)

    label_positions={.25:72,.50:102,.75:132}
    for q,k in label_positions.items():
        x=xf+q*(xg-xf)
        ax.plot(x,y,"--",color=C_TEAL,lw=1)
        ax.text(x[k]+.012,y[k]+(.012 if q!=.50 else -.008),
                f"x={q:g}",color=C_TEAL,fontsize=9.5,ha="left")

    ax.plot([xcrit],[y[-1]],'o',color=C_RED,ms=4)
    ax.annotate("Critical point",xy=(xcrit,y[-1]),xytext=(.34,.98),
                arrowprops=dict(arrowstyle="-",color=C_RED,lw=1),
                fontsize=11,color=C_TEXT)
    ax.text(xf[0],.055,"x=0: f",ha="center",fontsize=10)
    ax.text(xg[0],.055,"x=1: g",ha="center",fontsize=10)

    ar=fig.add_axes([.66,.22,.29,.60]); ar.axis("off")
    ar.text(.02,.79,r"$x=\dfrac{m_g}{m_f+m_g}$",fontsize=21,color=C_TEXT)
    ar.text(.02,.57,r"$v=v_f+x(v_g-v_f)$",fontsize=20,color=C_TEXT)
    ar.text(.02,.31,"0 ≤ x ≤ 1 in the dome",fontsize=14.5,color=C_TEXT)
    ar.text(.02,.18,"Quality is undefined\nfor a single-phase state.",
            fontsize=14.5,color=C_TEXT,linespacing=1.22)

    fig.text(.5,.095,
             "Schematic P–v dome; quality contours follow the exact linear specific-volume mixture rule at each pressure.\n"
             "x is vapor mass fraction, not vapor volume fraction. Saturated f and g boundaries meet at the critical point.",
             ha="center",va="center",fontsize=9.3,color=C_TEXT)
    save(fig,"0579","FIG-02-48-002")

def dome_panel(ax,title,xlab,ylab):
    ax.spines[['top','right']].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.set_title(title,fontsize=16,pad=7)
    ax.set_xlabel(xlab,fontsize=10)
    ax.set_ylabel(ylab,fontsize=10)

    y=np.linspace(.12,.88,180)
    t=np.clip((y-.12)/.76,0,1)
    # Smooth dome; both sides converge naturally at the critical point.
    xf=.12 + .10*(1-np.sqrt(np.clip(1-t,0,1)))
    xg=.88 - .66*(t**.86)
    xcrit=(xf[-1]+xg[-1])/2
    xf[-1]=xcrit; xg[-1]=xcrit

    ax.fill_betweenx(y,xf,xg,color=C_FILL)
    ax.plot(xf,y,color=C_BLUE,lw=1.7)
    ax.plot(xg,y,color=C_BLUE,lw=1.7)

    yy=.39; j=np.argmin(abs(y-yy))
    ax.annotate("",xy=(xg[j],yy),xytext=(xf[j],yy),
                arrowprops=dict(arrowstyle="-|>",color=C_RED,lw=1.5))
    ax.plot([xf[j],xg[j]],[yy,yy],'o',color=C_RED,ms=3)
    ax.text(xf[j],yy-.055,"f",ha="center",color=C_RED,fontsize=10.5)
    ax.text(xg[j],yy-.055,"g",ha="center",color=C_RED,fontsize=10.5)

def fig0583():
    fig=plt.figure(figsize=(10.8,5.8))
    fig.text(.5,.96,"The same constant-pressure vaporization crosses three property domes",
             ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)

    ax1=fig.add_axes([.055,.32,.27,.54])
    ax2=fig.add_axes([.365,.32,.27,.54])
    ax3=fig.add_axes([.675,.32,.27,.54])
    dome_panel(ax1,"P–v","v: specific volume (schematic)","P: pressure (schematic)")
    dome_panel(ax2,"T–s","s: specific entropy (schematic)","T: temperature (schematic)")
    dome_panel(ax3,"P–h","h: specific enthalpy (schematic)","P: pressure (schematic)")

    fig.text(.5,.205,
             "Saturated f → g: P and T remain constant while v, s, and h increase.",
             ha="center",fontsize=15.5,color=C_TEXT)
    fig.text(.5,.095,
             "Three schematic coordinate views of the same pure-substance equilibrium phase change below the critical point.\n"
             "Shapes and axes are qualitative and are not numerically cross-calibrated.",
             ha="center",va="center",fontsize=9.3,color=C_TEXT)
    save(fig,"0583","FIG-02-48-006")

def fig0614():
    fig=plt.figure(figsize=(900/72,540/72))
    fig.text(.5,.955,"A Carnot heat-engine cycle has two isotherms and two isentropes",
             ha="center",va="top",fontsize=16.5,fontweight="bold",color=C_TEXT)

    # Larger plot area with less dead space around it.
    ax=fig.add_axes([.07,.205,.54,.66])
    ax.set_xlim(.6,2.4); ax.set_ylim(0,720)
    ax.set_xlabel("Specific entropy s (kJ/(kg·K))",fontsize=10)
    ax.set_ylabel("Temperature T (K)",fontsize=10)
    ax.grid(alpha=.12)
    pts=np.array([[1,600],[2,600],[2,300],[1,300],[1,600]])
    ax.fill(pts[:,0],pts[:,1],color=C_FILL,alpha=.9)
    ax.plot(pts[:,0],pts[:,1],color=C_BLUE,lw=1.8)
    for (x1,y1),(x2,y2) in zip(pts[:-1],pts[1:]):
        ax.annotate("",xy=(x2,y2),xytext=(x1,y1),
                    arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.6))
    for i,(x,y) in enumerate(pts[:-1],1):
        ax.text(x+.04,y+18,str(i),fontsize=12,color=C_RED)

    # Condensed right-hand text block with intentionally even spacing.
    fig.text(.665,.745,r"$q_H=600\ \mathrm{kJ/kg}$",fontsize=16,color=C_TEXT)
    fig.text(.665,.665,r"$q_L=300\ \mathrm{kJ/kg}$",fontsize=16,color=C_TEXT)
    fig.text(.665,.515,r"$w_{net}=300\ \mathrm{kJ/kg}$",fontsize=16,color=C_TEXT)
    fig.text(.665,.405,r"$\eta=1-\dfrac{T_L}{T_H}=0.50$",fontsize=17,color=C_TEXT)
    fig.text(.665,.285,"Clockwise engine cycle",fontsize=13.5,color=C_TEXT)
    fig.text(.665,.225,"Δs across heat input = 1 kJ/(kg·K)",fontsize=13.5,color=C_TEXT)

    fig.text(.5,.075,
             "Internally reversible cycle between constant-temperature reservoirs. "
             "Rectangle area equals net work per unit mass because net cycle heat equals net work.",
             ha="center",fontsize=8.8,color=C_TEXT)

    save_exact(fig,"0614","FIG-02-53-002",900,540)

def fig0616():
    fig=plt.figure(figsize=(11,6.2))
    fig.text(.5,.96,"An ideal Brayton gas cycle connects compression, heating, expansion, and cooling",
             ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)

    ax=fig.add_axes([.045,.34,.53,.50]); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,7)
    boxes={"C":(0.3,4.6),"Combustor":(3.6,4.6),"T":(6.9,4.6),"Cooler":(3.6,.6)}
    sizes={"C":(2.2,1.7),"Combustor":(2.2,1.7),"T":(2.2,1.7),"Cooler":(2.2,1.7)}
    for name,(x,y) in boxes.items():
        w,h=sizes[name]
        ax.add_patch(Rectangle((x,y),w,h,fc=C_FILL,ec=C_BLUE,lw=1.2))
        ax.text(x+w/2,y+h/2,name,ha="center",va="center",
                fontsize=18 if name in ("C","T") else 13,color=C_TEXT)
    ax.annotate("",xy=(3.6,5.45),xytext=(2.5,5.45),arrowprops=dict(arrowstyle="-|>",color=C_TEAL,lw=1.5))
    ax.annotate("",xy=(6.9,5.45),xytext=(5.8,5.45),arrowprops=dict(arrowstyle="-|>",color=C_TEAL,lw=1.5))
    ax.plot([8.0,8.0,5.8],[4.6,1.45,1.45],color=C_BLUE,lw=1.4)
    ax.annotate("",xy=(5.8,1.45),xytext=(6.6,1.45),arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.4))
    ax.plot([3.6,1.4,1.4],[1.45,1.45,4.6],color=C_BLUE,lw=1.4)
    ax.annotate("",xy=(1.4,4.6),xytext=(1.4,3.5),arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.4))
    ax.text(2.9,6.15,"2",fontsize=11); ax.text(6.25,6.15,"3",fontsize=11)
    ax.text(8.4,3.3,"4",fontsize=11); ax.text(.65,3.2,"1",fontsize=11)

    at=fig.add_axes([.63,.34,.32,.50])
    ss=np.linspace(0,.86,160)
    low=300+420*(ss/.86)**1.25
    high=500+700*(ss/.86)**1.25
    at.plot(ss,high,color=C_RED,lw=1.7)
    at.plot(ss,low,color=C_TEAL,lw=1.7)
    at.plot([0,0],[300,500],color=C_BLUE,lw=1.7)
    at.plot([.86,.86],[720,1200],color=C_BLUE,lw=1.7)
    at.set_xlabel("s−s₁ (kJ/(kg·K))",fontsize=9)
    at.set_ylabel("T (K)",fontsize=9)
    at.grid(alpha=.12)
    for num,x,yv in [(1,0,300),(2,0,500),(3,.86,1200),(4,.86,720)]:
        at.text(x+.025,yv+18,str(num),fontsize=10)

    # Separate parameter and efficiency lines so the fraction never collides.
    fig.text(.50,.245,r"$r_p=6,qquad k=1.4$",ha="center",fontsize=15.5,color=C_TEXT)
    fig.text(.50,.165,r"$\eta_{Brayton}=1-\dfrac{1}{r_p^{(k-1)/k}}=0.401$",
             ha="center",fontsize=17,color=C_TEXT)

    fig.text(.5,.07,
             "Ideal air-standard cycle: compressor and turbine are isentropic; heat addition and rejection occur at constant pressure.\n"
             "The heater represents combustor heat addition; the cooler closes the idealized cycle.",
             ha="center",va="center",fontsize=9.3,color=C_TEXT)
    save(fig,"0616","FIG-02-53-004")

if __name__=="__main__":
    fig0521(); fig0579(); fig0583(); fig0614(); fig0616()
    print("Rebuilt 0521, 0579, 0583, 0614, 0616")

# trigger rebuild after visual QA
