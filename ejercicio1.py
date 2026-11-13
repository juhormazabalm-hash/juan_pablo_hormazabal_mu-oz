cantidad_chefs = 0
while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("Ingrese la cantidad de chefs a registrar:\n"))
        if cantidad_chefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0


chef_maestros = 0
chef_aprendices = 0


for numero_chef in range(1, cantidad_chefs + 1):
    
    
    codigo = input("Ingrese el código culinario:\n")
    while len(codigo.replace(" ", "")) != len(codigo) or len(codigo) < 6:
        codigo = input("Ingrese el código culinario: ")

    
    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("Ingrese la experiencia culinaria:\n"))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0

    
    if experiencia > 8:
        chef_maestros += 1
    else:
        chef_aprendices += 1


print(f"¡La escuela cuenta con {chef_maestros} Chefs Maestros y {chef_aprendices} Chefs Aprendices! ¡A cocinar!")