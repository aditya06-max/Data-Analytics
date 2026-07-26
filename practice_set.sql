USE adishop;

SELECT product_name , price, quantity 
FROM order_items 
JOIN products
ON order_items.product_id = products.product_id;

SELECT name , order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;

-- Display the customer name, order date, and order status
SELECT name, order_date, order_status
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;

-- Display the payment amount and payment mode for each customer.
SELECT amount , payment_mode
FROM payments
JOIN orders ON payments.order_id = orders.order_id
JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_status = 'Delivered'
    OR orders.order_status = 'PEnding';
    
-- Show every order with
-- Customer Name
-- Product Name
-- Quantity Purchased
SELECT name, product_name, quantity
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
JOIN products ON order_items.product_id = products.product_id;

-- Display only the products that were part of Delivered orders.
SELECT product_name , order_status
FROM products 
JOIN order_items ON products.product_id = order_items.product_id
JOIN orders ON order_items.order_id = orders.order_id
WHERE order_status = 'Delivered' ;

-- Show the names of customers whose orders were Cancelled.
SELECT name, order_status
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE order_status = 'Cancelled';

-- Show all customers who paid using UPI.
SELECT name , payment_mode
FROM customers 
JOIN orders ON customers.customer_id = orders.customer_id
JOIN payments ON orders.order_id = payments.order_id
WHERE payment_mode = 'UPI'; 

-- Display products costing more than ₹1000 that were actually ordered.
SELECT products.product_id, price, order_status
FROM products
JOIN order_items
    ON products.product_id = order_items.product_id
JOIN orders
    ON order_items.order_id = orders.order_id
WHERE price > 1000
  AND order_status != 'Cancelled';
  
-- Show all customers from Delhi who have placed an order.
SELECT name, city
FROM customers 
JOIN orders ON customers.customer_id = orders.customer_id
WHERE city = 'Delhi';
