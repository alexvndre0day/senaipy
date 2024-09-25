from dbcon import criar_conexao
from tkinter import messagebox
import mysql.connector
    

def InsertData(nome, email):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()       
        query = ("INSERT INTO clientes(nome, email) VALUES (%s, %s)")      
        values = (nome, email)
        cursor.execute(query, values)
        
        conn.commit()  
        messagebox.showinfo('Successo', 'Registro gravado. Valeu')
    except mysql.connector.Error as e:
        messagebox.showinfo('Xiiiiiii', e)
    finally:
        conn.close()