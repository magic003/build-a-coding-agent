import json
import os
from pathlib import Path


def _list_files(path: str = ".") -> str:
    result = []
    base_path = Path(path)

    if not base_path.exists():
        return json.dumps({"error": f"Path '{path}' does not exist"})

    for root, dirs, files in os.walk(path):
        root_path = Path(root)
        rel_root = (
            root_path.relative_to(base_path) if root_path != base_path else Path(".")
        )

        # Add directories with trailing slash
        for dir_name in dirs:
            rel_path = rel_root / dir_name
            if str(rel_path) != ".":
                result.append(f"{rel_path}/")

        # Add files
        for file_name in files:
            rel_path = rel_root / file_name
            if str(rel_path) != ".":
                result.append(str(rel_path))

    return json.dumps(result)
