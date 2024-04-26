import psycopg2
import csv

# Подключение к базе данных
connection_params = {
    "host": "localhost",
    "database": "postgres"
}
try:
    con = psycopg2.connect(**connection_params)

    # Открытие CSV файлов и вставка данных в базу
    with con:
        with con.cursor() as cur:
            # Вставка данных клиентов
            with open('north_data/customers_data.csv') as customer_file:
                customer_reader = csv.DictReader(customer_file)
                for customer_row in customer_reader:
                    cur.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        (customer_row['customer_id'], customer_row['company_name'], customer_row['contact_name']))

            # Вставка данных сотрудников
            with open('north_data/employees_data.csv') as employee_file:
                employee_reader = csv.DictReader(employee_file)
                for employee_row in employee_reader:
                    cur.execute(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                        (employee_row['employee_id'], employee_row['first_name'], employee_row['last_name'],
                         employee_row['title'], employee_row['birth_date'], employee_row['notes']))

            # Вставка данных заказов
            with open('north_data/orders_data.csv') as order_file:
                order_reader = csv.DictReader(order_file)
                for order_row in order_reader:
                    cur.execute(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                        (order_row['order_id'], order_row['customer_id'], order_row['employee_id'],
                         order_row['order_date'], order_row['ship_city']))
finally:
    # Закрытие соединения
    con.close()
