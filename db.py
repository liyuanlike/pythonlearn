import mysql.connector as mc
conn = mc.connect(host='localhost', user='rubb1sh', password='rubb1sh',
                  database='test2')
cursor = conn.cursor()
cursor.execute('create table student(id varchar(20) not null auto_increment,name varchar(20),city varchar(20),primary key(id))')
cursor.execute('insert into student(name, city) values(%s, %s)',['rubb1sh', 'yulin'])
cursor.rowcount
conn.commit()
cursor.close()
