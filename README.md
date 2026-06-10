# 📊 G20 Economic Dashboard

**Interactive Business Intelligence Dashboard for Global Economic Analysis**

An interactive Streamlit dashboard that visualizes GDP per capita, inflation, and unemployment across G20 countries using data from the World Bank API. The dashboard provides a comprehensive economic overview through interactive charts, maps, filters, and country-level analysis.

---

## 📌 Project Overview

This project transforms raw economic data into an interactive business intelligence dashboard that enables users to explore key economic indicators across G20 nations.

The dashboard is designed to support data-driven decision-making by providing intuitive visualizations and filtering capabilities for economic analysis.

### Key Economic Indicators

* GDP per Capita (USD)
* Inflation Rate (%)
* Unemployment Rate (%)

---

## 🚀 Features

### 📈 General Overview Dashboard

Provides a high-level view of economic conditions across all G20 countries.

Includes:

* Country counts by GDP category
* Country counts by inflation category
* Country counts by unemployment category
* Correlation heatmap between economic indicators
* Inflation vs Unemployment scatter plot
* GDP distribution by income group

---

### 💰 GDP Analysis

Dedicated GDP dashboard featuring:

* GDP per capita rankings
* Interactive country comparisons
* GDP category distribution
* Geographic GDP visualization
* GDP-focused filtering tools

---

### 📉 Inflation Analysis

Dedicated inflation dashboard featuring:

* Inflation rankings by country
* Inflation category analysis
* Interactive maps
* Distribution visualizations
* Country filtering and range selection

---

### 👥 Unemployment Analysis

Dedicated unemployment dashboard featuring:

* Unemployment rankings
* Labor market comparisons
* Geographic distribution
* Category breakdowns
* Interactive filtering

---

### 🎛 Interactive Filters

#### Global Filter

* Multi-select country filter
* Applied across all dashboard tabs

#### Tab-Level Filters

Each indicator includes:

* Dynamic range sliders
* Category filtering
* Real-time chart updates

---

## 📊 Visualizations

The dashboard includes:

* Interactive Bar Charts
* Scatter Plots
* Choropleth Maps
* Pie Charts
* Box Plots
* Correlation Heatmaps

All visualizations support:

* Hover interactions
* Zooming
* Panning
* Dynamic filtering

---

## 🛠️ Tech Stack

| Category        | Technology               |
|-----------------|--------------------------|
| Data Source     | World Bank Open Data API |
| Database        | SQLite                   |
| Dashboard       | Streamlit                |
| Visualization   | Plotly Express           |
| Data Processing | Pandas                   |
| Version Control | Git, GitHub              |

---

## 📁 Repository Structure

```text
economics-dashboard/
│
├── database/
│   └── economics.db
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/economics-dashboard.git
cd economics-dashboard
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the Database

Copy the SQLite database from the Economic Analysis project:

```bash
mkdir database
cp ../economic-analysis/database/economics.db database/
```

### 5. Run the Dashboard

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## 🧠 Usage Guide

### Sidebar Country Filter

Use the sidebar to select one or multiple G20 countries.

All dashboard visualizations update automatically.

---

### General Overview Tab

Analyze:

* Economic category distributions
* Indicator relationships
* GDP distribution by income group
* Inflation and unemployment interactions

---

### GDP Tab

Explore:

* GDP rankings
* Income categories
* GDP world map
* Country comparisons

---

### Inflation Tab

Explore:

* Inflation rankings
* Inflation categories
* Inflation distribution
* Geographic trends

---

### Unemployment Tab

Explore:

* Labor market performance
* Unemployment categories
* Country comparisons
* Regional patterns

---

### Raw Data View

Expand the data table section to inspect the filtered dataset behind each visualization.

---

## 🔗 Relationship to Economic Analysis Project

This dashboard complements the Economic Data AI Assistant project.

### Economic Data AI Assistant

Provides:

* World Bank API data pipeline
* SQLite database generation
* Text-to-SQL AI Assistant
* Economic Interpreter
* Country Report Generator

### G20 Economic Dashboard

Provides:

* Interactive visual analytics
* Business intelligence reporting
* Economic data exploration
* Dashboard-based decision support

Together, these projects demonstrate:

* Data Engineering
* Database Management
* Business Intelligence
* Data Visualization
* AI Integration
* Economic Analytics

---

## 🌐 Deployment

This project can be deployed directly to Streamlit Cloud because it does not require a local language model.

### Deployment Steps

1. Push the repository to GitHub.
2. Create a new Streamlit Cloud application.
3. Select this repository.
4. Set `app.py` as the entry point.
5. Deploy.

No secrets or additional configuration are required.

---

## 🧠 Skills Demonstrated

* Data Visualization
* Business Intelligence
* Dashboard Development
* Interactive Analytics
* Data Cleaning
* Data Transformation
* Exploratory Data Analysis (EDA)
* SQLite Database Integration
* Streamlit Development
* Plotly Visualization
* Git Version Control

---

## 🚧 Future Improvements

* Time-series analysis for historical trends
* Additional World Bank indicators
* Economic forecasting models
* Downloadable PDF reports
* Advanced country benchmarking
* Automated database updates
* Mobile-responsive dashboard design

---

## 📚 Data Source

World Bank Open Data API

https://data.worldbank.org/

Data is sourced from publicly available World Bank indicators and processed for educational and portfolio purposes.

---

## 📄 License

MIT License

Free to use, modify, and distribute.

---

## 🙏 Acknowledgements

* World Bank Open Data API
* Streamlit
* Plotly
* Pandas
* SQLite

---

## 👤 Author

**Muhammad Syawaluddin Bin Adzran**

* GitHub: https://github.com/Syawaluddin-Adzran
* LinkedIn: Add your LinkedIn URL

---

## 🏁 Final Note

Built as a portfolio project to demonstrate end-to-end business intelligence, dashboard development, data visualization, and economic analytics skills using real-world global economic data.