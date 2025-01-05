"""Hoy aprendi a no subestimar  el ejercicio, a realizar mis test antes de enviar mis cambios"""

def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer()) and num % 2 == 0

def isinteger(num):
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

def main():
    while True:
        try:
            numbers_str = input("Ingresar los números separados por coma ',': ")
            numbers = [float(num) for num in numbers_str.split(',')]

            operation = input("Ingrese la operación (+, *, even, int): ")

            if operation == '+':
                result = addmultiplenumbers(numbers)
                print("Resultado de la suma:", result)
            elif operation == '*':
                result = multiplymultiplenumbers(numbers)
                print("Resultado de la multiplicación:", result)
            elif operation == 'even':
                for num in numbers:
                    print(f"{num} es par: {isiteven(num)}")
            elif operation == 'int':
                for num in numbers:
                    print(f"{num} es entero: {isinteger(num)}")
            else:
                print("Operación no válida.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos separados por comas.")

if __name__ == "__main__":
    main()
