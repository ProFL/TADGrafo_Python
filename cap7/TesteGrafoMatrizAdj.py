''' Módulo que contém o teste para o TAD grafo por
matriz adjunta '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/matrizadj")
from EntradaDeGrafo import EntradaDeGrafo
from Grafo import Grafo

#pylint: disable=C0103

nVertices = int(input("No. vertices:"))
nArestas = int(input("No. arestas:"))
grafo = Grafo(nVertices)
for i in range(nArestas):
    a = EntradaDeGrafo.digitarAresta()
    grafo.insereAresta(a.v1, a.v2, a.peso)
    grafo.insereAresta(a.v2, a.v1, a.peso)
grafo.imprime()
input()
# grafoT = grafo.grafoTransposto()
# grafoT.imprime()
# input()
# a = EntradaDeGrafo.digitarAresta()
# if grafo.existeAresta(a.v1, a.v2):
#     print("Aresta já existe")
# else:
#     grafo.insereAresta(a.v1, a.v2, a.peso)
#     grafo.insereAresta(a.v2, a.v1, a.peso)
# grafo.imprime()
# input()
v1 = int(input("Lista adjacentes de: "))
if not grafo.listaAdjVazia(v1):
    adj = grafo.primeiroListaAdj(v1)
    while adj is not None:
        print("  " + str(adj.v2) + " (" + str(adj.peso) + ")")
        adj = grafo.proxAdj(v1)
    print()
    input()
print("Retira aresta: ")
a = EntradaDeGrafo.digitarAresta()
if grafo.existeAresta(a.v1, a.v2):
    grafo.retiraAresta(a.v1, a.v2)
    grafo.retiraAresta(a.v2, a.v1)
else:
    print("Aresta não existe.")
grafo.imprime()
print("Existe aresta: ")
a = EntradaDeGrafo.digitarAresta()
if grafo.existeAresta(a.v1, a.v2):
    print("  Sim")
else:
    print("  Não")

#pylint: enable=C0103
