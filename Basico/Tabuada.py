# Exibe o título da tabuada
print('\t Tabuada Abaixo ')

# Solicita ao usuário que digite o número para o qual deseja obter a tabuada
numero = int(input("Digite o número para o qual deseja saber a tabuada: "))

# Exibe o cabeçalho da tabuada com o número informado pelo usuário
print('\n' f'Tabuada de {numero}:' '\n')

# loop de repetição para calcular e exibir a tabuada do número informado
for v_taboada in range(1, 11):   
    # exibe cada linha da tabuada
    print(f'{numero} X {v_taboada} = {numero * v_taboada}')