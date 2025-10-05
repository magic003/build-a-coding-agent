def _read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{path}' was not found.")
    except PermissionError:
        raise PermissionError(f"You don't have permission to read '{path}'.")
    except Exception as e:
        raise Exception(f"An error occurred while reading '{path}': {str(e)}")
