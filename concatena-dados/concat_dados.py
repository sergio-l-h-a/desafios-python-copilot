from colorama import init, Fore, Style
init()
# Vamos recebe dois dads diferentes do usuário e concatena

nome = input("Digite seu nome: ")
sobreNome = input("Digite seu sobrenome: ")

print(f"{nome} {sobreNome}")


# Loop de validação para o nome
while True:
    nome = input(f"{Fore.CYAN}Digite seu nome:{Style.RESET_ALL} ")
    if nome.strip() == "":
        print(f"{Fore.RED}O nome não pode ser vazio. Tente novamente.{Style.RESET_ALL}")
    else:
        break

# Loop de validação para o sobrenome
while True:
    sobreNome = input(f"{Fore.CYAN}Digite seu sobrenome:{Style.RESET_ALL} ")
    if sobreNome.strip() == "":
        print(f"{Fore.RED}O sobrenome não pode ser vazio. Tente novamente.{Style.RESET_ALL}")
    else:
        break
print(f"{Fore.GREEN}Nome completo: {nome} {sobreNome}{Style.RESET_ALL}")

