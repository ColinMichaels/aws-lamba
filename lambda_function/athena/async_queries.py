import boto3
import time

client = boto3.client('athena')
max_wait_time = 300

from lambda_function.athena.interaction import execute_query


def start_async_query(query):
    try:
        query_execution_id = execute_query(query)  # from /athena/interaction.py
        start_time = time.time()

    except Exception as e:
        return {"error": f"Failed to start query execution: {str(e)}"}

        # Step 2: Check the query status until it's done
    while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > max_wait_time:
                return {"error": "Query timed out"}
            response = client.get_query_execution(QueryExecutionId=query_execution_id)
            status = response['QueryExecution']['Status']['State']

            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                break

            time.sleep(5)  # wait for 5 seconds before checking again
           

            # Step 3: If query succeeded, get the results
            if status == 'SUCCEEDED':
                results = client.get_query_results(QueryExecutionId=query_execution_id)
                return results.get('ResultSet', {})
            return {
                "message": "Query started successfully.",
                "query_execution_id": query_execution_id
            }