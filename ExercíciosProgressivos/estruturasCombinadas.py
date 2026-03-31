listaAlunos = [{"nome": '', "nota": 0}, 
               {"nome": '', "nota": 0}, 
               {"nome": '', "nota": 0}
]

for i in range(len(listaAlunos)):
    nome = input(f"NOME DO ALUNO {i+1}: ")
    nota = float(input(f"NOTA DO ALUNO {i+1}: "))
    listaAlunos[i]["nome"] = nome
    listaAlunos[i]["nota"] = nota

