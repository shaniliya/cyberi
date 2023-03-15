import sqlite3
import os

dbname= "babynames-gendered-2015 (1).sqlite"
def DB_Change(dbname, sql):
    connection = sqlite3.connect(dbname)  # create DB and connect
    cursor = connection.cursor()  # initialize
    cursor.execute(sql)  # what to do
    connection.commit()  # Done!!

def get_data(dbname, sql):
    connection = sqlite3.connect(dbname)  # create DB and connect
    cursor = connection.cursor()  # initialize
    cursor.execute(sql)
    data = cursor.fetchall()
    new_data = []
    for row in data:
        try:
            new_data.index(row[0])
        except ValueError:
            new_data.append(row[0])
    print(new_data)
    return new_data



def add():
    sql_add = f"INSERT INTO costumers VALUES ('{first_name}','{last_name}','{tel_num}','{email}',{age},{is_member})"
    DB_Change(dbname,sql_add)

def deli():
    sql_del =f"DELETE FROM costumers WHERE state != 'AK'"
    DB_Change(dbname,sql_del)


def show():
    sql_show = " SELECT state FROM gendered_names "
    listi = get_data(dbname, sql_show)#.remove("('").split("',)\n")
    return listi
#DB_Change(dbname,sql_create_db)


def make_folders(listi):
    for state in listi:
        #os.mkdir(state)
        os.rmdir(state)
make_folders(show())
