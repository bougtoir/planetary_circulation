#!/usr/bin/env python3
"""Phases 6-10: activity representation, dimensionality, persistence (incl. internal
cessation indicators), network metrics, energy-architecture comparison, robustness.
All outputs -> analysis/derived/, analysis/figures/, analysis/tables/."""
import os, json
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import networkx as nx
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROC = os.path.join(ROOT, "data", "processed")
DER = os.path.join(ROOT, "analysis", "derived")
FIG = os.path.join(ROOT, "analysis", "figures")
TAB = os.path.join(ROOT, "analysis", "tables")
for d in (DER, FIG, TAB): os.makedirs(d, exist_ok=True)

BODIES = ["Earth","Venus","Mars","Moon","Mercury","Io","Europa","Titan"]
EDGES  = ["E1","E2","E3","E4","E5","E6","E7"]
m = pd.read_csv(os.path.join(PROC, "planetary_circulation_master.csv"))
BATTR = json.load(open(os.path.join(PROC, "body_attributes.json")))

# ---------------- 6B evidence-state encoding ----------------
CODE = {"direct_active":4, "probable_active":3, "residual":2,
        "none_detected":1, "unknown":0, "structurally_absent":np.nan}
m["act_code"] = m.current_activity_status.map(CODE)
act = m.pivot(index="body", columns="edge_id", values="act_code")[EDGES].reindex(BODIES)
stat = m.pivot(index="body", columns="edge_id", values="current_activity_status")[EDGES].reindex(BODIES)
tier = m.pivot(index="body", columns="edge_id", values="measurement_tier")[EDGES].reindex(BODIES)
obs  = m.pivot(index="body", columns="edge_id", values="observability_class")[EDGES].reindex(BODIES)

# ---------------- Figure 2: activity/evidence matrix ----------------
fig, ax = plt.subplots(figsize=(7.2, 4.6))
cmap = ListedColormap(["#d9d9d9","#969696","#f0c040","#7fb069","#1f78b4"])  # ?,none?,res,prob,direct
data = act.values.astype(float)
disp = np.nan_to_num(data, nan=-1)
# six evidence states: absent(-1), unknown(0), none_detected(1), residual(2),
# probable(3), direct(4) -> indices 0..5
cmap2 = ListedColormap(["#f7f7f7","#cccccc","#969696","#f0c040","#8ec07c","#2166ac"])
im = ax.imshow(disp+1, cmap=cmap2, vmin=-0.5, vmax=5.5, aspect="auto")
ax.set_xticks(range(7), EDGES); ax.set_yticks(range(8), BODIES)
for i in range(8):
    for j in range(7):
        s = stat.iloc[i,j]
        txt = {"direct_active":"D","probable_active":"P","residual":"R",
               "none_detected":"0","unknown":"?","structurally_absent":"—"}[s]
        ax.text(j,i,txt,ha="center",va="center",fontsize=8,
                color="black")
ax.set_xticks(np.arange(-.5,7),minor=True); ax.set_yticks(np.arange(-.5,8),minor=True)
ax.grid(which="minor",color="white",lw=1.2); ax.tick_params(which="minor",length=0)
import matplotlib.patches as mp
leg = [mp.Patch(color="#2166ac",label="directly observed active (D)"),
       mp.Patch(color="#8ec07c",label="probable active (P)"),
       mp.Patch(color="#f0c040",label="residual/weak (R)"),
       mp.Patch(color="#969696",label="none detected (0)"),
       mp.Patch(color="#cccccc",label="unknown (?)"),
       mp.Patch(color="#f7f7f7",label="structurally absent (—)")]
ax.legend(handles=leg, loc="upper center", bbox_to_anchor=(0.5,-0.12), ncol=3,
          fontsize=7.5, frameon=False)
ax.set_title("Current circulation activity and evidence state (letters = state; D/P/R/0/—)")
fig.tight_layout(); fig.savefig(os.path.join(FIG,"fig2_activity_matrix.pdf"))
fig.savefig(os.path.join(FIG,"fig2_activity_matrix.png"), dpi=300); plt.close(fig)

# ---------------- Phase 7: dimensionality ----------------
# ordinal coding on non-absent cells; fill absent cells by column median for ordination only
X = act.values.copy()
keep = ~np.all(np.isnan(X), axis=0)
Xu = X[:, keep]; edges_u = [e for e,k in zip(EDGES,keep) if k]
colmed = np.nanmedian(Xu, axis=0)
Xf = np.where(np.isnan(Xu), colmed, Xu)
Xs = StandardScaler().fit_transform(Xf)
pca = PCA().fit(Xs)
evr = pca.explained_variance_ratio_
load = pd.DataFrame(pca.components_.T, index=edges_u,
    columns=[f"PC{i+1}" for i in range(len(edges_u))])
scores = pd.DataFrame(pca.transform(Xs), index=BODIES,
    columns=load.columns)
loo = {}
for b in BODIES:
    Xl = Xs[[i for i,x in enumerate(BODIES) if x!=b]]
    p = PCA().fit(Xl); loo[b] = p.explained_variance_ratio_[:3].tolist()
pd.DataFrame(loo, index=["PC1","PC2","PC3"]).T.to_csv(os.path.join(DER,"pca_loo.csv"))
load.to_csv(os.path.join(DER,"pca_loadings.csv"))
scores.to_csv(os.path.join(DER,"pca_scores.csv"))
pd.Series(evr, index=[f"PC{i+1}" for i in range(len(evr))]).to_csv(
    os.path.join(DER,"pca_explained.csv"))

# Fig 3: state-space
fig, ax = plt.subplots(figsize=(5.2,4.4))
ax.scatter(scores.PC1, scores.PC2, s=40, c="#2166ac")
LABOFF={"Io":(8,-8),"Mars":(-8,-3)}
LABHA={"Mars":"right"}
for b in scores.index:
    ax.annotate(b,(scores.loc[b,"PC1"],scores.loc[b,"PC2"]),
                textcoords="offset points",xytext=LABOFF.get(b,(6,4)),
                ha=LABHA.get(b,"left"),fontsize=9)
ax.axhline(0,ls=":",c="grey",lw=.7); ax.axvline(0,ls=":",c="grey",lw=.7)
ax.set_xlabel(f"PC1 ({evr[0]*100:.0f}% var)"); ax.set_ylabel(f"PC2 ({evr[1]*100:.0f}% var)")
ax.set_title("Evidence-state ordination (exploratory, n=8)")
fig.tight_layout(); fig.savefig(os.path.join(FIG,"fig3_ordination.pdf"))
fig.savefig(os.path.join(FIG,"fig3_ordination.png"),dpi=300); plt.close(fig)

# ---------------- Phase 8: persistence ----------------
# within-body persistence spectra: process-level persistence fractions plus
# internal-state cessation indicators (dynamo, volcanism cessation ages).
# fraction = duration / body_age; active -> right-censored at 1.0
spec_records=[]
for b in BODIES:
    age = BATTR[b]["age"]
    for e in EDGES:
        r = m[(m.body==b)&(m.edge_id==e)].iloc[0]
        if r.current_activity_status=="structurally_absent": continue
        if r.currently_active==1:
            spec_records.append(dict(body=b, proc=e, frac=1.0, frac_lo=1.0, frac_hi=1.0,
                                     censored=True, inferred=False))
        else:
            la,lo,hi = r.last_major_activity_age_Gyr, r.last_activity_lower_Gyr, r.last_activity_upper_Gyr
            if pd.isna(la): continue
            spec_records.append(dict(body=b, proc=e,
                frac=(age-la)/age, frac_lo=(age-hi)/age, frac_hi=(age-lo)/age,
                censored=False, inferred=False))
# dynamo cessation as internal-state indicator (not an edge).
# `dated` = cessation age constrained by measured evidence (crustal remanence on
# Mars; Apollo paleointensity on the Moon). Venus has no detected paleofield: its
# ~4-4.5 Ga shutdown is INFERRED from the present absence, so it is flagged
# inferred and excluded from the persistence-spread statistic (but still drawn).
dynamo_off = {"Mars":((4.1,4.1,4.14),True),"Moon":((2.0,1.0,3.5),True),
              "Venus":((4.5,4.0,4.5),False),
              "Mercury":None,"Earth":None,"Io":None,"Europa":None,"Titan":None}
for b,span in dynamo_off.items():
    if span is None: continue
    (la,lo,hi),dated = span
    age=BATTR[b]["age"]
    spec_records.append(dict(body=b, proc="dynamo(internal)", frac=(age-la)/age,
        frac_lo=(age-hi)/age, frac_hi=(age-lo)/age, censored=False,
        inferred=not dated))
spec = pd.DataFrame(spec_records)
spec.to_csv(os.path.join(DER,"persistence_spectrum.csv"), index=False)

# ONE primary persistence-spread statistic (harmonized main text + supplement):
#   spread(body) = max frac - min frac over DATED cessations + censored cells.
# Undated/inferred cessations (Venus dynamo) are excluded — they are not
# empirically measured events. The earlier IQR-based "API" variant is removed.
datable = spec[~spec.inferred]
spread = datable.groupby("body").frac.apply(lambda s: float(s.max()-s.min()))
spread = spread.reindex(BODIES).fillna(0.0)
spread.to_csv(os.path.join(DER,"persistence_spread.csv"))

# Monte Carlo over cessation-age intervals (uniform within [lo,hi]) on the SAME
# statistic: draw each dated cessation's frac, censored cells fixed at 1.0,
# spread = max - min of the drawn vector.
rng = np.random.default_rng(7)
mc=[]
for b in BODIES:
    sub = datable[datable.body==b]
    if len(sub)<2:
        mc.append(dict(body=b, spread_med=0.0, spread_lo=0.0, spread_hi=0.0)); continue
    draws=[]
    for _ in range(4000):
        vals=[1.0 if r.censored else rng.uniform(r.frac_lo, r.frac_hi)
              for _,r in sub.iterrows()]
        draws.append(max(vals)-min(vals))
    mc.append(dict(body=b, spread_med=np.median(draws),
                   spread_lo=np.percentile(draws,5),
                   spread_hi=np.percentile(draws,95)))
pd.DataFrame(mc).to_csv(os.path.join(DER,"spread_montecarlo.csv"), index=False)

# Fig 4: persistence spectra — one row per process, grouped by body
fig, ax = plt.subplots(figsize=(7.6,5.6))
yv=0; body_marks=[]
for b in BODIES:
    sub=spec[spec.body==b]
    start=yv
    for _,r in sub.iterrows():
        if r.censored:
            ax.plot([r.frac,1.04],[yv,yv],color="#2166ac",lw=2.6,solid_capstyle="butt")
            ax.plot(1.05,yv,marker=">",color="#2166ac",ms=4,clip_on=False)
        elif r.inferred:
            ax.plot([r.frac_lo,r.frac_hi],[yv,yv],color="#7f7f7f",lw=2.6,
                    solid_capstyle="butt",alpha=.7,ls=(0,(2,2)))
            ax.plot(r.frac,yv,"|",color="#555555",ms=6)
        else:
            ax.plot([r.frac_lo,r.frac_hi],[yv,yv],color="#b2182b",lw=2.6,
                    solid_capstyle="butt",alpha=.85)
            ax.plot(r.frac,yv,"|",color="black",ms=6)
        ax.text(-0.02,yv,r.proc,ha="right",va="center",fontsize=6.3)
        yv+=1
    body_marks.append((b,(start+yv-1)/2))
    yv+=0.9
ax.set_yticks([]); ax.set_xlim(-0.34,1.12); ax.set_ylim(-0.6,yv)
ax.invert_yaxis()
for b,y in body_marks:
    ax.text(-0.335,y,b,ha="left",va="center",fontsize=8.5,fontweight="bold")
ax.set_xlabel("persistence fraction of body age (arrow = still active, right-censored)")
ax.set_title("Within-body persistence spectra: asynchronous cessation")
import matplotlib.lines as ml
ax.legend(handles=[ml.Line2D([],[],color="#2166ac",lw=2.6,label="still active (censored)"),
                   ml.Line2D([],[],color="#b2182b",lw=2.6,label="ceased (dated interval)"),
                   ml.Line2D([],[],color="#7f7f7f",lw=2.6,ls=(0,(2,2)),
                             label="ceased (inferred, not dated)")],
          loc="lower right",fontsize=7,frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG,"fig4_persistence.pdf"))
fig.savefig(os.path.join(FIG,"fig4_persistence.png"),dpi=300); plt.close(fig)

# ---------------- Phase 9: network ----------------
# nodes: reservoirs present; edges supported if status in active/probable/residual
SUPPORT = {"direct_active","probable_active","residual"}
RANK = {"residual":1,"probable_active":2,"direct_active":3}
NODE_PRESENT = {b:set(["Core","Mantle","Crust/Ice Shell","Surface","Atmosphere","Space"])
                for b in BODIES}
# Subsurface Liquid node present wherever the master table does not mark E4 as
# structurally absent (Earth groundwater, Mars mid-crust liquid, icy/ocean moons)
for b in BODIES:
    e4 = m[(m.body==b)&(m.edge_id=="E4")].iloc[0].current_activity_status
    if e4 != "structurally_absent":
        NODE_PRESENT[b].add("Subsurface Liquid")
# Moon/Mercury: exosphere counts as tenuous Atmosphere node
EDGE_NODES = {"E1":("Mantle","Surface"),"E2":("Crust/Ice Shell","Crust/Ice Shell"),
    "E3":("Surface","Atmosphere"),"E4":("Subsurface Liquid","Surface"),
    "E5":("Atmosphere","Surface"),"E6":("Atmosphere","Space"),
    "E7":("Surface","Atmosphere")}
nets={}
for b in BODIES:
    G=nx.Graph(); G.add_nodes_from(NODE_PRESENT[b])
    # multiple process classes can couple the same reservoir pair (E3/E5/E7 all
    # link Surface<->Atmosphere): keep the strongest evidence state per link and
    # record every supporting process so none is silently overwritten
    agg = {}
    for e in EDGES:
        r=m[(m.body==b)&(m.edge_id==e)].iloc[0]
        u,v=EDGE_NODES[e]
        if r.current_activity_status not in SUPPORT or u not in G or v not in G:
            continue
        key=(u,v)
        if key not in agg:
            agg[key]={"processes":[],"strength":r.current_activity_status}
        agg[key]["processes"].append(e)
        if RANK[r.current_activity_status] > RANK[agg[key]["strength"]]:
            agg[key]["strength"]=r.current_activity_status
    for (u,v),d in agg.items():
        G.add_edge(u,v,strength=d["strength"],processes="+".join(d["processes"]))
    nets[b]=G
    # core->mantle->crust backbone always present structurally
rows=[]
for b,G in nets.items():
    comps=sorted(nx.connected_components(G),key=len,reverse=True)
    lcc=len(comps[0]) if comps else 0
    rows.append(dict(body=b, nodes=G.number_of_nodes(), edges=G.number_of_edges(),
        density=nx.density(G), n_components=len(comps), lcc=lcc,
        fragmentation=(G.number_of_nodes()-lcc)/max(G.number_of_nodes(),1)))
net=pd.DataFrame(rows); net.to_csv(os.path.join(DER,"network_metrics.csv"),index=False)
# process-level edge support count (0-7 per body, interpretable headline metric)
sup_cnt = m[m.current_activity_status.isin(SUPPORT)].groupby("body").size().reindex(BODIES)
net.set_index("body").assign(process_edges_supported=sup_cnt).to_csv(
    os.path.join(DER,"network_metrics.csv"))

# ---------------- Phase 10: energy architecture ----------------
eng=[]
for b in BODIES:
    e=BATTR[b]["energy"]
    eng.append(dict(body=b, **{k:(e[k] if e[k] else np.nan) for k in e},
                    age=BATTR[b]["age"], mass=BATTR[b]["mass"]))
en=pd.DataFrame(eng)
domclass={"Earth":"radiogenic+primordial (mixed internal)+stellar",
          "Venus":"internal (poorly constrained)+strong stellar",
          "Mars":"internal (declining)+stellar","Moon":"relict internal+tidal",
          "Mercury":"internal (dynamo persists)+strong stellar",
          "Io":"tidal-dominated","Europa":"tidal+relict internal",
          "Titan":"stellar-atmospheric+internal ocean"}
en["architecture"]=en.body.map(domclass)
# dominant CIRCULATION-DRIVING energy source (driver of the process architecture),
# NOT dominant total energy input (which is stellar insolation for every body)
dom_driver={"Earth":"radiogenic+primordial","Venus":"internal+stellar",
            "Mars":"internal (declining)","Moon":"relict internal+tidal",
            "Mercury":"internal (dynamo persists)","Io":"tidal",
            "Europa":"tidal+internal","Titan":"stellar-atmospheric"}
en["dom_driver"]=en.body.map(dom_driver)
en.to_csv(os.path.join(DER,"energy_architecture.csv"),index=False)

# null comparisons: Spearman of supported-process count vs age, mass
from scipy.stats import spearmanr
actsum = sup_cnt.astype(float)
res_null={}
for var in ["age","mass"]:
    v = en.set_index("body").loc[BODIES,var]
    rho,p = spearmanr(v, actsum)
    res_null[var]=dict(rho=rho, p=p)
json.dump(res_null, open(os.path.join(DER,"null_correlations.json"),"w"), indent=2)

summary = dict(pca_explained=evr[:4].tolist(), loo=loo,
               persistence_spread=spread.to_dict(),
               spread_mc={r["body"]:[r["spread_med"],r["spread_lo"],r["spread_hi"]]
                          for r in mc},
               process_edges_supported=sup_cnt.astype(int).to_dict(),
               network=rows, null=res_null)
json.dump(summary, open(os.path.join(DER,"analysis_summary.json"),"w"),
          indent=2, default=float)
print(json.dumps({k:v for k,v in summary.items() if k!="network"}, indent=2, default=float))
print(net.to_string(index=False))
