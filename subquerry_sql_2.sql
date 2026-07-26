-- Easy way to remember
-- IN = "Is this value in this list?" 📋
-- EXISTS = "Does at least one matching row exist?" ✅

USE ecom;

-- SQL executes the inner query first.
-- SELECT * FROM orders
-- WHERE city IN (
--    SELECT city FROM orders WHERE category = "Electronics"
--   );

-- EXISTS means
-- Does at least one row exist?

SELECT * FROM orders o
WHERE EXISTS (
   SELECT 1
   FROM orders
   WHERE city = o.city        --  WHERE city = o.city
-- This is called a correlated subquery.
-- The inner query refers to the outer query using o.city.
-- Imagine the outer query is currently looking at this row:

   AND category = "Furniture"
    );
    
    SELECT 1

-- Many beginners ask

-- Why 1?

-- Why not city?

-- Why not name?

-- Because

-- EXISTS doesn't care about the value.

-- It only checks

-- Did the query return at least one row?

-- You could write

-- SELECT 100

-- or

-- SELECT "Hello"

-- or

-- SELECT *

-- Everything works.

-- People use

-- SELECT 1

-- because it is short and indicates:

-- "I only care if a row exists."