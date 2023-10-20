import boto3

client = boto3.client('athena')

def fetch_table_metadata(database, table):
    response = client.get_table_metadata(
        CatalogName='AwsDataCatalog',
        DatabaseName=database,
        TableName=table
    )
    return response['TableMetadata']