USE ecom;

-- This is used when we use one parameter for searching our desired data 
CREATE INDEX idx_order
ON orders(city );

SELECT * FROM orders WHERE CITY = "Delhi" ;

-- Composite index , This is used when we are using two parameters to serch out our desired data.
-- CREATE INDEX idx_orders_city_orders_status
-- ON orders(city , order_status);

-- SELECT * FROM orders WHERE CITY = "Delhi" AND order_status = "Delivered";

-- These querry will use to delete the indexes we crete if we want.
-- DROP INDEX idx_orderz_city ON orders;
-- DROP INDEX idx_order_city ON orders;
-- Drop index idx_ordere_city On orders;
-- Drop index idx_orders_city_status ON orders;
-- Drop index idx_orders_city_orders_status ON orders;

