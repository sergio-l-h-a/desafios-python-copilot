# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
# Uma dica é: Utilize condicionais para realizar a verificação e, se possível, 
# faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

from colorama import init, Fore, Style

init()

def verificar_par_impar():
    while True:
        try:
            numero = int(input(f"{Fore.CYAN}Digite um número inteiro:{Style.RESET_ALL} "))
            break
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Por favor, digite um número inteiro.{Style.RESET_ALL}")

    if numero % 2 == 0:
        cor = Fore.GREEN
        resultado = "par"
    else:
        cor = Fore.YELLOW
        resultado = "ímpar"

    print(f"{cor}O número {numero} é {resultado}.{Style.RESET_ALL}")

verificar_par_impar()