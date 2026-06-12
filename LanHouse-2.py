import os

# Função limpar tela
def limpar():
    os.system('cls')

# Função Menu
def mostrarMenu():
    limpar()
    print("=== SISTEMA DE RESERVAS ===")
    print()
    print("1 - Reservar")
    print("2 - Cancelar")
    print("3 - Mapa de Assentos")
    print("4 - Sair")
    print()
    resposta = int(input("Digite a opção: "))
    return resposta

# Função ler dados — CORRIGIDA: agora retorna os valores
def lerDados():
    baia = int(input("Qual Baia (0 ou 1)?: "))
    computador = int(input("Qual Computador (0, 1 ou 2)?: "))
    return baia, computador  # <-- ESSENCIAL

# Função Mostrar
def mostrar():
    limpar()
    print("=== MAPA DE ASSENTOS ===")
    print()
    for i, baias in enumerate(lan):
        print(f"Baia {i}: {baias}")
    print()
    input("Pressione Enter para voltar...")

# Função Reservar/Cancelar
def operacao(b, c, op):
    lan[b][c] = op
    input("Operação realizada com sucesso! Pressione Enter...")

# Principal
lan = [["L","L","L"],["L","L","L"]]
resp = 0

while resp != 4:
    resp = mostrarMenu()
    match resp:
        case 1:
            print("Reservar")
            baia, computador = lerDados()  # <-- recebe os valores retornados
            operacao(baia, computador, "R")

        case 2:
            print("Cancelar")
            baia, computador = lerDados()  # <-- recebe os valores retornados
            operacao(baia, computador, "L")

        case 3:
            mostrar()

        case 4:
            print("Obrigado por usar o sistema!!")