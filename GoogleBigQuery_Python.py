from google.cloud import bigquery

# Inisialisasi client
client = bigquery.Client(project="my-gcp-project")

query = """
    SELECT DATE(transaction_timestamp) AS dt, COUNT(*) AS total_tx
    FROM `myproject.mydataset.transactions`
    WHERE transaction_timestamp >= '2025-01-01'
    GROUP BY dt
    ORDER BY dt
"""

job = client.query(query)

for row in job:
    print(row.dt, row.total_tx)