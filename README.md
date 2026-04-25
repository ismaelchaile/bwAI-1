# Google ADK Beginner

A beginner-friendly repository for exploring, testing, and building AI agents using the Google Agent Development Kit (ADK). This project includes several sample agents demonstrating different capabilities, from simple API calls to complex parallel routing.

## List of ADK features in this repo
* Advanced ADK installation for local development in Linux/Mac/Windows, or cloud development at GCP Cloud Shell
* Run of adk web UI and adk terminal UI
* Per-agent .env setup
* LLM agents
* Sub-agents
* Workflow agents: 
  * sequential
  * parallel
  * hybrid (sequential + parallel)
* Multi-tool calling: 
  * Function Tools: 
    * custom functions/methods in the code
    * custom functions/methods in the code + APIs calls
    * agent as a tool
* LiteLLM integration, for multi-model local or cloud calling
* Automatic multi-agent communications using output_key
* Running of custom functions/methods when the agent ends its job, using after_agent_callback

## 🗣️ Talk-workshop slides
This repo is part of the talk-workshop about AI & Agents: from theory to practice you can find in the next url:
https://aineth.ai/bwAI-1

The slides of the talk are a useful companion of this repo and can help you to enable your Gemini API KEY in GCP.

## 📂 Expected Directory Structure

To comply with ADK requirements, your custom agents must follow this exact directory structure:

```text
<parent_agents_dir>/ (recommended name agents)
  YOUR_AGENT_TYPE_FOLDER_NAME/
    .env
    __init__.py
    agent.py (must contain the root_agent)
```

## ⚙️ Prerequisites (Windows Users Only)
If you are using Windows, ensure you have the necessary tools installed before proceeding. Linux and macOS users can skip to the Installation section.

Install Git:
Open the <b>Command Prompt Terminal</b> and run:

```
winget install --id Git.Git -e --source winget
```
Alternatively, download it from your web browser via https://git-scm.com/install/windows.

Install Python 3.12:
If you don't have Python installed, you can search for and install version 3.12:

```
winget search Python.Python
winget install -e --id Python.Python.3.12
```
<b>Important</b>: Close and reopen your terminal after installation.

Once you reopened the Command Prompt terminal, run next commands for testing that git and python is working:
```
git
python --version
```

Update PowerShell Execution Policy (only if you use PowerShell in the next installation step):
If you have never run a PowerShell script before, you need to enable local script execution.
Open PowerShell as Administrator (Search > Right-click > "Run as Administrator").
Run the following command in PowerShell:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🚀 Installation
All dependencies are listed in requirements.txt. To set up the ADK environment and install the required packages automatically, run the setup script for your operating system.

Navigate to the scripts folder:

```
cd scripts
```
For Linux & macOS run:
```
./setup.sh
```

For Windows Command Prompt (preferred):
```
setup.bat
```
#### OR

For Windows PowerShell:
```
.\setup.ps1
```

## 🔑 API Key Activation
To use the agents, you must configure your Google Cloud API key:

Open the .env file in the root directory.

Replace <b> your_api_key_here </b> with your  Gemini GCP API key.

In Linux or macOS, move into the scripts folder and run the copyKey script:

```
cd scripts
./copyKey.sh
```
For Windows Command Prompt (preferred):
```
copyKey.bat
```
#### OR

For Windows PowerShell:
```
.\copyKey.ps1
```

## 🤖 Included Agents
This repository contains several sample agents inside the <b>agents/</b> folder to help you learn different ADK patterns:

1) gAgent: Tests a simple agent working with Gemini models using Vertex AI and an API Key.

2) liteLLMagent: Demonstrates a simple agent working with Gemma 4 (via Google API key) and Ollama local models using LiteLLM.

3) weatherAgent: Uses LiteLLM + Gemma 4 alongside an agent tool that fetches data from an external weather API (no API key required for the weather API).

4) toolAgent: Shows how one agent can utilize another agent as a tool.

5) subAgents: Demonstrates a Main/Router agent delegating a user query to a specialized Sub-Agent.

6) parallelAgent: Integrates parallel, sequential, and sub-agents into a sentence generator. It also highlights the use of states and the after_agent_callback for simple post-processing.

## 💻 Running the Agents
First, ensure your ADK environment is active. If not active, open adkLaunch.txt and copy/paste the launch command specific to your OS.

With ADK environment active, use the terminal or the web ui to run the agents

From the Terminal command line (Specific Agent):
From the root folder run:
```
adk run agents/YOUR_AGENT_TYPE_FOLDER_NAME
(Example: adk run agents/gAgent or adk run agents/liteLLMagent)
```

From the Web Interface:
The web UI allows you to interactively select and test your agents:


Using the provided script (Cloud Shell, Mac & Linux)
```
./adkWeb.sh
```

OR using the native ADK command
```
adk web agents
```

For Windows (PowerShell or CMD):
```
adkWeb.bat
```

## ➕ Running ADK with local models
You have as example the <b>liteLLMagent</b>, edit the agent.py and change the model according to the one you installed in your computer.
You can install ollama from the next link:
https://ollama.com/download

### 📝 Citation
If you use this software or derived works in your research or projects, please cite it as follows:

Title: Google ADK Beginner
Author: Ismael Chaile
LinkedIn: https://www.linkedin.com/in/ismaelchaile/
Date: April 2026
Repository: https://github.com/ismaelchaile/bwAI-1

Note: For formal academic citations, please refer to the CITATION.cff file in this repository for APA and BibTeX formats.