# Chatbot with LangChain, LangGraph & Docker

This repository contains a chatbot built using **LangChain**, **LangGraph**, and **Docker**.  
It demonstrates how to build conversational flows with memory, state management, and deployment inside a container.


### Setup Instructions
---
##### Steps to Set Up and Run the Codes

Follow these steps to set up and run the code for this project. Commands are provided for macOS, Windows, and Linux.

---

#### Prerequisites
- Ensure you have `conda` (or Python's built-in `venv` module) and `pip` installed.
- Use `conda` or `venv` based on your preference.
- Docker installed and running

---

### Option 1: Using Conda

#### Step 1: Create a Virtual Environment

##### macOS,Linux and Windows:
```bash
conda create -n project-env python=3.10
```

#### Step 2: Activate the Virtual Environment

##### macOS,Linux and Windows:
```bash
conda activate project-env
```

#### Step 3: Install Required Packages

##### macOS,Linux and Windows:
```bash
pip install -r requirements.txt
```

### Option 2: Using Python's Built-in venv

#### Step 1: Create a Virtual Environment

##### macOS,Linux and Windows:
```bash
python3 -m venv project-env
```

#### Step 2: Activate the Virtual Environment

##### macOS and Linux:
```bash
source project-env/bin/activate
```

##### Windows:
```bash
project-env\Scripts\activate
```
#### Step 3: Install Required Packages

##### macOS,Linux and Windows:
```bash
pip install -r requirements.txt
```

#### Step 4: create .env file

##### Add this in your .env file and replace the values with your API keys:
```bash
    PPLX_API_KEY="your_api_key"
    OPENAI_API_KEY="your_api_key"
    AZURE_OPENAI_KEY="your_api_key"
    AZURE_OPENAI_ENDPOINT="your_deployments_endpoint"
    AZURE_OPENAI_DEPLOYMENT_NAME="deployments_name"
    AZURE_OPENAI_API_VERSION="deployment_version"
```
#### Step 5: Run codes

```bash
    python code_name.py
```
#### Build Docker Image 

```bash
    docker build -t chatbot .
```
####  Run Docker Container
```bash
    docker run -it -e env_variable=value chatbot
```
