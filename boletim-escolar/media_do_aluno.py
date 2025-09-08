# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: 
# Utilize operadores aritméticos para realizar o cálculo da média.
media = 0
for x in range(1,4):
    nota = float(input(f"Digite sua nota {x}: "))
    media += nota
print(f"\nA média do aluno é: {media/3:.2f}\n")
