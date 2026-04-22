use northwind;

-- Write a query to list the product id, product name, and unit price of every product. This 
-- time, display them in ascending order by price.
select
	ProductID,
    ProductName,
    UnitPrice
from
	products
order by 
	UnitPrice ASC;

-- What are the products that we carry where we have at least 100 units on hand? Order 
-- them in descending order by price.
select
	ProductName,
    UnitPrice,
    UnitsInStock
from
	products
where 
	UnitsInStock >= 100
order by
	UnitPrice ASC;

-- What are the products that we carry where we have at least 100 units on hand? Order 
-- them in descending order by price. If two or more have the same price, list those in 
-- ascending order by product name. 
select
	ProductName,
    UnitPrice,
    UnitsInStock
from
	products
where 
	UnitsInStock >= 100
order by
	UnitPrice Desc,
    ProductName ASC; 
    
-- Write a query against the orders table that displays the total number of distinct 
-- customers who have placed orders, based on customer ID. Use an alias to label the 
-- count calculation as CustomerCount.
select 
distinct
	CustomerID
as
	CustomerCount
from
	orders;
	
-- Write a query against the orders table that displays the total number of distinct 
-- customers w o have placed orders, by customer ID, for each country where orders 
-- have been shipped. Again, use an alias to label the count as CustomerCount. Order 
-- the list by the CustomerCount, largest to smallest. 
select
	ShipCountry,
count(distinct CustomerID) as CustomerCount
from
	orders
Group by
	ShipCountry
Order by
	CustomerCount desc; 

-- What are the products that we carry where we have less than 25 units on hand, but 1 
-- or more units of them are on order? Write a query that orders them by quantity on 
-- order (high to low), then by product name.
select
	ProductName,
    UnitsInStock,
    UnitsOnOrder
from
	products
where
	UnitsInStock < 25 and UnitsOnOrder >= 1
ORDER BY
	UnitsOnOrder desc, ProductName;

-- Write a query to list each of the job titles in employees, along with a count of how 
-- many employees hold each job title.
select
	Title,
Count(distinct EmployeeID) as TitleCount
from
	employees
Group by
	Title;
    
-- What employees have a monthly salary that is between $2000 and $2500? Write a 
-- query that orders them by job title.
select
	Salary,
    FirstName,
    LastName,
    Title
from employees
where
	Salary BETWEEN 2000 and 2500
order by
	Title;