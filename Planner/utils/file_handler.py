import json
import os

STORAGE_DIR = "storage"

def load_from_json(filename):
    path = os.path.join(STORAGE_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_to_json(filename, data):
    path = os.path.join(STORAGE_DIR, filename)
    os.makedirs(STORAGE_DIR, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)