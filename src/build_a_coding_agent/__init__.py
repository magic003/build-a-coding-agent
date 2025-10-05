from google import genai

import tools
from agent import Agent


def main() -> None:
    client = genai.Client()
    agent = Agent(client=client, model="gemini-2.5-flash", tools=[tools.READ_FILE_TOOL])
    agent.run()
