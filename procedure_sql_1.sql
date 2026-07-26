USE ecom;

-- DELIMITER //

-- CREATE PROCEDURE get_delivered_orders()
-- BEGIN
--     SELECT * FROM orders
--     WHERE order_status = 'Delivered';
--     SELECT * FROM employees;
-- END//

-- DELIMITER ; 

DELIMITER //

CREATE PROCEDURE get_orders_by_city(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM orders
    WHERE city = city_name;
END//

DELIMITER ;
