import mysql.connector

# Replace with your database credentials
host = "localhost"
user = "root"
password = "root123"
database = "sys"

# Establish a connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor
cursor = conn.cursor()

# Create the Customers table if it doesn't exist
create_table_sql = """
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    PhoneNumber VARCHAR(20)
)
"""

cursor.execute(create_table_sql)

# Commit the changes
conn.commit()

# Example SQL query
sql = "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber) VALUES (%s, %s, %s, %s, %s)"
val = (4, "Jiji", "Gomez", 'jiji@gmail.com', '46765587')
cursor.execute(sql, val)

# Commit the changes
conn.commit()


# Close the cursor and connection
cursor.close()
conn.close()
