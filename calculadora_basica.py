def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def main():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")	
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: ")) 
    if opcion == "1":
        print("Resultado de la suma: ", suma(a,b))
    elif opcion == "2":
        print("Resultado de la resta: ", resta(a,b))
    elif opcion == "3":
        print("Saliendo de la calculadora...")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

main()