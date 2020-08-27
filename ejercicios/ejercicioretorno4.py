



def exponente(base,exponente):
    resultadoBase=base
    for x in range(1,exponente):
        resultadoBase=resultadoBase*base
    return resultadoBase

def factorial(numero):
    resultado = 1
    i = 1
    while i <= numero:
        resultado = resultado * i
        i = i + 1
    return resultado

def resultadoCalculoF(nf):
    resultadoFinal=1+nf
    for y in range(2,51):
        num1=exponente(nf,y)
        num2=factorial(y)
        num3=num1/num2
        resultadoFinal=resultadoFinal+num3
    print(f"El resultado de la funcion exponencial es: {resultadoFinal}")



def leerNumero():
    numeroFuncion=int(input("Digite un numero para sacar la funcion exponencial: "))
    resultadoCalculoF(numeroFuncion)


def main():
  leerNumero()


if __name__ =="__main__":
    main()   