from typing import Any, Callable, Dict


class Tool:
    def __init__(
        self,
        name: str,
        desc: str,
        parameters_schema: Dict[str, Any],
        function: Callable[..., Any],
    ) -> None:
        self.name = name
        self.desc = desc
        self.parameters_schema = parameters_schema
        self.function = function
