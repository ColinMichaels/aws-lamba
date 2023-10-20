import json

def format_response(results, format_type):
    if format_type == 'JSON':
        return json.dumps(results)
    # Add more formats (e.g., XML, CSV) as required