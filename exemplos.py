# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:15:38 2024

@author: guspa
"""



#%% Carregando bases via arquivo

"""
empresas0 = pd.read_csv("D:\PosDadosESALQ\TCC\Datas\Empresas0\empresas0.csv", sep=";", nrows=1000, encoding = "ISO-8859-1")

#print(empresas0.head(n=10).to_string(index=False))

"""

#%% Exemplo Carregando bases direto do biqquery com ponte de acesso via json

"""

#contaservico@gruposeconomicos.iam.gserviceaccount.com


# Configure o projeto do Google Cloud
project_id = 'gruposeconomicos'

#Consulta as empresas da base
query = '''
    SELECT * FROM basedosdados.br_me_cnpj.empresas where data = "2023-11-16 limit 1000"
'''

#cria processo de conexão com o bigquery
credentials = service_account.Credentials.from_service_account_file(filename="GBQ.json",
                                                                    scopes=["https://www.googleapis.com/auth/cloud-platform"])

empresas = pd.read_gbq(credentials=credentials, query=query)

# consulta as empresas - estabelecimentos
# flags ativas situacao_cadastral in ('1','2','4')
# 1 = nulo - informação desconhecida
# 2 = Ativa
# 4 = Inapta - empresa com alguma restrição e por isso, importante incluir no modelo
# flags identificador_matriz_filial = 1 = identifica que é matriz - o modelo só tratará matriz

# socios
# flag tipo = 1,2,3
# 1 = Pessoa Jurídica
# 2 = Pessoa Física
# 3 = Estrangeiro

"""

#%% 
import time
from datetime import datetime
inicio = datetime.now()
time.sleep(5)
fim = datetime.now()
dif = (fim - inicio)
print('DIF :',dif)
print('date ', datetime.now().strftime('%H:%M:%S'))


#%% MySqlConnection

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

# Exemplo de uso
if __name__ == '__main__':
    query = 'select * from grupo_economico.empresa_socios order by cnpj_basico limit 100'
    df_empresas = query_mysql_to_dataframe(query)
    print(df_empresas.head())  # Mostra as primeiras linhas do DataFrame
    
    
    
#%%Df teste
def df_teste():
    # Dados
    data = {
        'cnpj_basico': ['empresas', 'socios', 'estabelecimentos', 'empresa_socios'],
        'status': [True, True, True, True]
    }
    return pd.DataFrame(data)
    

#%% Grafo
import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo(socios, empresas, relacoes):
    """
    Cria um grafo que representa as relações entre sócios e empresas.
    
    :param socios: Lista de sócios.
    :param empresas: Lista de empresas.
    :param relacoes: Lista de tuplas representando relações (socio, empresa).
    :return: Um grafo NetworkX.
    """
    # Cria um grafo vazio
    G = nx.Graph()
    
    # Adiciona nós para sócios e empresas
    for socio in socios:
        G.add_node(socio, tipo='socio')
    for empresa in empresas:
        G.add_node(empresa, tipo='empresa')
    
    # Adiciona arestas para representar as relações
    for socio, empresa in relacoes:
        G.add_edge(socio, empresa)
    
    return G

def visualizar_grafo(G):
    """
    Visualiza um grafo usando Matplotlib.
    
    :param G: Um grafo NetworkX.
    """
    pos = nx.spring_layout(G)  # Calcula a posição dos nós
    
    # Define a cor dos nós com base no tipo
    node_colors = ['blue' if G.nodes[node]['tipo'] == 'socio' else 'green' for node in G.nodes()]
    
    # Desenha o grafo
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
    plt.show()

# Dados de exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'),('2', 'C'),('2', 'D'),('3', '1'),('3', 'E'),('3', 'A'),('4', '1'),('4', 'F'),('4', 'G')]

# Cria o grafo
G = criar_grafo(socios, empresas, relacoes)

# Visualiza o grafo
visualizar_grafo(G)


#%% Grafo - dataframe
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def criar_grafo(socios, empresas, relacoes):
    """
    Cria um grafo que representa as relações entre sócios e empresas.
    
    :param socios: Lista de sócios.
    :param empresas: Lista de empresas.
    :param relacoes: Lista de tuplas representando relações (socio, empresa).
    :return: Um grafo NetworkX.
    """
    G = nx.Graph()
    
    for socio in socios:
        G.add_node(socio, tipo='socio')
    for empresa in empresas:
        G.add_node(empresa, tipo='empresa')
    
    for socio, empresa in relacoes:
        G.add_edge(socio, empresa)
    
    return G

def separar_subgrafos(G):
    """
    Separa os componentes conectados do grafo em subgrafos.
    
    :param G: Um grafo NetworkX.
    :return: Lista de subgrafos.
    """
    subgrafos = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    return subgrafos

def converter_grafo_para_dataframe(subgrafo):
    """
    Converte um subgrafo em um dataframe com as arestas.
    
    :param subgrafo: Um subgrafo NetworkX.
    :return: DataFrame com as arestas do subgrafo.
    """
    edges = list(subgrafo.edges(data=False))
    df = pd.DataFrame(edges, columns=['socio', 'empresa'])
    return df

def visualizar_grafo(G):
    """
    Visualiza um grafo usando Matplotlib.
    
    :param G: Um grafo NetworkX.
    """
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['tipo'] == 'socio' else 'green' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
    plt.show()

# Dados de exemplo
# Dados de exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'),('2', 'C'),('2', 'D'),('3', '1'),('3', 'E'),('3', 'A'),('4', '1'),('4', 'F'),('4', 'G')]

# Cria o grafo
G = criar_grafo(socios, empresas, relacoes)

# Visualiza o grafo original
visualizar_grafo(G)

# Separa os subgrafos
subgrafos = separar_subgrafos(G)

# Converte cada subgrafo em dataframe e armazena em uma lista
dataframes = [converter_grafo_para_dataframe(subgrafo) for subgrafo in subgrafos]

# Exibe os dataframes gerados
for i, df in enumerate(dataframes):
    print(f"DataFrame do subgrafo {i+1}:\n", df, "\n")

    
#%% grafo com matriz
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def criar_grafo(socios, empresas, relacoes):
    """
    Cria um grafo que representa as relações entre sócios e empresas.
    
    :param socios: Lista de sócios.
    :param empresas: Lista de empresas.
    :param relacoes: Lista de tuplas representando relações (socio, empresa).
    :return: Um grafo NetworkX.
    """
    G = nx.Graph()
    
    for socio in socios:
        G.add_node(socio, tipo='socio')
    for empresa in empresas:
        G.add_node(empresa, tipo='empresa')
    
    for socio, empresa in relacoes:
        G.add_edge(socio, empresa)
    
    return G

def separar_subgrafos(G):
    """
    Separa os componentes conectados do grafo em subgrafos.
    
    :param G: Um grafo NetworkX.
    :return: Lista de subgrafos.
    """
    subgrafos = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    return subgrafos

def converter_grafo_para_matriz(subgrafo):
    """
    Converte um subgrafo em uma matriz com sócios nas linhas e empresas nas colunas.
    
    :param subgrafo: Um subgrafo NetworkX.
    :return: DataFrame representando a matriz.
    """
    socios = [n for n, d in subgrafo.nodes(data=True) if d['tipo'] == 'socio']
    empresas = [n for n, d in subgrafo.nodes(data=True) if d['tipo'] == 'empresa']
    
    # Cria uma matriz com zeros
    matriz = pd.DataFrame(0, index=socios, columns=empresas)
    
    # Popula a matriz com 1 onde há relação
    for socio, empresa in subgrafo.edges():
        matriz.at[socio, empresa] = 1
    
    return matriz

def visualizar_grafo(G):
    """
    Visualiza um grafo usando Matplotlib.
    
    :param G: Um grafo NetworkX.
    """
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['tipo'] == 'socio' else 'green' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
    plt.show()

# Dados de exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'), ('2', 'C'), ('2', 'D'), ('3', '1'), ('3', 'E'), ('3', 'A'), ('4', '1'), ('4', 'F'), ('4', 'G')]

# Cria o grafo
G = criar_grafo(socios, empresas, relacoes)

# Visualiza o grafo original
visualizar_grafo(G)

# Separa os subgrafos
subgrafos = separar_subgrafos(G)

# Converte cada subgrafo em matriz e armazena em uma lista de dataframes
dataframes = [converter_grafo_para_matriz(subgrafo) for subgrafo in subgrafos]

# Exibe os dataframes gerados
for i, df in enumerate(dataframes):
    print(f"Matriz do subgrafo {i+1}:\n", df, "\n")
    
#%% externalizando dataframe
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1],
    'C': [2, 4, 1, 3],
    'D': [3, 1, 4, 2]
}
df = pd.DataFrame(data, index=['1', '2', '3', '4'])

# Criação do heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')

# Configurações do gráfico
plt.title('Heatmap da Matriz de Dados')
plt.xlabel('Colunas')
plt.ylabel('Linhas')

# Mostrar o gráfico
plt.show()

#%% dataframe - matriz
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
socios = ['A', 'B', '4', 'C', 'D', 'E', 'F', 'G', '1']
empresas = ['1', '2', '3', '4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'), ('2', 'C'), ('2', 'D'), ('3', '1'), ('3', 'E'), ('3', 'A'), ('4', '1'), ('4', 'F'), ('4', 'G')]

# Criar DataFrame
df_relacoes = pd.DataFrame(relacoes, columns=['Empresa', 'Socio'])

# Criar uma matriz de zeros
matrix = pd.DataFrame(0, index=socios, columns=empresas)

# Preencher a matriz com base nas relações
for empresa, socio in relacoes:
    matrix.at[socio, empresa] = 1

# Depuração: imprimir a matriz
print(matrix)

# Configurar o estilo e a paleta de cores para o heatmap
cmap = sns.color_palette(["white", "yellow"])

# Criar heatmap usando Seaborn
plt.figure(figsize=(10, 8))
ax = sns.heatmap(matrix, annot=False, fmt="d", cmap=cmap, cbar=False, linewidths=.5, linecolor='black')

# Ajustar os labels
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.set_xlabel('Empresas')
ax.set_ylabel('Sócios')

# Adicionar título na parte inferior
plt.title('Matriz de Relações entre Sócios e Empresas', loc='center', y=-0.1)

# Salvar como arquivo de imagem
plt.savefig("matriz_relacoes.png")

# Exibir a figura
plt.show()
