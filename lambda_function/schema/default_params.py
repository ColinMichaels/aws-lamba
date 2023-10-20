PARAMS_SCHEMA = {
    "type": "object",
    "properties": {
        "start_date": {"type": "string", "pattern": "^\d{4}-\d{2}-\d{2}$"},
        "end_date": {"type": "string", "pattern": "^\d{4}-\d{2}-\d{2}$"},
        "site": {"type": "string"},
        "combiner": {"type": "string"},
        "inverter": {"type": "string"}
    },
    "required": ["start_date", "end_date", "site", "combiner", "inverter"]
}