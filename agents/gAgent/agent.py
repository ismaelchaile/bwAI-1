# --- Example using a Gemini/Gemma4 model with a multi-tool agent---

from google.adk.agents import Agent
from google.adk.models import Gemini
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

root_agent = Agent(
    model=Gemini(model="gemma-4-26b-a4b-it"), # OR "gemini-2.5-flash-lite"
    name="roll_die_agent",
    description=(
        "An agent that can roll a die and check if the result is a prime numbers"
    ),
    instruction="""
      You roll a die using the tool roll_die and answer questions about if the outcome of the die rolls is a prime number using the tool check_prime.
    """,
    tools=[roll_die, check_prime],
)