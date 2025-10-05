from typing import List, Optional

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
            function_call = self._get_function_call(response)
            while function_call is not None:
                function_call_result = self._execute_function_call(function_call)
                response = chat.send_message(function_call_result)
                function_call = self._get_function_call(response)

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

    def _get_function_call(
        self, response: types.GenerateContentResponse
    ) -> Optional[types.FunctionCall]:
        if response.candidates is None:
            return None

        content = response.candidates[0].content
        if content is None or content.parts is None:
            return None

        return content.parts[0].function_call

    def _execute_function_call(self, function_call: types.FunctionCall) -> types.Part:
        if function_call.name is None:
            return types.Part.from_function_response(
                name="unknown",
                response={"error": "Function call name is missing."},
            )

        tool = next((t for t in self.tools if t.name == function_call.name), None)
        if tool is None:
            return types.Part.from_function_response(
                name=function_call.name,
                response={"error": f"Tool {function_call.name} not found."},
            )

        print(f"\u001b[92mtool\u001b[0m: {function_call.name}({function_call.args})\n")
        try:
            result = tool.function(**(function_call.args or {}))
            return types.Part.from_function_response(
                name=function_call.name,
                response={"result": result},
            )
        except Exception as e:
            return types.Part.from_function_response(
                name=function_call.name,
                response={"error": str(e)},
            )
