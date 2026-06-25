# 03 · Register & Scan Fabric in Purview

> **Mission Briefing** — Maya connects Purview to Fabric so the lakehouse tables
> appear in the catalog and can be scanned for sensitive data.

## Step 0 — One-time tenant enablement
A Fabric **tenant admin** must allow Purview to read Fabric metadata:
- Fabric **Admin portal → Tenant settings** → enable Purview connectivity
  (a.k.a. "Microsoft Purview can connect…" / admin read-only APIs).
- For cross-tenant or service-principal scans, also configure a **Microsoft
  Purview managed identity** or app registration with Power BI/Fabric access.

## Step 1 — Register the Fabric source
In the Purview (Data Map) portal:
1. **Data Map → Sources → Register**.
2. Choose **Fabric** (formerly "Power BI").
3. Provide the **tenant ID**. Pick **Same tenant** (typical) or **Cross tenant**.
4. Assign it to a collection (e.g., `Lumina`). **Register**.

## Step 2 — Create a scan
1. On the registered Fabric source, click **New scan**.
2. Choose the authentication method:
   - **Managed identity** (recommended), or **service principal**.
   - Ensure that identity has the tenant access granted in Step 0.
3. Scope the scan to the `Lumina-Retail-Governance` workspace if scoping is offered.
4. **Scan rule set**: start with the **system default** (includes all built-in
   classifications). You'll attach custom rules in doc 05.
5. Set a **trigger** (Once is fine for the demo). **Save and run**.

## Step 3 — Watch the scan complete
- Monitor under the source's **Scans** tab until status = **Completed**.
- A first scan of a small lakehouse typically finishes in a few minutes.

## Step 4 — Browse the assets
1. **Data Catalog / Unified Catalog → Browse by source** → your Fabric workspace.
2. Drill into `LuminaLakehouse` → tables `customers`, `orders`, `products`.
3. Open `customers` and check the **Schema** tab — Purview should already show
   built-in classifications such as **Email Address**, **Credit Card Number**,
   and **U.S. SSN** on the relevant columns.

> If classifications are missing, confirm the columns hold realistic patterns and
> that the default scan rule set was used. Re-run the scan after fixes.

➡️ Next: [04 · Create glossary terms](04-glossary-terms.md)
