import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_json(file_name):

    path = BASE_DIR / "data" / file_name

    with open(path) as f:
        return json.load(f)