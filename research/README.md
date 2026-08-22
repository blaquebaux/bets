# Blaque Baux Bets — research

Is the gambling complex a durable "house always wins" premium or just levered consumer discretionary? Pure
prediction markets (Kalshi/Polymarket) are private; the testable surface is listed books + casinos + `BETZ`
vs `SPY`/`XLY`. Read-only Alpaca SIP bars. Verdicts use the fat-tail toolkit
([`_bets_common.py`](_bets_common.py): Jarque-Bera + Jensen's alpha + M²).

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
# python research/bets_1_sector.py       # [to build] gambling basket vs SPY/XLY: beta, Jensen α, M², JB
# python research/bets_2_vice_momentum.py # [to build] sin premium + trend, net of vol
```

## Planned scorecard

| # | Question | Metric | Status |
|---|----------|--------|--------|
| 1 | Distinct sector premium, or levered discretionary? | beta vs XLY, Jensen's α, M², JB | ☐ to build |
| 2 | Vice premium + tradeable momentum? | factor + trend, net of cost | ☐ to build |

**The prior:** high-beta discretionary with a secular legalization tailwind but heavy promotional cash burn
— likely more beta than premium; the data decides.

## Status
**[Concept] — plan defined, no sketches run.** Boundary set (prediction markets private; listed
books/casinos + `BETZ` testable). Next: sketch #1 (sector characterization) and #2 (vice/momentum).
