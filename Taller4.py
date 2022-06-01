#Samuel Aroca   
#Jim Díaz del Castillo
#Hamlet Pirazán 
#Giancarlo Cabrera
import math

class Taller4:

    def suma(a,b,n):
        return (a + b) % n

    def resta(a,b,n):
        return (a - b) % n

    def multi(a,b,n):
        return (a * b) % n

    def expo(a,b,n):
        return (math.pow(a,b)) % n

    def inverso(a,n):
        return (a*(math.pow(a,-1))) % n
        

    print("!!!Bienvenido a la calculadora de operaciones modulares!!!")
    print(" ")

    salir = 1

    while salir != 0:
        
        print("Ingrese los valores")
        print(" ")
        a = float(input("Digite el valor de a: "))
        print(" ")
        b = float(input("Digite el valor de b: "))
        print(" ")
        n = int(input("Digite el valor de n: "))
        print(" ")
        print("1 Suma, 2 Resta, 3 Multiplicación, 4 Exponenciación, 5 Inverso, 0 Para salir")
        print(" ")
        opc = int(input("Digite su opción: "))
        print(" ")

        if opc == 0:
            break

        elif opc == 1:

            print(suma(a,b,n))

        elif opc == 2:

            print(resta(a,b,n))

        elif opc == 3:

            print(multi(a,b,n))

        elif opc == 4:
            
            print(expo(a,b,n))

        elif opc == 5:
            
            resul = inverso(a,n)

            if resul == 1:
                print("Es inverso modular ", resul)
            else: 
                print("No es inverso modular ", resul)

        else:
            print("Elija una opcion correcta")

        print(" ")
        salir = int(input("Si desea salir digite 0, si no cualquier otro numero: "))
        print(" ")