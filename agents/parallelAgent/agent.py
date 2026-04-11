# Inspired from https://adk.dev/agents/workflow-agents/parallel-agents/#full-example-parallel-web-research

# This multi-agent workflow could be used for English learning purposes, where a student receives the words
# and he/she tries to create the sentence that has sense and compare with the words integrator resulting sentence.
# Pay attention to the use of different models, according to the complexity of the goal given to the agent
# Pay attention to the use of states to pass data from sub agents to the integrator agent.
# Pay attention to the use of after_agent_callback for states processing

from google.adk.agents import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.models import Gemini

# --- Constants ---
GAI_SIMPLE_MODEL = "gemini-2.5-flash-lite" 
GAI_POWERFUL_MODEL = "gemma-4-26b-a4b-it"

# --- 1. Define Word generator Sub-Agents (to run in parallel) ---
# Word 1: Noun generator
noun_producer_agent = Agent(
    name="noun_producer_agent",
    model=Gemini(model=GAI_SIMPLE_MODEL),
    instruction="""
    You are a random noun word producer. Your task it to produce only 1 noun word.
    """,
    description="Noun producer",
    # Store result in state for the integrator agent
    output_key="noun_word_result",
)

# Word 2: Verb generator
verb_producer_agent = Agent(
    name="verb_producer_agent",
    model=Gemini(model=GAI_SIMPLE_MODEL),
    instruction="""
    You are a random verb word producer. Your task it to produce only 1 verb word.
    """,
    description="Verb producer",
    # Store result in state for the integrator agent
    output_key="verb_word_result"
)

# Word 2: Adjective generator
adjective_producer_agent = Agent(
    name="adjective_producer_agent",
    model=Gemini(model=GAI_SIMPLE_MODEL),
    instruction="""
    You are a random adjective word producer. Your task it to produce only 1 adjective word.
    """,
    description="Adjective producer",
    # Store result in state for the integrator agent
    output_key="adjective_word_result"
)

# --- 2. Create the ParallelAgent (Runs words generators concurrently) ---
# This agent orchestrates the concurrent execution of the words generators.
# It finishes once all word generators have completed and stored their results in state.
parallel_words_generator_agent = ParallelAgent(
    name="parallel_words_generator_agent",
    sub_agents=[noun_producer_agent, verb_producer_agent, adjective_producer_agent],
    description="Runs multiple random word generator agents in parallel to generate each one a word."
)

# --- 3. Define the Integrator Agent (Runs *after* the parallel agents) ---
# This agent takes the results stored in the session state by the parallel agents
# and synthesizes them into a single, structured response.
integrator_agent = Agent(
    name="integrator_agent",
    model=Gemini(model=GAI_POWERFUL_MODEL),
    instruction="""
    You are responsible for combining the words you receive in the states {noun_word_result}, {verb_word_result} and {adjective_word_result} in a sentence that has sense.

    For the sentence, to have sense, you can add only simple modifiers as "the, a, an, etc" as well as minor morphological changes to the resulting input word.

    Once you have the final sentence, show it and its translation to Spanish too. Put each sentence in different lines.

    """,
    description="Combines the words received and simple modifiers to generates a phrase that has sense, strictly grounded on provided inputs.",
    output_key="sentence_result"
)

def use_states(callback_context):
    noun_length = len(callback_context.state.get("noun_word_result"))
    adjective_length = len(callback_context.state.get("adjective_word_result"))
    verb_length = len(callback_context.state.get("verb_word_result"))
    cleaned_english_sentence = callback_context.state.get("sentence_result").split('\n')[0].replace(" ", "")
    english_sentence_length = len(cleaned_english_sentence) - 1 # -1 for not compute the .
    original_length = noun_length + adjective_length + verb_length
    print("Original length of random words:", original_length)
    print("Clean english sentence:", cleaned_english_sentence)
    print("English sentence length:", english_sentence_length)
    print("Integrator 'quality' (1 is the best):", (1 - ((english_sentence_length - original_length) / original_length)))
    return

# --- 4. Create the Sequential Agent (Orchestrates the overall work flow) ---
# This is the main agent, it first executes the ParallelAgent
# to populate the state result of each sub_agent, and then executes the Integrator Agent to produce the final output.
sequential_pipeline_agent = SequentialAgent(
    name="sequential_pipeline_agent",
    # Run parallel words generator first, then the integrator
    sub_agents=[parallel_words_generator_agent, integrator_agent],
    description="Coordinates parallel words generator and synthesizes the results using the integrator agent",
    after_agent_callback=[use_states]
)

root_agent = sequential_pipeline_agent