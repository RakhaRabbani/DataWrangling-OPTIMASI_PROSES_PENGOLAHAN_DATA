SELECT 
    date_trunc('day', transaction_timestamp) AS dt,
    count(*) AS total_tx,
    sum(amount) AS total_amount
FROM 
    "analytics_db"."transactions_parquet"
WHERE 
    transaction_timestamp >= TIMESTAMP '2025-01-01'
GROUP BY 
    dt
ORDER BY 
    dt;