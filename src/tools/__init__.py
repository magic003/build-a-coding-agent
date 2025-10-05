from .read_file import _read_file
from .tool import Tool

READ_FILE_TOOL = Tool(
    name="read_file",
    desc="Reads the content of a file and returns it as a string.",
    parameters_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The relative path of a file in the working directory.",
            },
        },
        "required": ["path"],
    },
    function=_read_file,
)

__all__ = ["Tool", "READ_FILE_TOOL"]
