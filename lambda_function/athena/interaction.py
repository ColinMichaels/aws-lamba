import boto3
import time
import os

client = boto3.client('athena')

def execute_query(query):
    response = client.start_query_execution(
        QueryString=query,
        ResultConfiguration={'OutputLocation': os.}
    )
    return response['QueryExecutionId']



def wait_for_query_completion(query_execution_id):
    while True:
        response = client.get_query_execution(QueryExecutionId=query_execution_id)
        state = response['QueryExecution']['Status']['State']

        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return state
        
        time.sleep(5)  # wait for 5 seconds before checking again


def fetch_query_results(query_execution_id):
    response = client.get_query_results(QueryExecutionId=query_execution_id)
    return response['ResultSet']


def cancel_query(query_execution_id):
    response = client.stop_query_execution(
        QueryExecutionId=query_execution_id
    )
    return response
