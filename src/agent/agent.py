from google import genai


class Agent:
    def __init__(self, client: genai.Client, model: str = "gemma-3-27b-it") -> None:
        self.client = client
        self.model = model

    def run(self) -> None:
        print("Chat with the coding agent (type 'exit' to quit)")

        while True:
            user_message = input("\u001b[94mYou\u001b[0m: ")
            if user_message.lower() == "exit":
                break

            response = self.client.models.generate_content(
                model=self.model,
                contents=user_message,
            )
            print(f"\u001b[92mAgent\u001b[0m: {response.text}")
