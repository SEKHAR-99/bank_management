from database.connection import DatabaseConfig

# table creation function
def createTables():
    db_config = DatabaseConfig()
    # cursor object creation
    cursor = db_config.cursor()

    # tables query
    accounts_table_query = """create table if not exists accounts(
                            account int unsigned not null,
                            password varchar(30) not null,
                            primary key(account)
                        );"""

    user_table_query = """create table if not exists users(
                        userid int unsigned not null,
                        account int,
                        username varchar(50) not null,
                        email varchar(50) not null unique,
                        balance int unsigned not null,
                        created_at timestamp default current_timestamp,
                        primary key(userid),
                        foregin key(account) references accounts(account)
                    );"""


    Transactions_table_query = """create table if not exists transactions(
                                transactionid int unsigned not null,
                                account int,
                                transactiontype enum('DEBIT', 'CREDIT'),
                                amount int not null,
                                created_at timestamp default current_timestamp,
                                primary key(transactionid),
                                foregin key(account) references accounts(account)
                            );"""
    cursor.execute(accounts_table_query)
    cursor.execute(user_table_query)
    cursor.execute(Transactions_table_query)

    db_config.commit()
    cursor.close()
    db_conifg.close()