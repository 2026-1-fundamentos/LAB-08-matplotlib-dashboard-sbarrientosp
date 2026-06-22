"""Dashboard estático en HTML con visualizaciones del archivo shipping-data.csv."""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():

    os.makedirs("docs", exist_ok=True)

    df = pd.read_csv("files/input/shipping-data.csv", encoding="utf-8-sig")

    # 1. Shipping per Warehouse
    fig, ax = plt.subplots(figsize=(6, 4))
    counts = df["Warehouse_block"].value_counts().sort_index()
    ax.bar(counts.index, counts.values, color="steelblue", edgecolor="white")
    ax.set_title("Shipping per Warehouse Block")
    ax.set_xlabel("Warehouse Block")
    ax.set_ylabel("Number of Shipments")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # 2. Mode of Shipment
    fig, ax = plt.subplots(figsize=(6, 4))
    mode_counts = df["Mode_of_Shipment"].value_counts()
    ax.pie(
        mode_counts.values,
        labels=mode_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["steelblue", "coral", "mediumseagreen"],
    )
    ax.set_title("Mode of Shipment")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # 3. Average Customer Rating
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_rating = df.groupby("Mode_of_Shipment")["Customer_rating"].mean().sort_values()
    ax.barh(avg_rating.index, avg_rating.values, color="coral", edgecolor="white")
    ax.set_title("Average Customer Rating")
    ax.set_xlabel("Average Rating")
    ax.set_xlim(0, 5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # 4. Weight Distribution
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df["Weight_in_gms"], bins=30, color="mediumseagreen", edgecolor="white")
    ax.set_title("Weight Distribution (gms)")
    ax.set_xlabel("Weight (gms)")
    ax.set_ylabel("Frequency")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # 5. index.html
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shipping Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9; padding: 20px; }
        h1 { text-align: center; color: #2c3e50; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 1100px; margin: 0 auto; }
        .card { background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); padding: 15px; text-align: center; }
        .card img { width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="grid">
        <div class="card"><img src="shipping_per_warehouse.png" alt="Shipping per Warehouse"></div>
        <div class="card"><img src="mode_of_shipment.png" alt="Mode of Shipment"></div>
        <div class="card"><img src="average_customer_rating.png" alt="Average Customer Rating"></div>
        <div class="card"><img src="weight_distribution.png" alt="Weight Distribution"></div>
    </div>
</body>
</html>"""

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)