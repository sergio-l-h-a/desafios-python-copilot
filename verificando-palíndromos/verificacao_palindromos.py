# Vamos testar se uma palavra é um palíndromo?! Uma dica é: 
# Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
from colorama import init, Fore, Style
init()

palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print(Fore.GREEN + "\nA palavra é um palíndromo!\n".upper() + Style.RESET_ALL)
else:
    print("\n" + Fore.RED + "A palavra não é um palíndromo.\n".upper() + Style.RESET_ALL)