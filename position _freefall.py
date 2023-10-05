
#aquí pedimos las variables (altura, gravedad, velocidad y tiempo en ese orden)

height = float(input("insert the height: "))
gravity = float(input("insert the gravity: "))
velocity = float(input("initial velocity: "))
time = float(input("time: "))

#aquí aplicamos la fórmula (h=vt−1/2gt^2+H)

final_position = ( velocity * time - 1 ) / ( 2 * gravity * time**2 + height )

print (final_position)

