''' Módulo que contém o teste da detecção de componentes
fortemente conexos '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from EntradaDeGrafo import EntradaDeGrafo
from Dijkstra import Dijkstra

#pylint: disable=C0103

grafo = EntradaDeGrafo.digitarGrafo()
raiz = int(input("Raiz da ACMC:"))
grafo.imprime()
dj = Dijkstra(grafo)
dj.grafo.imprime()
dj.obterArvoreCMC(raiz)
dj.imprime()
dj.imprimeCaminho(0, 2)

#pylint: enable=C0103
