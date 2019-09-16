import sqlite3

conn=sqlite3.connect('BankDB.db')
c=conn.cursor()
global i
i=0

class SQLHandler:      
        
    def insert_table(self,data_list):
        global i
        print(data_list)
        print(data_list[0])
        c.execute('CREATE TABLE IF NOT EXISTS DataTable(ID INTEGER PRIMARY KEY,FName TEXT(20),LName TEXT(30),Account_Number INTEGER,Suply INTEGER)')
        c.execute("INSERT INTO DataTable (ID,FName,LName,Account_Number,Suply) VALUES (?,?,?,?,?)",(data_list[i],data_list[i+1],data_list[i+2],data_list[i+3],data_list[i+4]))
        conn.commit()

    def open_search(self,id_search):
        query_string ="SELECT Suply FROM DataTable WHERE ID = (?)"
        intended_suply=c.execute(query_string, (id_search,))
        intended_suply=c.fetchone()
        return intended_suply


    def add_sheets(self,intended_suply,id_search,sheet):
        l=list(intended_suply)
        new_suply=l[0]+sheet
        c.execute("UPDATE DataTable SET Suply = (?) WHERE ID = (?)" ,(new_suply,id_search,))
        conn.commit()

    def sub_sheets(self,intended_suply,id_search,sheet):
        l=list(intended_suply)
        new_suply=l[0]-sheet
        if new_suply>0 :
            c.execute("UPDATE DataTable SET Suply = (?) WHERE ID = (?)" ,(new_suply,id_search,))
            conn.commit()
            return True
        else:
            return False

    def withdraw(self,id_search):
        if c.execute("DELETE FROM DataTable WHERE ID=(?)",(id_search,)):
            conn.commit()
            return True
        else:
            return False

    def show(self):
        c.execute("select * from DataTable")
        data = c.fetchall() #data from database
        return data
