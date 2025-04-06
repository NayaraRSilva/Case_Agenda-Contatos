import json

agenda = []

def salvar_agenda():
  with open('agenda.json', 'w') as arquivo:
    json.dump(agenda, arquivo)
    print("Agenda salva com sucesso!")

def carregar_agenda():
  try:
    with open('agenda.json', 'r') as arquivo:
      agenda=json.load(arquivo)
      print("Agenda carregada com sucesso!")
      return agenda
  except:
    print("Nenhuma agenda foi encontrado. Iniciando uma nova agenda. \n")
    return []

def adicionar_contato(nome, telefone, email):
  contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
  }
  agenda.append(contato)
  print(f"Contato {nome} adicionado!")

def exibir_contatos():
   print("\n Contatos na agenda: ")
   for contato in agenda:
     print("Nome: ", contato['nome'])
     print("Telefone: ",contato['telefone'])
     print("E-mail: ", contato['email'])

def editar_contato():
  nome = input ("Digite o nome do contato que deseja editar: ")
  for contato in agenda:
    if contato['nome'] == nome:
      contato ['telefone'] = input("Digite o novo telefone: ")
      contato ['email'] = input("Digite o novo e-mail: ")
      print("Contato atualizado")
      break
    else:
      print("Contato não encontrado")

def remover_contato():
  nome = input("Digite o nome do contato que deseja remover: ")
  for contato in agenda:
    if contato['nome'] == nome:
      agenda.remove(contato)
      print("Contato removido")
      break
    else:
      print("Contato não encontrado")

agenda = carregar_agenda()

while True:
  print('\n -- Menu da Agenda --')
  print('1 - Adicionar contato')
  print('2 - Exibir Agenda')
  print('3 - Editar contato')
  print('4 - Remover contato')
  print('5 - Salvar Agenda ')
  print('6 - Sair')

  opcao = input ("Digite opção desejada ")
   
  if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    adicionar_contato(nome, telefone, email)
  
  elif opcao == "2":
    exibir_contatos()
  
  elif opcao == "3":
    editar_contato()

  elif opcao == "4":
    remover_contato()

  elif opcao == "5":
    salvar_agenda()

  elif opcao == "6":
     print("Encerrando a agenda")
     break
    
  else:
    print("Opção inválida. Tente novamente.")
   
