USE ecom;

SET autocommit = 0;

UPDATE orders
SET order_status = 'Cancelled22'
WHERE order_id = 3;

SELECT * FROM orders;

-- COMMIT;   -- This means we want to save the changes we made in the table because we turn off the autcommit in sql
-- ROLLBACK;   -- This is used to call off the saved changes we made in sql.

