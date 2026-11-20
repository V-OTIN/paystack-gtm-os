import json

COMPETITORS = ["Flutterwave", "Monnify", "Interswitch", "Remita"]


def handler(context):
    bw = context.get_input("builtwith")
    entry = (context.get_input("entry_type") or "").strip().lower()
    techs = []
    if isinstance(bw, dict):
        techs = bw.get("matchesFound") or []
    blob = json.dumps(bw).lower() if bw else ""

    if not bw or not techs:
        return {"gateway_status": "no_data", "gateway_name": "", "route": "needs_research", "cell": "",
                "route_reason": "BuiltWith returned no technologies for this domain. Check the site by hand."}
    if "paystack" in blob:
        return {"gateway_status": "paystack", "gateway_name": "Paystack", "route": "drop_paystack", "cell": "",
                "route_reason": "Paystack detected on the site (spec exclusion X1)."}
    name = next((c for c in COMPETITORS if c.lower() in blob), "")
    status = "competitor" if name else "none_detected"
    if entry == "new":
        cell = "A" if name else "B"
    else:
        cell = "C" if name else "D"
    reason = ("Competitor gateway on site: " + name + "." if name else "No payment gateway visible on the site.") + \
        " " + "Technologies found: " + str(len(techs)) + ". Cell " + cell + "."
    return {"gateway_status": status, "gateway_name": name, "route": "ready_for_review", "cell": cell,
            "route_reason": reason}
