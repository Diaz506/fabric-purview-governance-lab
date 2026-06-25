# 05 · Custom Classification Rules

> **Mission Briefing** — Built-in classifications catch email and credit cards,
> but only Maya knows what a Lumina **loyalty number** or **SKU** looks like. She
> teaches Purview with custom rules.

Full pattern reference (regex, column patterns, thresholds, local test):
[`classifications/custom-classification-rules.md`](../classifications/custom-classification-rules.md).

## Step 1 — Create the custom classifications
**Data Map → Annotation management → Classifications → New**. Create three:
| Classification name | Description |
|---------------------|-------------|
| `Lumina Loyalty Number` | Rewards member identifier |
| `Lumina Product SKU` | Catalog stock keeping unit |
| `Lumina Order ID` | Order transaction identifier |

## Step 2 — Create matching classification rules
**Data Map → Annotation management → Classification rules → New** (type:
*Regular expression*). One rule per classification:

| Rule | Data pattern (regex) | Column pattern (regex) | Threshold |
|------|----------------------|------------------------|-----------|
| Loyalty Number | `LUM-\d{8}` | `(?i)(loyalty[_ ]?(number\|num\|id))` | 60% |
| Product SKU | `SKU-[A-Z]{3}-\d{5}` | `(?i)(sku\|product[_ ]?code)` | 60% |
| Order ID | `ORD-\d{10}` | `(?i)(order[_ ]?id)` | 60% |

Attach each rule to its classification from Step 1.

## Step 3 — Add the rules to a scan rule set
1. **Data Map → Annotation management → Scan rule sets → New** (source type Fabric),
   or edit the default.
2. Under **custom classification rules**, enable the three Lumina rules.
3. Save as `Lumina-Retail-Ruleset`.

## Step 4 — Re-scan with the custom rule set
1. Go to the Fabric source → **New scan** (or edit the existing scan).
2. Select **Scan rule set = `Lumina-Retail-Ruleset`**.
3. **Run**.

## Step 5 — Verify custom classifications
After the scan completes, open:
- `customers.loyalty_number` → should show **Lumina Loyalty Number**.
- `products.product_sku` / `orders.product_sku` → **Lumina Product SKU**.
- `orders.order_id` → **Lumina Order ID**.

> If a custom rule doesn't fire: lower the threshold to 50%, confirm the column
> pattern matches the actual column name, and re-run.

➡️ Next: [06 · Run the demo](06-run-the-demo.md)
