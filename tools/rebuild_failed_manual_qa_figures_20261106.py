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

def fig0521():
    fig=plt.figure(figsize=(11,6.5))
    fig.text(.5,.955,"Linear superposition and transformed sections solve compatible elastic problems",ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)
    gs=fig.add_gridspec(3,6,height_ratios=[1.0,1.35,.55],left=.045,right=.965,top=.88,bottom=.1,hspace=.34,wspace=.36)
    a1=fig.add_subplot(gs[0,0:2]); beam_panel(a1,True,True,"P + w")
    a2=fig.add_subplot(gs[0,2:4]); beam_panel(a2,True,False,"P alone")
    a3=fig.add_subplot(gs[0,4:6]); beam_panel(a3,False,True,"w alone")
    fig.text(.338,.745,"=",fontsize=25,color=C_TEXT,ha="center")
    fig.text(.661,.745,"+",fontsize=25,color=C_TEXT,ha="center")

    axL=fig.add_subplot(gs[1,0:3]); axL.axis("off"); axL.set_xlim(0,10); axL.set_ylim(0,8)
    axL.text(5,7.55,"BONDED ORIGINAL SECTION",ha="center",fontsize=13,fontweight="bold",color=C_TEXT)
    axL.add_patch(Rectangle((3.2,1.9),3.6,2.3,fc=C_FILL,ec=C_BLUE,lw=1.3))
    axL.add_patch(Rectangle((3.2,4.2),3.6,2.3,fc=C_FILL2,ec=C_TEAL,lw=1.3))
    axL.text(5,3.0,"E₁ = 100 GPa",ha="center",va="center",fontsize=12,color=C_TEXT)
    axL.text(5,5.3,"E₂ = 200 GPa",ha="center",va="center",fontsize=12,color=C_TEXT)

    axR=fig.add_subplot(gs[1,3:6]); axR.axis("off"); axR.set_xlim(0,10); axR.set_ylim(0,8)
    axR.text(5,7.55,"REFERENCE E₁: WIDTH₂ → n b",ha="center",fontsize=13,fontweight="bold",color=C_TEXT)
    axR.add_patch(Rectangle((3.6,1.9),2.8,2.3,fc=C_FILL,ec=C_BLUE,lw=1.3))
    axR.add_patch(Rectangle((2.2,4.2),5.6,2.3,fc=C_FILL2,ec=C_TEAL,lw=1.3))
    axR.plot([1.8,8.2],[4.58,4.58],"--",color=C_RED,lw=1.3)
    axR.text(8.28,4.58,"NA",va="center",fontsize=11,color=C_RED)

    axB=fig.add_subplot(gs[2,:]); axB.axis("off")
    axB.text(.28,.72,"n = E₂/E₁ = 2",transform=axB.transAxes,ha="center",fontsize=15,color=C_TEXT)
    axB.text(.72,.72,"Neutral axis from transformed-area centroid",transform=axB.transAxes,ha="center",fontsize=14,color=C_TEXT)
    axB.text(.5,.2,"Superposition requires linear elasticity, small deformation, and unchanged boundary conditions.\nTransformed-section analysis assumes perfect bonding and common longitudinal strain.",transform=axB.transAxes,ha="center",va="center",fontsize=9.5,color=C_TEXT)
    save(fig,"0521","FIG-02-39-007")

def fig0579():
    fig=plt.figure(figsize=(10.8,6.2))
    fig.text(.5,.955,"Quality lines interpolate by vapor mass fraction between saturation limits",ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)
    gs=fig.add_gridspec(2,5,height_ratios=[1,.18],left=.06,right=.95,top=.88,bottom=.1,wspace=.42)
    ax=fig.add_subplot(gs[0,:3])
    ax.set_xlim(0,1.05); ax.set_ylim(0,1.05); ax.spines[['top','right']].set_visible(False); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Specific volume v (schematic)",fontsize=11); ax.set_ylabel("Pressure P (schematic)",fontsize=11)
    y=np.linspace(.1,.92,250); t=(y-.1)/.82
    xf=.12 + .12*(1-np.sqrt(1-t)); xg=.9 - .68*(t**.85)
    ax.fill_betweenx(y,xf,xg,color=C_FILL)
    ax.plot(xf,y,color=C_BLUE,lw=1.8); ax.plot(xg,y,color=C_BLUE,lw=1.8)
    for q in [.25,.5,.75]:
        x=xf+q*(xg-xf); ax.plot(x,y,"--",color=C_TEAL,lw=1)
        k=110; ax.text(x[k]+.01,y[k],f"x={q:g}",color=C_TEAL,fontsize=10)
    ax.plot([xf[-1]],[y[-1]],'o',color=C_RED,ms=4)
    ax.annotate("Critical point",xy=(xf[-1],y[-1]),xytext=(.35,.97),arrowprops=dict(arrowstyle="-",color=C_RED),fontsize=11)
    ax.text(xf[0],.06,"x=0: f",ha="center",fontsize=10); ax.text(xg[0],.06,"x=1: g",ha="center",fontsize=10)

    ar=fig.add_subplot(gs[0,3:]); ar.axis("off")
    ar.text(.02,.78,r"$x=\dfrac{m_g}{m_f+m_g}$",fontsize=22,color=C_TEXT)
    ar.text(.02,.55,r"$v=v_f+x(v_g-v_f)$",fontsize=22,color=C_TEXT)
    ar.text(.02,.28,"0 ≤ x ≤ 1 in the dome",fontsize=15,color=C_TEXT)
    ar.text(.02,.16,"Quality is undefined\nfor a single-phase state.",fontsize=15,color=C_TEXT,linespacing=1.25)

    ab=fig.add_subplot(gs[1,:]); ab.axis("off")
    ab.text(.5,.45,"Schematic P–v dome; quality contours follow the exact linear specific-volume mixture rule at each pressure.\nx is vapor mass fraction, not vapor volume fraction. Saturated f and g boundaries meet at the critical point.",ha="center",va="center",fontsize=9.5,color=C_TEXT)
    save(fig,"0579","FIG-02-48-002")

def dome_panel(ax,title,xlab,ylab):
    ax.spines[['top','right']].set_visible(False); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.set_title(title,fontsize=16,pad=8); ax.set_xlabel(xlab,fontsize=10); ax.set_ylabel(ylab,fontsize=10)
    y=np.linspace(.12,.88,180); t=(y-.12)/.76
    xf=.12+.08*(1-np.sqrt(1-t)); xg=.88-.55*(t**.9)
    ax.fill_betweenx(y,xf,xg,color=C_FILL)
    ax.plot(xf,y,color=C_BLUE,lw=1.7); ax.plot(xg,y,color=C_BLUE,lw=1.7)
    yy=.39; j=np.argmin(abs(y-yy))
    ax.plot([xf[j],xg[j]],[yy,yy],color=C_RED,lw=1.5)
    ax.annotate("",xy=(xg[j],yy),xytext=(xf[j],yy),arrowprops=dict(arrowstyle="-|>",color=C_RED,lw=1.5))
    ax.plot([xf[j],xg[j]],[yy,yy],'o',color=C_RED,ms=3)
    ax.text(xf[j],yy-.06,"f",ha="center",color=C_RED,fontsize=11); ax.text(xg[j],yy-.06,"g",ha="center",color=C_RED,fontsize=11)

def fig0583():
    fig=plt.figure(figsize=(10.8,6))
    fig.text(.5,.955,"The same constant-pressure vaporization crosses three property domes",ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)
    gs=fig.add_gridspec(3,3,height_ratios=[1,.22,.18],left=.06,right=.95,top=.87,bottom=.09,wspace=.22,hspace=.34)
    dome_panel(fig.add_subplot(gs[0,0]),"P–v","v: specific volume (schematic)","P: pressure (schematic)")
    dome_panel(fig.add_subplot(gs[0,1]),"T–s","s: specific entropy (schematic)","T: temperature (schematic)")
    dome_panel(fig.add_subplot(gs[0,2]),"P–h","h: specific enthalpy (schematic)","P: pressure (schematic)")
    a=fig.add_subplot(gs[1,:]); a.axis("off"); a.text(.5,.5,"Saturated f → g: P and T remain constant while v, s, and h increase.",ha="center",va="center",fontsize=16,color=C_TEXT)
    b=fig.add_subplot(gs[2,:]); b.axis("off"); b.text(.5,.5,"Three schematic coordinate views of the same pure-substance equilibrium phase change below the critical point.\nShapes and axes are qualitative and are not numerically cross-calibrated.",ha="center",va="center",fontsize=9.5,color=C_TEXT)
    save(fig,"0583","FIG-02-48-006")

def fig0614():
    fig=plt.figure(figsize=(10.6,6.2))
    fig.text(.5,.955,"A Carnot heat-engine cycle has two isotherms and two isentropes",ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)
    gs=fig.add_gridspec(2,5,height_ratios=[1,.16],left=.07,right=.95,top=.88,bottom=.1,wspace=.38)
    ax=fig.add_subplot(gs[0,:3]); ax.set_xlim(.6,2.4); ax.set_ylim(0,720)
    ax.set_xlabel("Specific entropy s (kJ/(kg·K))",fontsize=10); ax.set_ylabel("Temperature T (K)",fontsize=10); ax.grid(alpha=.12)
    pts=np.array([[1,600],[2,600],[2,300],[1,300],[1,600]])
    ax.fill(pts[:,0],pts[:,1],color=C_FILL,alpha=.9)
    ax.plot(pts[:,0],pts[:,1],color=C_BLUE,lw=1.8)
    for (x1,y1),(x2,y2) in zip(pts[:-1],pts[1:]):
        ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.6))
    for i,(x,y) in enumerate(pts[:-1],1):
        ax.text(x+.04,y+18 if i<3 else y+18,str(i),fontsize=12,color=C_RED)

    ar=fig.add_subplot(gs[0,3:]); ar.axis("off")
    ar.text(.02,.78,r"$q_H=600\ \mathrm{kJ/kg}$",fontsize=18,color=C_TEXT)
    ar.text(.02,.68,r"$q_L=300\ \mathrm{kJ/kg}$",fontsize=18,color=C_TEXT)
    ar.text(.02,.48,r"$w_{net}=300\ \mathrm{kJ/kg}$",fontsize=18,color=C_TEXT)
    ar.text(.02,.36,r"$\eta=1-\dfrac{T_L}{T_H}=0.50$",fontsize=19,color=C_TEXT)
    ar.text(.02,.16,"Clockwise engine cycle\nΔs across heat input = 1 kJ/(kg·K)",fontsize=14,color=C_TEXT,linespacing=1.25)

    ab=fig.add_subplot(gs[1,:]); ab.axis("off")
    ab.text(.5,.5,"Internally reversible cycle between constant-temperature reservoirs. Rectangle area equals net work per unit mass because net cycle heat equals net work.",ha="center",fontsize=9.5,color=C_TEXT)
    save(fig,"0614","FIG-02-53-002")

def fig0616():
    fig=plt.figure(figsize=(11,6.4))
    fig.text(.5,.96,"An ideal Brayton gas cycle connects compression, heating, expansion, and cooling",ha="center",va="top",fontsize=17,fontweight="bold",color=C_TEXT)
    gs=fig.add_gridspec(3,5,height_ratios=[1,.22,.18],left=.045,right=.965,top=.88,bottom=.08,wspace=.38,hspace=.28)
    ax=fig.add_subplot(gs[0,:3]); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,7)
    boxes={"C":(0.3,4.6),"Combustor":(3.6,4.6),"T":(6.9,4.6),"Cooler":(3.6,.6)}
    sizes={"C":(2.2,1.7),"Combustor":(2.2,1.7),"T":(2.2,1.7),"Cooler":(2.2,1.7)}
    for name,(x,y) in boxes.items():
        w,h=sizes[name]; ax.add_patch(Rectangle((x,y),w,h,fc=C_FILL,ec=C_BLUE,lw=1.2)); ax.text(x+w/2,y+h/2,name,ha="center",va="center",fontsize=18 if name in ("C","T") else 13,color=C_TEXT)
    ax.annotate("",xy=(3.6,5.45),xytext=(2.5,5.45),arrowprops=dict(arrowstyle="-|>",color=C_TEAL,lw=1.5))
    ax.annotate("",xy=(6.9,5.45),xytext=(5.8,5.45),arrowprops=dict(arrowstyle="-|>",color=C_TEAL,lw=1.5))
    ax.plot([8.0,8.0,5.8],[4.6,1.45,1.45],color=C_BLUE,lw=1.4); ax.annotate("",xy=(5.8,1.45),xytext=(6.6,1.45),arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.4))
    ax.plot([3.6,1.4,1.4],[1.45,1.45,4.6],color=C_BLUE,lw=1.4); ax.annotate("",xy=(1.4,4.6),xytext=(1.4,3.5),arrowprops=dict(arrowstyle="-|>",color=C_BLUE,lw=1.4))
    ax.text(2.9,6.15,"2",fontsize=11); ax.text(6.25,6.15,"3",fontsize=11); ax.text(8.4,3.3,"4",fontsize=11); ax.text(.65,3.2,"1",fontsize=11)

    at=fig.add_subplot(gs[0,3:]); s=np.linspace(0,.86,160)
    low=300+420*(s/.86)**1.25; high=500+700*(s/.86)**1.25
    at.plot(s,high,color=C_RED,lw=1.7); at.plot(s,low,color=C_TEAL,lw=1.7)
    at.plot([0,0],[300,500],color=C_BLUE,lw=1.7); at.plot([.86,.86],[720,1200],color=C_BLUE,lw=1.7)
    at.set_xlabel("s−s₁ (kJ/(kg·K))",fontsize=9); at.set_ylabel("T (K)",fontsize=9); at.grid(alpha=.12)
    for num,x,y in [(1,0,300),(2,0,500),(3,.86,1200),(4,.86,720)]: at.text(x+.025,y+18,str(num),fontsize=10)

    af=fig.add_subplot(gs[1,:]); af.axis("off")
    af.text(.5,.62,r"$r_p=6,\quad k=1.4$",ha="center",fontsize=16,color=C_TEXT)
    af.text(.5,.20,r"$\eta_{Brayton}=1-\dfrac{1}{r_p^{(k-1)/k}}=0.401$",ha="center",fontsize=18,color=C_TEXT)

    ab=fig.add_subplot(gs[2,:]); ab.axis("off")
    ab.text(.5,.5,"Ideal air-standard cycle: compressor and turbine are isentropic; heat addition and rejection occur at constant pressure.\nThe heater represents combustor heat addition; the cooler closes the idealized cycle.",ha="center",va="center",fontsize=9.5,color=C_TEXT)
    save(fig,"0616","FIG-02-53-004")

if __name__=="__main__":
    fig0521(); fig0579(); fig0583(); fig0614(); fig0616()
    print("Rebuilt 0521, 0579, 0583, 0614, 0616")
