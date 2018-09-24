class Nota:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setValor(self, valor):
        self.valor = valor

    def getDescricao(self):
        return self.descricao

    def getValor(self):
        return self.valor