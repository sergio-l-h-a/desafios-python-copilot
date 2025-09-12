# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

from colorama import init, Fore, Style
init()

print('\n')
entrada = input("Digite alguma coisa para ver o resultado: ")

quant = int(input("Digite um número: "))

for x in range(quant):

    print(Fore.CYAN + entrada.upper() + Style.RESET_ALL, end=' ')
 
print('\n\n')