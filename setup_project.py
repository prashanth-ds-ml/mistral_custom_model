import os

# Define the directory structure
directories = [
    "notebooks",
    "src",
    "scripts",
    "checkpoints",
    "logs"
]

# Define the files to create
files = {
    "README.md": "# Mistral Custom Model\n\nThis repository contains the code and scripts to build, train, and fine-tune a custom implementation of the Mistral language model.\n\n## Directory Structure\n\n- **notebooks/**: Jupyter notebooks for initial experimentation.\n- **src/**: Source code for the model, dataset, and utilities.\n- **scripts/**: Shell scripts to run training, fine-tuning, and inference.\n- **checkpoints/**: Directory to save model checkpoints.\n- **logs/**: Directory to save training and evaluation logs.\n- **requirements.txt**: Python dependencies.\n- **.gitignore**: Files and directories to ignore in git.\n",
    ".gitignore": "# Python files\n*.pyc\n__pycache__/\n\n# Virtual environment\nvenv/\n\n# Jupyter Notebook checkpoints\n.ipynb_checkpoints/\n\n# Logs and Checkpoints\nlogs/\ncheckpoints/\n",
    "requirements.txt": "torch\ntransformers\nnumpy\npandas\ntqdm\njupyter\n",
    "src/__init__.py": "",
    "src/config.py": "",
    "src/dataset.py": "",
    "src/model.py": "",
    "src/train.py": "",
    "src/inference.py": "",
    "src/utils.py": "",
    "src/fine_tune.py": "",
    "scripts/run_train.sh": "#!/bin/bash\n# This script runs the training process\n\nsource venv/bin/activate\npython src/train.py\n",
    "scripts/run_fine_tune.sh": "#!/bin/bash\n# This script runs the fine-tuning process\n\nsource venv/bin/activate\npython src/fine_tune.py\n",
    "scripts/setup_env.sh": "#!/bin/bash\n# This script sets up the Python environment and installs dependencies\n\npython3 -m venv venv\nsource venv/bin/activate\npip install -r requirements.txt\n",
    "scripts/run_inference.sh": "#!/bin/bash\n# This script runs inference using the trained model\n\nsource venv/bin/activate\npython src/inference.py\n"
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

# Make shell scripts executable
for script in ["scripts/run_train.sh", "scripts/run_fine_tune.sh", "scripts/setup_env.sh", "scripts/run_inference.sh"]:
    os.chmod(script, 0o755)

print("Project structure has been set up successfully.")
