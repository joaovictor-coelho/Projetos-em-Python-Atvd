#Import OS
import os

#Função limpar tela
def limpar ():
    os.system('cls')
    return

#Função Menu
def mostrarMenu ():
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

#Função ler dados
def lerDados ():
    global baia
    global computador
    baia = int(input("Qual Baia (0 ou 1)?: "))
    computador = int(input("Qual Computador (0, 1 ou 2)?: "))
    
    
#Função Mostrar
def mostrar():
    print("Mapa de Assentos")
    for baias in lan:
        print(baias)
    input()
    
#Função Reservar/Cancelar

def operacao(b,c,op):
    global lan
    lan[b][c]=op
    input("Operação realizada com sucesso!")


#Principal
#Variáveis Globais
lan = [["L","L","L"],["L","L","L"]]
resp = 0
baia = 0
computador = 0

while resp!=4:
    resp = mostrarMenu()
    match resp:
        case 1:
            print("Reservar")
            lerDados()
            operacao(baia,computador,"R")
        
        case 2:
            print("Cancelar")
            lerDados()
            operacao(baia,computador,"L")
        
        case 3:
            mostrar()
        
        case 4:
            print("Obrigado por usar o sistema!!")
            
            
if __name__ == "__main__":
        
    