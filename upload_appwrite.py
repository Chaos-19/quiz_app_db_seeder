import os
import json

from main import get_json_from_image
from create_collection import create_document

def list_files_in_directory(directory_path):
    try:
        # Get the list of all files and directories
        files = os.listdir(directory_path)
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
directory_path = 'Last Year National Exit Exam'
files = list_files_in_directory(directory_path)


for file in files:
    result = get_json_from_image(f"./{directory_path}/{file}").text
    result = result.replace("```json", "").replace("```", "")
    create_document(json.loads(result))
    print(f'{file} Document Created Successfully!')
