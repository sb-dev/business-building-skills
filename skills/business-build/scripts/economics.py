#!/usr/bin/env python3
"""Deterministic contribution and simple cash-schedule calculator.

Input JSON example:
{"currency":"GBP","unit":"engagement","period":"per engagement","revenue":2400,"variable_costs":{"delivery_labour":800,"payment_fee":50},"opening_cash":1000,"cash_receipts":[2400],"cash_obligations":[800,50]}
"""
import argparse, json, sys

def number(v, name):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError(f"{name} must be numeric")
    return float(v)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("input", nargs="?", help="JSON file; omit to read stdin")
    args=p.parse_args()
    data=json.load(open(args.input, encoding="utf-8")) if args.input else json.load(sys.stdin)
    for key in ("currency","unit","period","revenue","variable_costs"):
        if key not in data: raise ValueError(f"missing required field: {key}")
    if not isinstance(data["variable_costs"], dict): raise ValueError("variable_costs must be an object")
    revenue=number(data["revenue"],"revenue")
    costs={k:number(v,f"variable_costs.{k}") for k,v in data["variable_costs"].items()}
    variable_total=sum(costs.values())
    out={"currency":data["currency"],"unit":data["unit"],"period":data["period"],"revenue":revenue,"variable_costs":costs,"variable_cost_total":variable_total,"contribution":revenue-variable_total}
    if any(k in data for k in ("opening_cash","cash_receipts","cash_obligations")):
        opening=number(data.get("opening_cash",0),"opening_cash")
        receipts=[number(v,"cash_receipts[]") for v in data.get("cash_receipts",[])]
        obligations=[number(v,"cash_obligations[]") for v in data.get("cash_obligations",[])]
        out["cash"]={"opening":opening,"receipts_total":sum(receipts),"obligations_total":sum(obligations),"closing":opening+sum(receipts)-sum(obligations)}
    json.dump(out, sys.stdout, indent=2, sort_keys=True); print()

if __name__=="__main__":
    try: main()
    except (ValueError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(2)
