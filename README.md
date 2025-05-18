# 🌞 Solar Radiation Analysis - Senegal (Week 0 Challenge)

## 📌 Project Overview

This project is part of the **Solar Challenge Week 0**, focusing on analyzing solar radiation data from **Senegal**. The main objectives are:

- 📁 Git version control  
- ⚙️ Python environment setup  
- 📊 Exploratory Data Analysis (EDA)  
- 📈 Data cleaning and profiling  

---

## 🧰 Project Structure

solar-challenge-week1/
│
├── notebooks/ # Jupyter Notebooks (EDA, analysis, etc.)
│ └── senegal_eda2.ipynb # Main cleaned and validated notebook
│
├── scripts/ # Supporting scripts for data handling
│
├── tests/ # Unit tests (optional)
│
├── .github/workflows/ # GitHub Actions CI workflow
│
├── .vscode/ # VS Code settings
│
├── requirements.txt # Python dependencies
├── README.md # You're here!
└── .gitignore # Ignored files and folders

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Launch Jupyter Notebook
bash
Copy
Edit
jupyter notebook
📊 Dataset
The dataset is sourced from EnergyDataInfo.
A local copy is saved at:

bash
Copy
Edit
notebooks/senegal_raw.csv
Note: This file is excluded from Git via .gitignore.

📒 Notebooks
senegal_eda2.ipynb:
Contains the full exploratory workflow:

✅ Missing value analysis

✅ Outlier detection and handling

✅ Time series visualizations

✅ Correlation studies between variables

✅ Notebook Validation
The notebook has been validated using nbformat and is compatible with GitHub rendering.

To fix a broken notebook (e.g., not appearing in GitHub due to formatting issues), run:

bash
Copy
Edit
python fix_notebook.py
🧪 GitHub Actions (CI)
Basic GitHub Actions workflow included to:

Set up the Python environment

(Future scope) Run notebook checks and unit tests

Workflow file: .github/workflows/unittests.yml

🚧 Notes
Raw datasets are excluded from version control.

Always ensure your Jupyter kernel matches the virtual environment interpreter.

The project follows modular structure for scalability.

📬 Feedback & Contribution
If you spot an issue or want to contribute, feel free to:

Open a GitHub Issue

Submit a Pull Request
