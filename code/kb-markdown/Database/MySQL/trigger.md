# trigger

## introduction

```
use test;

create table sales(id int primary key, product varchar(30) not null, value numeric(10,2));

create table sales_update(
	id int primary key auto_increment, 
	product_id int not null, 
    changed_at timestamp,
	before_value numeric(10,2) not null, 
    after_value numeric(10,2) not null);
    
drop table sales_update;
    
    
insert into sales (id, product, value) values (3, "Cake", 0.80);

select * from sales;

update sales set value = 0.60 where id = 3;

delimiter $$

create trigger before_sales_update before update on sales for each row
begin

	insert into sales_update(product_id, changed_at, before_value, after_value)
		value (old.id, now(), old.value, new.value);

end$$


delimiter ;

select * from sales_update;



```

## validations

```
use test;

drop table products;
create table products (id int primary key auto_increment, value numeric(10,2) not null);


set delimiter $$

create trigger before_products_insert before insert on products for each row
begin

	if new.value > 100.0 then
		set new.value := 100.0;
    end if;

end$$

create trigger before_products_update before update on products for each row
begin

	if new.value > 100.0 then
		set new.value := 100.0;
    end if;

end$$

set delimiter ;


insert into products (value) values (500);

update products set value = 102 where id=1;

select * from products;
```

## trigger and transactions

```
use test;

show tables;

create table sales(id int primary key auto_increment, product varchar(45) not null, sold numeric(8,2) not null);

create table sales_totals(id int primary key auto_increment, total numeric(11,2) not null, day date);

alter table sales_totals add unique (day);

show index from sales_totals;


delimiter $$

create trigger before_sales_insert before insert on sales for each row
begin

	declare today date default date(now());
	declare count int default 0;
    
	select count(*) from sales_totals where day = today into count for update;
    
    if count = 0 then
		insert into sales_totals (total, day) values (new.sold, today);
	else
		update sales_totals set total = total + new.sold where day = today;
	end if;

end$$

delimiter ;

drop trigger before_sales_insert;

select * from sales;
select * from sales_totals;


insert into sales (product, sold) values ("Dog Lead Deluxe", 10.00);


set sql_safe_updates=0;
delete from sales;
delete from sales_totals;



```

## exercise

```


Create a table of animals that includes a text-type column (e.g. varchar or text) called "animal_name".

Create a trigger that prevents you from inserting any animal name containing the word "cat". E.g. "Wildcat", "Housecat", etc.

If someone tries to insert any kind of cat, the trigger should insert "xxx" instead and should log the attempted entry, including the animal name,
in a "violations" table, along with the date and time it occurred.

Animals
primary key
animal name
(anything else)

Violations
primary key
animal name
date and time
```

## exercise solution

```
use test;

create table animals (id int primary key auto_increment, animal_name varchar(50) not null);

create table violations(id int primary key auto_increment, animal_name varchar(50) not null, moment datetime not null);


delimiter $$

create trigger before_animals_insert before insert on animals for each row
begin

	if new.animal_name like "%cat%" then
    
		insert into violations (animal_name, moment) values (new.animal_name, now());
    
		set new.animal_name = "xxx";
    
    end if;

end$$

delimiter ;

insert into animals (animal_name) values ("Housecat");

select * from animals;
select * from violations;
```