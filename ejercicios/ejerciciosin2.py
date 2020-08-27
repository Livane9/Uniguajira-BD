def numeroPrimonoPrimo(numero):
    numeroPrimo="es primo"
    numeroNo="no es primo"
    contador=0
    for x in range(1,numero+1):
        if numero%x==0:
            contador=contador+1
    if contador==2:
        print(f"El numero: {numeroPrimo}")
    else:
        print(f"El numero: {numeroNo}")

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 numeroPrimonoPrimo(numero)

def main():
  leerNumero()

if __name__ =="__main__":
    main()   

