num1 = int(input("Intoduce un numero:"))
num2 = int(input("Introduce otro numero:"))

operacion = input("Introduce una operacion (+ - * / ): ")


match operacion:

    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2

print(f"El resultado de {num1} {operacion} {num2} es = {res}")