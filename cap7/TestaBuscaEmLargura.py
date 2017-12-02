''' Módulo que contém o teste da BFS '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from EntradaDeGrafo import EntradaDeGrafo
from BuscaEmLargura import BuscaEmLargura

grafo = EntradaDeGrafo.digitarGrafo()
grafo.imprime()
bfs = BuscaEmLargura(grafo)
bfs.buscaEmLargura()
for v in range(grafo.numVertices):
    print("d["+str(v)+"]:" + str(bfs.d[v]) + " -- antecessor["+str(v)+"]:" + str(bfs.antecessor[v]))
bfs.imprimeCaminho(0, 2)