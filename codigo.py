from datetime import date

datos_correctos = False
while not datos_correctos:
    try:

        nombre = input("¿cual es tu nombre?")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        
        año_nacimiento = int(input("¿en que año naciste"))

        año_actual = date.today().year
        if año_nacimiento > año_actual or año_nacimiento < 1900:

            raise ValueError("el año de nacimiento no es valido")
        
        edad = año_actual - año_nacimiento
        print(f"hola {nombre} tu edad es {edad}")

        datos_correctos = True
    except ValueError as e: 

        print(f"error {e} Intenta de nuevo")