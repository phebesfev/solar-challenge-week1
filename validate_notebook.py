# validate_notebook.py
import nbformat
from nbformat.validator import validate, ValidationError

notebook_path = "notebooks/senegal_eda.ipynb"  # <- Your actual file

try:
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    validate(nb)
    print("✅ Notebook is valid.")
except ValidationError as e:
    print("❌ Notebook is INVALID:", e)
except Exception as e:
    print("⚠️ Failed to read notebook:", e)
