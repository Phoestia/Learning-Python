import sqlite3
#create data base
db = sqlite3.connect('database.db')
db.execute('drop table if exits person')
db.execute('create table person(firstname text, secondname text, age int)')
db.execute('create table people(firstname text, secondname text, age int)')
