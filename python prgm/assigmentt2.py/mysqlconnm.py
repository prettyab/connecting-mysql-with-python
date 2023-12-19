# import mysql.connector
# host='localhost'
# user='root'
# password='root123'
# database='sys'
# conn=mysql.connector.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )
# cursor=conn.cursor()
# create_table_sql = """CREATE TABLE IF NOT EXISTS rolls(EnrollmentID int PRIMARY KEY,Student name varchar(224),CourseID int)"""
# cursor.execute(create_table_sql)
# conn.commit()
# sql="insert into rolls(EnrollmentID int PRIMARY KEY,Student name varchar(224),CourseID int)values(%s,%s,%s)"
# val=(1, 'anu', 101),(2, 'siji', 102),(3, 'suja', 101)
# cursor.execute(sql,val)
# conn.commit()
# cursor.close()
# conn.close()
# import mysql.connector

# host = 'localhost'
# user = 'root'
# password = 'root123'
# database = 'sys'

# conn = mysql.connector.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )
# cursor = conn.cursor()

# # create_table_sql = """CREATE TABLE  rolls(
# #                         EnrollmentID int PRIMARY KEY,
# #                         StudentName varchar(224),
# #                         CourseID int)"""

# # cursor.execute(create_table_sql)
# conn.commit()

# sql = "INSERT INTO rolls (EnrollmentID, StudentID, CourseID) VALUES (%s, %s, %s)"
# val = (1, 44, 101), (2, 21, 102), (3, 20, 101)

# cursor.executemany(sql, val)
# conn.commit()

# cursor.close()
# conn.close()

