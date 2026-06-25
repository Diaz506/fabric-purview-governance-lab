#!/usr/bin/env python3
"""
Lumina Retail Co. — synthetic data generator for the Purview governance lab.

Generates three CSV files with intentionally PII-rich and pattern-rich columns so
that Microsoft Purview can demonstrate:
  * Built-in classifications  (email, phone, credit card, national ID, etc.)
  * Custom classification rules (loyalty number, SKU, order ID — see
    classifications/custom-classification-rules.md)
  * Glossary term mapping      (see glossary/retail-glossary-terms-import.csv)

Pure standard library — no pip install required.

Usage:
    python generate_synthetic_data.py --rows 500 --out ./out

All values are fully synthetic. Credit-card numbers are the public Luhn-valid
*test* numbers published by payment providers and are NOT real cards.
"""
from __future__ import annotations

import argparse
import csv
import os
import random
from datetime import date, datetime, timedelta

# -----------------------------------------------------------------------------
# Reference pools (all fictional)
# -----------------------------------------------------------------------------
FIRST_NAMES = [
    "Maya", "Liam", "Sofia", "Noah", "Aisha", "Diego", "Emma", "Kai", "Priya",
    "Lucas", "Yuki", "Omar", "Chloe", "Mateo", "Zara", "Ethan", "Ines", "Arjun",
    "Nora", "Hugo", "Lena", "Tariq", "Mila", "Felix", "Amara",
]
LAST_NAMES = [
    "Chen", "Garcia", "Okafor", "Novak", "Haddad", "Silva", "Nguyen", "Patel",
    "Rossi", "Kowalski", "Andersson", "Diaz", "Khan", "Tanaka", "Murphy",
    "Schmidt", "Costa", "Reyes", "Ivanov", "Bauer",
]
CITIES = [
    ("Seattle", "WA", "US", "98101"), ("Austin", "TX", "US", "73301"),
    ("Denver", "CO", "US", "80201"), ("Miami", "FL", "US", "33101"),
    ("Chicago", "IL", "US", "60601"), ("Boston", "MA", "US", "02108"),
    ("Portland", "OR", "US", "97201"), ("Atlanta", "GA", "US", "30301"),
]
STREETS = ["Maple Ave", "Oak St", "Pine Rd", "Cedar Ln", "Birch Way",
           "Elm Blvd", "Willow Ct", "Aspen Dr"]
CATEGORIES = ["Apparel", "Footwear", "Electronics", "Home", "Beauty",
              "Outdoor", "Toys", "Grocery"]
SUPPLIERS = ["NorthPeak Supply", "Vertex Goods", "Harbor Imports",
             "BrightLeaf Co.", "Summit Wholesale"]
PAYMENT_METHODS = ["credit_card", "paypal", "gift_card", "apple_pay"]

# Public Luhn-valid TEST card numbers (not real accounts).
TEST_CARDS = [
    "4111111111111111", "4012888888881881", "5555555555554444",
    "5105105105100100", "378282246310005", "6011111111111117",
]


def rand_email(first: str, last: str, i: int) -> str:
    domains = ["example.com", "mailtest.org", "demo-inbox.net"]
    return f"{first.lower()}.{last.lower()}{i % 97}@{random.choice(domains)}"


def rand_phone() -> str:
    return f"+1-{random.randint(200,989)}-{random.randint(200,989)}-{random.randint(1000,9999)}"


def rand_ssn() -> str:
    # Synthetic US SSN-shaped value to trigger built-in 'U.S. SSN' classification.
    return f"{random.randint(100,899):03d}-{random.randint(10,99):02d}-{random.randint(1000,9999):04d}"


def rand_dob() -> str:
    start = date(1950, 1, 1)
    return (start + timedelta(days=random.randint(0, 25000))).isoformat()


def loyalty_number() -> str:
    # Custom classification pattern: LUM-\d{8}
    return f"LUM-{random.randint(0, 99999999):08d}"


def sku() -> str:
    # Custom classification pattern: SKU-[A-Z]{3}-\d{5}
    letters = "".join(random.choice("ABCDEFGHJKLMNPQRSTUVWXYZ") for _ in range(3))
    return f"SKU-{letters}-{random.randint(0, 99999):05d}"


def order_id() -> str:
    # Custom classification pattern: ORD-\d{10}
    return f"ORD-{random.randint(0, 9999999999):010d}"


def generate_products(n: int) -> list[dict]:
    rows = []
    for _ in range(n):
        cat = random.choice(CATEGORIES)
        cost = round(random.uniform(3, 240), 2)
        rows.append({
            "product_sku": sku(),
            "product_name": f"{cat} Item {random.randint(100,999)}",
            "category": cat,
            "supplier": random.choice(SUPPLIERS),
            "unit_cost": cost,
            "list_price": round(cost * random.uniform(1.3, 2.6), 2),
            "in_stock": random.randint(0, 5000),
        })
    return rows


def generate_customers(n: int) -> list[dict]:
    rows = []
    for i in range(n):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        city, state, country, zip_ = random.choice(CITIES)
        rows.append({
            "customer_id": f"CUST-{100000 + i}",
            "first_name": first,
            "last_name": last,
            "email": rand_email(first, last, i),
            "phone": rand_phone(),
            "loyalty_number": loyalty_number(),
            "national_id": rand_ssn(),
            "date_of_birth": rand_dob(),
            "street_address": f"{random.randint(1,9999)} {random.choice(STREETS)}",
            "city": city,
            "state": state,
            "postal_code": zip_,
            "country": country,
            "credit_card_number": random.choice(TEST_CARDS),
            "marketing_consent": random.choice([True, False]),
            "created_at": (datetime.now() - timedelta(days=random.randint(0, 1200))).isoformat(timespec="seconds"),
        })
    return rows


def generate_orders(n: int, customers: list[dict], products: list[dict]) -> list[dict]:
    rows = []
    for _ in range(n):
        cust = random.choice(customers)
        prod = random.choice(products)
        qty = random.randint(1, 6)
        unit = float(prod["list_price"])
        rows.append({
            "order_id": order_id(),
            "customer_id": cust["customer_id"],
            "loyalty_number": cust["loyalty_number"],
            "order_date": (date.today() - timedelta(days=random.randint(0, 365))).isoformat(),
            "product_sku": prod["product_sku"],
            "quantity": qty,
            "unit_price": unit,
            "total_amount": round(unit * qty, 2),
            "payment_method": random.choice(PAYMENT_METHODS),
            "ship_to_email": cust["email"],
            "ship_to_postal_code": cust["postal_code"],
        })
    return rows


def write_csv(path: str, rows: list[dict]) -> None:
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {len(rows):>6} rows -> {path}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate synthetic Lumina Retail data.")
    ap.add_argument("--rows", type=int, default=500, help="customer & order row count")
    ap.add_argument("--products", type=int, default=120, help="product row count")
    ap.add_argument("--out", default="out", help="output directory")
    ap.add_argument("--seed", type=int, default=42, help="random seed for reproducibility")
    args = ap.parse_args()

    random.seed(args.seed)
    os.makedirs(args.out, exist_ok=True)

    print("Generating synthetic Lumina Retail Co. data...")
    products = generate_products(args.products)
    customers = generate_customers(args.rows)
    orders = generate_orders(args.rows * 3, customers, products)

    write_csv(os.path.join(args.out, "products.csv"), products)
    write_csv(os.path.join(args.out, "customers.csv"), customers)
    write_csv(os.path.join(args.out, "orders.csv"), orders)
    print("Done. Upload these CSVs to your Fabric Lakehouse Files area (see docs/02).")


if __name__ == "__main__":
    main()
