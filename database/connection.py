import mysql.connector as SQLC

def DatabaseConfig():
    db_config = SQLC.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'bank'
    )
    return db_config