''' Módulo que contém o teste da detecção de componentes
fortemente conexos '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
from EntradaDeGrafo import EntradaDeGrafo
from Cfc import Cfc

#pylint: disable=C0103

# grafo = EntradaDeGrafo.digitarGrafo()
grafo = Grafo(3)
arestas = [[0, 1], [0, 2], [1, 2]]
for aresta in arestas:
    grafo.insereAresta(aresta[0], aresta[1])
grafo.imprime()
cfc = Cfc(grafo)
cfc.obterCfc()

#pylint: enable=C0103
