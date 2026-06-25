# Fabric → Purview Governance Lab

A small, story-driven demo that governs **Microsoft Fabric** data with
**Microsoft Purview** — business glossary terms, built-in classifications, and
custom classification rules — using fully **synthetic** retail data.

> **The story.** *Lumina Retail Co.* is a fictional omnichannel retailer. Data
> steward **Maya Chen** must bring order to customer, order, and product data
> landing in Fabric: shared definitions, known sensitive data, and clear owners.
> Each lab opens with a short **Mission Briefing**.

---

## What you'll build
1. **Fabric** workspace + lakehouse with `customers`, `orders`, `products` tables.
2. **Synthetic data** that is intentionally PII-rich and pattern-rich.
3. A **Purview scan** of the Fabric source.
4. A **business glossary** of 14 retail terms (with hierarchy + stewards).
5. **Custom classification rules** for loyalty numbers, SKUs, and order IDs.
6. A **10-minute demo talk track**.

## Labs
Work through the labs in order — each opens with a **Mission Briefing**:

| # | Lab | What you'll do |
|---|-----|----------------|
| 00 | [Prerequisites](docs/00-prerequisites.md) | Accounts, licenses, permissions |
| 01 | [Create Fabric artifacts](docs/01-fabric-artifacts.md) | Workspace + lakehouse |
| 02 | [Generate & load synthetic data](docs/02-generate-synthetic-data.md) | Generate CSVs, load Delta tables |
| 03 | [Register & scan Fabric in Purview](docs/03-purview-register-scan.md) | Register source, run a scan |
| 04 | [Create glossary terms](docs/04-glossary-terms.md) | Import 14 retail terms |
| 05 | [Custom classification rules](docs/05-classification-rules.md) | Loyalty number, SKU, order ID rules |
| 06 | [Run the demo](docs/06-run-the-demo.md) | 10-minute talk track |

## Repository layout
```
.
├── README.md
├── docs/
│   ├── 00-prerequisites.md          accounts, licenses, permissions
│   ├── 01-fabric-artifacts.md       create workspace + lakehouse
│   ├── 02-generate-synthetic-data.md generate + load CSVs
│   ├── 03-purview-register-scan.md  register Fabric source + scan
│   ├── 04-glossary-terms.md         create / import glossary
│   ├── 05-classification-rules.md   custom classification rules
│   └── 06-run-the-demo.md           demo script / talk track
├── data/
│   └── generate_synthetic_data.py   synthetic retail data generator (stdlib only)
├── notebooks/
│   └── load_to_lakehouse.py         Fabric notebook: CSV → Delta tables
├── glossary/
│   └── retail-glossary-terms-import.csv  Purview bulk-import template (14 terms)
└── classifications/
    └── custom-classification-rules.md    regex rules + thresholds + local test
```

## Quick start
```powershell
# 1. Generate synthetic data (no pip install needed)
# Always run it with `python` — do NOT run `.\generate_synthetic_data.py`
# directly on Windows (it can exit silently via the .py file association).
python data\generate_synthetic_data.py --rows 500 --products 120 --out out

# 2. Follow the docs in order
#    docs/00 → docs/06
```

## Demo at a glance
| Layer | What Purview shows |
|-------|--------------------|
| Built-in classifications | Email, Phone, Credit Card, U.S. SSN on `customers` |
| Custom classifications | Lumina Loyalty Number, Product SKU, Order ID |
| Glossary | Customer → Loyalty Member → Loyalty Number hierarchy |
| Stewardship | Each key term has an owner (Maya Chen et al.) |

## Synthetic data & safety
All data is generated locally and is entirely fictional. Credit-card values are
the public **Luhn-valid test numbers** published by payment providers — they are
**not** real cards. No real personal data is used anywhere in this lab.

## Cast
- **Maya Chen** — Data Steward / governance lead
- **Raj Patel** — Commerce data owner (orders, products)
- **Privacy Office & Security Team** — sensitive-data stewards

---
Built as a teaching lab. Start with [docs/00-prerequisites.md](docs/00-prerequisites.md).
