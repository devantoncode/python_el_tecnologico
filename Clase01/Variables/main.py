# ? Definición de Variables
nombre_mujer = "Maria Garcia"
nombre_hombre = "Jose Cato"

print(nombre_mujer, "\n", nombre_hombre)
print(nombre_mujer + "\n" + nombre_hombre)


# ? Fundición de Variables
nombre = "Pepito"
print(nombre)
nombre = "Gatita"

nombre = str("Pepito")
nombre = str("Gatita")
edad = int(20)

# ? Variables permitidas y no permitidas
# ! PERMITADAS
mivar = "Hola"
mi_var = "Hola"
_mi_var = "Hola"
miVar = "Hola"
mivar200 = "Hola"

# ! NO PERMITIDAS
# 2var = "Hola"
# mi-var = "Hola"
# mi var = "Hola"
# $\var = "Hola"
# print = "Hola"

# ? Case Sensitive
mivariable = "Juanita"
miVariable = "Robertita"
print(mivariable)

# ? Nombres al entorno de variables (upper, camell, snake)
mi_saludo = "Bienvenido Mundo"
miSaludo = "Bienvenido Mundo 2"
MiSaludo = "Bienvenido Mundo 3"

# ? Asignación Múltiple
x, y, z = "Hola", "Adios", "Mundo"
print(z, y, x)

nombre1 = nombre2 = nombre3 = "Oscar"
print(nombre3)

# ? Variable CONSTANTE
VALORPI = 3.1416