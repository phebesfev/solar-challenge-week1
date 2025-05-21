# ☀️ Solar Data Dashboard

An interactive Streamlit dashboard to explore solar radiation data (GHI, DNI, DHI) across Benin, Togo, and Sierra Leone. Includes Senegal data preprocessing and multi-country comparison notebooks. Built for the KAIM Solar Challenge Week 0.

![Dashboard Screenshot](screenshots/dashboard_main.png)

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/solar-dashboard.git
cd solar-dashboard ```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt ```

### 3. Run the app

```bash
cd app
streamlit run main.py ```

📁 Project Structure

solar-challenge-week1/
├── .gitignore                   # Excludes 'data/' and other artifacts
├── .vscode/
│   └── settings.json            # Editor settings
├── app/
│   ├── __init__.py
│   ├── main.py                  # Main Streamlit dashboard
│   └── utils.py                 # Data loading & plotting functions
├── data/                        # Raw/cleaned CSV files (excluded by .gitignore)
├── github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI workflow
├── notebooks/
│   ├── compare_countries.ipynb # GHI comparison: Benin, Togo, Sierra Leone
│   └── senegal_eda.ipynb       # Senegal data cleaning and EDA
├── requirements.txt            # Python dependencies
├── screenshots/
│   ├── dashboard_main.png
│   └── top_days_table.png
├── scripts/
│   ├── __init__.py
│   └── README.md               # Script usage notes (if any)
├── source/                     # (Optional) source files for further extension
├── tests/                      # Unit and integration tests
├── venv/                       # Virtual environment (excluded by .gitignore)
└── README.md                   # Project documentation (this file)

📊 Features
📈 Box plot of GHI distribution per country

📋 Summary statistics (GHI, DNI, DHI)

🔝 Top 5 highest-GHI days per country

🌍 Country selection: Benin, Togo, Sierra Leone

📊 Notebook: average GHI comparison (3 countries)

🧹 Notebook: Senegal dataset cleaning and EDA

📦 Requirements
Install with:

```
pip install -r requirements.txt
```
requirements.txt contents:

text
Copy
Edit
streamlit
pandas
plotly
matplotlib
seaborn




