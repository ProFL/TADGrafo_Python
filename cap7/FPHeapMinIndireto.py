''' Módulo que implementa um Heap de Mínimo Indireto '''

import copy

#pylint: disable=C0103

class FPHeapMinIndireto:
    ''' Classe que implementa uma Fila de Prioridade
    Heap de Mínimo Indireto '''
    def __init__(self, p=[], v=[]): #pylint: disable=W0102
        self.peso = p
        self.fp = copy.deepcopy(v)
        self.n = len(self.fp) - 1
        self.pos = [i + 1 for i in range(self.n)]

    def refaz(self, esq=0, direita=0):
        ''' Balanceia a heap '''
        esq = int(esq)
        direita = int(direita)
        j = esq * 2
        x = int(self.fp[esq])
        while j <= direita:
            if j < direita and self.peso[self.fp[j]] > self.peso[self.fp[j + 1]]:
                j = j + 1
            if self.peso[x] <= self.peso[self.fp[j]]:
                break
            self.fp[esq] = self.fp[j]
            self.pos[self.fp[j]] = esq
            esq = j
            j = esq * 2
        self.fp[esq] = x
        self.pos[x] = esq

    def constroi(self):
        ''' Constrói a heap '''
        esq = int(self.n / 2 + 1)
        while esq > 1:
            esq = esq - 1
            self.refaz(esq, self.n)

    def retiraMin(self):
        ''' Retira o elemento da frente da fila se
        disponível e o retorna ou lança uma exception
        se a fila estiver vazia '''
        minimo = 0
        if self.n < 1:
            raise Exception("Erro: heap vazio")
        else:
            minimo = self.fp[1]
            self.fp[1] = self.fp[self.n]
            self.pos[self.fp[self.n]] = 1
            self.n = self.n - 1
            self.refaz(1, self.n)
        return minimo

    def diminuiChave(self, i=0, chaveNova=0.0):
        ''' Modifica a chave do elemento i para chaveNova '''
        i = int(self.pos[int(i)])
        x = int(self.fp[int(i)])
        if chaveNova < 0:
            raise ValueError("Erro: chaveNova com valor incorreto")
        self.peso[x] = chaveNova
        while i > 1 and self.peso[x] <= self.peso[self.fp[int(i / 2)]]:
            self.fp[i] = self.fp[int(i / 2)]
            self.pos[self.fp[int(i / 2)]] = i
            i = int(i / 2)
        self.fp[i] = x
        self.pos[x] = i

    def vazio(self):
        ''' Retorna se o heap está vazio '''
        return self.n == 0

    def imprime(self):
        ''' Imprime a heap '''
        for i in range(self.n):
            print(str(self.peso[int(self.fp[i])]), end=' ')
        print()

#pylint: enable=C0103
