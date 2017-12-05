''' Módulo com implementação de uma fila encadeada '''

class Fila:
    ''' Classe com implementação de uma fila encadeada '''
    class Celula:
        ''' Classe que define uma célula da fila '''
        def __init__(self, _item=object(), _prox=object()):
            self.item = _item
            self.prox = _prox

    def __init__(self):
        self.frente = Fila.Celula()
        self.tras = self.frente
        self.frente.prox = None

    def insere(self, objeto=object()):
        ''' Insere o objeto na lista '''
        self.tras.prox = Fila.Celula()
        self.tras = self.tras.prox
        self.tras.item = objeto
        self.tras.prox = None

    def remove(self):
        ''' Remove o atual primeiro elemento da fila e
        retorna o novo primeiro elemento da fila '''
        item = None
        if self.vazia():
            raise Exception("Erro: A fila esta vazia")
        self.frente = self.frente.prox
        item = self.frente.item
        return item

    def vazia(self):
        ''' Retorna verdadeiro se a lista estiver vazia '''
        return self.frente == self.tras

    def imprime(self):
        ''' Imprime a lista com os elementos separados
        por espaços '''
        aux = self.frente.prox
        while aux != None:
            print(" " + str(aux.item), end='')
            aux = aux.prox
        print()
