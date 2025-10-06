from .edit_file import _edit_file
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

EDIT_FILE_TOOL = Tool(
    name="edit_file",
    desc="Make edits to a text file. Replaces 'old_str' with 'new_str' in the given file."
    " 'old_str' and 'new_str' MUST be different from each other. If the file specified with path doesn't exist, it will be created.",
    parameters_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The path to the file",
            },
            "old_str": {
                "type": "string",
                "description": "Text to search for(empty string for new files) - must match exactly and must only have one match exactly",
            },
            "new_str": {
                "type": "string",
                "description": "Text to replace old_str with",
            },
        },
        "required": ["path", "old_str", "new_str"],
    },
    function=_edit_file,
)

__all__ = ["Tool", "READ_FILE_TOOL", "LIST_FILE_TOOL", "EDIT_FILE_TOOL"]
