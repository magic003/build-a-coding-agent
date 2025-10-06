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
            function_calls = self._get_function_calls(response)
            while function_calls:
                results = []
                for function_call in function_calls:
                    function_call_result = self._execute_function_call(function_call)
                    results.append(function_call_result)
                response = chat.send_message(results)
                function_calls = self._get_function_calls(response)

            print(f"\u001b[93mAgent\u001b[0m: {response.text}")

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

    def _get_function_calls(
        self, response: types.GenerateContentResponse
    ) -> List[types.FunctionCall]:
        if response.candidates is None:
            return []

        content = response.candidates[0].content
        if content is None or content.parts is None:
            return []

        return [
            part.function_call
            for part in content.parts
            if part.function_call is not None
        ]

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
