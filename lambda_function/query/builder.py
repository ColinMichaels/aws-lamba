from jsonschema import ValidationError
from validation.table_schema import validate_params_against_schema
from schema.default_params import PARAMS_SCHEMA

def build_query_from_params(params):
    try:
        validate_params_against_schema(params=params, schema=PARAMS_SCHEMA)
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
        
    start_date, end_date, site, combiner, inverter = params
    query = f"""
        SELECT * FROM my_athena_table
        WHERE date BETWEEN '{start_date}' AND '{end_date}' 
        AND site = '{site}' 
        AND combiner = '{combiner}'
        AND inverter = '{inverter}'
    """
    return query