import pandas as pd

df = pd.read_csv("data/products.csv")

def recommend_products(category, budget):

    filtered = df[
        (df["category"].str.lower() == category.lower()) &
        (df["price"] <= budget)
    ]

    return filtered.sort_values(
        by="rating",
        ascending=False
    )