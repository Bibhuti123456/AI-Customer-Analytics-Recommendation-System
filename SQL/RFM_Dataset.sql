USE ecommerce_project;

-- Find last purchase date.
SELECT
CustomerID,
MAX(InvoiceDate) AS Last_Purchase
FROM ecommerce_sales
GROUP BY CustomerID;

-- Frequency
SELECT
CustomerID,
COUNT(DISTINCT InvoiceNo) AS Frequency
FROM ecommerce_sales
GROUP BY CustomerID
ORDER BY Frequency DESC;

-- Monetary Value
SELECT
CustomerID,
ROUND(
SUM(Revenue),
2
) AS Monetary
FROM ecommerce_sales
GROUP BY CustomerID
ORDER BY Monetary DESC;

SELECT *
FROM customer_rfm
LIMIT 10;

-- SELECT *
-- FROM ecommerce_sales
-- WHERE InvoiceNo LIKE 'C%';