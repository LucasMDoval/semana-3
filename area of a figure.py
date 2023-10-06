
#funcion que calcula el area de un circulo, necesito el input del radio
def figure_area (radio):
    area_circle = (2.1416 * radio**2)
    return area_circle

#pido el radio al usuario
radio = float(input("introduce el radio del círculo: "))

#guardo el area calculada por la función en una variable
resultado_area = figure_area(radio)

#imprimo el area calculada
print (resultado_area)





