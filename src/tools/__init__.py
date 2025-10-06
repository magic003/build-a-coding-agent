from .list_files import _list_files
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

LIST_FILE_TOOL = Tool(
    name="list_files",
    desc="List files and directories at a given path. If no path is provided, lists files in the current directory.",
    parameters_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Optional relative path to list files from. Defaults to current directory if not provided.",
            },
        },
    },
    function=_list_files,
)

__all__ = ["Tool", "READ_FILE_TOOL", "LIST_FILE_TOOL"]
