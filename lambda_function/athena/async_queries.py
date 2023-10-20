def start_async_query(query):
    query_execution_id = execute_query(query)  # from /athena/interaction.py
    return {
        "message": "Query started successfully.",
        "query_execution_id": query_execution_id
    }