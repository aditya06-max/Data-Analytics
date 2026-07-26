USE ecom; 
-- UPDATE orders SET seller_id= NULL WHERE order_id IN (1,13,14);

SELECT
o.order_id, o.product, o.city AS customer_city,
s.seller_name
FROM orders o
LEFT JOIN sellers s
ON o.seller_id = s.seller_id;

-- SELECT * FROM orders;