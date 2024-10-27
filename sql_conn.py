import pymysql
import csv

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="MyNewPass",
    database="employee",
    port=3306
)


mycursor=conn.cursor()

# command1="INSERT INTO EMPLOYEE_DETAILS VALUES (%s,%s,%s,%s,%s)"
# val=(101,"Thiru",105,8000,54)
# mycursor.execute(command1,val)

# command2="SELECT * FROM EMPLOYEE_DETAILS"
# mycursor.execute(command2)




# mycursor.execute("SELECT * FROM employee_details")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# arr=[(102, 'John Doe', 1, 55000, 28),
#     (103, 'Jane Smith', 2, 62000, 32),
#     (104, 'Sam Johnson', 1, 58000, 27),
#     (105, 'Chris Lee', 3, 72000, 45),
#     (106, 'Anna Brown', 2, 50000, 24),
#     (107, 'Tom Harris', 1, 54000, 29),
#     (108, 'Nancy White', 4, 68000, 38),
#     (109, 'Steve Black', 3, 75000, 41),
#     (110, 'Sara Green', 2, 53000, 30),
#     (111, 'Michael Blue', 4, 64000, 36)]



# result="update from employee_details set emp_name=%s where emp_id=%s "
# val=("kamal",101)
# mycursor.execute(result,val)
# conn.commit()
# print(mycursor.rowcount, "record(s) affected")

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM employee_details")

myresult = mycursor.fetchall()
header=['emp_id','emp_name','dept_id','salary','age']

with open("data.csv",'w',newline='') as new_file:
    writer=csv.writer(new_file)
    writer.writerow(header)
    writer.writerows(myresult)


  

conn.close()