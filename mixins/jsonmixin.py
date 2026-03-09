import json
from contextlib import contextmanager
from typing import Dict, Generator, Any


class JSONMixin:

    @staticmethod
    @contextmanager
    def file_handler(file_name: str, mode: str) -> Generator:
        file = open(file_name, mode)
        try:
            yield file
        finally:
            file.close()

    @classmethod
    def load_json(cls, file_name: str) -> Dict[str, Any]:

        with cls.file_handler(file_name, "r") as f:
            return json.load(f)

    @classmethod
    def save_json(cls, file_name: str, data: Dict) -> None:

        with cls.file_handler(file_name, "w") as f:
            json.dump(data, f, indent=4)