#SOMA
def soma(a,b):
    resultado = a + b    
    return resultado   

print (soma(10,10)) # OK : irá retornar a soma correta dos valores 

#SOMAZOADA
def soma_zoada(a,b):
    
    a = 10 
    b = 5 #
    resultado = a+b    
    return resultado   

print ( soma_zoada(10,29)) # OK  : a soma sempre vai ser a equivalente aos valores pré definidos na variável.

#SOMA3
def soma3(a,b,c):
    dois_primeiros = soma(a,b)
    resultado = soma(dois_primeiros,c)
    return resultado

print (soma3(10,3,5)) # OK : Irá somar os três numeros sugeridos de maneira correta.

#QUADRADO
def quadrado(a):
    resposta = a*a
    return resposta

print(quadrado(4)) # OK : A resposta sempre será o numero x ele mesmo (quadrado²).
