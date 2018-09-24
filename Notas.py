class Notas:
    def __int__(self):
        print("inicializado")

    def __init__(self, n1, n2, nFinal):
        self.n1 = n1
        self.n2 = n2
        self.nFinal = nFinal

    def __init__(self):
        print("inicializado")

    def setN1(self, n1):
        self.n1 = n1

    def setN2(self, n2):
        self.n2 = n2

    def setNFinal(self, nFinal):
        self.nFinal = nFinal

    def getN1(self):
        return self.n1

    def getN2(self):
        return self.n2

    def getNFinal(self):
        return self.nFinal