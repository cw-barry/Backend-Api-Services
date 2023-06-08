import json
from django.http import JsonResponse
import os


def practice_view(request, file):
    # Specify the path to the JSON file
    file_path = file + '.json'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "practice", file_path)
    print(file_path)

    try:

        with open(file_path, 'r') as file:
            # Load the JSON data from the file
            data = json.load(file)
    
    except:
        data = {"error" : "No such a file"}

    # Return the JSON data as a response
    return JsonResponse(data, safe=False)
