# Vamos solicitar dois números de entrada e depois vamos realizar uma operação simples entre eles.
from colorama import init, Fore, Style

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input(f"Escolha qual tipo de operação deseja fazer? ({Fore.CYAN}{("+ - * /")}{Style.RESET_ALL}): ")

#operacao = input("Escolha qual tipo de operação deseja fazer?' +, -, *, /:  ")


if operacao == '+':
    print(f"{num1 + num2}")
elif operacao == '-':
    print(f"{abs(num1 - num2)}")
elif operacao == '*':
    print(f"{num1 * num2}")
elif operacao == '/':
    print(f"{num1 / num2}")
else:
    print("Operação invalida!")
