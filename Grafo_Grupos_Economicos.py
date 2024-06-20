#%% projeto
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
from pyvis.network import Network
import networkx as nx


# Definir os DataFrames globais
df_socios = pd.DataFrame()
df_empresas = pd.DataFrame()

# Massa de exemplo exemplo
socios = ['A', 'B','4','C', 'D','E','F','G','1']
empresas = ['1', '2','3','4']
relacoes = [('1', 'A'), ('1', 'B'), ('1', '4'), ('2', 'C'), ('2', 'D'), ('3', '1'), ('3', 'E'), ('3', 'A'), ('4', '1'), ('4', 'F'), ('4', 'G')]
##rel = pd.DataFrame(relacoes, columns=["empresa","socio"])

def recupera_massa():
    """
    query = '''
       select CONCAT (a.cnpj_basico,'-',a.razao_social) as empresas, CONCAT (a.nome_socio,'-', a.doc_socio) as socios
            from grupo_economico.empresa_socios a 
            order by cnpj_basico
            limit 100;
        '''
    """
    query = '''
        select  CONCAT (a.cnpj_basico,'-',a.razao_social) as empresas, CONCAT (a.nome_socio,'-', a.doc_socio) as socios
        from grupo_economico.empresa_socios a 
        where a.cnpj_basico in(
        	select cnpj_basico
        	from grupo_economico.empresa_socios
        	where doc_socio = '57444283000188' and nome_socio = 'INFRACON ENGENHARIA E COMERCIO LTDA'
        	)
        
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
        if subgrafo.number_of_edges() > 5:
            visualizar_grafo(subgrafo)
            visualiza_grafo_interativo(subgrafo)


def visualiza_grafo_interativo(subgrafo):
    # Crie uma rede interativa usando pyvis
    net = Network(notebook=True, width="2080px", height="1080px", directed=False)
    
    # Adicione os nós e as arestas ao objeto pyvis Network, identificando o tipo de nó
    for node in subgrafo.nodes():
        node_size = subgrafo.degree(node)
        if node_size > 10:
            node_size = 10
        elif node_size >=5 & node_size < 10:
            node_size = 5
        else:
            node_size = 2
        if subgrafo.nodes[node]['tipo'] == 'socio':
            no = ('Sócio = ' + df_socios[df_socios['socios'] == node].iloc[0]).to_string(index=False)
            net.add_node(node, label=node, color='green', title=no, size=node_size )
        else:
            no = ('Empresa = ' + df_empresas[df_empresas['empresas'] == node].iloc[0]).to_string(index=False)
            net.add_node(node, label=node, color='blue', title=no, size=node_size )
    
    # Adicione as arestas ao objeto pyvis Network
    for edge in subgrafo.edges():
        net.add_edge(edge[0], edge[1])
    
    
    # Adicione os nós e as arestas ao objeto pyvis Network
    ##net.from_nx(subgrafo)
    
    # Desative a física para que os nós não se movimentem automaticamente
    net.toggle_physics(True)
    net.show_buttons(filter_=['physics','Nodes'])
    """
    # Configure os nós para permitir reposicionamento manual
    for node in net.nodes:
        node['fixed'] = False
        node['physics'] = False
    """
    
    # Salve a visualização do grafo em um arquivo HTML
    net.show('grafo_interativo.html')

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