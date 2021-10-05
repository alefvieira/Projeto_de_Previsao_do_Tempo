import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect("previsao_tempo.db")
        cursor = con.cursor()

    except Error as ex:
        print("Erro ao conectar: ",ex)
    return con
# CASO SEJA NECESSARIO REABRIR A CONEXAO COM O BANCO DE DADOS
vcon=ConexaoBanco()

