# scripts/generate_static_charts.py
import os
import sqlite3
import pandas as pd
import plotly.express as px
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Set up paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)
os.makedirs('outputs/static_charts', exist_ok=True)

# Load data
def load_data():
    conn = sqlite3.connect("database/economics.db")
    df = pd.read_sql("SELECT * FROM economic_cleaned", conn)
    conn.close()
    return df

df = load_data()
filtered_df = df.copy()

def save_fig(fig, filename, width=1000, height=600):
    fig.write_image(os.path.join('outputs/static_charts', filename), width=width, height=height)

# ============================================================
# GENERAL OVERVIEW CHARTS (ONLY ONE COPY OF CATEGORY COUNTS)
# ============================================================
# 1. GDP category counts
gdp_cat_counts = filtered_df["gdp_category"].value_counts().reset_index()
gdp_cat_counts.columns = ["GDP Category", "Count"]
fig = px.bar(gdp_cat_counts, x="GDP Category", y="Count", color="GDP Category",
             title="Number of Countries by GDP Category", text="Count")
save_fig(fig, "gen_gdp_category_counts.png")

# 2. Inflation category counts
inf_cat_counts = filtered_df["inflation_category"].value_counts().reset_index()
inf_cat_counts.columns = ["Inflation Category", "Count"]
fig = px.bar(inf_cat_counts, x="Inflation Category", y="Count", color="Inflation Category",
             title="Number of Countries by Inflation Category", text="Count")
save_fig(fig, "gen_inflation_category_counts.png")

# 3. Unemployment category counts
unemp_cat_counts = filtered_df["unemployment_category"].value_counts().reset_index()
unemp_cat_counts.columns = ["Unemployment Category", "Count"]
fig = px.bar(unemp_cat_counts, x="Unemployment Category", y="Count", color="Unemployment Category",
             title="Number of Countries by Unemployment Category", text="Count")
save_fig(fig, "gen_unemployment_category_counts.png")

# 4. Correlation heatmap
numeric_cols = ["gdp_per_capita", "inflation", "unemployment"]
corr = filtered_df[numeric_cols].corr()
fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r",
                title="Correlation Matrix (GDP per capita, Inflation, Unemployment)")
save_fig(fig, "gen_correlation_heatmap.png")

# 5. Inflation vs Unemployment scatter
fig = px.scatter(
    filtered_df,
    x="inflation", y="unemployment", size="gdp_per_capita", color="country_code",
    hover_name="country_code", size_max=60,
    labels={"inflation": "Inflation (%)", "unemployment": "Unemployment (%)"},
    title="Inflation vs Unemployment (bubble size = GDP per capita)"
)
save_fig(fig, "gen_inflation_vs_unemployment.png", width=1200)

# 6. Box plot: GDP per capita by GDP category
fig = px.box(filtered_df, x="gdp_category", y="gdp_per_capita", color="gdp_category",
             title="GDP per capita Distribution by Income Group",
             labels={"gdp_category": "GDP Category", "gdp_per_capita": "GDP per capita (USD)"})
save_fig(fig, "gen_gdp_boxplot.png")

# 7. Box plot: Inflation by Inflation Category
fig = px.box(filtered_df, x="inflation_category", y="inflation", color="inflation_category",
             title="Inflation Distribution by Inflation Category",
             labels={"inflation_category": "Inflation Category", "inflation": "Inflation (%)"})
save_fig(fig, "gen_inflation_boxplot.png")

# 8. Box plot: Unemployment by Unemployment Category
fig = px.box(filtered_df, x="unemployment_category", y="unemployment", color="unemployment_category",
             title="Unemployment Distribution by Unemployment Category",
             labels={"unemployment_category": "Unemployment Category", "unemployment": "Unemployment (%)"})
save_fig(fig, "gen_unemployment_boxplot.png")

# ============================================================
# METRIC TABS CHARTS (WITHOUT DUPLICATE CATEGORY COUNTS)
# ============================================================
def save_metric_charts(metric, metric_label, y_axis_label, category_col, category_label):
    filtered = filtered_df

    # Bar chart: countries on x, metric on y
    fig = px.bar(
        filtered,
        x="country_code", y=metric, color=category_col,
        title=f"{metric_label} by Country",
        hover_data=["inflation", "unemployment", "gdp_category", "inflation_category", "unemployment_category"],
        labels={metric: y_axis_label, "country_code": "Country"}
    )
    save_fig(fig, f"{metric}_bar_chart.png", width=1200)

    # Scatter plot (specific to metric)
    if metric == "gdp_per_capita":
        fig = px.scatter(
            filtered,
            x="inflation", y="unemployment", size=metric, color="country_code",
            hover_name="country_code", size_max=60,
            labels={"inflation": "Inflation (%)", "unemployment": "Unemployment (%)"},
            title=f"{metric_label} (bubble size) vs Inflation & Unemployment"
        )
    else:
        fig = px.scatter(
            filtered,
            x="gdp_per_capita", y=metric, size=metric, color="country_code",
            hover_name="country_code", size_max=60,
            labels={"gdp_per_capita": "GDP per capita (USD)", metric: y_axis_label},
            title=f"{metric_label} vs GDP per capita"
        )
    save_fig(fig, f"{metric}_scatter.png", width=1000)

    # Choropleth map
    fig = px.choropleth(
        filtered,
        locations="country_code", color=metric,
        hover_name="country_code",
        hover_data=["gdp_per_capita", "inflation", "unemployment", category_col],
        title=f"{metric_label} across G20 countries",
        color_continuous_scale="Viridis", projection="natural earth"
    )
    save_fig(fig, f"{metric}_choropleth.png", width=1200, height=700)

    # Pie chart (category distribution)
    pie_counts = filtered[category_col].value_counts().reset_index()
    pie_counts.columns = [category_label, "Count"]
    fig = px.pie(
        pie_counts, values="Count", names=category_label,
        title=f"{category_label} Distribution (all countries)", hole=0.4
    )
    save_fig(fig, f"{metric}_pie.png", width=800, height=800)

# Generate metric charts (no category count bars)
save_metric_charts("gdp_per_capita", "GDP per capita", "GDP per capita (USD)",
                   "gdp_category", "GDP Category")
save_metric_charts("inflation", "Inflation", "Inflation (%)",
                   "inflation_category", "Inflation Category")
save_metric_charts("unemployment", "Unemployment", "Unemployment (%)",
                   "unemployment_category", "Unemployment Category")

# ============================================================
# COMBINE ALL PNGs INTO A SINGLE PDF
# ============================================================
png_files = sorted([f for f in os.listdir('outputs/static_charts') if f.endswith('.png')])
if png_files:
    with PdfPages('outputs/static_charts/economic_report.pdf') as pdf:
        for png in png_files:
            img_path = os.path.join('outputs/static_charts', png)
            img = plt.imread(img_path)
            plt.figure(figsize=(11, 8.5))
            plt.imshow(img)
            plt.axis('off')
            plt.title(png.replace('_', ' ').replace('.png', ''), fontsize=10)
            pdf.savefig()
            plt.close()
    print("✅ Combined PDF saved to outputs/static_charts/economic_report.pdf")
else:
    print("No PNG files found to combine into PDF.")

print("✅ All static charts saved to outputs/static_charts/")