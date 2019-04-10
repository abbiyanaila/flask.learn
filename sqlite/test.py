import sqlite3 #import library

connection = sqlite3.connect('data.db') #initialise the connection, for url

cursor = connection.cursor() #allow to select and start things, cursor (run query and store the result)

create_table = "CREATE TABLE users (id int, username text, password text)" # create table
cursor.execute(create_table) #run query create_table

user = (1, ' desi', 'qwerty')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'fandi', 'qwer'),
    (3, 'ratno', 'aswd')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()