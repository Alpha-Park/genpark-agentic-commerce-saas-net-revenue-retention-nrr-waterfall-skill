# genpark-agentic-commerce-saas-net-revenue-retention-nrr-waterfall-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Enterprise SaaS ARR cohort renewal, expansion, contraction, churn waterfall and Net Revenue Retention calculator.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `compute_saas_nrr_waterfall`
- **Category**: `agentic_commerce`

### Method Documentation
Compute Enterprise SaaS ARR revenue bridge waterfall, Net Revenue Retention (NRR), and Gross Revenue Retention (GRR).
Calculates starting cohort ARR, expansion ARR, contraction ARR, churned ARR, and new customer ARR.
Evaluates Rule of 40 and benchmark health metrics against top-quartile public SaaS companies.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "compute_saas_nrr_waterfall",
    "arguments": {
    "starting_cohort_arr": 5000000.0,
    "expansion_arr": 950000.0,
    "contraction_arr": 150000.0,
    "churn_arr": 200000.0,
    "new_logo_arr": 1200000.0
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
