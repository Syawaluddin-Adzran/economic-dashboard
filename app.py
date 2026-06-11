# streamlit_app.py (updated)
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Economic G20 Dashboard", layout="wide")
st.title("📊 Economic G20 Dashboard")
st.markdown("Explore GDP per capita, inflation, and unemployment through interactive visualisations.")

# ---------- Load data ----------
@st.cache_data
def load_data():
    conn = sqlite3.connect("database/economics.db")
    df = pd.read_sql("SELECT * FROM economic_cleaned", conn)
    conn.close()
    return df

df = load_data()

# ---------- Sidebar: Country filter ----------
st.sidebar.header("Filters")
countries = st.sidebar.multiselect(
    "Select countries",
    options=sorted(df["country_code"].unique()),
    default=sorted(df["country_code"].unique())
)

filtered_df = df[df["country_code"].isin(countries)]

if filtered_df.empty:
    st.warning("No data for the selected countries. Please adjust filters.")
    st.stop()

# ---------- Helper function for metric tabs (GDP, Inflation, Unemployment) ----------
# Removed duplicate category count bar charts; only keep bar, scatter, map, pie, and add box plot.
def create_metric_tab(metric, metric_label, y_axis_label, min_val, max_val, default_range, category_col, category_label):
    st.header(f"{metric_label}")

    # Slider for metric range
    metric_range = st.slider(
        f"Filter by {metric_label} range",
        min_value=float(min_val),
        max_value=float(max_val),
        value=default_range,
        step=(max_val - min_val) / 100,
        key=f"slider_{metric}"
    )
    filtered = filtered_df[
        (filtered_df[metric] >= metric_range[0]) &
        (filtered_df[metric] <= metric_range[1])
    ]
    if filtered.empty:
        st.warning(f"No countries in the selected {metric_label} range. Adjust the slider.")
        return

    # 1. Bar chart: countries vs metric, coloured by its own category
    fig_bar = px.bar(
        filtered,
        x="country_code",
        y=metric,
        color=category_col,
        title=f"{metric_label} by Country",
        hover_data=["inflation", "unemployment", "gdp_category", "inflation_category", "unemployment_category"],
        labels={metric: y_axis_label, "country_code": "Country"}
    )
    st.plotly_chart(fig_bar, use_container_width=True, key=f"bar_{metric}")

    # 2. Box plot: distribution of the metric by its own category (NEW)
    st.subheader(f"{metric_label} Distribution by {category_label}")
    fig_box = px.box(
        filtered,
        x=category_col,
        y=metric,
        color=category_col,
        title=f"Spread of {metric_label} within each {category_label.lower()}",
        labels={category_col: category_label, metric: y_axis_label}
    )
    st.plotly_chart(fig_box, use_container_width=True, key=f"box_{metric}")

    # 3. Scatter plot: metric vs GDP per capita (or vs others)
    if metric == "gdp_per_capita":
        fig_scatter = px.scatter(
            filtered,
            x="inflation",
            y="unemployment",
            size=metric,
            color="country_code",
            hover_name="country_code",
            size_max=60,
            labels={"inflation": "Inflation (%)", "unemployment": "Unemployment (%)"},
            title=f"{metric_label} (bubble size) vs Inflation & Unemployment"
        )
        st.plotly_chart(fig_scatter, use_container_width=True, key=f"scatter_{metric}")
    else:
        fig_scatter = px.scatter(
            filtered,
            x="gdp_per_capita",
            y=metric,
            size=metric,
            color="country_code",
            hover_name="country_code",
            size_max=60,
            labels={"gdp_per_capita": "GDP per capita (USD)", metric: y_axis_label},
            title=f"{metric_label} vs GDP per capita"
        )
        st.plotly_chart(fig_scatter, use_container_width=True, key=f"scatter_{metric}")

    # 4. Choropleth map
    fig_map = px.choropleth(
        filtered,
        locations="country_code",
        color=metric,
        hover_name="country_code",
        hover_data=["gdp_per_capita", "inflation", "unemployment", category_col],
        title=f"{metric_label} across G20 countries",
        color_continuous_scale="Viridis",
        projection="natural earth"
    )
    st.plotly_chart(fig_map, use_container_width=True, key=f"map_{metric}")

    # 5. Pie chart: category distribution
    pie_counts = filtered[category_col].value_counts().reset_index()
    pie_counts.columns = [category_label, "Count"]
    fig_pie = px.pie(
        pie_counts,
        values="Count",
        names=category_label,
        title=f"{category_label} Distribution (filtered countries)",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True, key=f"pie_{metric}")

# ---------- Determine slider ranges ----------
gdp_min = df["gdp_per_capita"].min()
gdp_max = df["gdp_per_capita"].max()
inf_min = df["inflation"].min()
inf_max = df["inflation"].max()
unemp_min = df["unemployment"].min()
unemp_max = df["unemployment"].max()

gdp_default = (gdp_min, gdp_max)
inf_default = (inf_min, inf_max)
unemp_default = (unemp_min, unemp_max)

# ---------- Create Tabs ----------
tab_general, tab_gdp, tab_inf, tab_unemp = st.tabs(
    ["📊 General Overview", "💰 GDP per capita", "📈 Inflation", "👥 Unemployment"])

# ========== GENERAL OVERVIEW TAB ==========
with tab_general:
    st.header("General Overview of Selected Countries")

    # 1. Number of countries by GDP category
    st.subheader("Number of Countries by GDP Category")
    gdp_cat_counts = filtered_df["gdp_category"].value_counts().reset_index()
    gdp_cat_counts.columns = ["GDP Category", "Count"]
    fig_gdp_cat_bar = px.bar(
        gdp_cat_counts,
        x="GDP Category",
        y="Count",
        color="GDP Category",
        title="How many countries fall into each income group?",
        text="Count"
    )
    st.plotly_chart(fig_gdp_cat_bar, use_container_width=True, key="gen_gdp_cat_bar")

    # 2. Number of countries by inflation category
    st.subheader("Number of Countries by Inflation Category")
    inf_cat_counts = filtered_df["inflation_category"].value_counts().reset_index()
    inf_cat_counts.columns = ["Inflation Category", "Count"]
    fig_inf_cat_bar = px.bar(
        inf_cat_counts,
        x="Inflation Category",
        y="Count",
        color="Inflation Category",
        title="How many countries experience each level of inflation?",
        text="Count"
    )
    st.plotly_chart(fig_inf_cat_bar, use_container_width=True, key="gen_inf_cat_bar")

    # 3. Number of countries by unemployment category
    st.subheader("Number of Countries by Unemployment Category")
    unemp_cat_counts = filtered_df["unemployment_category"].value_counts().reset_index()
    unemp_cat_counts.columns = ["Unemployment Category", "Count"]
    fig_unemp_cat_bar = px.bar(
        unemp_cat_counts,
        x="Unemployment Category",
        y="Count",
        color="Unemployment Category",
        title="How many countries fall into each unemployment level?",
        text="Count"
    )
    st.plotly_chart(fig_unemp_cat_bar, use_container_width=True, key="gen_unemp_cat_bar")

    # 4. Correlation heatmap
    st.subheader("Correlation Between Economic Indicators")
    numeric_cols = ["gdp_per_capita", "inflation", "unemployment"]
    corr = filtered_df[numeric_cols].corr()
    fig_heatmap_gen = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix (GDP per capita, Inflation, Unemployment)"
    )
    st.plotly_chart(fig_heatmap_gen, use_container_width=True, key="gen_heatmap")

    # 5. Scatter plot: Inflation vs Unemployment (size = GDP per capita)
    st.subheader("Inflation vs Unemployment (bubble size = GDP per capita)")
    fig_scatter_gen = px.scatter(
        filtered_df,
        x="inflation",
        y="unemployment",
        size="gdp_per_capita",
        color="country_code",
        hover_name="country_code",
        size_max=60,
        labels={"inflation": "Inflation (%)", "unemployment": "Unemployment (%)"},
        title="Relationship between inflation and unemployment – each bubble is a country"
    )
    st.plotly_chart(fig_scatter_gen, use_container_width=True, key="gen_scatter")

    # (GDP box plot moved to GDP tab; removed from here)

# ========== GDP TAB ==========
with tab_gdp:
    create_metric_tab("gdp_per_capita", "GDP per capita", "GDP per capita (USD)",
                      gdp_min, gdp_max, gdp_default, "gdp_category", "GDP Category")

# ========== INFLATION TAB ==========
with tab_inf:
    create_metric_tab("inflation", "Inflation", "Inflation (%)",
                      inf_min, inf_max, inf_default, "inflation_category", "Inflation Category")

# ========== UNEMPLOYMENT TAB ==========
with tab_unemp:
    create_metric_tab("unemployment", "Unemployment", "Unemployment (%)",
                      unemp_min, unemp_max, unemp_default, "unemployment_category", "Unemployment Category")

# ---------- Raw data table ----------
with st.expander("📋 View filtered raw data (based on country selection)"):
    st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.caption("Data source: World Bank API (latest available year). Dashboard built with Streamlit and Plotly.")