CREATE DATABASE IF NOT EXISTS ecommerce_project;

USE ecommerce_project;

  CREATE TABLE ecommerce_sales (
      InvoiceNo VARCHAR(20),
      StockCode VARCHAR(20),
      Description VARCHAR(255),
      Quantity INT,
      InvoiceDate DATETIME,
      UnitPrice DECIMAL(10,2),
      CustomerID VARCHAR(20),
      Country VARCHAR(100),
      Revenue DECIMAL(12,2),
      Month INT,
      Year INT,
      Day INT,
      Hour INT
 );
