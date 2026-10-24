#!/usr/bin/env python3
"""Derive measurement_dictionary.csv, activity/persistence/observability matrices,
and coverage-gate statistics from the master table."""
import pandas as pd, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "data", "processed")
m = pd.read_csv(os.path.join(DATA, "planetary_circulation_master.csv"))

# ---- measurement dictionary (Phase 2): interpretive annotation per cell
interp = {
 ("Earth","E1"):("magma flux","measured eruption/emplacement rates","km3/yr","high"),
 ("Earth","E2"):("plate recycling","plate velocity & seismicity","cm/yr","high"),
 ("Earth","E3"):("hydrologic flux","global evaporation","km3/yr","high"),
 ("Earth","E4"):("fluid exchange","hydrothermal heat/water flux","W, kg/s","medium"),
 ("Earth","E5"):("deposition flux","dust emission/deposition","kg/yr","high"),
 ("Earth","E6"):("escape flux","H/He escape","kg/s","medium"),
 ("Earth","E7"):("redox flux","photosynthetic O2/C cycle","mol/yr","high"),
 ("Venus","E1"):("volcanic resurfacing","SAR change+SO2 transient","rate unknown","medium"),
 ("Venus","E2"):("deformation","young rifts/tesserae","-","low"),
 ("Venus","E3"):("surface-atmosphere exchange","chemical weathering","-","low"),
 ("Venus","E4"):("none (no subsurface liquid)","-","-","absent"),
 ("Venus","E5"):("aerosol deposition","H2SO4 cycle","-","medium"),
 ("Venus","E6"):("ion escape","measured ion flux","s-1","high"),
 ("Venus","E7"):("photochemistry","SO2 cycle","-","medium"),
 ("Mars","E1"):("recent volcanism","youngest unit ages","Ga","medium"),
 ("Mars","E2"):("seismicity","marsquake catalog","count/rate","high"),
 ("Mars","E3"):("CO2 cycle","seasonal polar exchange","fraction atm","high"),
 ("Mars","E4"):("deep groundwater","seismic inference","-","low"),
 ("Mars","E5"):("dust deposition","opacity/dune tracking","-","high"),
 ("Mars","E6"):("escape","MAVEN measured fluxes","s-1","high"),
 ("Mars","E7"):("photochemistry","perchlorate/O2 cycle","-","medium"),
 ("Moon","E1"):("volcanism","youngest basalt ages","Ga","high"),
 ("Moon","E2"):("contraction tectonics","moonquakes+scarps","-","high"),
 ("Moon","E3"):("exosphere migration","OH/H2O diurnal","-","medium"),
 ("Moon","E4"):("none","-","-","absent"),
 ("Moon","E5"):("n/a (no atmosphere)","-","-","absent"),
 ("Moon","E6"):("sputtering","exosphere species","-","medium"),
 ("Moon","E7"):("space weathering","optical maturity","-","low"),
 ("Mercury","E1"):("volcanism","youngest plains age ~3.5 Ga","Ga","high"),
 ("Mercury","E2"):("contraction","young graben <300 Ma","Ma","medium"),
 ("Mercury","E3"):("volatile sublimation","hollows activity","-","medium"),
 ("Mercury","E4"):("none","-","-","absent"),
 ("Mercury","E5"):("exosphere deposition","Na cycle","-","medium"),
 ("Mercury","E6"):("sputtering/magnetospheric","FIPS/MASCS","-","high"),
 ("Mercury","E7"):("space weathering","hollows","-","low"),
 ("Io","E1"):("volcanic heat flow","global mean flux","W/m2","high"),
 ("Io","E2"):("resurfacing","cm/yr burial","cm/yr","high"),
 ("Io","E3"):("SO2 cycle","diurnal atmosphere","-","high"),
 ("Io","E4"):("none (no volatile reservoir; melt layer is E1 evidence)","-","-","absent"),
 ("Io","E5"):("plume fallout","deposit maps","-","high"),
 ("Io","E6"):("torus supply","~1 t/s","kg/s","high"),
 ("Io","E7"):("sulfur cycling","photochemistry","-","low"),
 ("Europa","E1"):("cryovolcanism","plume detections contested","-","low"),
 ("Europa","E2"):("ice tectonics","surface age 40-90 Myr","Myr","high"),
 ("Europa","E3"):("exosphere exchange","O2 sputter atmosphere","-","medium"),
 ("Europa","E4"):("ocean-ice exchange","induction+chaos models","-","medium"),
 ("Europa","E5"):("radiolytic deposition","hydrate mapping","-","medium"),
 ("Europa","E6"):("sputtering","exosphere loss","-","medium"),
 ("Europa","E7"):("oxidant cycle","models","-","low"),
 ("Titan","E1"):("cryovolcanism","morphology disputed","-","low"),
 ("Titan","E2"):("tectonics","graben/ridges","-","low"),
 ("Titan","E3"):("methane cycle","lakes/rain/evap","-","high"),
 ("Titan","E4"):("ocean-shell exchange","Love k2 gravity","-","medium"),
 ("Titan","E5"):("haze deposition","dunes/haze flux","kg/Myr","high"),
 ("Titan","E6"):("escape","INMS fluxes","amu/s","high"),
 ("Titan","E7"):("photochemistry","INMS/CIRS products","-","high"),
}
rows=[]
for _,r in m.iterrows():
    iv = interp.get((r.body, r.edge_id), ("","","","unknown"))
    rows.append(dict(body=r.body, edge_id=r.edge_id, process_name=r.process_name,
        ideal_variable=iv[0], attainable_variable=iv[1], unit=iv[2],
        expected_tier=r.measurement_tier, expected_observability=r.observability_class,
        cross_body_comparable=iv[3],
        current_state_interpretation=r.current_activity_status,
        persistence_interpretation=("right-censored: active today" if r.currently_active else
            f"ceased/none; last activity {r.last_major_activity_age_Gyr} Ga"),
        principal_uncertainty=(r.notes if isinstance(r.notes,str) else ""),
        primary_reference=r.primary_reference if isinstance(r.primary_reference,str) else ""))
pd.DataFrame(rows).to_csv(os.path.join(DATA,"measurement_dictionary.csv"), index=False)

# ---- matrices
def pivot(col):
    return m.pivot(index="body", columns="edge_id", values=col)[
        ["E1","E2","E3","E4","E5","E6","E7"]].reindex(
        ["Earth","Venus","Mars","Moon","Mercury","Io","Europa","Titan"])
act = pivot("current_activity_status")
obs = pivot("observability_class")
tier = pivot("measurement_tier")
# persistence fraction: active -> censored at 1.0 marker 'censored'; else (age-last_age)/age
pact = m.copy()
def pfrac(r):
    if r.currently_active==1: return 1.0  # right-censored at body age
    if pd.isna(r.last_major_activity_age_Gyr): return float("nan")
    return max(0.0, (r.body_age_Gyr - r.last_major_activity_age_Gyr)/r.body_age_Gyr)
pact["persistence_fraction"] = pact.apply(pfrac, axis=1)
pers = pact.pivot(index="body", columns="edge_id", values="persistence_fraction")[
    ["E1","E2","E3","E4","E5","E6","E7"]].reindex(act.index)

act.to_csv(os.path.join(DATA,"activity_matrix.csv"))
obs.to_csv(os.path.join(DATA,"observability_matrix.csv"))
tier.to_csv(os.path.join(DATA,"tier_matrix.csv"))
pers.to_csv(os.path.join(DATA,"persistence_matrix.csv"))

# ---- coverage gate
evaluable = m[~m.measurement_tier.isin(["D"]) ]
abc = (m.measurement_tier.isin(["A","B","C"])).sum()
bodies_ok = (evaluable.groupby("body").edge_id.nunique() >= 4).sum()
stats = dict(total_cells=len(m), tier_counts=m.measurement_tier.value_counts().to_dict(),
    abc_cells=int(abc), abc_frac=abc/len(m),
    quant_cells=int(m.current_activity_estimate.notna().sum()),
    bodies_with_ge4_evaluable=int(bodies_ok),
    gate="GO" if (abc/len(m)>=0.7 and bodies_ok>=5) else ("CONDITIONAL" if abc/len(m)>=0.5 else "NO-GO"))
json.dump(stats, open(os.path.join(DATA,"coverage_stats.json"),"w"), indent=2)
print(json.dumps(stats, indent=2))
print("\nActivity matrix:\n", act)
print("\nPersistence fractions:\n", pers.round(2))
