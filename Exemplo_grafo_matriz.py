# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:34:54 2024

@author: guspa
"""

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
    
    
# Função para varrer as relações entre os nós do grafo
def varrer_relacoes(subgrafo):
    """
    Varrer todas as relações entre os nós de um grafo.
    
    :param grafo: Um grafo NetworkX.
    """
    visualizar_grafo(subgrafo)
    
    socios = [n for n, d in subgrafo.nodes(data=True) if d['tipo'] == 'socio']
    empresas = [n for n, d in subgrafo.nodes(data=True) if d['tipo'] == 'empresa']
    
    
    # Cria uma matriz com zeros
    matriz = pd.DataFrame(0, index=socios, columns=empresas)
    
    for aresta in subgrafo.edges(data=True):
        tipo_origem = subgrafo.nodes[aresta[0]]['tipo']
        tipo_destino = subgrafo.nodes[aresta[1]]['tipo']
        if subgrafo.nodes[aresta[0]]['tipo'] == 'socio':
            socio = aresta[0]
            empresa = aresta[1]
        else:
            socio = aresta[1]
            empresa = aresta[0]
        print(f"Relação entre {aresta[0]} ({tipo_origem}) e {aresta[1]} ({tipo_destino})")
        matriz.at[socio, empresa] = 1
    
    
    return matriz


def grava_grafo(subgrafo):
    
    data = {'empresas':[], 'socios':[], 'id_grupo':[]}
    df_grafo = pd.DataFrame(columns=['empresas','socios','id_grupo'])
    
    for aresta in subgrafo.edges(data=True):
        if subgrafo.nodes[aresta[0]]['tipo'] == 'socio':
            socio = aresta[0]
            empresa = aresta[1]
        else:
            socio = aresta[1]
            empresa = aresta[0]
        data['empresas'].append(empresa)
        data['socios'].append(socio)
        data['id_grupo'].append(1)
        df_aux = pd.DataFrame({'empresas':[empresa], 'socios':[socio],'id_grupo':1})
        
        df_grafo = pd.concat([df_grafo, df_aux], ignore_index=True) 

    print(df_grafo)
    
# Dados de exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'), ('2', 'C'), ('2', 'D'), ('3', '1'), ('3', 'E'), ('3', 'A'), ('4', '1'), ('4', 'F'), ('4', 'G')]
##rel = pd.DataFrame(relacoes, columns=["empresa","socio"])

# Cria o grafo
G = criar_grafo(socios, empresas, relacoes)

# Visualiza o grafo original
visualizar_grafo(G)

# Separa os subgrafos
subgrafos = separar_subgrafos(G)

# Varrer subgrafos 
#dataframe_matriz = [varrer_relacoes(subgrafo) for subgrafo in subgrafos]

# Converte cada subgrafo em matriz e armazena em uma lista de dataframes
#dataframes = [converter_grafo_para_matriz(subgrafo) for subgrafo in subgrafos]

dataframe_matriz = [grava_grafo(subgrafo) for subgrafo in subgrafos]

# Exibe os dataframes gerados
for i, df in enumerate(dataframe_matriz):
    print(f"Matriz do subgrafo {i+1}:\n", df, "\n")