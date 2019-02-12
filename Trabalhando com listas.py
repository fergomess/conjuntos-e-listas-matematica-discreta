#Criando listas
lista = []
print(lista)

lista = ['carro','peixe',123,111]
print(lista)

nova_lista = ['pedra',lista]
print(nova_lista)



''' Pertinência '''
#Verificando se um determinado elemento pertence a uma lista utilizando o operador de pertinência in
lista = ['carro','peixe',123,111]
print('peixe' in lista)
print('gato' in lista)



''' Igualdade '''
#Verificando a igualdade entre listas
lista1 = [123, 111]
lista2 = [123, 111]
print(lista1 == lista2)



''' Subconjunto '''
#Verificando se os elementos de 'c2' estão incluídos em 'c3'
c2 = [1, 2, 3]
c3 = [1, 2, 3, 4, 5, 6]
print(c2<=c3)
