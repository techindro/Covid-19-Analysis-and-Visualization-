# 🦠 Covid-19-Analysis-and-Visualization-


Interactive analysis and visualization of global COVID-19 data using **Plotly Express**, Pandas, Matplotlib, and WordCloud.

---

## 📊 What's Inside

| Feature | Description |
|---|---|
| Bar Charts | Top countries by cases, deaths, tests |
| Bubble Charts | Continent-wise and country-wise scatter plots |
| Animated Maps | Choropleth maps (Jan – Jul 2020) |
| Line / Scatter | Country-specific trends (USA default) |
| Word Cloud | Leading causes of COVID-19 deaths |

---

## 🗂️ Project Structure

```
covid19-analysis/
├── data/                    # ← place your CSV files here
│   ├── covid.csv
│   ├── covid_grouped.csv
│   └── coviddeath.csv
├── notebooks/
│   └── covid19_analysis.ipynb
├── src/
│   └── analysis.py          # standalone Python script
├── requirements.txt
└── README.md
```

---

## ⚡ Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<techindro>/covid19-analysis.git
cd covid19-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add datasets
Download the three CSV files and place them in the `data/` folder:
- `covid.csv` – country-level snapshot
- `covid_grouped.csv` – daily time-series by country
- `coviddeath.csv` – death conditions

> 📥 Datasets are available on [Kaggle – COVID-19 Dataset](https://www.kaggle.com/).

### 4. Run the notebook
```bash
jupyter notebook notebooks/covid19_analysis.ipynb
```

Or run the script directly:
```bash
python src/analysis.py
```

> **Google Colab:** open the notebook, change `pio.renderers.default` to `'colab'`, and upload your CSVs.

---

## 🔬 Datasets

| Dataset | Rows | Key Columns |
|---|---|---|
| `covid.csv` | 209 | Country/Region, TotalCases, TotalDeaths, TotalRecovered, TotalTests |
| `covid_grouped.csv` | 35 156 | Date, Country/Region, Confirmed, Deaths, Recovered, New cases |
| `coviddeath.csv` | varies | Condition, Condition Group |

---

## 📈 Sample Visualizations

- **Top 15 Countries – Total Cases** (bar chart)
- **Continent-wise Bubble Chart** (scatter)
- **Global Confirmed Cases** animated choropleth (Blues scale)
- **USA Daily Trends** line & bar charts
- **Word Cloud** – Influenza & Pneumonia are the leading conditions

---

## 🛠️ Tech Stack

- Python 3.9+
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [WordCloud](https://github.com/amueller/word_cloud)

---

## 📄 License

MIT © 2026
