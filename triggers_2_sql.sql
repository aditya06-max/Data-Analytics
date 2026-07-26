UPDATE orders
SET order_status = 'Cancelled'
WHERE order_id = 2;

SELECT * FROM order_cancellation;

SELECT * FROM orders;
