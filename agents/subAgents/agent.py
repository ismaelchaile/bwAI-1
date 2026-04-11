# --- Example using a Gemini/Gemma4 model with an agent using multiple sub agents---
# See https://adk.dev/tools-custom/function-tools/#key-aspects-of-this-example

from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini

from gAgent.agent import root_agent as gAgent
from weatherAgent.agent import root_agent as wAgent

root_agent = Agent(
    model=Gemini(model="gemma-4-26b-a4b-it"), # OR "gemini-2.5-flash-lite"
    name="router_agent",
    description=(
        "You acts as a router selecting the right agent according to the user query"
    ),
    instruction="""
       Select the right sub agent depending on the user request.
    """,
    sub_agents=[gAgent, wAgent],
)
