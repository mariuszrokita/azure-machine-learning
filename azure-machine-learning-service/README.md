# Create a workspace by using Python

## Create virtual environment

```bash
# Create environment
conda create -n amlenv -y Python=3.6

# Activate environment
conda activate amlenv
```

## Install the core components

```bash
# Install Jupyter
conda install nb_conda

# Install the base SDK and Jupyter Notebook
pip install azureml-sdk[notebooks]

# Install other required packages
pip install -r notebooks/requirements.txt
```
