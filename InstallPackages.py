# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:20:45 2024

@author: guspa

Objetivo: importar aplicações e pacotes necessarios para execução do projeto
Também são definidos quais libs são necessárias instalar, para executar o projeto

"""

#%% Instalando pacotes
#!pip install basedosdados # APAGAR

!pip install pandas
!pip install --upgrade pandas_gbq #lib para conseguir criar as conexoes com o bigquery
!pip install mysql-connector-python
!pip install --upgrade bigframes #lib para manipular grandes dataframes = usado para extrair os dados das tabelas do BigQuery
!pip install bigframes google-cloud-bigquery #lib para manipular grandes dataframes = usado para extrair os dados das tabelas do BigQuery
!pip install sqlalchemy
!pip install pyvis
!pip install pandas seaborn matplotlib

#%% Import packages
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

import mysql.connector
from mysql.connector import Error

#import basedosdados as bd # APAGAR

