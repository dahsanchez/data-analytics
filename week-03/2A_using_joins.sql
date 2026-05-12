use northwind;

-- 1. Create a single query to list the product id, product name, unit price and category 
-- name of all products. Order by category name and within that, by product name.
select * from products;
select * from categories;

select
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName
from	
	products
join
	categories
on	
	products.CategoryID = categories.CategoryID
Order by
	CategoryName, ProductName;
    
-- 2. Create a single query to list the product id, product name, unit price and supplier 
-- name of all products that cost more than $75. Order by product name.
select * from products;
select * from suppliers;

select 
	ProductID,
    ProductName,
    UnitPrice,
    CompanyName
from
	products
join
	suppliers
on	
	products.SupplierID = suppliers.SupplierID
Order by
	ProductName;
    
-- 3. Create a single query to list the product id, product name, unit price, category name, 
-- and supplier name of every product. Order by product name.
select * from products;
select * from categories;
select * from supppliers;

select 
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName,
    CompanyName
from
	products
join
	categories
on 
	products.CategoryID = categories.CategoryID
join
	suppliers
on
	products.SupplierID = suppliers.SupplierID
order by
	ProductName;
    
-- 4. Create a single query to list the order id, ship name, ship address, and shipping 
-- company name of every order that shipped to Germany. Assign the shipping company 
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it 
-- shipped to.
select * from orders;
select * from shippers;

select 
	OrderID,
    ShipName,
    ShipAddress,
    CompanyName as Shipper
from
	orders
join
	shippers
on 
	orders.ShipVia = shippers.ShipperID
where 
	orders.ShipCountry = 'Germany'
order by
	Shipper, ShipName;
-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by 
-- ship name, with a count of how many orders were shipped for that ship name.
select 
    ShipName,
	count(*) as OrderCount
from
	orders
join
	shippers
on 
	orders.ShipVia = shippers.ShipperID
where 
	orders.ShipCountry = 'Germany'
group by
	ShipName
order by
	ShipName;
    
-- 6. Create a single query to list the order id, order date, ship name, ship address of all 
-- orders that included Sasquatch Ale.
-- ∗ Hint: You will need to join on three tables to accomplish this. (One of these tables 
-- has a sneaky space in the name, so you will need to surround it with backticks, like 
-- this: `table name`)
select * from orders;
select * from products;
select * from `order details`;

SELECT
    orders.OrderID,
    OrderDate,
    ShipName,
    ShipAddress
FROM orders 
JOIN `order details` 
    ON orders.OrderID = `order details`.OrderID
JOIN products
    ON `order details`.ProductID = products.ProductID
WHERE products.ProductName = 'Sasquatch Ale';
