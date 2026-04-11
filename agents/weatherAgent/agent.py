# Inspired from a Google Colab 
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .tools.weatherTool import get_live_weather_forecast

# --- Agent Definition: An agent that uses a tool for calling an API ---
root_agent = Agent(
    name="weather_aware_planner",
    model=LiteLlm(model="gemini/gemma-4-26b-a4b-it"),
    description="A trip planner that checks the real-time weather before making suggestions.",
    instruction="You are a cautious trip planner. Before suggesting any outdoor activities, you MUST use the `get_live_weather_forecast` tool to check conditions. Incorporate the live weather details into your recommendation.",
    tools=[get_live_weather_forecast]
)