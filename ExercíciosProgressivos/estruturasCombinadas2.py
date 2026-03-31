contatos = []
preenchido = 0
def cadastrarContato():
    nome = input("NOME: ")
    telefone = int(input("TELEFONE "))
    form = {"nome": nome, "telefone": telefone}
    contatos.append(form)
    
def exibirContato():
    for i in range(len(contatos)):
        print(f"CADASTRO {i+1}:\n NOME: {contatos[i]['nome']}\n TELEFONE: {contatos[i]['telefone']}")
def buscarContato(p):
    print(f"CADASTRO {p-1}:\n NOME: {contatos[p-1]['nome']}\n TELEFONE: {contatos[p-1]['telefone']}")    
while True:
    print("" \
    "1- Cadastrar Contato\n" \
    "2- Exibir Contato\n" \
    "3- Buscar Contato pelo Índice\n" \
    "0- Sair")
    menu = int(input())

    match menu:
        case 1:
            cadastrarContato()
            preenchido = 1
            continue
        case 2:
            if preenchido == 1:
                exibirContato()
            else:
                print("Não foi preenchido")
        case 3:
            indice = int(input("Qual indice você deseja? "))
            buscarContato(indice)
        case _:
            quit()
