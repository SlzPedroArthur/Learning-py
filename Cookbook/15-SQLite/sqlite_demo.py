import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute('''CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#          )''')
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Anna', 'Vieira', 90000)
emp_3 = Employee('Pedro', 'Freitas', 9000000)

c.execute('INSERT INTO employees VALUE (?, ?, ?)', (emp_1.first, emp_1.last, emp_3.pay))

conn.commit()

c.execute('INSERT INTO employees VALUES (:first, :last, :pay)', {'first': emp_2.first, 'last' : emp_2.last, 'pay' : emp_2.pay})

# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

# conn.commit()


c.execute("SELECT * FROM employees WHERE last = 'Schafer'")

print(c.fetchall())

conn.commit()

conn.close()