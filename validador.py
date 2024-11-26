from datetime import date 
datos_correctos = False

while not datos_correctos:
    try:

        año_nacimiento = int(input("Hola ¿En que año naciste"))

        año_actual = date.today().year

        if año_nacimiento > año_actual or año_nacimiento < 1900 : 
            raise ValueError("el año de nacimiento no es válido")

        edad = año_actual - año_nacimiento
        if edad >= 18:
             print(f"Hola tienes {edad} y eres mayor de edad")

        if edad < 18:
            print (f"Hola tienes {edad} y eres menor de edad ")


        datos_correctos = True

    except ValueError as e: 
        print(f"error {e}Intentalo de nuevo")





    

    
