from Notas import Notas


class Disciplina:
    def __init__(self, nome, professor, notas, carga, faltas, aulas):
        self.nome = nome
        self.professor = professor
        self.notas = notas
        self.carga = carga
        self.faltas = faltas
        self.aulas = aulas

    def __init__(self):
        self.notas = Notas()

    def setNome(self, nome):
        self.nome = nome

    def setProfessor(self, professor):
        self.professor = professor

    def setNotas(self, notas):
        self.notas = notas

    def setCarga(self, carga):
        self.carga = carga

    def setFaltas(self, faltas):
        self.faltas = faltas

    def setAulas(self, aulas):
        self.aulas = aulas

    def getNome(self):
        return self.nome

    def getProfessor(self):
        return self.professor

    def getNotas(self):
        return self.notas

    def getCarga(self):
        return self.carga

    def getFaltas(self):
        return self.faltas

    def getAulas(self):
        return self.aulas