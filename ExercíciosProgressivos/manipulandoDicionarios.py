cadastro ={
    "nome": "",
    "idade": 0,
    "cidade": "",
}

nome = input("[NOME] ")
cadastro["nome"] = nome
idade = input("[IDADE] ")
cadastro["idade"] = idade
cidade = input("[CIDADE] ma")
cadastro["cidade"] = cidade
for i in cadastro:
    print(i.upper(), cadastro[i])
