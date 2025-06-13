from main_calculadora import calcular_area_retangulo

from main_calculadora import calcular_area_triangulo

from main_calculadora import calcular_area_circulo

operacao=int(input("Digite a operação que voçe deseja: 1-Área Retângulo/2-Área Triângulo/3-Área Circulo: "))

if operacao == 1:
    base = float(input("Digite a base do seu Retângulo: "))
    altura = float(input("Digite a altura do seu Retângulo: "))
    calcular_area_retangulo(base,altura)
    print("A área do seu Retângulo é:",calcular_area_retangulo(base,altura))
elif operacao == 2:
    base =  float(input("Digite a base do seu Triângulo: "))
    altura = float(input("Digite a altura do seu Triângulo: "))
    calcular_area_triangulo(base,altura)
    print("A área do seu Triângulo é:",calcular_area_triangulo(base,altura))
else:
    raio =  float(input("Digite o Raio do seu Circulo: "))
    calcular_area_circulo(raio)
    print("A área do seu circulo é:",calcular_area_circulo(raio))




def calcular_area_retangulo(base,altura):
    areart= base*altura
    return areart
def calcular_area_triangulo(base,altura):
    areatr= (base*altura)/2
    return areatr
def calcular_area_circulo(raio):
    areaci= (raio**2)*3.14
    return areaci
    
