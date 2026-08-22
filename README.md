# Blaque Baux Bets

**The house always wins? Sports betting, casinos, and prediction markets as a sector.**

Bets is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Bets points that engine at the gambling
complex and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/bets.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Legalized US sports betting (post-2018) turned gambling into a fast-growing listed sector: online books
(`DKNG`, `FLUT`, `RSI`, `GENI`), casinos (`MGM`, `LVS`, `WYNN`, `CZR`, `BYD`, `PENN`), and the
retail-speculation adjacent (`HOOD`). The folk claim is "the house always wins" — a structural edge that
should compound. The honest question: is gambling a **distinct, durable sector premium**, or just a
**high-beta consumer-discretionary bet** that burns promotional cash and whipsaws with risk appetite?

**Data honesty — the pure prediction-market plays are private.** Kalshi and Polymarket (the prediction-market
core of the user's thesis) are **private** — no ticker, unobservable from bars — a stated gap. The listed
betting/casino names and the `BETZ` (Roundhill Sports Betting) ETF are the testable surface; `HOOD` stands
in, imperfectly, for listed retail-speculation flow.

## Research plan (Path A)

- **Is "the house wins" in the tape?** The betting/casino basket (and `BETZ`) vs `SPY`/`XLY`: beta, Jensen's
  alpha, M², Jarque-Bera. Distinct premium, or levered discretionary?
- **Vice premium & momentum.** Test the classic "sin stock" outperformance and whether the sector's strong
  trends are tradeable net of its high vol.
- **Cash-burn tell.** Separate the profitable operators (casinos) from the promotional cash-burners (online
  books pre-profitability) — is the "edge" real economics or subsidized growth?

## Status
**[Concept] — scaffolded, not yet built.** Thesis, data-honesty boundary (Kalshi/Polymarket private; listed
books/casinos + `BETZ` testable), and the Path-A plan are defined. Verdicts use the fat-tail toolkit
(Jarque-Bera + Jensen's alpha + M²) — apt for a skewed, high-beta sector. No research run yet; no live driver.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   _bets_common.py (loaders + JB/Jensen/M² toolkit) + sketches + scorecard  [to build]
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
