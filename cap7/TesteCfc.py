''' Módulo que contém o teste da detecção de componentes
fortemente conexos '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from EntradaDeGrafo import EntradaDeGrafo
from Cfc import Cfc

#pylint: disable=C0103

grafo = EntradaDeGrafo.digitarGrafo()
grafo.imprime()
cfc = Cfc(grafo)
cfc.obterCfc()

#pylint: enable=C0103
