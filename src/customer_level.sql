SELECT
    customer_id,
    MIN(invoicedate::timestamp)::date          AS first_purchase,
    MAX(invoicedate::timestamp)::date          AS last_purchase,
    COUNT(DISTINCT invoice)                    AS frequency,
    SUM(quantity * price)                      AS monetary
FROM online_retail_raw
WHERE customer_id IS NOT NULL
  AND invoice NOT LIKE 'C%'
  AND quantity > 0
  AND price > 0
GROUP BY customer_id
ORDER BY monetary DESC;