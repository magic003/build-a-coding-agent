from typing import List

from google import genai
from google.genai import types

from tools import Tool


class Agent:
    def __init__(
        self,
        client: genai.Client,
        model: str,
        tools: List[Tool],
    ) -> None:
        self.client = client
        self.model = model
        self.tools = tools

    def run(self) -> None:
        print("Chat with the coding agent (type 'exit' to quit)\n")

        chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(tools=self._tool_declarations()),
        )

        while True:
            user_message = input("\u001b[94mYou\u001b[0m: ")
            if user_message.lower() == "exit":
                break

            response = chat.send_message(user_message)
            print(f"\u001b[92mAgent\u001b[0m: {response.text}")

    def _tool_declarations(self) -> List[types.Tool]:
        tool_declarations = []
        for tool in self.tools:
            decl = types.FunctionDeclaration(
                name=tool.name,
                description=tool.desc,
                parameters=types.Schema(**tool.parameters_schema),
            )
            tool_declarations.append(types.Tool(function_declarations=[decl]))
        return tool_declarations
