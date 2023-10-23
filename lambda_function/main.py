import json
from utils.error_handling import AthenaQueryError, InputValidationError
from utils.logging import log_event
from validation.params import extract_parameters
from athena.interaction import execute_query, wait_for_query_completion, fetch_query_results
from security.sanitizer import clean_parameter
from query.builder import build_query_from_params
from response.formatter import format_response, get_response_headers


def lambda_handler(event, context):

    try:

        log_event(event)
        params = extract_parameters(event)
        query = build_query_from_params(params)
        query_execution_id = execute_query(query)
        wait_for_query_completion(query_execution_id)
        results = fetch_query_results(query_execution_id)
        formatted_results = format_response(results, 'JSON')
        return formatted_results
    
    except AthenaQueryError as e:
        results = formatted_results(500, json.dumps({'error': str(e)} ))
        return results
    
    except InputValidationError as e:
        results = formatted_results(422, json.dumps({'error': str(e)} ))
        return results

    except Exception as e:  # Catch all other exceptions
        results = formatted_results(500, json.dumps({'error': str(e)} ))
        return results