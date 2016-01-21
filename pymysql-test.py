#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='hanfeng',
                            db='mysql',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
        # Create a new record
        # sql = '''create table user_table (
        #             user_id INT NOT NULL AUTO_INCREMENT,
        #             user_name VARCHAR(100) NOT NULL,
        #             user_age INT,
        #             submission_date DATE,
        #             PRIMARY KEY (user_id) 
        #         );
        #       '''
        # cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "select version(), current_date;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        print(type(result))
except Exception as e:
    raise e
finally:
    connection.close()
