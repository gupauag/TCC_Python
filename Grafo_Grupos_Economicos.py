#%% projeto
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:45:17 2024

@author: guspa

Objetivo: Criar referencias entre as empresas
Criação de grafo de referencia entre os integantes recursivamente até terminar o conexto das bases

"""

import connections as con
import ETL_BigQuery as etl

import pandas as pd

import networkx as nx
from concurrent.futures import ThreadPoolExecutor

# lib para criar a visão grafica do grafo
from pyvis.network import Network 

# lib para criar a visão grafica da matriz
import seaborn as sns
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
    """
    query = '''
       select CONCAT (a.cnpj_basico,'-',a.razao_social) as empresas, CONCAT (a.nome_socio,'-', a.doc_socio) as socios
            from grupo_economico.empresa_socios a 
            order by cnpj_basico
            limit 100;
        '''
    """
    query = '''
        select CONCAT (a.cnpj_basico,'-',a.razao_social) as empresas, CONCAT (a.nome_socio,'-', a.doc_socio) as socios
        from grupo_economico.empresa_socios a 
        where a.cnpj_basico in(
            select cnpj_basico
            from grupo_economico.empresa_socios
            where (doc_socio = '57444283000188' and nome_socio = 'INFRACON ENGENHARIA E COMERCIO LTDA') 
                #(doc_socio = '***105976**' and nome_socio = 'FLAVIO AUGUSTO DOS SANTOS') or
                #(doc_socio = '***798487**' and nome_socio = 'FLAVIA CASSIANO FRAGA') or
                #(doc_socio = '27870967000180' and nome_socio = 'HODIE SERVICOS TECNICOS E GERENCIAMENTO DE OBRAS LTDA') or
                #(doc_socio = '***436218**' and nome_socio = 'TANIA REGINA SANTIAGO PEREIRA CAMISA NOVA') or
                #(doc_socio = '***599401**' and nome_socio = 'ALEXANDRE JUNIO MAMEDES') # duas emprasas diferentes
            );
    '''
    return con.query_mysql_to_dataframe(query)

def trata_massa_grafo(df_empresa_socios):
    global df_socios, df_empresas  # Declarar as variáveis globais
    
    df_socios = df_empresa_socios[['socios']].copy() 
    df_empresas = df_empresa_socios[['empresas']].copy() 

def criar_grafo(socios, empresas, relacoes, chunk_size=1000):
    """
    Cria um grafo que representa as relações entre sócios e empresas.
    
    :param socios: Lista de sócios.
    :param empresas: Lista de empresas.
    :param relacoes: Lista de tuplas representando relações (socio, empresa).
    :return: Um grafo NetworkX.
    """
    G = nx.Graph()

    """
    #cria os nós do tipo sócios
    for index, row in socios.iterrows():
        G.add_node(row['socios'], tipo='socio')

    #cria os nós do tipo empresas
    for index, row in empresas.iterrows():
        G.add_node(row['empresas'], tipo='empresa')
    """
    # Criar threads para adicionar nós de sócios e empresas
    with ThreadPoolExecutor(max_workers=2) as executor:
        #.result é utilizado para esperar a finalização da thread
        executor.submit(adicionar_nos_socios, G, socios).result()
        executor.submit(adicionar_nos_empresas, G, empresas).result()
    
    #vincula os nós e cria as arestas do grafo
    for row in relacoes.itertuples(index=False):
        G.add_edge(row.socios, row.empresas)

        
    return G


def adicionar_nos_socios(G, socios):
    #cria os nós do tipo sócios
    for index, row in socios.iterrows():
        G.add_node(row['socios'], tipo='socio')

def adicionar_nos_empresas(G, empresas):
    #cria os nós do tipo empresas
    for index, row in empresas.iterrows():
        G.add_node(row['empresas'], tipo='empresa')
    

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
        visualizar_grafo(subgrafo)
        visualiza_grafo_interativo(subgrafo)
        
    """ aplicado somente quando quero gerar varios de uma vez só q com varios grandes
    for subgrafo in subgrafos:
        if subgrafo.number_of_edges() > 5:
            visualizar_grafo(subgrafo)
            visualiza_grafo_interativo(subgrafo)
    """
def converter_grafo_para_matriz(subgrafo):
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

def visualiza_matriz(df):
    # Configurar o estilo e a paleta de cores para o heatmap
    cmap = sns.color_palette(["white", "yellow"])
    
    # Criar heatmap usando Seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(df, annot=False, fmt="d", cmap=cmap, cbar=False, linewidths=.5, linecolor='black')
    
    # Ajustar os labels
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    ax.set_xlabel('Empresas', fontstyle='italic')
    ax.set_ylabel('Sócios')
    
    # Adicionar título na parte inferior
    plt.title('Matriz de Relações entre Sócios e Empresas', loc='center', y=-0.1)
    
    # Salvar como arquivo de imagem
    plt.savefig("matriz_relacoes.png")
    
    # Exibir a figura
    plt.show()


# MAIN
if __name__ == '__main__':
    
    """ massa de teste & evidencias
    df_empresa_socios = recupera_massa()
    trata_massa_grafo(df_empresa_socios)
    
    # Cria o grafo
    G = criar_grafo(df_socios, df_empresas, df_empresa_socios)
    
    # Separa os subgrafos
    subgrafos = separar_subgrafos(G)
    contar_arestas(subgrafos)
    
    # Converte cada subgrafo em matriz e armazena em uma lista de dataframes
    dataframes = [converter_grafo_para_matriz(subgrafo) for subgrafo in subgrafos]
    
    [visualiza_matriz(df) for df in dataframes]
    
    """
    
    ## executa massivamente grafo
        
    #processa_bigquery = False ## cria df com os dados pré grafo
    grava_grupo = False ## grava no MYSQL os grupos gerados
    table_name = 'empresa_socios_pre_grafo'
    
    sql_query = etl.cria_sql_query(table_name)
    
    df_empresa_socios = etl.unload_df(table_name, sql_query)  
    
    trata_massa_grafo(df_empresa_socios)
    
    # Cria o grafo
    G = criar_grafo(df_socios, df_empresas, df_empresa_socios)
    
    # Separa os subgrafos
    subgrafos = separar_subgrafos(G)