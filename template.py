# TEMPLATE used to create the project structure

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Adult_Income"

# list of files
list_of_files = [
    "data/.gitkeep",

    "reports/.gitkeep",
    "reports/charts/.gitkeep",
    "reports/summary_tables/.gitkeep",

    "src/Data Cleaning.ipynb",
    "src/Data Analysis.ipynb",
    "src/build_pdf_report.py",

    "README.md",
    "requirements.txt"
]

# logic to create the above files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")