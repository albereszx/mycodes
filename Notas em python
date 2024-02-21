Desenvolvi um simples código em Python, onde avalio notas escolares (aprovado/reprovado/recuperação):

# CODIGO

class Escola:

    def __init__(self, nome, escola, ano, nota) :
        self.nome = nome
        self.escola = escola
        self.ano = ano
        self.nota = nota



    def decisao(self):
        if self.nota > 6 :
            print (f' {self.nome}, você foi aprovado com a nota : {self.nota}')
        elif 6 > self.nota >= 5 :
            print (f' {self.nome}, você está de recuperação, pois sua nota foi : {self.nota}')
        elif self.nota < 5 :
            print (f' {self.nome}, infelizmente você foi reprovado com a nota :{self.nota}')


print (40*'-')
print ("Seja Bem vindo ao programa de notas escolar")
print (40*'-')


nome = input('Qual o seu nome ? ')
escola = input (f'Olá {nome} , em qual escola você estuda ? ')
ano = input('Qual ano você está cursando ?')
nota = float(input('Quando você tirou na prova final  ? '))
            

infos = Escola(nome,escola,ano,nota)

infos.decisao()
