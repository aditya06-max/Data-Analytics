USE ecom;

-- ALTER TABLE orders
-- DROP  FOREIGN KEY fk_orders_seller;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_seller
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id)
ON DELETE SET NULL;

SELECT * FROM orders;