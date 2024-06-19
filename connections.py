# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:28:08 2024

@author: guspa

Objetivo: Centraliza as conexões

"""

## Import packages
import pandas as pd
import sqlalchemy


def get_connection():
    database_username = 'root'
    database_password = 'Grumysql'
    database_host     = 'localhost'
    database_port     = '3306'
    database_name     = 'grupo_economico'
    
    # Criação da string de conexão
    connection_string = f'mysql+mysqlconnector://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}'
    
    # Criação do engine usando sqlalchemy
    engine = sqlalchemy.create_engine(connection_string)
    
    return engine

def query_mysql_to_dataframe(query):
    # Cria a conexão
    engine = get_connection()
    
    # Executa a consulta e carrega os dados em um DataFrame
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    
    return df