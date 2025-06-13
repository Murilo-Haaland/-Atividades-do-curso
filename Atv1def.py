def calcular_imc (peso,altura):
 imc=peso/(altura*altura)
 
 return imc
 
def main():
    nome=input("Digite seu nome: ")
    altura=float(input("Digite sua altura: "))
    peso=float(input("Digite seu peso: "))
    
    resultado = calcular_imc(peso,altura)
    
    print(nome,"seu imc é:",resultado)

main()
