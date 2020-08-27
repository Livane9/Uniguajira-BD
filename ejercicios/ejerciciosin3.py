def numeroPerfectonoPerfecto(numero):
    numeroPerfecto="es perfecto"
    numeroNo="no es perfecto"
    suma=0
    for i in range(1,numero):
        if numero%i==0:
            suma=suma+i
    if numero==suma:
        print(f"El numero: {numeroPerfecto}")
    else:
        print(f"El numero: {numeroNo}")
    

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 numeroPerfectonoPerfecto(numero)


def main():
  leerNumero()


if __name__ =="__main__":
    main()   