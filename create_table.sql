create table employees (
    employee_id int PRIMARY KEY,
    first_name varchar(25),
    last_name varchar(25),
    title text,
    birth_date date,
    notes text
);

create table customers (
    customer_id varchar(5) PRIMARY KEY,
    company_name text,
    contact_name text
);

create table orders (
    order_id int PRIMARY KEY,
    customer_id varchar(5),
    employee_id smallint,
    order_date date,
    ship_city varchar(20),
    foreign key (customer_id) references customers (customer_id)
    match simple on update no action on delete no action,
    foreign key (employee_id) references employees (employee_id)
    match simple on update no action on delete no action
);

