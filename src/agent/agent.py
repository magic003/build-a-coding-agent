from google import genai


class Agent:
    def __init__(self, client: genai.Client, model: str = "gemma-3-27b-it") -> None:
        self.client = client
        self.model = model

    def run(self) -> None:
        print("Chat with the coding agent (type 'exit' to quit)")

        chat = self.client.chats.create(model=self.model)

        while True:
            user_message = input("\u001b[94mYou\u001b[0m: ")
            if user_message.lower() == "exit":
                break

            response = chat.send_message(user_message)
            print(f"\u001b[92mAgent\u001b[0m: {response.text}")
