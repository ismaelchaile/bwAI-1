Markdown
# Google ADK Beginner

A beginner-friendly repository for exploring, testing, and building AI agents using the Google Agent Development Kit (ADK). This project includes several sample agents demonstrating different capabilities, from simple API calls to complex parallel routing.

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
Open Command Prompt and run:

DOS
```
winget install --id Git.Git -e --source winget
```
Alternatively, download it from your web browser via git-scm.com/install/windows.

<b>Important</b>: Close and reopen your terminal after installation.

Install Python 3.12:
If you don't have Python installed, you can search for and install version 3.12:

DOS
```
winget search Python.Python
winget install -e --id Python.Python.3.12
```
<b>Important</b>: Close and reopen your terminal after installation.

Update PowerShell Execution Policy:
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

For Windows PowerShell:
```
.\setup.ps1
```
#### OR

For Windows Command Prompt:
```
setup.bat
```

## 🔑 API Key Activation
To use the agents, you must configure your Google Cloud API key:

Open the .env file in the root directory.

Replace <b> your_api_key_here </b> with your  Gemini GCP API key.

In Linux or macOS, navigate to the scripts folder and run the copyKey script:

```
cd scripts
./copyKey.sh
```

For Windows PowerShell:
```
.\copyKey.ps1
```
#### OR

For Windows Command Prompt:
```
copyKey.bat
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

### 📝 Citation
If you use this software or derived works in your research or projects, please cite it as follows:

Title: Google ADK Beginner
Author: Ismael Chaile
LinkedIn: https://www.linkedin.com/in/ismaelchaile/
Date: April 2026
Repository: https://github.com/ismaelchaile/bwAI-1

Note: For formal academic citations, please refer to the CITATION.cff file in this repository for APA and BibTeX formats.