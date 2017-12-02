''' Módulo com implementação de uma lista encadeada '''

#pylint: disable=C0103

class Lista:
    ''' Classe com implementação de uma lista encadeada '''
    class Celula:
        ''' Classe que define uma célula da lista '''
        def __init__(self, _item=object(), _prox=object()):
            self.item = _item
            self.prox = _prox

    def __init__(self):
        self.primeiro = Lista.Celula()
        self.pos = self.primeiro
        self.ultimo = self.primeiro
        self.primeiro.prox = None

    def pesquisa(self, chave=object()):
        ''' Retorna o item se encontrado ou
        None se não encontrado. '''
        if self.vazia() or chave is None:
            return None
        aux = self.primeiro
        while aux.prox is not None:
            if aux.prox.item == chave:
                return aux.prox.item
            aux = aux.prox
        return None

    def insere(self, objeto=object()):
        ''' Insere o objeto no final da lista '''
        self.ultimo.prox = Lista.Celula()
        self.ultimo = self.ultimo.prox
        self.ultimo.item = objeto
        self.ultimo.prox = None

    def inserePrimeiro(self, item=object()):
        ''' Insere o item no início da lista '''
        aux = self.primeiro.prox
        self.primeiro.prox = Lista.Celula()
        self.primeiro.prox.item = item
        self.primeiro.prox.prox = aux

    def retira(self, chave=object()):
        ''' Retira o elemento chave se este
        for encontrado, retorna None se não for
        e lança uma exception se a lista estiver
        vazia ou a chave for None '''
        if self.vazia() or chave is None:
            raise Exception("Erro: Lista vazia ou chave inválida")
        aux = self.primeiro
        while aux.prox is not None and not aux.prox.item == chave:
            aux = aux.prox
        if aux.prox is None:
            return None
        q = aux.prox
        item = q.item
        aux.prox = q.prox
        if aux.prox is None:
            self.ultimo = aux
        return item

    def retiraPrimeiro(self):
        ''' Retira e retorna o primeiro elemento da lista
        ou lança uma exceção se vazia '''
        if self.vazia():
            raise Exception("Erro: Lista vazia")
        aux = self.primeiro
        q = aux.prox
        item = q.item
        aux.prox = q.prox
        if aux.prox is None:
            self.ultimo = aux
        return item

    def vazia(self):
        ''' Retorna verdadeiro se a lista for vazia '''
        return self.primeiro == self.ultimo

    def imprime(self):
        ''' Imprime os elementos da lista, um por linha '''
        aux = self.primeiro.prox
        while aux is not None:
            print(aux.item)
            aux = aux.prox

    def estaNaLista(self, chave=object()):
        ''' Retorna se o elemento chave está na lista '''
        obj = self.pesquisa(chave)
        return obj is not None

    def getPrimeiro(self):
        ''' Retorna e itera para o primeiro elemento da lista '''
        self.pos = self.primeiro
        return self.proximo()

    def proximo(self):
        ''' Retorna e itera para o próximo elemento da lista '''
        self.pos = self.pos.prox
        if self.pos is None:
            return None
        else:
            return self.pos.item

#pylint: enable=C0103
