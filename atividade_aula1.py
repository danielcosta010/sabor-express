nome = 'Daniel'
idade = 41

print(f'Meu nome é {nome} tenho {idade} anos.')
print('Estou aprendendo python na escola de programação da Alura.')
print('A', 'L', 'U', 'R', 'A', sep='\n')


pi = 3.14159

pi_arredondado = round(pi,  2)

# Utilizado round()
print(f'O valor arrendondado de pi é: {pi_arredondado}')
# Utilizado f-string
print(f'O valor de pi arredondao é: {pi:.2f}')
# Utilizado format()
print('O valor de pi arredondao é: {:.2f}'.format(pi))