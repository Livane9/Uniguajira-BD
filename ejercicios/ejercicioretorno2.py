def numeroPrimonoPrimo(numero):
    numeroPrimo="es primo"
    numeroNo="no es primo"
    contador=0
    for x in range(1,numero+1):
        if numero%x==0:
            contador=contador+1
    if contador==2:
        return numeroPrimo
    else:
        return numeroNo

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 resultado=numeroPrimonoPrimo(numero)
 print(f"El numero: {resultado}")

def main():
  leerNumero()


if __name__ =="__main__":
    main()   