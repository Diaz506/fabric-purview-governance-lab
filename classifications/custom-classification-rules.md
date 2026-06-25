# Custom Classification Rules — Lumina Retail Co.

Microsoft Purview ships with 200+ **built-in** classifications (email, phone,
credit card, U.S. SSN, etc.). The synthetic dataset is designed so several of
these fire automatically. On top of those, this lab defines **custom**
classification rules for retailer-specific identifiers.

---

## 1. Built-in classifications you will see (no setup required)

| Column | Built-in classification expected |
|--------|----------------------------------|
| `email`, `ship_to_email` | Email Address |
| `phone` | U.S. Phone Number |
| `national_id` | U.S. Social Security Number (SSN) |
| `credit_card_number` | Credit Card Number |
| `date_of_birth` | Date of Birth |
| `postal_code`, `ship_to_postal_code` | U.S. ZIP Code |

> These require no configuration — they apply during a scan automatically.

---

## 2. Custom classification rules to create

Create these in the Purview portal under
**Data Map → Annotation management → Classifications → New custom classification**,
then a matching **Classification rule** (type: *Regular expression*).

### 2.1 Lumina Loyalty Number
| Field | Value |
|-------|-------|
| Classification name | `Lumina Loyalty Number` |
| Friendly description | Lumina Rewards member identifier |
| Rule type | Regular expression |
| **Data pattern (regex)** | `LUM-\d{8}` |
| **Column pattern (regex)** | `(?i)(loyalty[_ ]?(number|num|id))` |
| Minimum match threshold | 60% |
| Applies to columns | `customers.loyalty_number`, `orders.loyalty_number` |

### 2.2 Lumina Product SKU
| Field | Value |
|-------|-------|
| Classification name | `Lumina Product SKU` |
| Rule type | Regular expression |
| **Data pattern (regex)** | `SKU-[A-Z]{3}-\d{5}` |
| **Column pattern (regex)** | `(?i)(sku|product[_ ]?code)` |
| Minimum match threshold | 60% |
| Applies to columns | `products.product_sku`, `orders.product_sku` |

### 2.3 Lumina Order ID
| Field | Value |
|-------|-------|
| Classification name | `Lumina Order ID` |
| Rule type | Regular expression |
| **Data pattern (regex)** | `ORD-\d{10}` |
| **Column pattern (regex)** | `(?i)(order[_ ]?id)` |
| Minimum match threshold | 60% |
| Applies to columns | `orders.order_id` |

---

## 3. Regex quick-test

Validate the patterns locally before entering them in Purview:

```powershell
python - <<'PY'
import re
samples = {
  r"LUM-\d{8}": "LUM-04827193",
  r"SKU-[A-Z]{3}-\d{5}": "SKU-QРX-00421".replace("Р","P"),
  r"ORD-\d{10}": "ORD-0000539182",
}
for pat, val in samples.items():
    print(f"{pat:20} {val:18} -> {bool(re.fullmatch(pat, val))}")
PY
```

(On Windows PowerShell, prefer running the equivalent `re` checks via a saved
`.py` file — PowerShell has no heredoc.)

---

## 4. How custom rules differ from built-ins

* **Data pattern** matches the *values* in a column sample.
* **Column pattern** (optional) boosts confidence when the *column name* matches.
* **Minimum match threshold** is the % of sampled rows that must match for the
  classification to be applied to the column.
* A scan applies the first custom rule that meets threshold; keep patterns
  specific to avoid collisions with built-ins.

See `docs/05-classification-rules.md` for the click-through steps.
