def linha():
  print('======================================================================================')

linha()
print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.')
linha()
pessoa = {
  'nome': 'Daniel',
  'idade': 41,
  'cidade': 'Belo Horizonte'
}
linha()
print('2 - Utilizando o dicionário criado no item 1:')
linha()

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoa.update({'idade': 21})
print(pessoa)
pessoa['idade'] = 31
print(pessoa)

pessoa['profissao'] = 'Programador'
print(pessoa)
# Remova o campo 'cidade' do dicionário
del pessoa['cidade']
print(pessoa)
pessoa.pop('idade')
print(pessoa)

linha()
print('3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.')
linha()
dicionario = {
  1: 1**2, 2: 2**2, 3: 3**2, 4: 4**2, 5: 5**2
}
print(dicionario)

dicionario_loop_for = {
  i: i**2 for i in range(1,7)
}
print(dicionario_loop_for)

linha()
print('4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.')
linha()

pesquise_chave = {
  'nome': 'Daniel',
  'idade': 41,
  'cidade': 'Belo Horizonte'
  }
print('idade' in pesquise_chave) # True

linha()
print('5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.')
linha()
frase = "Python é uma linguagem de programação muito fácil fácil de aprender e usar"
palavras = frase.split()
dicionario_palavras = {}
for palavra in palavras:
  if palavra in dicionario_palavras:
    dicionario_palavras[palavra] += 1
  else:
    dicionario_palavras[palavra] = 1
print(dicionario_palavras)
