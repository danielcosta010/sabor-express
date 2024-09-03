# Atividade 1

numero_digitado = int(input('Digite um número: '))

if numero_digitado % 2 == 0:
  print('O número é par')
else: 
  print('O número é impar')

# match numero_digitado % 2:
#   case 0:
#     print('O número é par')
#   case 1:
#     print('O número é impar')

print('--------------------------------------')

# Atividade 2
idade_usuario = int(input('Digite sua idade: '))
if idade_usuario <= 12:
  print('Você é criança')
elif 12 < idade_usuario < 18:
  print('Você é adolescente')
else: 
  print('Você é adulto')

print('-------------------------------------')

# Atividade 3
nome_usuario = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

if nome_usuario == 'Daniel' and senha == '1234':
  print('Bem-vindo, Daniel')
else:
  print('Nome ou senha incorreto')

# print(f'Seu nome é {nome_usuario}')
# print(f'Seu nome tem {len(nome_usuario)} letras')
print('-------------------------------------')

# Atividade 4
eixo_x = int(input('Digite o numero no eixo x: '))
eixo_y = int(input('Digite o numero no eixo y: '))
if eixo_x > 0 and eixo_y > 0:
  print('O ponto está no primeiro quadrante')
elif eixo_x < 0 and eixo_y > 0:
  print('O ponto está no segundo quadrante')
elif eixo_x < 0 and eixo_y < 0:
  print('O ponto está no terceiro quadrante')
elif eixo_x > 0 and eixo_y < 0:
  print('O ponto está no quarto quadrante')
else:
  print('O ponto está na origem')