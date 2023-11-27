import os
from pathlib import Path
import logging

# Basic configuration for logging
logging.basicConfig(level=logging.INFO)

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "schema.yaml",
    "app.py",
    "main.py",
    "setup.py",
    "main.py"
    "logs.py",  # Added a comma to separate this item from the next one
    "exception.py",
]

for filepth in list_of_files:
    filepath = Path(filepth)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"File created at: {filepath}")
    else:
        logging.info(f"File already present at: {filepath}")
