def clean_parameter(param):
    # Example: Remove any semicolons or SQL comment hints
    sanitized = param.replace(';', '').replace('--', '')
    return sanitized