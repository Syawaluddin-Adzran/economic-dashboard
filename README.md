# 📊 Economic G20 Dashboard
Interactive Business Intelligence Dashboard for Global Economic Analysis

An interactive Streamlit dashboard that visualises GDP per capita, inflation, and unemployment across G20 countries using data from the World Bank API. The dashboard provides a comprehensive economic overview through interactive charts, maps, filters, and country-level analysis.

In addition, the repository includes a **static chart generator** (`scripts/generate_static_charts.py`) that exports all dashboard visualisations as high-resolution PNG images and a combined PDF report – perfect for presentations, documentation, and embedding in your portfolio.

---

## 📌 Project Overview
This project transforms raw economic data into an interactive business intelligence dashboard that enables users to explore key economic indicators across G20 nations. The dashboard is designed to support data-driven decision-making by providing intuitive visualisations and filtering capabilities for economic analysis.

### Key Economic Indicators
- GDP per Capita (USD)
- Inflation Rate (%)
- Unemployment Rate (%)

---

## 🚀 Features

### 📈 General Overview Dashboard
Provides a high-level view of economic conditions across all G20 countries.

Includes:
- Country counts by GDP category
- Country counts by inflation category
- Country counts by unemployment category
- Correlation heatmap between economic indicators
- Inflation vs Unemployment scatter plot

---

### 💰 GDP Analysis
Dedicated GDP dashboard featuring:
- GDP per capita rankings (bar chart)
- GDP per capita distribution by income group (box plot)
- Interactive country comparisons
- GDP category distribution (pie chart)
- Geographic GDP visualisation (choropleth map)
- Dynamic range slider for GDP per capita

---

### 📉 Inflation Analysis
Dedicated inflation dashboard featuring:
- Inflation rankings by country (bar chart)
- Inflation distribution by inflation category (box plot)
- Interactive maps
- Inflation category distribution (pie chart)
- Dynamic range slider for inflation

---

### 👥 Unemployment Analysis
Dedicated unemployment dashboard featuring:
- Unemployment rankings (bar chart)
- Unemployment distribution by unemployment category (box plot)
- Labor market comparisons
- Geographic distribution (choropleth map)
- Category breakdowns (pie chart)
- Dynamic range slider for unemployment

---

## 🎛 Interactive Filters
- **Global Filter:** Multi-select country filter applied across all tabs
- **Tab-Level Filters:** Dynamic range sliders for each indicator (GDP, inflation, unemployment) that update charts in real time

---

## 📊 Visualisations
The dashboard includes:
- Interactive Bar Charts
- Scatter Plots
- Choropleth Maps
- Pie Charts
- Box Plots
- Correlation Heatmaps

All visualisations support hover interactions, zooming, panning, and dynamic filtering.

---

## 🖼️ Static Chart Generator (Built-in)

Run `scripts/generate_static_charts.py` to export **every chart** from the dashboard as PNG images and compile them into a single PDF report.

### Use cases:
- Embedding static charts in GitHub README
- Academic or business reports
- Portfolio documentation
- Offline snapshots of economic data

### Outputs:
Saved in `outputs/static_charts/`:
- Category distributions
- Correlation heatmap
- Scatter plots
- Box plots
- GDP / inflation / unemployment visualisations

---

## 🛠️ Tech Stack

| Category           | Technology                     |
|--------------------|--------------------------------|
| Data Source        | World Bank Open Data API       |
| Database           | SQLite                         |
| Dashboard          | Streamlit                      |
| Visualisation      | Plotly Express                 |
| Data Processing    | Pandas                         |
| Static Export      | Plotly + Kaleido + Matplotlib  |
| Version Control    | Git, GitHub                    |

---

## 📁 Repository Structure

```
economics-dashboard/
│
├── database/
│   └── economics.db
│
├── scripts/
│   └── generate_static_charts.py
│
├── outputs/
│   └── static_charts/
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

### 2. Create Virtual Environment
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

### 4. Add Database
```bash
mkdir database
cp ../economic-analysis/database/economics.db database/
```

### 5. Run Dashboard
```bash
streamlit run app.py
```

Open: http://localhost:8501

---

### 6. Generate Static Charts & PDF (Optional)
```bash
pip install kaleido matplotlib
python scripts/generate_static_charts.py
```

---

## 🧠 Usage Guide

- **Sidebar Filter** → Select countries (global filtering)
- **General Tab** → Correlation + macro overview
- **GDP Tab** → GDP ranking, map, distribution
- **Inflation Tab** → Inflation analysis
- **Unemployment Tab** → Labour market analysis
- **Raw Data View** → Inspect filtered dataset

---

## 🔗 Relationship to Economic Analysis Project

This dashboard complements the **Economic Data AI Assistant** project:

- Data pipeline from World Bank API
- SQLite database generation
- Text-to-SQL AI assistant
- Economic interpretation engine

This project focuses on:
- Interactive visual analytics
- Business intelligence dashboards
- Decision support systems

---

## 🧠 Skills Demonstrated
- Data Visualization
- Business Intelligence
- Dashboard Development
- Data Cleaning & EDA
- SQLite Database Integration
- Streamlit Apps
- Plotly Charts
- Static Report Generation
- Git Version Control

---

## 🚧 Future Improvements
- Time-series economic trends
- Forecasting models
- Automated data updates
- Advanced country benchmarking
- PDF report downloader
- Mobile responsive UI

---

## 📚 Data Source
World Bank Open Data API  
https://data.worldbank.org/

---

## 📄 License
MIT License

---

## 🙏 Acknowledgements
- World Bank
- Streamlit
- Plotly
- Pandas
- SQLite
- Kaleido

---

## 👤 Author
**Muhammad Syawaluddin Bin Adzran**

GitHub: https://github.com/Syawaluddin-Adzran  
LinkedIn: https://www.linkedin.com/in/muhammad-syawaluddin-bin-adzran/

---

## 🏁 Final Note
Built as a portfolio project demonstrating end-to-end business intelligence, data visualization, and economic analytics using real-world global data.