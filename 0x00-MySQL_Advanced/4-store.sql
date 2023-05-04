-- Create a trigger when order is inserted
CREATE TRIGGER my_trigger
AFTER INSERT
ON orders
 FOR EACH ROW UPDATE items SET quantity= quantity - NEW.number 
WHERE name = NEW.item_name;
