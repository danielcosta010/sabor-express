import os

restaurantes = [
  {
    'nome': 'Big Sabor', 
    'categoria': 'Hamburgueria',
    'ativo': False
  },
  {
    'nome': 'Boizão',
    'categoria': 'Pizzaria',
    'ativo': True
  },
  {
    'nome': 'Cantina',
    'categoria': 'italiana',
    'ativo': False
  }
]

def exibir_nome_do_programa():
  print('''
  ░██████╗░█████╗░██████╗░░█████╗░██████╗░ 
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
  ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
  ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
  ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
  ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝
  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
  ''')

def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurantes')
  print('3. Ativar restaurante')
  print('4. Sair\n')

def limpando_programa(texto):
  os.system('cls')
  print(texto)


def voltar_ao_menu_principal():
  input('Digite enter para voltar ao menu inicial: ')
  main()

def finaizar_app():
  limpando_programa('Finalizando app')

def opcao_invalida():
  print('Opção inválida!\n')
  

def cadastrar_novo_restaurante():
    limpando_programa('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite no nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def lista_restaurantes():
  limpando_programa('Restaurantes cadastrados')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = restaurante['ativo']
    print(f'- {nome_restaurante} | {categoria} | {ativo}')
  voltar_ao_menu_principal()
  
  
def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      lista_restaurantes()
    elif opcao_escolhida == 3:
      print('Ativar restaurante')
    elif opcao_escolhida == 4:
      finaizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

# ↓↓↓↓↓↓↓↓↓↓↓ o match é uma opção ao if elif else ↓↓↓↓↓↓↓↓↓↓↓↓
  # match opcao_escolhida:
  #   case 1:
  #     print('Cadastrar restaurante')
  #   case 2:
  #     print('Listar restaurantes')
  #   case 3:
  #     print('Ativar restaurante')
  #   case 4:
  #     print('Finalizar app')
  #   case _:
  #     print('Opção inválida')

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()


if __name__ == '__main__':
  main()


# numero = - 1

# while numero <= 0:
#   numero = int(input('Digite um numero positivo: '))

# print(f'Voce digitou o numero: {numero}')