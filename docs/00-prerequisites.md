# 00 · Prerequisites

> **Mission Briefing** — Before data steward **Maya Chen** can govern Lumina
> Retail's data, she needs the right accounts, licenses, and permissions in place.

## Accounts & licenses
- **Microsoft Fabric** capacity (Trial works) with permission to create a workspace.
- **Microsoft Purview** account. Either:
  - The **new Microsoft Purview portal** (Unified Catalog + Data Map), or
  - A classic **Purview / Microsoft Purview governance** account with a Data Map.
- An **Entra ID** account that is a member of the Fabric tenant.

## Required roles / permissions
| Task | Role needed |
|------|-------------|
| Create Fabric workspace, lakehouse | Fabric **Admin/Member** on the workspace |
| Let Purview scan Fabric | Tenant **"Microsoft Purview can connect to Power BI/Fabric"** tenant setting enabled |
| Register & scan source | Purview **Data Source Administrator** + **Data Reader** on the collection |
| Create glossary terms | Purview **Data Curator** on the collection / governance domain |
| Create classifications & rules | Purview **Data Curator** (or Classification admin) |

## Tenant setting for Fabric → Purview
A Fabric/Power BI **tenant admin** must enable, in the Fabric Admin portal:
- **Admin API settings → "Microsoft Purview can connect to this tenant"** (or the
  equivalent "Allow service principals / Purview to access read-only admin APIs").

## Local tooling (for synthetic data)
- **Python 3.10+** (no third-party packages required).
- Git + the **GitHub CLI** (`gh`) if you want to clone/push this repo.

## What you'll build
1. A Fabric **workspace** + **lakehouse** with `customers`, `orders`, `products` tables.
2. A Purview **scan** of that Fabric source.
3. A **glossary** of 14 retail terms.
4. **Custom classification rules** for loyalty numbers, SKUs, and order IDs.
5. A guided **demo** mapping terms + classifications onto the scanned assets.

➡️ Next: [01 · Create Fabric artifacts](01-fabric-artifacts.md)
