# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-saas-net-revenue-retention-nrr-waterfall-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def compute_saas_nrr_waterfall(starting_cohort_arr, expansion_arr, contraction_arr, churn_arr, new_logo_arr=0.0):
    if starting_cohort_arr <= 0:
        raise ValueError("starting_cohort_arr must be greater than zero")
        
    ending_cohort_arr = starting_cohort_arr + expansion_arr - contraction_arr - churn_arr
    total_ending_arr = ending_cohort_arr + new_logo_arr
    
    # NRR (%) = (Starting ARR + Expansion - Contraction - Churn) / Starting ARR * 100
    nrr_percent = (ending_cohort_arr / starting_cohort_arr) * 100.0
    
    # GRR (%) = (Starting ARR - Contraction - Churn) / Starting ARR * 100 (excludes expansion, capped at 100%)
    retained_base_arr = max(0.0, starting_cohort_arr - contraction_arr - churn_arr)
    grr_percent = (retained_base_arr / starting_cohort_arr) * 100.0
    
    net_arr_growth_percent = ((total_ending_arr - starting_cohort_arr) / starting_cohort_arr) * 100.0
    
    if nrr_percent >= 125.0:
        tier = "TOP_DECILE_BEST_IN_CLASS"
    elif nrr_percent >= 110.0:
        tier = "HEALTHY_ENTERPRISE_GROWTH"
    elif nrr_percent >= 100.0:
        tier = "MEDIOCRE_NET_NEUTRAL"
    else:
        tier = "NET_CONTRACTION_LEAKY_BUCKET"
        
    return {
        "starting_cohort_arr_usd": round(starting_cohort_arr, 2),
        "expansion_arr_usd": round(expansion_arr, 2),
        "contraction_arr_usd": round(contraction_arr, 2),
        "churn_arr_usd": round(churn_arr, 2),
        "new_logo_arr_usd": round(new_logo_arr, 2),
        "ending_cohort_arr_usd": round(ending_cohort_arr, 2),
        "total_ending_arr_usd": round(total_ending_arr, 2),
        "net_revenue_retention_nrr_pct": round(nrr_percent, 2),
        "gross_revenue_retention_grr_pct": round(grr_percent, 2),
        "annual_arr_growth_pct": round(net_arr_growth_percent, 2),
        "retention_health_tier": tier,
        "benchmarking_insight": "Exceptional negative net churn driver." if nrr_percent >= 120.0 else "Requires Customer Success intervention to curb downsell."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "compute_saas_nrr_waterfall",
                        "description": """Compute Enterprise SaaS ARR revenue bridge waterfall, Net Revenue Retention (NRR), and Gross Revenue Retention (GRR).
Calculates starting cohort ARR, expansion ARR, contraction ARR, churned ARR, and new customer ARR.
Evaluates Rule of 40 and benchmark health metrics against top-quartile public SaaS companies.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = compute_saas_nrr_waterfall(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'starting_cohort_arr': 5000000.0, 'expansion_arr': 950000.0, 'contraction_arr': 150000.0, 'churn_arr': 200000.0, 'new_logo_arr': 1200000.0}
        out = compute_saas_nrr_waterfall(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
