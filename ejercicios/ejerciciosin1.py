def numeroParImpar(numero):
    numeroPar="numero par"
    numeroImpar="numero impar"
    if numero%2 ==0:
        print(f"El numero es un: {numeroPar}")
    else: 
        print(f"El numero es un: {numeroImpar}")

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 numeroParImpar(numero)
def main():
  leerNumero()


if __name__ =="__main__":
    main()   