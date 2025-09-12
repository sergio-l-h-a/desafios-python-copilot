# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: 
# Utilize operadores aritméticos para realizar o cálculo da média.

from colorama import init, Fore, Style

init()

media = 0

for x in range(1,4):

    nota = float(input(f"Digite sua nota {x}: "))
    media += nota

print(f"\nA média do aluno é: {media/3:.2f}\n")


if media/3 >= 7:
    print(Fore.GREEN + f"Aluno aprovado!".upper() + "\n" + Style.RESET_ALL)

elif media/3 >= 5 and media/3 < 7:

    print(Fore.YELLOW + f"Aluno em recuperação!".upper() + "\n" + Style.RESET_ALL)

else:
    print(Fore.RED + f"Aluno reprovado!".upper() + "\n" + Style.RESET_ALL)
