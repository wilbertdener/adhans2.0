import mysql.connector
from listar import *
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="adhans"
)




#sql = "INSERT INTO usuario (nome, login, senha ) VALUES (%s, %s, %s)"
#val = ("Wilbert","wilbert","")
#mycursor.execute(sql, val)

#mydb.commit()
#mycursor.execute("CREATE TABLE exame (id INT AUTO_INCREMENT PRIMARY KEY,grupo VARCHAR(255), data DATE	)")#id	


#print(mycursor.rowcount, "record inserted.")
"""sql = "INSERT INTO foto (nome	endereco	tempo	id_usuario	id_exame grupo) VALUES (%s, %s)"
val = [
  ('h1-1', '',0,1,),"""




      

def novatabela():
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),login VARCHAR(255),senha VARCHAR(255))")
  #mycursor.execute("CREATE TABLE foto (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),endereco VARCHAR(255),tempo INT,id_usuario	INT,id_exame INT)")#
  #mycursor.execute("CREATE TABLE dados (id INT AUTO_INCREMENT PRIMARY KEY,id_foto INT, r INT, g INT, b INT, h1 INT,	s1 INT, v INT, h2 INT, l INT, s2 INT, lesao BOOLEAN	)")#id	
  #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  #mycursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),login VARCHAR(255),senha VARCHAR(255))")
  #mycursor.execute("CREATE TABLE foto (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),endereco VARCHAR(255),tempo INT,id_usuario	INT,id_exame INT)")#
  #mycursor.execute("CREATE TABLE dados (id INT AUTO_INCREMENT PRIMARY KEY,id_foto INT, r INT, g INT, b INT, h1 INT,	s1 INT, v INT, h2 INT, l INT, s2 INT, lesao BOOLEAN	)")#id	
  #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

  mycursor.execute(sql, val)

  mydb.commit()
  
def novalinha(tabela,colunas,val):
  mycursor = mydb.cursor()
  sql = "INSERT INTO ",tabela," (",colunas,") VALUES (%s, %s, %s)"
  val = [
    ('cont', '2023-06-26','v1-1'),
    ('cont', '2023-06-26','v2-1'),
    ('cont', '2023-06-26','v2-2'),
    ('cont', '2023-07-03','v3-1'),
    ('cont', '2023-07-03','v3-2'),
    ('cont', '2023-07-10','v4-1'),
    ('cont', '2023-07-10','v4-2'),
    ('cont', '2023-07-10','v5-1'),
    ('cont', '2023-08-07','v6-1'),
    ('cont', '2023-08-07','v6-2'),
    ('cont', '2023-08-07','v6-3'),
    ('cont', '2023-08-07','v7-1')
  ]


  mycursor.executemany(sql, val)

  mydb.commit()
  
  
def exame(diretorio,grupo):
  arquivos = listardiretorio(diretorio)
  arq2 = []
  

  for arq in arquivos:
    arq2.append(arq[0:7])

  for sigla in sorted(set(arq2)):
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO exame (grupo, data, sigla) VALUES (%s, %s, %s)"
    val = (grupo, date.today(),sigla)
    mycursor.execute(sql, val)
    mydb.commit()
  


