import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cleaned_data.csv")

basket = pd.crosstab(
    df["CustomerID"],
    df["Description"]
)

similarity = cosine_similarity(basket.T)

similarity_df = pd.DataFrame(
    similarity,
    index=basket.columns,
    columns=basket.columns
)

product = "WHITE HANGING HEART T-LIGHT HOLDER"

if product in similarity_df.columns:

    recommendations = (
        similarity_df[product]
        .sort_values(ascending=False)
        .head(11)
    )

    print("\nRecommended Products:\n")
    print(recommendations)

else:
    print("Product not found.")