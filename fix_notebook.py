import nbformat
import os

notebook_path = 'notebooks/senegal_eda2.ipynb'

if not os.path.exists(notebook_path):
    print(f"Notebook not found at: {notebook_path}")
else:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    print(f"Notebook has {len(nb.cells)} cells.")

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print("Notebook rewritten successfully ✅")
