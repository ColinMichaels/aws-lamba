def validate_params_against_schema(params, schema):
    for param in params:
        if param not in schema:
            raise ValueError(f"{param} is not a valid column or value in the table schema.")
    return True