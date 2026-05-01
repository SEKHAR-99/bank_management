import mysql.connector as SQLC

# database config
db_config = SQLC.connect(
    host = 'localhost',
    username = 'root',
    password = 'root' # your mysql password
)

# step2
# cursor objects creation
cursor = db_config.cursor()
print(db_config)
print(cursor)

# step3
# excuete method
cursor.execute("CREATE DATABASE IF NOT EXISTS BANK1;")
print(cursor)
cursor.execute('USE BANK1')
print(cursor)
cursor.execute("CREATE TABLE IF NOT EXISTS accounts(acc int, name varchar(30), amount int)")
print(cursor)

query = "insert into accounts(account, name, amount) values(%s. %s, %s)"
cursor.execute(query,(101,"sekhar",2000))
db_config.commit()