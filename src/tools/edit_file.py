def _edit_file(path: str, old_str: str, new_str: str) -> str:
    if not path or old_str == new_str:
        raise ValueError("Invalid input parameters")

    try:
        with open(path, "r") as file:
            old_content = file.read()
    except FileNotFoundError:
        if old_str == "":
            # Create a new file if old_str is empty and file doesn't exist
            with open(path, "w") as file:
                file.write(new_str)
            return "OK"
        else:
            raise FileNotFoundError(f"File not found: {path}")

    new_content = old_content.replace(old_str, new_str)

    if old_content == new_content and old_str != "":
        raise ValueError("old_str not found in file")

    with open(path, "w") as file:
        file.write(new_content)
    return "OK"
