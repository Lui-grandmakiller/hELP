nombre = input("¿cual es tu nombre? ")

año_de_nacimiento = int(input("¿en que año naciste?"))

from datetime import date 
año_actual = date.today().year
edad = año_actual - año_de_nacimiento

print(f"Tienes {edad}años xd")