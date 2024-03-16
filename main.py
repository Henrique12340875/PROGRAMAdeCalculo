def adicao(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def init():
    while(True):
        print("Escolha uma opcao:")
        print("1-Adicao")
        print("2-Subtracao")
        print("3-Multiplicacao")
        print("4-Divisao")
        print("5-Fechar")
        dec = input("R:")

        if(dec == "1"):
            n1 = int(input("Digite um numero:"))
            n2 = int(input("Digite outro numero:"))
            print(adicao(n1,n2))
        elif(dec == "2"):
            n1 = int(input("Digite um numero:"))
            n2 = int(input("Digite outro numero:"))
            print(subtracao(n1,n2))
        elif(dec == "3"):
            n1 = int(input("Digite um numero:"))
            n2 = int(input("Digite outro numero:"))
            print(multiplicacao(n1,n2))
        elif(dec == "4"):
            n1 = int(input("Digite um numero:"))
            n2 = int(input("Digite outro numero:"))
            print(divisao(n1,n2))
        elif(dec == "5"):
            break

if __name__ == '__main__':
    init()