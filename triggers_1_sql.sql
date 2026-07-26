USE ecom;

-- CREATE TABLE
-- order_cancellation (
--     log_id INT PRIMARY KEY
-- AUTO_INCREMENT,
--     order_id INT,
--     cancellation_on DATETIME,
--     reason VARCHAR(100)
-- );


  DELIMITER //
  CREATE TRIGGER
  trg_log_order_cancel
  AFTER UPDATE ON orders
  FOR EACH ROW 
  BEGIN
      IF NEW.order_status = "Cancelled"
      AND OLD.order_status <> "Cancelled" THEN
      
INSERT INTO order_cancellation (order_id, cancellation_on, reason)
 
 VALUES (NEW.order_id, NOW(), 'Order cancelled by user');
 
 END IF ;
 
 END//
 
 DELIMITER ; 

-- DROP TRIGGER   trg_log_order_cancel;
 
 