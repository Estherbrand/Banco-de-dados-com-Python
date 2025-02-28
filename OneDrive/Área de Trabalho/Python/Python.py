import sqlite3

# Conecta ao banco de dados (usando o caminho completo)
db_path = 'C:/Users/deise/OneDrive/Área de Trabalho/Banco_de_dados.db'
Python = sqlite3.connect(db_path)
cursor = Python.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)

#cursor.execute('CREATE TABLE alunos(id INT, nome VARChAR (100), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Deise", 43, "Gestão de Qualidade")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Denise", 43, "Nutrição")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Joao", 22, "Engenharia Mecanica")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Rebeca", 19, "Administração")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Esther", 21, "Medicina")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Maria Eduarda", 18, "Engenharia Mecanica")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Izaque", 25, "Engenharia Mecanica")')

#3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".

cursor.execute('SELECT nome FROM alunos')
for aluno in cursor:
    print(aluno)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in cursor:
    print(aluno)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT nome,curso FROM alunos WHERE curso = "Engenharia Mecanica" ORDER BY nome')
for aluno in cursor:
   print(aluno)

#d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = cursor.fetchone()[0]
print(f"Total de alunos: {total_alunos}")

#4. Atualização e Remoção
#) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 23 WHERE nome = "Joao"')
for aluno in cursor:
  print(aluno)

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=7')
print("Registro deletado com sucesso.")

#5. Criar uma Tabela e Inserir Dados.Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome VARChAR (100), idade INT, saldo FLOAT)')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Rebeca", 18, 5.50)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Esther", 21, 3500.25)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Tatiana", 45, 70000.60)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Miriam", 50, 10000.52)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Adriana", 31, 1500.32)')

# 6 - Consultas e Funções Agregadas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for cliente in cursor:
    nome, idade = cliente
    print(nome, idade)

#b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]
print(f"Saldo médio dos clientes: {saldo_medio}")

#c) Encontre o cliente com o saldo máximo
cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
cliente_max_saldo = cursor.fetchone()
if cliente_max_saldo:
    nome, saldo = cliente_max_saldo
    print(f"Cliente com o saldo máximo: {nome}, Saldo: {saldo}")

#d) Conte quantos clientes têm saldo acima de 100.
cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 100')
saldo_maior_100 = cursor.fetchone()[0]
print(f"Quantidade de clientes com saldo acima de 100: {saldo_maior_100}")

#7- Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico

cursor.execute('UPDATE clientes SET saldo = 2500.5 WHERE nome = "Rebeca"')
cursor.execute('SELECT nome, saldo FROM clientes WHERE nome = "Rebeca"')
for cliente in cursor:
    nome, saldo = cliente
    print(nome, saldo)

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=1')

#8 - Criar uma segunda tabela chamada compras
cursor.execute('''CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY(cliente_id) REFERENCES clientes(id))''')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(4, "Notebook", 2500.00)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(2, "Smartphone", 1500.00)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(3, "Tablet", 800.00)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(5, "Smartwatch", 300.00)')

# Consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id''')
for row in cursor.fetchall():
    nome, produto, valor = row
    print(f"Cliente: {nome}, Produto: {produto}, Valor: {valor}")


Python.commit()
Python.close()
print("Conexão com o banco de dados fechada.")