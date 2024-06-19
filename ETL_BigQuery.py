 # -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:20:45 2024

@author: guspa

Objetivo: realizar o ETL dos dados da base do BigQuery para dentro do MySQL
É possivel executa o projeto utilizando somente o BigQuery e é mais recomendável, porém será necessario a compra
de uma nova sessão no google, para conseguir executar diversas queries simultâneas;

"""

#%% IMPORTS centralizados

import pandas as pd
from google.oauth2 import service_account
import bigframes.pandas as bpd
import gc

import os
import time
from google.cloud import bigquery
import connections

import sqlalchemy
from sqlalchemy import create_engine as ce

import time
from datetime import datetime


# Unload BigQuery tables - Grupos economicos
def unload_df(table_name, sql_query):
    ini = datetime.now()
       
    print(f'unload_df: Incio da consulta no bigquery')
    df = load_table_Bigquery(sql_query, table_name)
    
    #trata typos campos dataframe
    df = trata_campos_saida(table_name, df)
    
    fim = datetime.now()
    dif = (fim - inicio)
    
    print(f'unload_df: Fim do unload da tabela {table_name} :',dif)
    return df

# load_table_Bigquery Genérico
def load_table_Bigquery(sql_query, base):

    print(f'load_table_Bigquery: Incio da consulta no bigquery: {base}')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GBQ.json'
    client = bigquery.Client()
    
    # Captura o tempo antes da execução do método
    inicio = datetime.now()
    
    print(f'load_table_Bigquery: Inicio do processo query_job {base}: ', datetime.now().strftime('%H:%M:%S'))
    
    query_job = client.query(sql_query)
    
    print(f'load_table_Bigquery: Inicio do processo pre while query_job {base}: ', datetime.now().strftime('%H:%M:%S'))
    
    while query_job.state != 'DONE':
            query_job.reload()
            # check again after 3 seconds
            time.sleep(3)
     
    fim = datetime.now()
    dif = (fim - inicio)
    if query_job.state == 'DONE':
        df = query_job.to_dataframe()
        print("load_table_Bigquery: Tempo de processamento: ", dif)
        return df
    else:
        print(query_job.result())

# Insert MySql
def insert_mySql(table_name, dataframe):    
    print(f'insert_mySql: Cria conexao {table_name} :',datetime.now().strftime('%H:%M:%S'))
    # cria conexao com o MYSql
    engine = get_connection()
    
    # insert ussando lotes de 1000 em 1000
    insert_data_in_chunks(engine, dataframe, table_name, chunk_size=1000)

def get_connection():
    database_username = 'root'
    database_password = 'Grumysql'
    database_host     = 'localhost:3306'
    database_name     = 'grupo_economico'
    
    # Connect to MySQL
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password, 
                                                          database_host, database_name))
    
    return database_connection

def insert_data_in_chunks(engine, dataframe, table_name, chunk_size=1000):
    #captura horario do comeco do processo
    ini = datetime.now()
    
    print(f'insert_data_in_chunks: Inicio do processo de inclusao {table_name}: ',ini.strftime('%H:%M:%S'))
    with engine.connect() as connection:
        for start in range(0, len(dataframe), chunk_size):
            end = start + chunk_size
            chunk = dataframe.iloc[start:end] #recupera 1000 linhas
            chunk.to_sql(name=table_name, con=connection, if_exists='append', index=False)
            #print(f"Inserção via chunk {start} to {end}")
    fim = datetime.now()
    dif = (fim - inicio)
    print(f'insert_data_in_chunks: Fim do processo de inclusao {table_name}: ',dif)

def cria_sql_query(tabela):
        
    if tabela == 'empresas':         #Consulta as empresas da base

        sql_query = '''
            SELECT cnpj_basico
                ,razao_social
                ,porte
            FROM basedosdados.br_me_cnpj.empresas 
            where data = "2023-11-16"
        '''
        return sql_query
    elif tabela == 'socios':         #Consulta os socios
        sql_query = '''
            SELECT cnpj_basico
                ,tipo
                ,nome
                ,documento
                ,qualificacao
                ,faixa_etaria
            FROM basedosdados.br_me_cnpj.socios 
            where data = "2023-11-16"
        '''
        return sql_query
    elif tabela == 'empresa_socios':         #Consulta os empresasVssocios
        sql_query = '''
            SELECT a.cnpj_basico
                  ,a.razao_social
                  ,a.porte
                  ,c.tipo as tipo_socio
                  ,c.nome as nome_socio
                  ,c.documento as doc_socio
                  ,c.qualificacao as qualificacao_socio
                  ,c.faixa_etaria as faixa_etaria_socio
            FROM basedosdados.br_me_cnpj.empresas a 
            INNER JOIN basedosdados.br_me_cnpj.estabelecimentos b on a.cnpj_basico = b.cnpj_basico
                        and b.situacao_cadastral in ("1","2","4") and b.identificador_matriz_filial = "1" 
            INNER JOIN basedosdados.br_me_cnpj.socios c on a.cnpj_basico = c.cnpj_basico and c.data = "2023-11-16"
            where a.data = "2023-11-16" and b.data = "2023-11-16"
        '''
        return sql_query
    else:                           #Consulta os estabelecimentos
        sql_query = '''
            SELECT cnpj_basico
                ,cnpj
                ,nome_fantasia
                ,identificador_matriz_filial
                ,situacao_cadastral
            FROM basedosdados.br_me_cnpj.estabelecimentos 
            where data = "2023-11-16"
            and identificador_matriz_filial = "1"
        '''
        return sql_query

def trata_campos_saida(table_name, df):
    if table_name == 'empresas':         #Consulta as empresas da base
        print(f'trata_campos_saida: Incio do tratamento do dataFrame {table_name}: ' ,datetime.now().strftime('%H:%M:%S'))
        #ajusta colunas do dafa_frame empresas
        return df.astype(dtype= {"cnpj_basico":"object","razao_social":"object","porte":"int"})   
        
    elif table_name == 'socios':         #Consulta os socios
        print(f'trata_campos_saida: Incio do tratamento do dataFrame {table_name}: ' ,datetime.now().strftime('%H:%M:%S'))
        #ajusta colunas do dafa_frame socios
        return df.astype(dtype= {"cnpj_basico":"object","tipo":"int","nome":"object","documento":"object","qualificacao":"int","faixa_etaria":"int"})   
    
    elif table_name == 'empresa_socios':         #Consulta os empresa_socios
        print(f'trata_campos_saida: Incio do tratamento do dataFrame {table_name}: ' ,datetime.now().strftime('%H:%M:%S'))
        #ajusta colunas do dafa_frame empres_socios
        return df.astype(dtype= {"cnpj_basico":"object","razao_social":"object","porte":"int","tipo_socio":"int","nome_socio":"object","doc_socio":"object","qualificacao_socio":"int","faixa_etaria_socio":"int"}) 
    
    else:                           #Consulta os estabelecimentos
        print(f'trata_campos_saida: Incio do tratamento do dataFrame {table_name}: ' ,datetime.now().strftime('%H:%M:%S'))
        #ajusta colunas do dafa_frame estabelecimento
        return df.astype(dtype= {"cnpj_basico":"object","cnpj":"object","nome_fantasia":"object","identificador_matriz_filial":"int","situacao_cadastral":"int"})   
    
    
def control_execucao_tabelas():
    # Dados
    data = {
        'tabela': ['empresas', 'socios', 'estabelecimentos', 'empresa_socios'],
        'status': [True, True, True, True]
    }
    return pd.DataFrame(data)
    
# MAIN
if __name__ == '__main__':
 
    try:
        #TODO: fazer o controle via banco de dados!!!
        tables = control_execucao_tabelas()
        
        for index, row in tables.iterrows():
            table_name = row['tabela']
            if row['status'] == False:
                sql_query = cria_sql_query(table_name)
                
                
                print(f'Main: Inicio processo de unload_df tabela {table_name} :',datetime.now().strftime('%H:%M:%S'))
                df = unload_df(table_name, sql_query)   
                
                print(f'Main: Inicio processo de insert mySql {table_name} :',datetime.now().strftime('%H:%M:%S'))
                insert_mySql(table_name, df) 
                
                print(f'Main: Limpa memoria processo {table_name} :',datetime.now().strftime('%H:%M:%S'))
                #limpeza de memória
                del df
                gc.collect()
                              
            else:
                print(f'Tabela {table_name} já foi carregada anteriormente')
        
        
        """
            query = sql_query()
            
            table_name = 'empresas'
            print(f'Main: Inicio processo de load_df_empresas {table_name} :',datetime.now().strftime('%H:%M:%S'))
            df_empresas = unload_df(table_name, query)      
            
            print(f'Main: Inicio processo de insert mySql {table_name} :',datetime.now().strftime('%H:%M:%S'))
            insert_mySql(table_name, df_empresas)    
            
            print(f'Main: Limpa memoria processo {table_name} :',datetime.now().strftime('%H:%M:%S'))
            #limpeza de memória
            del df_empresas
            gc.collect()
            
            tables.loc[tables[tables['tabela'] == 'empresas'].index, 'status'] = 'true'
           
            """
        
        
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)