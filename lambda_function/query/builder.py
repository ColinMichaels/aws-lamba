def build_query_from_params(params):
    start_date, end_date, site, combiner, inverter = params
    query = f"""
        SELECT * FROM my_athena_table
        WHERE date BETWEEN '{start_date}' AND '{end_date}' 
        AND site = '{site}' 
        AND combiner = '{combiner}'
        AND inverter = '{inverter}'
    """
    return query