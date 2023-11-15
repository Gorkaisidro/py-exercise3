"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  numAdivinar = random.randint(1, 10)
  adivinado = False
  """"
  GORKA COMEME LOS HUEVOS
  """
  while not adivinado:
        numUsuario = int(input(f"Adivina el número (1-10): "))
        if numUsuario == numAdivinar:
            print(f"Felicidades, adivinaste el número {numAdivinar}")
            adivinado = True
        elif numUsuario < numAdivinar:
            print("El número es mayor. Inténtalo de nuevo.")
        else:
            print("El número es menor. Inténtalo de nuevo.")



def multiplication_table():
   # Solicitar al usuario que introduzca un número
    number = int(input("Introduce un número para la tabla de multiplicar: "))

    # Imprimir la tabla de multiplicar
    print(f"Tabla de multiplicar para {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


def basic_calculator():
   while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            # Realizar la operación según el operador ingresado
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("Operador no válido. Inténtalo de nuevo.")
                continue  # Volver a solicitar la entrada

            print(f"{num1} {operator} {num2} => Result: {result}")
            break  # Salir del bucle mientras si la operación se realiza con éxito

        except ValueError:
   
          print("Error: Ingresa números válidos. Inténtalo de nuevo.")

          print("{num1} {operator} {num2} => Result:", result)


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()