# Exercicio 1
arr_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_nomes = ['Maria', 'Ana', 'Juventina', 'Deomina']
arr_datas = [1982, 2024]

# Exercicio 2
def separacao(): 
  print('----------------------------')

for numero in arr_numeros:
  print(numero)

separacao()

for nome in arr_nomes:
  print(nome)

separacao()

for data in arr_datas:
  print(data)

separacao()

# Exercicio 3 return soma numeros impares
def soma_impares(arr):
  return sum([num for num in arr if num % 2 != 0])


print(soma_impares(arr_numeros))
separacao()

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
  print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número para tabuada: '))
for i in range(1, 11):
  print(f'{numero} X {i} = {numero * i}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
arr_soma_numeros = [1, 2, 3, 4, 5]
soma = 0
try:
  for i in arr_soma_numeros:
    soma += i
  print(f'Soma dos elementos é: {soma}')
except Exception as e:
    print(f'Erro: {e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
arr_media = [12, 21, 3, 14, 5,]
try:
  media = sum(arr_media) / len(arr_media)
  print(f'A média do arr_media é: {media}')
except ZeroDivisionError:
  print('Lista vazia')
except Exception as e:
  print(f'Ocorreu um erro {e}')
