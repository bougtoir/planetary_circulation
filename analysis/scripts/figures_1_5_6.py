#!/usr/bin/env python3
"""Figures 1 (ontology schematic), 5 (representative networks), 6 (energy architectures)."""
import os, json
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import networkx as nx

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROC = os.path.join(ROOT,"data","processed"); FIG = os.path.join(ROOT,"analysis","figures")
m = pd.read_csv(os.path.join(PROC,"planetary_circulation_master.csv"))
BATTR = json.load(open(os.path.join(PROC,"body_attributes.json")))

# ---------------- Figure 1: reservoir ontology ----------------
fig, ax = plt.subplots(figsize=(7.4,4.6))
pos = {"Core":(1,0),"Mantle":(1,1),"Crust/Ice Shell":(1,2),"Subsurface Liquid":(2.6,1.6),
       "Surface":(1,3),"Atmosphere":(1,4),"Space":(1,5)}
for n,(x,y) in pos.items():
    ax.add_patch(mp.FancyBboxPatch((x-0.42,y-0.16),0.84,0.32,
        boxstyle="round,pad=0.03",fc="#eef2f5",ec="#31597f",lw=1.2))
    ax.text(x,y,n,ha="center",va="center",fontsize=8.5)
arrows=[("Mantle","Surface","E1"),("Crust/Ice Shell","Crust/Ice Shell","E2"),
        ("Surface","Atmosphere","E3/E7"),("Subsurface Liquid","Surface","E4"),
        ("Atmosphere","Surface","E5"),("Atmosphere","Space","E6"),
        ("Core","Mantle","internal"),("Mantle","Crust/Ice Shell","internal")]
for u,v,lab in arrows:
    if u==v:
        ax.annotate("",xy=(pos[u][0]+0.42,pos[u][1]),xytext=(pos[u][0]+0.9,pos[u][1]),
                    arrowprops=dict(arrowstyle="<->",color="#555",lw=1,
                                    connectionstyle="arc3,rad=0"))
        ax.text(pos[u][0]+1.05,pos[u][1],lab,fontsize=7.5,va="center")
        continue
    x1,y1=pos[u]; x2,y2=pos[v]
    ax.annotate("",xy=(x2,y2-0.16),xytext=(x1,y1+0.16),
                arrowprops=dict(arrowstyle="<->",color="#31597f",lw=1.4))
    ax.text((x1+x2)/2+0.5,(y1+y2)/2,lab,fontsize=7.5,color="#31597f")
for i,(src,y) in enumerate([("primordial + radiogenic",0.5),("tidal",1.0),("stellar",4.0)]):
    ax.annotate("",xy=(0.55,y),xytext=(-1.15,y),
        arrowprops=dict(arrowstyle="->",color="#c07020",lw=1.6))
    ax.text(-1.2,y,src,ha="right",va="center",fontsize=8,color="#c07020")
ax.set_xlim(-2.4,3.4); ax.set_ylim(-0.5,5.5); ax.axis("off")
ax.set_title("Common reservoir ontology: seven nodes, seven process classes E1–E7,\n"
             "three external/internal energy drivers")
fig.tight_layout(); fig.savefig(os.path.join(FIG,"fig1_ontology.pdf"))
fig.savefig(os.path.join(FIG,"fig1_ontology.png"),dpi=300); plt.close(fig)

# ---------------- Figure 5: representative networks ----------------
SUPPORT={"direct_active","probable_active","residual"}
RANK={"residual":1,"probable_active":2,"direct_active":3}
NP={b:set(["Core","Mantle","Crust/Ice","Surface","Atmosphere","Space"]) for b in
    ["Earth","Venus","Mars","Moon","Mercury","Io","Europa","Titan"]}
# Subsurface Liquid node present wherever E4 is not structurally absent
for b in NP:
    if m[(m.body==b)&(m.edge_id=="E4")].iloc[0].current_activity_status!="structurally_absent":
        NP[b].add("Subsurface\nLiquid")
EN={"E1":("Mantle","Surface"),"E3":("Surface","Atmosphere"),"E4":("Subsurface\nLiquid","Surface"),
    "E5":("Atmosphere","Surface"),"E6":("Atmosphere","Space"),"E7":("Surface","Atmosphere")}
# E2 self-loop drawn as ring marker on Crust/Ice
show=["Earth","Mars","Moon","Io","Europa","Titan"]
npos={"Core":(0,0),"Mantle":(0,0.9),"Crust/Ice":(0,1.8),"Subsurface\nLiquid":(1.15,1.8),
      "Surface":(0,2.7),"Atmosphere":(0,3.6),"Space":(0,4.5)}
fig,axs=plt.subplots(2,3,figsize=(9.6,7.6))
scol={"direct_active":"#2166ac","probable_active":"#8ec07c","residual":"#f0c040"}
for ax,b in zip(axs.flat,show):
    G=nx.Graph(); G.add_nodes_from(NP[b])
    e2 = m[(m.body==b)&(m.edge_id=="E2")].iloc[0]
    agg={}
    for e,(u,v) in EN.items():
        r=m[(m.body==b)&(m.edge_id==e)].iloc[0]
        if r.current_activity_status in SUPPORT and u in G and v in G:
            key=(u,v)
            if key not in agg or RANK[r.current_activity_status]>RANK[agg[key]]:
                agg[key]=r.current_activity_status
    for (u,v),st in agg.items():
        G.add_edge(u,v,st=st)
    if e2.current_activity_status in SUPPORT:
        G.add_edge("Crust/Ice","Crust/Ice",st=e2.current_activity_status)
    for u,v,d in G.edges(data=True):
        if u==v:
            ax.add_patch(mp.Ellipse((npos[u][0]+0.42,npos[u][1]),0.5,0.34,fill=False,
                                    ec=scol[d["st"]],lw=1.8))
        else:
            x1,y1=npos[u]; x2,y2=npos[v]
            ax.plot([x1,x2],[y1,y2],color=scol[d["st"]],lw=2.0,solid_capstyle="round",
                    zorder=1)
    for n in G.nodes:
        x,y=npos[n]
        ax.add_patch(mp.Circle((x,y),0.30,fc="#eef2f5",ec="#31597f",lw=1.1,zorder=2))
        ax.text(x,y,n,ha="center",va="center",fontsize=6.4,zorder=3)
    # faded absent SL node
    if "Subsurface\nLiquid" not in G:
        x,y=npos["Subsurface\nLiquid"]
        ax.add_patch(mp.Circle((x,y),0.30,fc="none",ec="#bbbbbb",lw=1,ls="--",zorder=2))
        ax.text(x,y,"absent",ha="center",va="center",fontsize=5.6,color="#999",zorder=3)
    ne=sum(1 for e in ["E1","E2","E3","E4","E5","E6","E7"]
           if m[(m.body==b)&(m.edge_id==e)].iloc[0].current_activity_status in SUPPORT)
    ax.set_title(f"{b} — {ne}/7 process classes supported",fontsize=9)
    ax.set_xlim(-0.8,1.8); ax.set_ylim(-0.5,4.9); ax.axis("off")
import matplotlib.lines as ml
leg=[ml.Line2D([],[],color=scol[k],lw=2,label=l) for k,l in
     [("direct_active","directly observed"),("probable_active","probable"),
      ("residual","residual")]]
fig.legend(handles=leg,loc="lower center",ncol=3,fontsize=8,frameon=False)
fig.suptitle("Circulation networks on the common reservoir ontology",fontsize=11)
fig.tight_layout(rect=(0,0.04,1,1))
fig.savefig(os.path.join(FIG,"fig5_networks.pdf"))
fig.savefig(os.path.join(FIG,"fig5_networks.png"),dpi=300); plt.close(fig)

# ---------------- Figure 6: energy architecture vs supported edges ----------------
supcnt = m[m.current_activity_status.isin(SUPPORT)].groupby("body").size()
spread = pd.read_csv(os.path.join(ROOT,"analysis","derived","persistence_spread.csv"),
                     index_col=0).frac
dom = (pd.read_csv(os.path.join(ROOT,"analysis","derived","energy_architecture.csv"),
       index_col=0)["dom_driver"]).to_dict()
cmapc={"tidal":"#d95f02","radiogenic+primordial":"#1b9e77","internal+stellar":"#7570b3",
       "internal (declining)":"#7570b3","relict internal+tidal":"#666666",
       "internal (dynamo persists)":"#1b9e77","stellar-atmospheric":"#e6ab02","tidal+internal":"#d95f02"}
fig,axs=plt.subplots(1,2,figsize=(8.6,3.6))
ax=axs[0]
for b in supcnt.index:
    ax.scatter(BATTR[b]["age"],supcnt[b],s=60,color=cmapc[dom[b]],zorder=3)
    ax.annotate(b,(BATTR[b]["age"],supcnt[b]),textcoords="offset points",xytext=(5,3),
                fontsize=8)
ax.set_xlabel("body age (Gyr)"); ax.set_ylabel("supported process classes (of 7)")
ax.set_title("Activity vs age: no monotonic decline")
ax=axs[1]
order=["Earth","Venus","Mars","Moon","Mercury","Io","Europa","Titan"]
ax.bar([b for b in order],[spread.get(b,0) for b in order],
       color=[cmapc[dom[b]] for b in order])
ax.set_ylabel("persistence spread (max−min fraction)")
ax.set_title("Asynchronous cessation is not ordered by energy source")
ax.tick_params(axis="x",rotation=45)
for tick,b in zip(ax.get_xticklabels(),order): tick.set_fontsize(8)
fig.tight_layout(); fig.savefig(os.path.join(FIG,"fig6_energy.pdf"))
fig.savefig(os.path.join(FIG,"fig6_energy.png"),dpi=300); plt.close(fig)
print("figs 1,5,6 done")
