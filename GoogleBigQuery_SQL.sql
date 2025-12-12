SELECT
    DATE(transaction_timestamp) AS dt,
    COUNT(*) AS total_tx,
    SUM(amount) AS total_amount
FROM
    `project.dataset.transactions` -- Perhatikan penggunaan backtick (`)
WHERE
    transaction_timestamp >= '2025-01-01'
GROUP BY
    dt
ORDER BY
    dt;