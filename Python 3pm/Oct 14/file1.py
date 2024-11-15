'''
file handling : for managing files 

.py
.programming files
.excel 
.word file
.bin 
.db file    
'''

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost')

cursor = cnx.cursor()


# cursor.execute("CREATE DATABASE Universal")
cursor.execute("SHOW DATABASES")



for x in cursor: 
    print(x)
print(cnx)
cnx.close()