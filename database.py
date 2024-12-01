import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", # https://db.danielkong.com/database, 129.154.34.23
  #host="127.0.0.1",
  user="root",
  password="",
  database="test_database"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE test_database")


# mycursor.execute("SELECT * FROM students")

# myresult = mycursor.fetchall()

# print(type(myresult))

# for x in myresult:
#   print(x)

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)

mydb.commit()