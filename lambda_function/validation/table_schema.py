from jsonschema import validate, ValidationError

def validate_params_against_schema(params, schema):
    """
    Validate a dictionary of parameters against a given JSON schema.
    
    Parameters:
    - params: Dictionary containing the parameters to validate.
    - schema: Dictionary defining the JSON schema against which to validate.

    Returns:
    - True if the parameters match the schema.
    Throws:
    - ValidationError if the parameters don't match the schema.
    """
    try:
        validate(instance=params, schema=schema)
        return True
    except ValidationError as e:
        raise ValueError(f"{e} is not a valid column or value in the table schema.")

def validate_params_against_schema_manual(params, schema):
    for param in params:
        if param not in schema:
            raise ValueError(f"{param} is not a valid column or value in the table schema.")
    return True