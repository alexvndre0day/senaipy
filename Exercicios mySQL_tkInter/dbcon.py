import mysql.connector

def criar_conexao():
	return mysql.connector.connect(host="localhost", user="root", password="", database="aula18set")

conn = criar_conexao()
