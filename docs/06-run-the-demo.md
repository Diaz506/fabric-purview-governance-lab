# 06 · Run the Demo

> **Mission Briefing** — Everything is in place. Time for Maya to tell the
> governance story to stakeholders in ~10 minutes.

## Talk track (suggested 10-minute flow)

### 1. The problem (1 min)
"Lumina Retail lands customer, order, and product data in Fabric. Nobody agrees
on definitions, and we don't know where sensitive data lives."

### 2. The catalog (2 min)
- Show **Data Catalog → LuminaLakehouse** with `customers`, `orders`, `products`.
- Open `customers` **Schema**: point out auto-detected **Email**, **Credit Card**,
  **U.S. SSN** classifications. "Purview found these automatically."

### 3. Custom classifications (2 min)
- Show `loyalty_number` → **Lumina Loyalty Number**, `product_sku` → **Lumina
  Product SKU**, `order_id` → **Lumina Order ID**.
- "We taught Purview our own identifiers with regex rules."

### 4. Business glossary (2 min)
- Open the **Glossary**; show the hierarchy
  **Customer → Loyalty Member → Loyalty Number**.
- Open a term, show definition + steward (**Maya Chen**).

### 5. Tie it together (2 min)
- On `customers.loyalty_number`, **link the glossary term** *Loyalty Number*
  to the column (Schema → column → Edit → Glossary terms).
- "Now a business definition, a data owner, and a sensitivity classification all
  live on the same column."

### 6. Why it matters (1 min)
- **Privacy**: PII and Payment Card columns are flagged for PCI/GDPR scope.
- **Discovery**: anyone can search 'loyalty number' and find the authoritative column.
- **Stewardship**: every key term has an owner.

## Demo checklist
- [ ] Lakehouse tables loaded (`customers`, `orders`, `products`)
- [ ] Scan completed with built-in + custom classifications visible
- [ ] 14 glossary terms imported and approved
- [ ] At least one glossary term linked to a scanned column
- [ ] Saved searches / screenshots captured as a backup

## Reset / cleanup
- Delete the Fabric **workspace** `Lumina-Retail-Governance` to remove the lakehouse.
- In Purview, remove the **scan**, **source**, custom **classifications/rules**,
  and **glossary terms** if you want a clean slate.

## Extend the demo
- Add **sensitivity labels** (Microsoft Purview Information Protection) on top of
  classifications.
- Add a **DLP** or **access policy** scenario for the `national_id` column.
- Show **lineage** by adding a Fabric pipeline/dataflow that derives a curated
  table from `orders`.
