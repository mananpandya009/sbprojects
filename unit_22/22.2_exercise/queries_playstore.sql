-- Comments in SQL Start with dash-dash --
-- Exercise 22.1  Part 4
select * from analytics where id=1880;
select id,app_name from analytics where last_updated = '2018-08-01';
select category, count(*) as total_apps from analytics group by category; 
select app_name,reviews from analytics order by reviews desc limit 5; 
select app_name, reviews, rating from analytics where rating > 4.8 order by reviews desc limit 1;  
select category, avg(rating) as avg_rating from analytics group by category order by avg_rating desc;
select app_name, price, rating from analytics where rating < 3 order by price desc limit 1;   
select * from analytics where min_installs <= 50 and rating is not null order by rating desc; 
select app_name from analytics where rating < 3 and reviews > 10000;       
select app_name, reviews, rating, price from analytics where price >= 0.10 and price <= 1.00 order by reviews desc limit 10; 
select * from analytics order by last_updated asc limit 1;
select * from analytics order by price desc limit 1;
select sum(reviews) as total_reviews from analytics;
select category, count(*) from analytics group by category where count(*) > 300; 
select category, count(*) from analytics group by category having count(*) > 300; 
