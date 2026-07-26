-- SELECT * FROM orders WHERE discount_percent < 30;
-- SELECT city, customer_name, quantity FROM orders;
-- SELECT * FROM orders WHERE delivery_date is NULL;
-- SELECT * FROM orders WHERE city = 'Delhi' AND order_status = 'Delivered';
-- SELECT * FROM orders WHERE city = 'Delhi' OR order_status = 'Delivered';
SELECT customer_name , order_date, price_per_unit FROM orders ORDER BY order_date DESC;
