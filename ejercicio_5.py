# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
palabra_1 = str(input('Ingrese palabra 1:'))

palabra_2 = str(input('Ingrese palabra 2:'))

# Objetivo:
# De la primera palabra tome las primeras tres letras,
# utilice el operador dos puntos :
# De la segunda palabra tome las primeras dos letras
# utilice el operador dos puntos 

# Alumno:
# Crear una variable llamada palabra_combinada
# con los recortes solicitados de las variables
# palabra_1 y palabra_2 en el orden correspondiente


# Imprima en pantalla la variable palabra_combinada

print("las 3 primeras letras de cada palabra son: ")
primeras_a = palabra_1[:3]   # Obtendré los primeros 3 caracteres
print("De la primera palabra los 3 carcateres son :",primeras_a)

primeras_b = palabra_2[:3]   # Obtendré los primeros 3 caracteres
print("De la segunda palabra los 3 carcateres son :", primeras_b)

palabra_combinada= primeras_a + primeras_b
print("Combinando los 3 primeros caracteres de cada palabra quedaría : ", palabra_combinada)


