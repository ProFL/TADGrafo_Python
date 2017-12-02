''' Módulo que contém o teste da DFS '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from EntradaDeGrafo import EntradaDeGrafo
from BuscaEmProfundidade import BuscaEmProfundidade

#pylint: disable=C0103

grafo = EntradaDeGrafo.digitarGrafo()
grafo.imprime()
dfs = BuscaEmProfundidade(grafo)
dfs.buscaEmProfundidade()
for v in range(grafo.numVertices):
    print("d["+str(v)+"]:"+str(dfs.d[v])+" -- f["+str(v)+"]:"+
          str(dfs.f[v])+" -- antecessor["+str(v)+"]:" + str(dfs.antecessor[v]))

#pylint: enable=C0103
