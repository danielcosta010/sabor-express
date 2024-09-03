import os

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

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

def finaizar_app():
  os.system('cls')
  print('Finalizando app\n')

def escolher_opcoes():
  if opcao_escolhida == 1:
    print('Cadastrar restaurante')
  elif opcao_escolhida == 2:
    print('Listar restaurantes')
  elif opcao_escolhida == 3:
    print('Ativar restaurante')
  elif opcao_escolhida == 4:
    finaizar_app()
  else:
    print('Opção inválida')

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
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()


if __name__ == '__main__':
  main()