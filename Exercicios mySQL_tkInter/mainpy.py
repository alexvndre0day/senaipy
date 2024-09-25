from dbcon import criar_conexao

conn = criar_conexao()
cursor = conn.cursor()

query = ("SELECT idCliente, nome, email FROM clientes ")
cursor.execute(query)

for (idCliente, nome, email) in cursor:
  print(f"Cliente ({idCliente}) - {nome} @ {email}")

cursor.close()
conn.close()