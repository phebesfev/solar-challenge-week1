[⚠️ Suspicious Content] 🌞 Solar Radiation Analysis - Senegal (Week 0 Challenge)
📌 Project Overview
This project is part of the Solar Challenge Week 0, focusing on analyzing solar radiation data from Senegal. The goal is to build foundational skills in:

📁 Git version control

⚙️ Python environment setup

📊 Exploratory Data Analysis (EDA)

📈 Data cleaning and profiling

🧰 Project Structure
bash
Copy
Edit
solar-challenge-week1/
│
├── notebooks/              # Jupyter Notebooks (EDA, analysis, etc.)
│   ├── senegal_eda2.ipynb  # Main cleaned and validated notebook
│
├── scripts/                # Supporting scripts for data handling
│
├── tests/                  # Unit tests (optional)
│
├── .github/workflows/      # GitHub Actions CI workflow
│
├── .vscode/                # VS Code settings
│
├── requirements.txt        # Python dependencies
├── README.md               # You're here!
└── .gitignore              # Ignored files and folders
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Launch Jupyter
bash
Copy
Edit
jupyter notebook
📊 Dataset
The dataset used is from EnergyDataInfo. A local copy is stored in:

bash
Copy
Edit
notebooks/senegal_raw.csv
📒 Notebooks
senegal_eda2.ipynb: Contains full EDA including:

Missing value analysis

Outlier handling

Time series visualization

Correlation studies

✅ Validation
Notebook format has been validated using nbformat and is compatible with GitHub rendering.

🚧 Notes
Raw data is excluded from version control (.gitignore).

For broken JSON notebooks, see fix_notebook.py in root to reformat.

🧪 GitHub Actions (CI)
Includes a basic GitHub Actions workflow to:

Validate environment

Run unit tests (future scope)
