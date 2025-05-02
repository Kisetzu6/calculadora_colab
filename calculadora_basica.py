import pandas as pd
import matplotlib.pyplot as plt

def calculadora():
    while True:
        print("\nCalculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Gráfica de función lineal")
        print("Escribe 'salir' para terminar")
        
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion.lower() == "salir":
            print("Hasta luego")
            break
        
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 + num2
            print(f"La suma es: {resultado}")
            
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 - num2
            print(f"La resta es: {resultado}")
            
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 * num2
            print(f"La multiplicación es: {resultado}")
            
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print(f"La división es: {resultado}")
            else:
                print("No se puede dividir por cero.")
                
        elif opcion == "5":
            x = pd.Series(range(-10, 11))
            m = float(input("Ingrese la pendiente (m): "))
            b = float(input("Ingrese el intercepto (b): "))
            y = m * x + b
            
            plt.plot(x, y)
            plt.title(f"Gráfica de y = {m}x + {b}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
            
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")

calculadora()