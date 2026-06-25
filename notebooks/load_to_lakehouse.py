# Fabric notebook source — load synthetic CSVs into Delta tables.
# Attach this notebook to LuminaLakehouse, then run the cells in order.
# Each "# CELL" marker is one notebook cell. You can paste them individually
# or use Fabric's "Import notebook from .py" if available.

# CELL 1 — read raw CSVs from the Lakehouse Files area
# Assumes you uploaded customers.csv, orders.csv, products.csv into Files/raw/
base = "Files/raw"

customers = (
    spark.read.option("header", True).option("inferSchema", True)
    .csv(f"{base}/customers.csv")
)
orders = (
    spark.read.option("header", True).option("inferSchema", True)
    .csv(f"{base}/orders.csv")
)
products = (
    spark.read.option("header", True).option("inferSchema", True)
    .csv(f"{base}/products.csv")
)

print("customers:", customers.count())
print("orders   :", orders.count())
print("products :", products.count())

# CELL 2 — quick preview (handy during the demo)
display(customers.limit(10))

# CELL 3 — write managed Delta tables that Purview will catalog
(customers.write.format("delta").mode("overwrite")
    .option("overwriteSchema", "true").saveAsTable("customers"))
(orders.write.format("delta").mode("overwrite")
    .option("overwriteSchema", "true").saveAsTable("orders"))
(products.write.format("delta").mode("overwrite")
    .option("overwriteSchema", "true").saveAsTable("products"))

print("Tables written: customers, orders, products")

# CELL 4 — verify the tables are queryable
display(spark.sql("SELECT customer_id, email, loyalty_number, national_id FROM customers LIMIT 5"))
