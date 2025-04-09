# House Prices Analysis App

This project is an interactive data visualization dashboard built using Preswald and Plotly Express. The app analyzes a house prices dataset by filtering key features and rendering dynamic visualizations based on user input.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Key Functionalities](#key-functionalities)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Overview

The House Prices Analysis App allows users to explore key aspects of a house prices dataset interactively. The app:
- Filters data based on user-defined conditions using a slider.
- Offers a dropdown to choose between different types of visualizations.
- Uses a SQL query to show a subset of the data.
- Dynamically updates visualizations (bar chart, box plot, and scatter plots) based on the filtered data.

## Dataset

The dataset is assumed to be the **House Prices** dataset (commonly available on sites like Kaggle) and is stored as `data/train.csv`. The app focuses on the following important columns:

- **HouseStyle:** The style of the house.
- **Neighborhood:** The neighborhood where the house is located.
- **YearBuilt:** The year the house was originally built.
- **YearRemodAdd:** The year of the house's remodel or addition.
- **RoofStyle:** The roof style of the house.
- **SalePrice:** The sale price of the house.

## Key Functionalities

### Data Loading and Preparation
- **Connection:** Uses the Preswald `connect()` function to initialize data sources as specified in the `preswald.toml` file.
- **Dataset Retrieval:** Loads the dataset using `get_df("train")`, where `"train"` must match the key defined in `preswald.toml`.
- **Column Selection & Conversion:** Selects only the important columns and converts numeric fields (e.g., `YearBuilt`, `YearRemodAdd`, `SalePrice`) into proper numeric types.

### Data Filtering
- **SQL Query:** Executes a SQL query to filter houses with `YearRemodAdd > 2000` and displays the results using the `table()` widget.
- **Slider Widget:** Adds a slider using the `slider()` function labeled "Minimum Sale Price" so that users can filter houses with `SalePrice` greater than or equal to the slider's value. The filtered table is updated dynamically.

### Dynamic Visualizations
- **Dropdown Widget:** Provides a dropdown (via `selectbox()`) to let users select a type of visualization.
- **Visualization Options:** Depending on the user's selection, the app renders:
  - **Bar Chart:** Displays the average SalePrice by HouseStyle.
  - **Box Plot:** Shows the SalePrice distribution by the top 10 Neighborhoods.
  - **Scatter Plots:** 
    - SalePrice vs. YearBuilt colored by RoofStyle.
    - SalePrice vs. YearRemodAdd colored by HouseStyle.
- **Plot Rendering:** Visualizations are created using Plotly Express and are updated based on the current filtered data.

