from google import genai

from agent import Agent


def main() -> None:
    print("Hello from build-a-coding-agent!")
    client = genai.Client()
    agent = Agent(client)
    agent.run()
