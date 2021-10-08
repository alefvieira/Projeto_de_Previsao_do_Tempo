import Conexao_BD
import pandas as pd
import numpy as np
import xmltodict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from urllib.request import urlopen
from sqlite3 import Error
import json
import os
from PIL import Image
import requests

# ESSA FUNÇÃO FAZ O UPDATE, INSERT E CREATE NO BANCO DE DADOS
def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Ação realizada com sucesso !")
    except Error as ex:
        print(ex)
    # finally:
    #     print("Operação Realizada com sucesso") 

# ESSA FUNÇÃO FAZ O SELECT
def consultar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        conexao.commit()
        return resultado

    except Error as ex:
        print(ex)

def chamaXML():
    # VAI PEGAR TODAS AS INFORMAÇÕES DA XML
    file = urlopen('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    dataxml = pd.DataFrame(data['capitais']['metar'])
    # O COMANDO LOC[[]] SERVE PARA SELECINAR A LINHA DA DATAFRAME
    return data


def criarTabelas():
    sql = "CREATE TABLE IF NOT EXISTS capitais(codigo text primary key, capital text, uf text, regiao text)"
    # paramentro criando a conexão com o banco e enviando o comando sql
    query(Conexao_BD.vcon, sql)

    sql = "CREATE TABLE IF NOT EXISTS valores(codigo text UNIQUE, atualizacao text, pressao integer, temperatura integer, tempo text, tempo_desc text, umidade integer, vento_dir integer, vento_int integer, intensidade text, FOREIGN KEY(codigo) REFERENCES capitais(codigo))"
    query(Conexao_BD.vcon, sql)

def insertCapitais():
    sql = """INSERT INTO capitais(codigo, capital, uf, regiao) VALUES 
    ('SBAR',	'Aracaju'		,'SE','Nordeste'),
    ('SBBE',	'Belém'			,'PA','Norte'),
    ('SBCF',	'Belo Horizonte','MG','Sudeste'),
    ('SBBV',	'Boa Vista'		,'RR','Norte'),
    ('SBBR',	'Brasília'		,'DF','Centro-Oeste'),
    ('SBCG',	'Campo Grande'	,'MS','Centro-Oeste'),
    ('SBCY',	'Cuiabá'		,'MT','Centro-Oeste'),
    ('SBCT',	'Curitiba'		,'PR','Sul'),
    ('SBFL',	'Teresina'		,'SC','Sul'),
    ('SBFZ',	'Fortaleza'		,'CE','Nordeste'),
    ('SBGO',	'Goiânia'		,'GO','Centro-Oeste'),
    ('SBJP',	'João Pessoa'	,'PB','Nordeste'),
    ('SBMQ',	'Macapá'		,'AP','Norte'),
    ('SBMO',	'Maceió'		,'AL','Nordeste'),
    ('SBMN',	'Manaus'		,'AM','Norte'),
    ('SBNT',	'Natal'			,'RN','Nordeste'),
    ('SBPA',	'Porto Alegre'	,'RS','Sul'),
    ('SBPV',	'Porto Velho'  	,'RO','Norte'),
    ('SBRF',	'Recife'  		,'PE','Nordeste'),
    ('SBRB',	'Rio Branco'	,'AC','Norte'),
    ('SBRJ',	'Rio de Janeiro','RJ','Sudeste'),
    ('SBSV',	'Salvador'		,'BA','Nordeste'),
    ('SBSL',	'São Luís'		,'MA','Nordeste'),
    ('SBSP',	'São Paulo'		,'SP','Sudeste'),
    ('SBTE',	'Teresina'    	,'PI','Nordeste'),
    ('SBVT',	'Vitória'		,'ES','Sudeste')"""
    
    query(Conexao_BD.vcon, sql)

# FUNÇÃO QUE GERA O ARQUIVO JSON
def funcao_json(nome_arquivo, sql):
    
    dados_capitais = consultar(Conexao_BD.vcon, sql)
    # print("teste",dados_capitais)

    with open(f'static/{nome_arquivo}.json', 'w', encoding='utf-8') as f:
        json.dump(dados_capitais, f, ensure_ascii=False)

def criaConteudoJSON():
    compara =  function_compara()

    if compara == True:
        sql_v = "SELECT capitais.capital, valores.codigo, valores.atualizacao, valores.pressao, valores.temperatura, valores.tempo, valores.tempo_desc, valores.umidade, valores.vento_dir, valores.vento_int, valores.intensidade, capitais.regiao FROM valores, capitais WHERE capitais.codigo = valores.codigo" 
        dados_capitais = consultar(Conexao_BD.vcon, sql_v)
        
        with open(f'static/conteudo_secao.json', 'w', encoding='utf-8') as f:
            json.dump(dados_capitais, f, ensure_ascii=False)
    
# funcao_json("valores", "SELECT * FROM valores")
# funcao_json("capitais", SELECT * FROM capitais)
#_____________________

def insertValores():
    sql = f"INSERT or REPLACE INTO valores  VALUES ('{data[i]['codigo']}','{data[i]['atualizacao']}',{int(data[i]['pressao'])},{int(data[i]['temperatura'])},'{data[i]['tempo']}','{data[i]['tempo_desc']}',{int(data[i]['umidade'])},{int(data[i]['vento_dir'])},{int(data[i]['vento_int'])},'{data[i]['intensidade']}') " 
    query(Conexao_BD.vcon, sql)

#ADICIONAR OS GRAFICOS
def query_cria_grafico(tygrafico):
    compara =  function_compara()

    #ESSE IF VAI IMPERDIR QUE OS MESMOS GRAFICOS SE REPITAM
    if compara == True:
        # ESTRUTURA DE REPETIÇÃO QUE VAI GERAR OS GRAFICOS
        lista_graficos = ['Nordeste' , 'Norte', 'Centro-Oeste', 'Sul', 'Sudeste']

        for repet in lista_graficos:
            sql = f"SELECT  capitais.capital, valores.pressao, valores.temperatura, valores.umidade, valores.vento_dir, valores.vento_int, valores.atualizacao FROM valores, capitais WHERE valores.codigo = capitais.codigo  and capitais.regiao = '{repet}'"
            res = consultar(Conexao_BD.vcon, sql)

            dic = {
                'capital': "",
                'pressao': "",
                'temperatura': "",
                'umidade': "",
                'vento_dir': "",
                'vento_int': "",
            }
            colunas = pd.DataFrame(res) # ESSE METODO COLOCA NOMES NAS COLUNAS
            # print(colunas)
            dic['capital'] = colunas[0]
            dic['pressao'] = colunas[1]
            dic['temperatura'] = colunas[2]
            dic['umidade'] = colunas[3]
            dic['vento_dir'] = colunas[4]
            dic['vento_int'] = colunas[5]

            # sns.set(rc={'figure.figsize': (7.2, 5), 'font.size': 5})
            # sns.set(rc={})    width: 642px;height: 483px;
            plt.rcParams.update({'figure.figsize': (7.5, 5.1), 'font.size': 9})

            if tygrafico == 'pressao':
                colunas = pd.DataFrame(dic, columns=['capital', 'pressao'])
                plot = sns.barplot(data=colunas, x='capital', y='pressao')

            elif tygrafico == 'temperatura': 
                colunas = pd.DataFrame(dic, columns=['capital', 'temperatura'])
                plot = sns.barplot(data=colunas, x='capital', y='temperatura')

            elif tygrafico == 'umidade': 
                colunas = pd.DataFrame(dic, columns=['capital', 'umidade'])
                plot = sns.barplot(data=colunas, x='capital', y='umidade')

            elif tygrafico == 'vento_dir': 
                colunas = pd.DataFrame(dic, columns=['capital', 'vento_dir'])
                plot = sns.barplot(data=colunas, x='capital', y='vento_dir')
                
            elif tygrafico == 'vento_int': 
                colunas = pd.DataFrame(dic, columns=['capital', 'vento_int'])
                plot = sns.barplot(data=colunas, x='capital', y='vento_int')
            
            else: break

            plot.get_figure().savefig(f"static/graficos/grafico_{repet}_{tygrafico}.png")
            plt.close()
            
            # esse metodo vai selecionar a imagem e vai exclui-la da pasta
            imagem = Image.open(os.path.join(f"static/graficos/grafico_{repet}_{tygrafico}.png")) # vai selecionar a imagem
            redimencionarImagem = imagem.resize((550, 400)) # vai redimencionar a imagem
            nome_sem_ext = os.path.splitext(f"static/graficos/grafico_{repet}_{tygrafico}.png")[0]

            redimencionarImagem.save(os.path.join(nome_sem_ext+ '.gif' )) # vai salvar a imagem como o novo formato
        # os.remove(f"static/graficos/grafico_{repet}_{tygrafico}.png")
        
        # from datetime import  date
        # data_e_hora_atuais = date.today()
        # print(data_e_hora_atuais)


    print("FEITO")
 

# query_cria_grafico('umidade')
# query_cria_grafico('pressao')
# query_cria_grafico('temperatura')
# query_cria_grafico('vento_dir')
# query_cria_grafico('vento_int')

# FUNÇÃO QUE ATUALIZA O BANCO DE DADOS E CHAMA AS FUNÇÕES DE GERAR GRAFICOS E ATUALIZAR JSON
def atualizarValores():
    compara =  function_compara()
    data = chamaXML()

    dec = data['capitais']['metar']
    # print(f"{compara[0][0]} : {dec[0]['atualizacao']}")
    if compara == True:
        for i in  range(0, len(dec)):
            if dec[i]['tempo_desc'] ==  "PredomÃ­nio de Sol":
                dec[i]['tempo_desc'] = "Predomínio de Sol"
            if dec[i]['tempo_desc'] == "Chuvas periÃ³dicas":
                dec[i]['tempo_desc'] = "Chuvas Periódicas"

            sql = f"INSERT or REPLACE INTO valores  VALUES ('{dec[i]['codigo']}','{dec[i]['atualizacao']}',{int(dec[i]['pressao'])},{int(dec[i]['temperatura'])},'{dec[i]['tempo']}','{dec[i]['tempo_desc']}',{int(dec[i]['umidade'])},{int(dec[i]['vento_dir'])},{int(dec[i]['vento_int'])},'{dec[i]['intensidade']}') " 
            query(Conexao_BD.vcon, sql)
        criaConteudoJSON() # VAI ATUALIZAR O ARQUIVO JSON
        
    # else: 
    #     print("ESTÃO IGUAIS OU DEU ERRO")
def function_compara():
    sql_compara = "SELECT atualizacao FROM valores where codigo = 'SBBE'"
    compara = consultar(Conexao_BD.vcon, sql_compara)

    data = chamaXML()
    dec = data['capitais']['metar']

    if compara[0][0] != dec[0]['atualizacao']:
        return True
    print('False')
    return False


# print(compara)
# criarTabelas()
# insertCapitais()
# insertValores()
# atualizarValores()

