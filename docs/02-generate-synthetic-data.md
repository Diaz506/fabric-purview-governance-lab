# 02 · Generate & Load Synthetic Data

> **Mission Briefing** — No real customers are harmed in this demo. Maya
> generates fully synthetic, PII-shaped data so Purview has something to classify.

## Step 1 — Generate the CSVs locally
From the repo root:

```powershell
python data\generate_synthetic_data.py --rows 500 --products 120 --out out
```

Output (in `.\out`):
- `customers.csv` — 500 rows
- `orders.csv` — 1,500 rows
- `products.csv` — 120 rows

All values are synthetic. Credit-card values are public **test** numbers, not real
cards. Adjust `--rows` for a bigger demo.

## Step 2 — Upload to the Lakehouse Files area
1. Open `LuminaLakehouse` in Fabric.
2. **Files → … (right-click) → Upload → Upload files**.
3. Upload the three CSVs into a folder named `raw`.

## Step 3 — Load Files → Delta Tables
**Option A — Notebook (recommended):**
Run [`notebooks/load_to_lakehouse.py`](../notebooks/load_to_lakehouse.py) cells.
It reads each CSV from `Files/raw/` and writes managed tables `customers`,
`orders`, `products` with inferred types.

**Option B — UI:**
For each CSV: **Files/raw → right-click the file → Load to Tables → New table**,
keep the suggested name.

## Step 4 — Verify
In **Tables**, you should see `customers`, `orders`, `products`. Open `customers`
and confirm columns like `email`, `national_id`, `loyalty_number` are present.

> 🔎 Tip: a row count and a quick preview now makes the later Purview scan results
> easy to explain in the demo.

➡️ Next: [03 · Register & scan Fabric in Purview](03-purview-register-scan.md)
