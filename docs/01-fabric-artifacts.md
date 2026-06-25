# 01 · Create Fabric Artifacts

> **Mission Briefing** — Maya stands up the landing zone: a workspace and a
> lakehouse that will hold Lumina's customer, order, and product data.

## Step 1 — Create a workspace
1. Go to **https://app.fabric.microsoft.com**.
2. **Workspaces → New workspace**.
3. Name: `Lumina-Retail-Governance`. Assign a Fabric/Trial capacity. **Apply**.

## Step 2 — Create a Lakehouse
1. Inside the workspace: **+ New item → Lakehouse**.
2. Name: `LuminaLakehouse`. **Create**.
3. You now have two areas:
   - **Files** — raw landing zone (we'll upload CSVs here).
   - **Tables** — Delta tables that Purview will catalog.

## Step 3 — (Recommended) prepare the table load notebook
We'll load the synthetic CSVs into managed Delta tables so Purview sees clean,
typed tables named `customers`, `orders`, `products`.

- **+ New item → Notebook**, attach it to `LuminaLakehouse`.
- The load logic is in [`notebooks/load_to_lakehouse.py`](../notebooks/load_to_lakehouse.py).
  Paste its cells into the notebook (or import the file).

> You can also skip the notebook and use the lakehouse UI
> **Files → … → Load to Tables**, but the notebook gives you clean column types
> and is repeatable.

## Step 4 — What "good" looks like
After the next two docs you should have, in **LuminaLakehouse → Tables**:

| Table | Key sensitive columns |
|-------|-----------------------|
| `customers` | email, phone, national_id, credit_card_number, loyalty_number, date_of_birth |
| `orders` | order_id, loyalty_number, ship_to_email, product_sku |
| `products` | product_sku, supplier, list_price |

➡️ Next: [02 · Generate & load synthetic data](02-generate-synthetic-data.md)
