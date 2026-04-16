/*
a)  When you expand columns in the actor table, you can see thhe of the column names.
b) When you expand columns in the film table it shows all the column names.
c) the table that has both film_id and actor_id is the film_actor table.
d) THe table includes data about movie rentlas, returns, who rented it, and last updated. This data is hard to hread due to the fact its all id numbers that id have to look up sepratly.alter
e) The table shows inventory_id,film_id, and store_id.
f) I feel like i would need  the tables film and rental. these tables are related by both having rental_date in their tables.
*/

select rental_date from rental;
select film_id from film;
