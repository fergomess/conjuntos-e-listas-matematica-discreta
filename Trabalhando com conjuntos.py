#Recursos da linguagem PYTHON que permitam identificar as relações de pertinência, continência, subconjunto e igualdade.


#Adicionando e removendo elementos de um conjunto
c = {1, 2, 3, 4}
c.add(5)
c.discard(2)
print c



''' Subconjunto '''
#Verificando se o conjunto 'a' é um subconjunto do conjunto 'b'
a = {2 , 3}
b = {1 , 2 , 3 , 4}
print(a. issubset ( b ))

#Verificando se o conjunto 'b' é o superconjunto do conjunto 'a'
a = {2 , 3}
b = {1 , 2 , 3 , 4}
print(b. issupperset ( a ))



'''Pertinência '''
#Verificando se um determinado elemento pertence a um conjunto utilizando o operador de pertinência in
A = {1, 2, 3, 4}
print(5 in A)

#Verificando se um determinado elemento NÃO pertence a um conjunto utilizando o operador de pertinência not in
A = {1, 2, 3, 4}
print(5 not in A)
	


''' Igualdade '''
#Verificando a igualdade entre conjuntos
A = {1, 2, 3}
B = {3, 2, 1}
print(A == B)



''' Continência '''	
#Verificando se o conjunto 'g' está contido em no conjunto'f'
f = {1 , 2 , 3 , 4}
g = {2, 4}
print(g. issubset(f))

