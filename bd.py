       
import mysql.connector
from listar import *
from datetime import date

import sqlite3
import pandas as pd


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="adhans"
)
  
def exame(diretorio,grupo):
  arquivos = listardiretorio(diretorio)
  arq2 = []
  

  for arq in arquivos:
    arq2.append(arq[0:2])

  for sigla in sorted(set(arq2)):
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO exame (grupo, data, sigla) VALUES (%s, %s, %s)"
    val = (grupo, date.today(),sigla)
    mycursor.execute(sql, val)
    mydb.commit()
    
    
def histamina(grupo,sigla, tempo):
     
    
  mycursor = mydb.cursor()
  sql = "INSERT INTO histamina (grupo, data, sigla, tempo) VALUES (%s, %s, %s, %s)"
  val = (grupo, date.today(),sigla, tempo)
  mycursor.execute(sql, val)
  mydb.commit()

def dados(rgb, hsv, hls, nome, tempo, lesao,num):
  
  mycursor = mydb.cursor()
  sql = "INSERT INTO dados (foto,tempo, r,g,b,h1,s1,v,h2,l,s2,lesao,total_pixels) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,%s,%s)"
  val = (nome, tempo,rgb[0],rgb[1],rgb[2],hsv[0],hsv[1],hsv[2],hls[0],hls[1],hls[2],lesao,num)
  mycursor.execute(sql, val)
  mydb.commit()
    
    
def get_dados(nome):
      
  mycursor = mydb.cursor()
  
  sql = "SELECT * FROM dados WHERE foto ='%s'" %nome 
  print(sql)
  #val = (nome,rgb[0],rgb[1],rgb[2],hsv[0],hsv[1],hsv[2],hls[0],hls[1],hls[2],lesao)
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  
  #sql_query = pd.read_sql_query("SELECT * FROM dados WHERE foto ='%s'" %nome )
  
  
  return myresult
  
def dados_pd(nome):
  mycursor = mydb.cursor()
  df = pd.read_sql_query("SELECT * FROM dados WHERE foto ='%s'" %nome, mydb)
  return df

#exame("roi dentro","h1")

def lesao_pd(local):
  mycursor = mydb.cursor()
  df = pd.read_sql_query("SELECT * FROM dados WHERE lesao ='%s'" %local, mydb)
  return df


def todos_dados():
  mycursor = mydb.cursor()
  df = pd.read_sql_query("SELECT * FROM dados", mydb)
  return df


def dados_padra(rgb, hsv, hls, nome, tempo ):
      
  mycursor = mydb.cursor()
  sql = "INSERT INTO dados_padronizados (foto,tempo, r,g,b,h1,s1,v,h2,l,s2) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
  val = (nome, tempo,rgb[0],rgb[1],rgb[2],hsv[0],hsv[1],hsv[2],hls[0],hls[1],hls[2])
  mycursor.execute(sql, val)
  mydb.commit()
  
def dados_padra_semtime(rgb, hsv, hls, nome ):
      
  mycursor = mydb.cursor()
  sql = "INSERT INTO dados_pad_lesao_time (grupo,r,g,b,h1,s1,v,h2,l,s2) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
  val = (nome, rgb[0],rgb[1],rgb[2],hsv[0],hsv[1],hsv[2],hls[0],hls[1],hls[2])
  mycursor.execute(sql, val)
  mydb.commit()


def get_dados_pad_les_tim():
  mycursor = mydb.cursor()
  df = pd.read_sql_query("SELECT * FROM dados_pad_lesao_time " , mydb)
  return df

def probabilidade(rgb, hsv, hls, grupo,menor ):
      
  mycursor = mydb.cursor()
  sql = "INSERT INTO probabilidade (grupo,r,g,b,h1,s1,v,h2,l,s2,menor_que) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)"
  val = (grupo, rgb[0],rgb[1],rgb[2],hsv[0],hsv[1],hsv[2],hls[0],hls[1],hls[2],menor)
  mycursor.execute(sql, val)
  mydb.commit()
  
def get_dados_pad():
  mycursor = mydb.cursor()
  df = pd.read_sql_query("SELECT * FROM dados_padronizados " , mydb)
  return df