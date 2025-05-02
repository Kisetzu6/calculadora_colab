import pandas as pd
import matplotlib.pyplot as plt

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2

def numerob(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def calculadora():
    while True:
        print("Calculadora")
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
        
        elif opcion in ["1", "2", "3", "4"]:
            num1 = numerob("Ingrese el primer número: ")
            num2 = numerob("Ingrese el segundo número: ")
            
            if opcion == "1":
                resultado = suma(num1, num2)
                print(f"La suma es: {resultado}")
            elif opcion == "2":
                resultado = resta(num1, num2)
                print(f"La resta es: {resultado}")
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"La multiplicación es: {resultado}")
            elif opcion == "4":
                resultado = division(num1, num2)
                print(f"La división es: {resultado}")
        
        elif opcion == "5":
            try:
                m = numerob("Ingrese la pendiente (m): ")
                b = numerob("Ingrese el intercepto (b): ")
                x = pd.Series(range(-10, 11))
                y = m * x + b
                
                plt.plot(x, y)
                plt.title(f"Gráfica de y = {m}x + {b}")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.show()
            except Exception as e:
                print(f"Error al generar la gráfica: {e}")
                
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")

calculadora()
