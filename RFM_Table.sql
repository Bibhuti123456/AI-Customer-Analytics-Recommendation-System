DROP TABLE IF EXISTS customer_rfm;

CREATE TABLE customer_rfm AS
SELECT
    CustomerID,

    DATEDIFF(
        (SELECT MAX(InvoiceDate)
         FROM ecommerce_sales),
        MAX(InvoiceDate)
    ) AS Recency,

    COUNT(DISTINCT InvoiceNo) AS Frequency,

    ROUND(SUM(Revenue),2) AS Monetary

FROM ecommerce_sales

GROUP BY CustomerID;

-- export The customer_rfm table correctly into a CSV file (Doing this because if I export from result grid the only 1000 rows are exported,because of the result grid limit)
  SELECT * FROM customer_rfm
  INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customer_rfm.csv'
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n';

-- To get the MYSql permitted path to export
SHOW VARIABLES LIKE 'secure_file_priv';

