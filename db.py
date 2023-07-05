import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE student(
            id integer primary key,
            name text,
            age text,
            rollno text,
            dob text,
            gender text,
            contact text,
            address text
        )
        """

        self.con.commit()
    # Insert function
    def insert(self,name, age, rollno, dob, gender, contact, address):
        self.cur.execute("insert into student values(NULL,?,?,?,?,?,?,?)", (name, age, rollno, dob, gender, contact, address))
        self.con.commit()
    #fetch all data from db
    def fetch(self):
        self.cur.execute("SELECT * from student")
        rows=self.cur.fetchall()
        return rows
    #delete a record in db
    def remove(self,id):
        self.cur.execute("delete from student where id=?", (id,))
        self.con.commit()
    #update a record in db
    def update(self,id,name, age, rollno, dob, gender, contact, address):
        self.cur.execute("update student set name=?, age=?, rollno=?, dob=?, gender=?, contact=?, address=?)", (name, age, rollno, dob, gender, contact, address))
        self.con.commit()



