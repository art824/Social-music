"""Unit economics + 18-month projection for Social Music (venture model module).
Every input is labeled: measured / sourced / assumption. Re-run: python3 unit_economics.py"""

SCENARIOS = {
    # price: market anchors Emodo $49.99, generics $10-48, Tuneshine $199.99 (sourced, competitors module); chosen price = assumption
    "pessimista": dict(price=59, bom=30, assembly=4, tariff=0.25, freight=2.0, fulfil=8.0, returns=0.08, cac=40,
                      cf_backers=300, dtc_start=40, dtc_growth=0.00),
    "base":       dict(price=69, bom=22, assembly=3, tariff=0.20, freight=1.5, fulfil=7.0, returns=0.05, cac=25,
                      cf_backers=1000, dtc_start=100, dtc_growth=0.10),
    "otimista":   dict(price=79, bom=16, assembly=2.5, tariff=0.15, freight=1.0, fulfil=6.0, returns=0.03, cac=12,
                      cf_backers=2500, dtc_start=300, dtc_growth=0.15),
}
PAY_PCT, PAY_FIXED = 0.029, 0.30       # card processing, standard US online rate (sourced from general Stripe pricing, not re-checked)
CF_FEE = 0.05 + 0.04                   # crowdfunding platform 5% + processing ~3-5% (assumption based on Kickstarter's published model)
CF_CAC_SHARE = 0.5                     # crowdfunding backers cost half the DTC CAC (assumption, low)
FIXED_ONE_TIME = dict(fcc=5500, un383=1000, tooling=8000, prototypes=2000, legal=1500)  # FCC/UN38.3 = market-research Q5 ranges (low); rest assumption
MONTHLY_FIXED = 150                    # store + app accounts + tools (assumption); founder salary = 0 (flattering assumption)

def unit(s):
    factory = s["bom"] + s["assembly"]
    landed = factory * (1 + s["tariff"]) + s["freight"]
    var = landed + s["fulfil"] + s["price"] * (PAY_PCT + s["returns"]) + PAY_FIXED
    gm = s["price"] - var
    return factory, landed, var, gm, gm - s["cac"]

def projection(s):
    factory, landed, var, gm, _ = unit(s)
    cash, low, low_m, rows, breakeven = 0.0, 0.0, 0, [], None
    dtc = s["dtc_start"]
    for m in range(1, 19):
        inflow = outflow = 0.0
        units = 0
        if m <= 6:                                   # build & certify
            outflow += sum(FIXED_ONE_TIME.values()) / 6
        if m == 8:                                   # crowdfunding campaign closes: cash in, ads out
            inflow += s["cf_backers"] * s["price"] * (1 - CF_FEE)
            outflow += s["cf_backers"] * s["cac"] * CF_CAC_SHARE
        if m == 10:                                  # pay factory for backer units + 300 stock units
            outflow += (s["cf_backers"] + 300) * landed
        if m == 12:                                  # deliver backers
            outflow += s["cf_backers"] * (s["fulfil"] + s["price"] * s["returns"])
            units = s["cf_backers"]
        if m >= 13:                                  # direct sales (inventory bought each month at landed cost)
            units = round(dtc)
            inflow += units * s["price"]
            outflow += units * (var + s["cac"])
            dtc *= 1 + s["dtc_growth"]
        if m >= 7:
            outflow += MONTHLY_FIXED
        net = inflow - outflow
        cash += net
        if cash < low:
            low, low_m = cash, m
        if breakeven is None and m >= 13 and cash >= 0:
            breakeven = m
        rows.append((m, units, round(inflow), round(outflow), round(net), round(cash)))
    return rows, round(low), low_m, breakeven

if __name__ == "__main__":
    for name, s in SCENARIOS.items():
        factory, landed, var, gm, contrib = unit(s)
        print(f"\n=== {name} === price ${s['price']}")
        print(f"factory cost = BOM {s['bom']} + assembly {s['assembly']} = ${factory:.2f}")
        print(f"landed = {factory:.2f} x (1+{s['tariff']}) + freight {s['freight']} = ${landed:.2f}")
        print(f"variable/unit = landed + fulfilment {s['fulfil']} + price x (pay {PAY_PCT}+returns {s['returns']}) + {PAY_FIXED} = ${var:.2f}")
        print(f"gross profit/unit = {s['price']} - {var:.2f} = ${gm:.2f}  (margin {gm/s['price']:.0%})")
        print(f"contribution after CAC {s['cac']} = ${contrib:.2f}")
        fixed = sum(FIXED_ONE_TIME.values())
        print(f"one-time fixed = ${fixed}; break-even units on gross profit = {fixed/gm:.0f}" if gm > 0 else "gross profit <= 0")
        rows, low, low_m, be = projection(s)
        print(f"cash low point ${low} in month {low_m}; cumulative cash month 18 = ${rows[-1][5]}; cash-positive from month {be}")
        print("month | units | in | out | net | cumulative")
        for r in rows:
            print(" | ".join(str(x) for x in r))
