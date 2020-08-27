def numeroParImpar(numero):
    numeroPar="numero par"
    numeroImpar="numero impar"
    if numero%2 ==0:
        return numeroPar
    else: 
        return numeroImpar    

def leerNumero():
 numero=int(input("Ingrese un numero:"))
 resultado=numeroParImpar(numero)
 print(f"Este numero es un: {resultado}")

def main():
  leerNumero()


if __name__ =="__main__":
    main()   