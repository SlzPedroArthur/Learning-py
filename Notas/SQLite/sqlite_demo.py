import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:') #connect('db_NAME.db')

c = conn.cursor()

c.execute('''CREATE TABLE employees (
            first text,
            last text,
            pay integer
         )''')

def insert_emp(emp):
   with conn:
      c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp.first, 'last' : emp.last, 'pay' : emp.pay})

def get_emps_by_lastname(lastname):
   c.execute("SELECT * FROM employees WHERE last = :last", {'last' : lastname})
   return c.fetchall()

def update_pay(emp, pay):
   with conn:
      c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
               {'first' : emp.first, 'last' : emp.last, 'pay' : pay})

def remove_emp(emp):
   with conn:
      c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first' : emp.first, 'last' : emp.last})

emp_1 = Employee('Anna', 'Vieira', 90000)
emp_2 = Employee('Pedro', 'Freitas', 900000)
emp_3 = Employee('João', 'Freitas', 80000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

emps = get_emps_by_lastname('Freitas')
print(emps)

update_pay(emp_2, 12000000)
remove_emp(emp_3)

emps = get_emps_by_lastname('Freitas')
print(emps)
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp_2.first, 'last' : emp_2.last, 'pay' : emp_2.pay})

# conn.commit()

# c.execute('INSERT INTO employees VALUES (:first, :last, :pay)', {'first': emp_3.first, 'last' : emp_3.last, 'pay' : emp_3.pay})

# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last =:last", ('Vieira',) )
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last =:last", {'last' : 'Freitas'})
# print(c.fetchall())

# conn.commit()
conn.close()