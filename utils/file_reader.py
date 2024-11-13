import json


class FileReader:
    @staticmethod
    def read_file(file_path) -> str:
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def read_json(file_path) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)
