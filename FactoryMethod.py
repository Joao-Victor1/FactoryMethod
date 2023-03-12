#Importação do módulo ABC (Abstract Base Classes) - Para definir classes abstratas:
from abc import ABC, abstractmethod
import os, time

class Portaria: 
    def criaRelacao(self):
        pass
    
    def verificaRelacao(self):
        entrada = self.criaRelacao()

        result = f"\nPortaria: Sendo verificado no sistema\n{entrada.permissao()}"
        return result

#Classe de criação da relação aluno:
class RelacaoAluno(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao

    
    def criaRelacao(self):
        return Aluno(self.name, self.relacao)

#Classe de criação da relação professor:        
class RelacaoProfessor(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def criaRelacao(self):
        return Professor(self.name, self.relacao)
    
#Classe de criação da relação coordenador:
class RelacaoCoodernador(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def criaRelacao(self):
        return Coordenador(self.name, self.relacao)

#Classe de criação da relação diretor:
class RelacaoDiretor(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def criaRelacao(self):
        return Diretor(self.name, self.relacao)
    
#Classe de criação da relação administrativo:
class RelacaoAdministrativo(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def criaRelacao(self):
        return Administrativo(self.name, self.relacao)

#Classe de criação da relação vestibulando:
class RelacaoVestibulando(Portaria):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def criaRelacao(self):
        return Vestibulando(self.name, self.relacao)
    
class Entrada(ABC):
    @abstractmethod
    def permissao(self):
        pass

class Aluno(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result
    
class Professor(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result

class Coordenador(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result
    
class Diretor(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result
 
class Administrativo(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result
 
class Vestibulando(Entrada):
    def __init__(self, name, relacao):
        self.name = name
        self.relacao = relacao
    
    def permissao(self):
        result = (f"{self.name} tem relação com a FATEC como: {self.relacao}",
                  "entrada permitida!")
        return result
 
def secretaria(Portaria: Portaria):
    print(f"\nSistema iniciado para {Portaria.__class__.__name__}.",
          f"{Portaria.verificaRelacao()}")

#Menu
def menu():
    
    os.system("cls")
    print("Bem vindo a portaria\n")
    print("Aperte a tecla Q para encerrar o programa.\n")
    print("A. Acessar instituição\n")
    
    #variável de opções do menu:
    opcao = input("Selecione: ")

    if opcao == "a":
        nome = input("Digite seu nome: ")
        relacao = input("Digite sua relação com a Instituição: ")

        if (relacao == "Aluno") or (relacao == "aluno"):
            secretaria(RelacaoAluno(nome, relacao))
            time.sleep(5)
            
        elif(relacao == "Professor") or (relacao == "professor"):
            secretaria(RelacaoProfessor(nome, relacao))
            time.sleep(5)
        
        elif(relacao == "Coordenador") or (relacao == "coordenador"):
            secretaria(RelacaoCoodernador(nome, relacao))
            time.sleep(5)
        
        elif(relacao == "Diretor") or (relacao == "diretor"):
            secretaria(RelacaoDiretor(nome, relacao))
            time.sleep(5)
            
        elif(relacao == "Administrativo") or (relacao == "administrativo"):
            secretaria(RelacaoAdministrativo(nome, relacao))
            time.sleep(5)
            
        elif(relacao == "Vestibulando") or (relacao == "vestibulando"):
            secretaria(RelacaoVestibulando(nome, relacao))
            time.sleep(5)
        
        else:
            print(f"\n{nome} não tem nenhuma relação com a instituição, acompanhar até a scretaria\n")
    elif opcao == 'q':
        print("\nSaindo...\n")
        exit()

while True:
    menu()





