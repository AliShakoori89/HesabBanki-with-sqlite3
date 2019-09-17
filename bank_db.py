import sqlite3


global i
i=0

class SQLHandler:      
    def __init__(self,database='BankDB.db'):
        self.database = database
        self.conn=sqlite3.connect(self.database)
        self.c=self.conn.cursor()

    def insert_table(self,data_list):
        global i
        self.c.execute('SELECT ID FROM DataTable')
        x=self.c.fetchall()
        # print(x)
        # b=str(data_list[i])
        # t=tuple(str(data_list[i]))
        print(t)
        if t in x:
            return False
        else:
            self.c.execute('CREATE TABLE IF NOT EXISTS DataTable(ID INTEGER PRIMARY KEY,FName TEXT(20),LName TEXT(30),Account_Number INTEGER,Suply INTEGER)')
            self.c.execute("INSERT INTO DataTable (ID,FName,LName,Account_Number,Suply) VALUES (?,?,?,?,?)",(data_list[i],data_list[i+1],data_list[i+2],data_list[i+3],data_list[i+4]))
            self.conn.commit()

    def open_search(self,id_search):
        query_string ="SELECT Suply FROM DataTable WHERE ID = (?)"
        intended_suply=self.c.execute(query_string, (id_search,))
        intended_suply=self.c.fetchone()
        return intended_suply


    def add_sheets(self,intended_suply,id_search,sheet):
        l=list(intended_suply)
        new_suply=l[0]+sheet
        self.c.execute("UPDATE DataTable SET Suply = (?) WHERE ID = (?)" ,(new_suply,id_search,))
        self.conn.commit()

    def sub_sheets(self,intended_suply,id_search,sheet):
        l=list(intended_suply)
        new_suply=l[0]-sheet
        if new_suply>0 :
            self.c.execute("UPDATE DataTable SET Suply = (?) WHERE ID = (?)" ,(new_suply,id_search,))
            self.conn.commit()
            return True
        else:
            return False

    def withdraw(self,id_search):
        if self.c.execute("DELETE FROM DataTable WHERE ID=(?)",(id_search,)):
            self.conn.commit()
            return True
        else:
            return False

    def show(self):
        self.c.execute("select * from DataTable")
        data = self.c.fetchall() #data from database
        return data
