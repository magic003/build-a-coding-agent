from google import genai


class Agent:
    def __init__(self, client: genai.Client):
        self.client = client

    def run(self) -> None:
        pass
