# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:45:17 2024

@author: guspa

Objetivo: Criar referencias entre as empresas
Criação de grafo de referencia entre os integantes recursivamente até terminar o conexto das bases

"""

import connections as con
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Definir os DataFrames globais
df_socios = pd.DataFrame()
df_empresas = pd.DataFrame()

# Massa de exemplo exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'), ('2', 'C'), ('2', 'D'), ('3', '1'), ('3', 'E'), ('3', 'A'), ('4', '1'), ('4', 'F'), ('4', 'G')]
##rel = pd.DataFrame(relacoes, columns=["empresa","socio"])

def recupera_massa():
    query = '''
       select CONCAT (a.cnpj_basico,'-',a.razao_social) as empresas, CONCAT (a.nome_socio,'-', a.doc_socio) as socios
            from grupo_economico.empresa_socios a 
            order by cnpj_basico
            limit 100;
        '''
    return con.query_mysql_to_dataframe(query)

def trata_massa_grafo(df_empresa_socios):
    global df_socios, df_empresas  # Declarar as variáveis globais
    
    df_socios = df_empresa_socios[['socios']].copy() 
    df_empresas = df_empresa_socios[['empresas']].copy() 

def criar_grafo(socios, empresas, relacoes):
    """
    Cria um grafo que representa as relações entre sócios e empresas.
    
    :param socios: Lista de sócios.
    :param empresas: Lista de empresas.
    :param relacoes: Lista de tuplas representando relações (socio, empresa).
    :return: Um grafo NetworkX.
    """
    G = nx.Graph()
    
    for index, row in socios.iterrows():
        G.add_node(row['socios'], tipo='socio')
    for index, row in empresas.iterrows():
        G.add_node(row['empresas'], tipo='empresa')
    
    for row in relacoes.itertuples(index=False):
        G.add_edge(row.socios, row.empresas)
    
    return G

def separar_subgrafos(G):
    """
    Separa os componentes conectados do grafo em subgrafos.
    
    :param G: Um grafo NetworkX.
    :return: Lista de subgrafos.
    """
    subgrafos = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    return subgrafos

def visualizar_grafo(G):
    """
    Visualiza um grafo usando Matplotlib.
    
    :param G: Um grafo NetworkX.
    """
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['tipo'] == 'socio' else 'green' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
    plt.show()

def contar_arestas(subgrafos):
    for subgrafo in subgrafos:
        if subgrafo.number_of_edges() > 3:
            visualizar_grafo(subgrafo)


# MAIN
if __name__ == '__main__':
    
    df_empresa_socios = recupera_massa()
    trata_massa_grafo(df_empresa_socios)
    
    # Cria o grafo
    G = criar_grafo(df_socios, df_empresas, df_empresa_socios)

    # Visualiza o grafo original
    visualizar_grafo(G)

    # Separa os subgrafos
    subgrafos = separar_subgrafos(G)
    contar_arestas(subgrafos)