import json

class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data):
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)

