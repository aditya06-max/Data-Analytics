USE ecom;

-- SELECT AVG(price_per_unit) FROM orders;

-- SELECT * FROM orders
-- WHERE price_per_unit > (
--     SELECT AVG(price_per_unit) FROM orders
-- );

SELECT *, (SELECT AVG(price_per_unit) FROM orders) AS Average FROM orders;