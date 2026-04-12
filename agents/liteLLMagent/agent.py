# --- Example using LiteLLM + Ollama models OR LiteLLM + Gemini API, to call Gemma 4 with a multi-tool agent---
# Inspired from --> https://adk.dev/agents/models/ollama/

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import random

def roll_die():
    """Simulates rolling a single six-sided die."""
    return random.randint(1, 6)

def check_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    
    # Check for divisors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

# Models starting with gemini/ need an Gemini API KEY
# Models starting with ollama_chat/ need Ollama in your computer and the corresponding model downloaded
root_agent = Agent(
    model=LiteLlm(model="gemini/gemma-4-26b-a4b-it"),  # OR "ollama_chat/gpt-oss:20b" OR "ollama_chat/gemma4:e2b" "gemini/gemma-4-26b-a4b-it", "gemini/gemma-4-31b-it"
    name="roll_die_agent",
    description=(
        "An agent that can roll a die and check if the result is a prime numbers"
    ),
    instruction="""
      You roll a die and answer questions about the outcome of the die rolls.
    """,
    tools=[
        roll_die,
        check_prime,
    ],
)