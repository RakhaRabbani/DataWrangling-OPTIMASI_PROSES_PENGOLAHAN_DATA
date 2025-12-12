import boto3
import time

client = boto3.client('athena', region_name='ap-southeast-1')

DATABASE = 'analytics_db'
OUTPUT_LOCATION = 's3://my-athena-query-results/'

query = """
    SELECT count(*) FROM analytics_db.transactions_parquet
    WHERE transaction_timestamp >= TIMESTAMP '2025-01-01'
"""

# Memulai eksekusi query
resp = client.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': DATABASE},
    ResultConfiguration={'OutputLocation': OUTPUT_LOCATION}
)

qid = resp['QueryExecutionId']

# Polling sampai selesai
while True:
    status = client.get_query_execution(QueryExecutionId=qid)['QueryExecution']['Status']['State']
    
    if status in ('SUCCEEDED', 'FAILED', 'CANCELLED'):
        break
    
    time.sleep(1)

if status == 'SUCCEEDED':
    results = client.get_query_results(QueryExecutionId=qid)
    print(results['ResultSet']['Rows'])
else:
    print("Query failed:", status)