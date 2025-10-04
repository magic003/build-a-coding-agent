from google import genai

from agent import Agent


def main() -> None:
    client = genai.Client()
    agent = Agent(client)
    agent.run()
