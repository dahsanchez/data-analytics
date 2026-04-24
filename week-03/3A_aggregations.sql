use northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a 
-- second query to find the name of the product that has that price.
select min(UnitPrice) as CheapestItem
from
products;

select
	ProductName,
    UnitPrice
from
	products
where 
	UnitPrice = 
(select min(UnitPrice) as CheapestItem
from
products);
    
-- 2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help 
-- using the ROUND function to round the average price to the nearest cent.)
select round(avg(distinct UnitPrice),2) as AvgPrice
from 
	products;
    
-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then 
-- write a second query to find the name of the product with that price, plus the name of 
-- the supplier for that product.
select max(UnitPrice) as MostExpensive
from
	products;
    
select
	ProductName,
    UnitPrice,
    CompanyName as SupplierName
from
	products
join
	suppliers
on
	products.SupplierID = suppliers.SupplierID
where
	UnitPrice = 
    (select round(max(UnitPrice),2) as MostExpensive
    from
	products);

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly 
-- salaries).
select round(sum(distinct Salary),2) as MonthlyPayroll
from employees;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any 
-- employee makes. (Just the amounts, not the specific employees!)alter
select 
	round(min(Salary),2) as LowestSalary,
	round(max(Salary),2) as HighestSalary
from
	employees;
    
-- 6. Write a query to find the name and supplier ID of each supplier and the number of 
-- items they supply. Hint: Join is your friend here.
select
	suppliers.SupplierID,
	CompanyName as SupplierName, 
	count(ProductID) as NumberOfItems
from
	suppliers
join
	products
on 
	suppliers.SupplierID = products.SupplierID
group by 
	suppliers.SupplierID, suppliers.CompanyName;

-- 7. Write a query to find the list of all category names and the average price for items in 
-- each category.
select
    categories.CategoryName,
   round(avg(products.UnitPrice),2) as AvgPrice
from 
	categories 
join
	products
on
	categories.CategoryID = products.CategoryID
group by
    categories.CategoryName;
    
-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what 
-- is the name of each supplier and the number of items they supply.
select
	suppliers.CompanyName as SupplierName,
	count(products.ProductID) as NumberOfItems
from
	suppliers
join 
	products 
on
	suppliers.SupplierID = products.SupplierID
group by
	suppliers.SupplierID, suppliers.CompanyName
having 
	count(products.ProductID) >= 5;
-- Write a query to list products currently in inventory by the product id, product name, 
-- and inventory value (calculated by multiplying unit price by the number of units on 
-- hand). Sort the results in descending order by value. If two or more have the same 
-- value, order by product name. If a product is not in stock, leave it off the list.
select
	ProductID,
    ProductName,
    round(UnitPrice * UnitsInStock,2) as InventoryValue
from
	products
where
	UnitsInStock > 0
order by
	InventoryValue desc, ProductName;
