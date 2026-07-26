USE ecom;
-- SELECT COUNT(*)   -- Returns the total numbers of orders.
-- FROM orders;

-- SELECT SUM(quantity * price_per_unit) AS total_revenue   
-- From orders;

-- SELECT AVG(price_per_unit) AS avg_price
-- From orders;

-- SELECT MIN(price_per_unit), MAX(price_per_unit) 
-- FROM orders;

-- SELECT customer_name,
-- ROUND(price_per_unit, 0)
-- FROM orders;

-- SELECT UPPER(customer_name), LOWER(city)
-- FROM orders;

-- SELECT customer_name,
-- LENGTH(customer_name) FROM orders;

-- SELECT current_date;  --  this querry gives current date 

-- SELECT current_time;    -- This querry gives the current time.

-- SELECT order_id,
-- DATEDIFF(delivery_date, order_date) AS delivery_days   -- This querry will give us the number of days taken to deliver the product.
-- FROM orders;

-- SELECT *
-- FROM orders
-- WHERE YEAR(order_date) = 2024;