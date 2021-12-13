from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase("QSQLITE", "db")
db.setDatabaseName("D:\PDF files Vinuni 1st year\Second Year\Fall Semester 2021\MATH2020 - Discrete Mathematics\Mini Project\Official version\SQLDatabase\data.sqlite")
db.open()

RememberMe = QtSql.QSqlDatabase.addDatabase("QSQLITE", "RememberMe")
RememberMe.setDatabaseName("D:\PDF files Vinuni 1st year\Second Year\Fall Semester 2021\MATH2020 - Discrete Mathematics\Mini Project\Official version\SQLDatabase\RememberMe.sqlite")

RememberMe.open()

query = QtSql.QSqlQuery(db)
query.exec_("create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL);")
# Example: query.exec_("insert into userdata (username, email, password) values('lammartial', 'lamvo0912@gmail.com', '091202');")

query1 = QtSql.QSqlQuery(RememberMe)
query1.exec_("create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL);")




