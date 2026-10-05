#!/usr/bin/python3
# =============================================================================
# bets_1_house_premium.py — is there a "house premium" for EQUITY holders, or just consumer-discretionary beta?
# The gambling complex is +EV for the house — but does owning the house (BETZ / casinos / books) earn alpha,
# or is it just high-beta consumer discretionary dressed up? Test: the gaming basket + BETZ vs SPY AND vs XLY.
# If alpha ≈ 0 once you control for XLY (consumer-disc) beta, the "house edge" never reaches the shareholder.
# =============================================================================
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bets_common import panel, rets, riskadj, jensens_alpha
import numpy as np

CASI=["MGM","LVS","WYNN","CZR","BYD","PENN"]; BOOK=["DKNG","FLUT","RSI","GENI"]
P,dates=panel(["BETZ"]+CASI+BOOK+["SPY","XLY"])
R={s:rets(P[s]) for s in P}
def basket(names):
    have=[s for s in names if s in R];
    if not have: return None
    n=min(len(R[s]) for s in have); return np.mean(np.vstack([R[s][-n:] for s in have]),axis=0)
print("="*90); print(f"BETS — house premium or consumer beta?  ({dates[0]} → {dates[-1]}, {len(dates)} days)"); print("="*90)
spy=R["SPY"]; xly=R.get("XLY")
print(f"\n  {'':12}{'Sharpe':>8}{'CAGR':>8}{'maxDD':>8}{'β/SPY':>7}{'α/SPY':>9}{'α/XLY':>9}")
def line(nm,r):
    if r is None: return None
    m=min(len(r),len(spy)); a=riskadj(r[-m:],spy[-m:]); axly=jensens_alpha(r[-m:],xly[-len(r[-m:]):])["alpha_ann"] if xly is not None else float('nan')
    print(f"  {nm:12}{a['sh']:>+8.2f}{a['cagr']*100:>+7.0f}%{a['dd']*100:>+7.0f}%{a['beta']:>+7.2f}{a['alpha_ann']*100:>+8.1f}%{axly*100:>+8.1f}%")
    return a['alpha_ann'], axly
res={}
res["BETZ"]=line("BETZ",R.get("BETZ")); res["casinos"]=line("casinos",basket(CASI)); res["books"]=line("books",basket(BOOK))
# verdict: does any leg keep POSITIVE alpha after controlling for consumer-disc (XLY) beta?
keeps=[k for k,v in res.items() if v and np.isfinite(v[1]) and v[1]>0.01]
if keeps: verdict=f"CONDITIONAL: {', '.join(keeps)} retain positive alpha even vs XLY — a sliver of real house premium reaches holders there."
else:     verdict="NULL-ish: once you control for consumer-discretionary (XLY) beta, the house edge does NOT reach the equity holder — gaming names are high-beta XLY, not an alpha source. The house wins; the shareholder just rides consumer beta."
print(f"\n  VERDICT: {verdict}")
print("  (Books carry a short, volatile sample — DKNG/FLUT/RSI/GENI listed 2020-24; read their legs with that caveat.)")
