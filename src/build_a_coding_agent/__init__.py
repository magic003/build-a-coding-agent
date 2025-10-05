from google import genai

from agent import Agent


def main() -> None:
    client = genai.Client()
    agent = Agent(client=client, model="gemma-3-27b-it", tools=[])
    agent.run()
