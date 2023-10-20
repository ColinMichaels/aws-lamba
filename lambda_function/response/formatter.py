def get_response_headers():
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }


def format_response(status_code, body=None, error=None):
    """
    Standardizes the Lambda's responses. 
    :param status_code: The HTTP status code for the response.
    :param body: The main content of the response.
    :param error: Any error message to be included.
    :return: A dictionary representing the formatted response.
    """
    response = {
        "statusCode": status_code,
        "headers": get_response_headers()
    }

    if body:
        response["body"] = json.dumps({
            "data": body,
            "error": None
        })
    elif error:
        response["body"] = json.dumps({
            "data": None,
            "error": error
        })
    else:
        response["body"] = json.dumps({
            "data": None,
            "error": None
        })

    return response

