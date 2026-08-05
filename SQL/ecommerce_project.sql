USE ecommerce_project;

SELECT COUNT(*)
FROM ecommerce_sales;

-- Total Revenue
SELECT
ROUND(SUM(Revenue),2) AS Total_Revenue
FROM ecommerce_sales;

-- Total Orders
SELECT
COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM ecommerce_sales;

-- Total Customers
SELECT
COUNT(DISTINCT CustomerID) AS Total_Customers
FROM ecommerce_sales;

-- Average Order Value
SELECT
ROUND(
SUM(Revenue) /
COUNT(DISTINCT InvoiceNo),
2
) AS Average_Order_Value
FROM ecommerce_sales;

-- Top 10 Customers
SELECT
CustomerID,
ROUND(SUM(Revenue),2) AS Revenue
FROM ecommerce_sales
GROUP BY CustomerID
ORDER BY Revenue DESC
LIMIT 10;

-- Top 10 Products
SELECT
Description,
ROUND(SUM(Revenue),2) AS Revenue
FROM ecommerce_sales
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;

-- Revenue by Country
SELECT
Country,
ROUND(SUM(Revenue),2) AS Revenue
FROM ecommerce_sales
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10;