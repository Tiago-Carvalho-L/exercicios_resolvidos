#EXERCICIO 1
print('EXERCICIO 1')
print('Qual será o valor da variável "soma"?')
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k 
print (f'O valor da variável "soma" será: {soma}')

#-------------------------------------------------

#EXERCICIO 2
print('-'*30)
print('EXERCICIO 2')
print('(--- SEQUÊNCIA FIBONACCI ---)')
numero = int(input('Qual número você quer descobrir se pertence a sequência Fibonacci? '))

p1 = 0 
p2 = 1
contador = 3
fibonacci = [p1, p2]
while contador <= numero:
    p3 = p1 + p2
    fibonacci.append(p3)
    p1 = p2
    p2 = p3
    contador = contador + 1
print(fibonacci)
if numero in fibonacci:
    print('O número informado PERTENCE a sequência')
else:
    print('O número informado NÃO PERTENCE a sequência')
    
#-------------------------------------------------------

#EXERCICIO 3
print('-'*30)
print('EXERCICIO 3')  
print('a) 1, 3, 5, 7, __')
print('Próximo elemento = 9')
print('')
print('b) 2, 4, 8, 16, 32, 64, __')
print('Próximo elemento = 128')
print('')
print('c) 0, 1, 4, 9, 16, 25, 36, __')
print('Próximo elemento = 49')
print('')
print('d) 4, 16, 36, 64, ___')
print('Próximo elemento = 100')
print('')
print('e) 1, 1, 2, 3, 5, 8, ___')
print('Próximo elemento = 13')
print('')
print('f) 2,10, 12, 16, 17, 18, 19, ___')
print('Próximo elemento = 20')

print('-'*30)
#---------------------------------------------

#EXERCICIO 4´

print('EXERCICIO 4')
print('O carro estava mais próximo')

#O CARRO ESTAVA MAIS PRÓXIMO

#---------------------------------------------

#EXERCICIO 5 
print('-'*30)
print('EXERCICIO 5')

palavra = input('Digite uma palavra e esta será ivertida: ')
print(palavra[::-1])