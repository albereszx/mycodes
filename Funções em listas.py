Fazendo um  função que recebe uma lista de números e retorna a
soma de todos eles. NÃO utilizando a função sum do python. 
'''

lista = [5,10,15,20,30]
def soma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

print (soma(lista)) # OK : Irá exibir a SOMA dos itens da lista 

#Fazendo uma função que recebe uma lista de números e retorna a média.
#ou seja, soma todos os números e divide pela quantidade de numeros

def media(lista):
    media = soma(lista)/len(lista)
    return media

print(media(lista)) # OK :  irá exibir a MEDIA dos itens da lista 

#Fazendo uma função que acrescenta o proximo numero a uma lista.
#por exemplo cresce([7,8]) deve devolver [7,8,9]
def cresce(lista):

    ultimaposicao = len(lista)-1
    ultimovalor = lista[ultimaposicao]
    proximovalor = (ultimovalor) + 1
    lista.append(proximovalor)
    return lista

print(cresce(lista)) # OK : será acrescentado um valor posterior ao último da lista 
