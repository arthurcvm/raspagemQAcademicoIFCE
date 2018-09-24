import time

from selenium import webdriver
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import sys

from Disciplina import Disciplina
from Nota import Nota


class Raspagem():
    driver = 0

    def __init__(self, login, senha):
        display = Display(visible=0, size=(1024, 768))
        display.start()
        self.driver = webdriver.Chrome('./chromedriver')
        # Log path added via service_args to see errors if something goes wrong (always a good idea - many of the errors I encountered were described in the logs)
        # And now you can add your website / app testing functionality:
        self.driver.get('https://qacademico.ifce.edu.br/qacademico/index.asp?t=1001')
        username = self.driver.find_element_by_name("LOGIN")
        password = self.driver.find_element_by_name("SENHA")
        username.send_keys(login)
        password.send_keys(senha)
        login_attempt = self.driver.find_element_by_id("btnOk")
        login_attempt.click()
        time.sleep(2) #Pequeno mas de suma importância para não retornar a mesma page
        # print(driver.page_source)
        self.driver.get('https://qacademico.ifce.edu.br/qacademico/index.asp?t=2071')
        # print(driver.page_source)
        # driver.click...
    def diarios(self):
        url = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=2071"
        self.driver.get(url)
        html = self.driver.page_source
        dev = open("./diarioIfce.html", encoding="ISO-8859-1")
        soup = BeautifulSoup(html, 'html.parser')

        # print(soup.find_all(width="100%")[6].find_all("table")[1])

        table = soup.find_all(width="100%")[6].find_all("table")[1]

        # print(table.find_all("tr", attrs={"bgcolor":True}))

        disciplinas = table.find_all("tr", attrs={"bgcolor":True})

        mats = []
        lastMat = -1

        for i in range(1, len(disciplinas)):
            disciplina = Disciplina()

            if (len(disciplinas[i].find_all("tr", attrs={"class":True})) == 0) and (len(disciplinas[i]('strong')) > 0): #Melhorar
                titulo = disciplinas[i]('strong')[0].string.split("- ")
                # print(disciplinas[i]('strong')[0].string.split("- "))
                disciplina.setNome(titulo[2].split("(")[0])
                # print(titulo[2].split("(")[0])

                # print(disciplinas[i].findAll("td")[5].string)
                disciplina.setCarga(disciplinas[i].findAll("td")[5].string)
                disciplina.setAulas(disciplinas[i].findAll("td")[7].find("a").string)
                # print(disciplinas[i].findAll("td")[7].find("a").string)
                disciplina.setFaltas(disciplinas[i].findAll("td")[11].string)
                # print(disciplinas[i].findAll("td")[11].string)

            elif len(disciplinas[i].find_all("div", attrs={"class":"conteudoTitulo"})) > 0:
                #Cada etapa conta como uma disciplina

                # print(disciplinas[i].find_all("td", attrs={"colspan":"2"})[0])
                blocoNotas = disciplinas[i].find_all("td", attrs={"colspan":"2"})[0]

                # print(blocoNotas.find_all("div", attrs={"class":"conteudoTitulo"})[0].string)
                nomeNota = blocoNotas.find_all("div", attrs={"class":"conteudoTitulo"})[0].string
                # print(blocoNotas.find_all("tr", attrs={"class": "conteudoTexto"})[0].find_all("td")[4].string)
                descricoes = blocoNotas.find_all("tr", attrs={"class": "conteudoTexto"})

                notas = []

                #Pega notas referente a essa etapa
                for descricao in descricoes:
                    # print(descri.find_all("td")[4].string.split("Nota: ")[1])
                    nota = Nota("", descricao.find_all("td")[4].string.split("Nota: ")[1])
                    notas.append(nota)

                if nomeNota == "N1":
                    mats[lastMat].getNotas().setN1(notas)
                elif nomeNota == "N2":
                    mats[lastMat].getNotas().setN2(notas)
                else:
                    mats[lastMat].notas.setNFinal(notas)

                # print(descricao.split("Nota: ")[1])

            if (len(disciplinas[i].find_all("tr", attrs={"class":True})) == 0) and (len(disciplinas[i]('strong')) > 0):  # Melhorar
                mats.append(disciplina)
                lastMat = (len(mats) - 1)

        return mats

    def boletim(self):
        url = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=2032"
    def horario(self):
        url = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=2010"
    def calendario(self):
        url = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=2020"
    def material(self):
        url = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=2061"


if len(sys.argv) == 3:
    # print(sys.argv[1])
    # print(sys.argv[2])
    login = sys.argv[1]
    senha = sys.argv[2]
    ola = Raspagem(sys.argv[1], sys.argv[2])
    print(ola.diarios())