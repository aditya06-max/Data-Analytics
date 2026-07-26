USE ecom;
SELECT * FROM orders
-- WHERE city IN ("Delhi", "Mumbai", "Bangalore");

-- WHERE city NOT IN ("Delhi", "Mumbai", "Bangalore");
-- WHERE payment_mode NOT IN ("Cash", "UPI");

-- WHERE price_per_unit BETWEEN 1000 AND 20000;

-- WHERE price_per_unit NOT BETWEEN 0 AND 1000;

-- WHERE city LIKE "%L%" ;

-- WHERE city LIKE "%rab%"

-- WHERE product LIKE "%table%";

-- WHERE customer_name LIKE "Pr_ya _ingh";

WHERE category IN ("Electronics", "Furniture")
AND price_per_unit BETWEEN 1000 AND 10000;

