* Keep next structure, it is requested to be as shown next by ADK:
Expected directory structure:
  <agents_dir>/
    YOUR_AGENT_TYPE_FOLDER_NAME/
      agent.py (with root_agent)

* Installation
- Move to the scripts folder and run the setup file according to your OS.
- ./setup.sh --> run for install adk env and all packages in Linux and Mac
- .\setup.ps1 or setup.bat --> run for install adk env and all packages in Windows
- requirements.txt --> list of packages to install

* API KEY activation
- edit the file .env and replace your_api_key_here with the api key you get from GCP.
- move inside scripts folder and run ./copyKey.sh (Linux & Mac compatible) 

* Launch ADK environment
- open adkLaunch.txt and copy & paste the command according to your OS

* Agents inside agents folder
1) gAgent --> for testing a simple agent works with Gemini models with Vertex AI & API Key
2) liteLLMagent --> for testing a simple agent working with Gemma 4 with Google API key and Ollama local models using LiteLLM.
3) weatherAgent --> it uses LiteLLM + Gemma 4, and an agent tool using an external weather API (no API key needed)
4) toolAgent --> it shows how an agent can use other agent as a tool
5) subAgents --> it shows how a main/router agent delegates the user query to a sub agent
6) parallelAgent --> it integrates parallel, sequential and sub agents in a sentence generator, additionally it shows the use of states and after_agent_callback for simple processing after the agent finish.

* How to run the agents:
- From terminal (one specific agent):
adk run agents/YOUR_AGENT_TYPE_FOLDER_NAME --> e.g. gAgent or liteLLMagent

- From web (selecting the agent in the web interface):
./adkWeb.sh (cloudShell compatible) OR adk web agents
