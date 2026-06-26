# 04 · Create Glossary Terms

> **Mission Briefing** — Maya gives Lumina a shared business vocabulary so
> "loyalty number" means the same thing to marketing, finance, and engineering.

The repo ships a ready-to-import glossary:
[`glossary/retail-glossary-terms-import.csv`](../glossary/retail-glossary-terms-import.csv)
— 14 terms covering Customer, Order, Product, and Sensitive Data concepts with a
small hierarchy (e.g., `Loyalty Number` → parent `Loyalty Member` → parent `Customer`).

## Option A — Bulk import (classic Data Map glossary)
1. **Data Map → Glossary**.
2. **Import terms** → download the **sample template** once to confirm the column
   order matches your tenant's term template.
3. Upload `retail-glossary-terms-import.csv`.
   - Columns: `Name, Status, Definition, Acronym, Resources, Related Terms,
     Synonyms, Stewards, Experts, Parent Term Name`.
   - Multi-valued fields use `;` as the separator (e.g., `Customer;Order`).
4. Map columns if prompted, then **Import**. Resolve any steward email warnings
   (the sample uses `@lumina.example`; swap for real users or clear the column).

## Option B — Unified Catalog (new Purview portal)
The new portal organizes terms under a **governance domain** and uses a
**different CSV template** than the classic Data Map glossary. Its sample
template columns are: `name, description, owners, experts, acronyms, resources`.
Use the matching file
[`glossary/unified-catalog-terms-import.csv`](../glossary/unified-catalog-terms-import.csv).
1. **Unified Catalog → Governance domains → New** → `Lumina Retail`.
2. Inside the domain, **Glossary → Bulk import** → download the sample template
   once to confirm the column order, then upload `unified-catalog-terms-import.csv`.
   - `owners`/`experts` must be **real users in your tenant**. The sample uses
     `@lumina.example` placeholders — swap them for real users or clear the
     column, otherwise the import fails on user validation.
   - This template has no parent/related/synonyms columns, so set the term
     **hierarchy** (e.g., `Loyalty Number` → `Loyalty Member` → `Customer`) in
     the portal after import (or use Option A to import hierarchy directly).
3. Assign **owners/stewards** and set status to **Published/Approved**.

## Option C — Create a few by hand (fastest for a live demo)
Create these 4 to show the concept, then mention the CSV for the full set:
- **Customer**, **Loyalty Number** (child of Loyalty Member), **PII**, **SKU**.

## Verify
- Glossary shows 14 approved terms.
- Open **Loyalty Number** → confirm its **parent** is **Loyalty Member** and it
  lists a steward.

➡️ Next: [05 · Custom classification rules](05-classification-rules.md)
