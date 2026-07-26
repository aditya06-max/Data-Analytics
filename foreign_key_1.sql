USE ecom; 

-- This querry will create a relationship between orders and seller table. 
-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id);

INSERT INTO orders (seller_id, product, quantity, price_per_unit)
VALUES (3, 'Phone', 1, 120000);

SELECT * FROM orders;