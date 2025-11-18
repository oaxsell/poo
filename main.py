from personagem import Personagem

print("""
███╗░░░███╗░█████╗░██╗░░██╗███████╗██████╗░██╗███████╗███████╗░█████╗░
████╗░████║██╔══██╗██║░██╔╝██╔════╝██╔══██╗██║╚════██║╚════██║██╔══██╗
██╔████╔██║███████║█████═╝░█████╗░░██████╔╝██║░░███╔═╝░░███╔═╝███████║
██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░██╔═══╝░██║██╔══╝░░██╔══╝░░██╔══██║
██║░╚═╝░██║██║░░██║██║░╚██╗███████╗██║░░░░░██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
""")
print("1. Cadastrar pizzaria")
print("2. Listar pizzarias")
print("3. Ativar pizzaria")
print("4. Sair")
opcao = int(input("Escolha uma opção: "))
print("Quais os dados dos personagem?")

# snake_case
# VARIAVEL_PI = 3.14 UPPER_SNAKE_CASE
# PascalCase NomeDaClasse
# PEP-8 Convenção de código Python

p1 = Personagem(nome="Enzo", idade=17, altura=1.75, peso=70, cor="pardo")

print(f"O nome do personagem é {p1.nome}")
print(f"A idade do personagem é {p1.idade}")
print(f"A altura do personagem é {p1.altura}")
print(f"O peso do personagem é {p1.peso}")
print(f"A cor do personagem é {p1.cor}")
