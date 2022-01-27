-- write your queries here
select * from owners join vehicles on owners.id = vehicles.owner_id; 
select first_name, last_name,avgcount(owner_id) from owners join vehicles on owners.id = vehicles.owner_id group by (first_name,last_name); 
select first_name, last_name,avg(price) as average_price,count(owner_id) 
from owners 
join vehicles 
on owners.id = vehicles.owner_id 
group by (first_name,last_name)
having count(owner_id) > 1 and avg(price) > 10000
order by first_name desc;     
