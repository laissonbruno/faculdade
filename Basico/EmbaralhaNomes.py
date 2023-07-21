import random  # Importa o módulo 'random' para gerar números aleatórios

def embaralha(nome):
    # Converte a string 'nome' em uma lista de caracteres
    a = list(nome)

    # Embaralha os elementos da lista aleatoriamente
    random.shuffle(a)

    # Junta os caracteres da lista novamente em uma string
    # a ordem embaralhada e converte todos os caracteres para letras minúsculas
    a = ''.join(a).lower()

    # Imprime a string embaralhada e em letras minúsculas
    print(a)

# Loop infinito para executar continuamente o embaralhamento
while True:
    nome = input('Digite algo: ')  # Solicita ao usuário que digite algo
    embaralha(nome)  # Chama a função 'embaralha' para embaralhar e imprimir o resultado
