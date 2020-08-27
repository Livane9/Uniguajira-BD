def numeroPerfectonoPerfecto(numero):
    numeroPerfecto="es perfecto"
    numeroNo="no es perfecto"
    suma=0
    for i in range(1,numero):
        if numero%i==0:
            suma=suma+i
    if numero==suma:
        return numeroPerfecto
    else:
        return numeroNo
    

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 resultado=numeroPerfectonoPerfecto(numero)
 print(f"El numero: {resultado}")

def main():
  leerNumero()


if __name__ =="__main__":
    main()   