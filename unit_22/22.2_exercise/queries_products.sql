-- Comments in SQL Start with dash-dash --
--Exercise 22.1  Part 3

insert into products (name,price,can_be_returned) values ('chair',44.00,false);
insert into products (name,price,can_be_returned) values ('stool',25.99,true);
insert into products (name,price,can_be_returned) values ('table',124.00,false);
select * from products;
select name from products;
select name,price from products;
select * from products where can_be_returned = true;
select * from products where price < 44;
select * from products where price <= 99.99 and price >= 22.50;
update products set price = price - 20 where price > 20;
delete from products where price < 25;
update products set price = price + 20 where price > 0;
update products set can_be_returned = true where price > 0; 
