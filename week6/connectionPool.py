# Connection Pool就像是政府先與捷安特(資料庫)一次下單/付款/交貨10台ubike(connection)存放於ubike站 (connection pool) 供民眾租借使用，民眾若不使用時就返還到ubike站(connection pool)可供其他人使用；會比民眾每個人自己去跟捷安特(資料庫)下單/付款/交貨(連結資料庫)，還要來得有效率且安全。
# connection pool 的功能是作為 connection 的「快取區」，基本的使用流程是在程式一啟動就向資料庫建立一定數量的連線，
# 並存放於 connection pool 裡，後續程式 getConnection() 時是直接向 connection pool  取用，用完後呼叫 connection.close() 就會放回 connection pool
# 下方為以mysql-connector-python，實作Connection Pool：

import mysql.connector
from mysql.connector import pooling

conPool = pooling.MySQLConnectionPool(user='root', password='password', host='localhost', database='website', pool_name='websiteConPool', pool_size=10)

con1 = conPool.get_connection()
con2 = conPool.get_connection()

cursor = con1.cursor()
cursor.execute('SELECT * FROM member')
result = cursor.fetchall()
print(result)

cursor.close()
con1.close()
con2.close()

