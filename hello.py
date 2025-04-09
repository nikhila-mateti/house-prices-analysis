from preswald import text, selectbox, plotly, connect, get_df, table, query,slider
import pandas as pd
import plotly.express as px
import os

# --- 1. Initialize and load the dataset ---
connect()  # Initializes connection to preswald.toml data sources
df = get_df("train")  # "train" must match the key in your preswald.toml

# Debug: Output the current working directory for verification
text("# House Prices Analysis")
text("Explore the House Prices dataset with interactive filters and unique visualizations.")

# --- 2. Select only the important columns ---
important_columns = ["HouseStyle", "Neighborhood", "YearBuilt", "YearRemodAdd", "RoofStyle", "SalePrice"]
df = df[important_columns]

# --- 2. Unique SQL Query: Filter houses with LotArea greater than 7500 with fewer columns---
sql = "SELECT HouseStyle, Neighborhood, YearBuilt, YearRemodAdd, RoofStyle, SalePrice FROM train WHERE  YearRemodAdd > 2000"
big_lot_df = query(sql, "train")
#big_lot_df = big_lot_df[]
#table(big_lot_df, title="Houses with YearRemodAdd > 2000")
# Display the houses with LotArea > 7500 from the SQL query
#table(big_lot_df, title="Houses with LotArea > 7500")

# Convert numeric columns to proper types for plotting/filtering.
df["YearBuilt"] = pd.to_numeric(df["YearBuilt"], errors="coerce")
df["YearRemodAdd"] = pd.to_numeric(df["YearRemodAdd"], errors="coerce")
df["SalePrice"] = pd.to_numeric(df["SalePrice"], errors="coerce")

sale_price_threshold = slider("Minimum Sale Price", min_val=0, max_val=1000000, default=200000)
filtered_df = df[df["SalePrice"] >= sale_price_threshold]

table(filtered_df, title="Houses with SalePrice >= " + str(sale_price_threshold))

# --- 3. App Title and Instructions ---
text("# House Prices Visualization")
text("Use the dropdown below to select the graph you want to see.")


# --- 4. Add a Dropdown (selectbox) Widget to Choose the Visualization ---
vis_option = selectbox(
    "Select Visualization",
    options=[
        "Bar Chart: Average SalePrice by HouseStyle",
        "Box Plot: SalePrice Distribution by Top 10 Neighborhoods",
        "Scatter Plot: SalePrice vs. YearBuilt Colored by RoofStyle",
        "Scatter Plot: SalePrice vs. YearRemodAdd Colored by HouseStyle"
    ]
)

# --- 5. Display the Visualization Based on User Selection ---
if vis_option == "Bar Chart: Average SalePrice by HouseStyle":
    # Compute average SalePrice by HouseStyle.
    avg_saleprice = df.groupby("HouseStyle", as_index=False)["SalePrice"].mean()
    fig = px.bar(
        avg_saleprice,
        x="HouseStyle",
        y="SalePrice",
        title="Average SalePrice by HouseStyle",
        labels={"HouseStyle": "House Style", "SalePrice": "Average Sale Price"}
    )
    plotly(fig)

elif vis_option == "Box Plot: SalePrice Distribution by Top 10 Neighborhoods":
    # Select the top 10 neighborhoods by count.
    top_neighborhoods = df["Neighborhood"].value_counts().nlargest(10).index.tolist()
    df_top = df[df["Neighborhood"].isin(top_neighborhoods)]
    fig = px.box(
        df_top,
        x="Neighborhood",
        y="SalePrice",
        title="SalePrice Distribution by Top 10 Neighborhoods",
        labels={"Neighborhood": "Neighborhood", "SalePrice": "Sale Price"}
    )
    plotly(fig)

elif vis_option == "Scatter Plot: SalePrice vs. YearBuilt Colored by RoofStyle":
    fig = px.scatter(
        df,
        x="YearBuilt",
        y="SalePrice",
        color="RoofStyle",
        title="SalePrice vs. YearBuilt Colored by RoofStyle",
        labels={"YearBuilt": "Year Built", "SalePrice": "Sale Price", "RoofStyle": "Roof Style"}
    )
    plotly(fig)

elif vis_option == "Scatter Plot: SalePrice vs. YearRemodAdd Colored by HouseStyle":
    fig = px.scatter(
        df,
        x="YearRemodAdd",
        y="SalePrice",
        color="HouseStyle",
        title="SalePrice vs. YearRemodAdd Colored by HouseStyle",
        labels={"YearRemodAdd": "Year Remodeled/Added", "SalePrice": "Sale Price", "HouseStyle": "House Style"}
    )
    plotly(fig)

else:
    text("Please select a visualization option from the dropdown.")
