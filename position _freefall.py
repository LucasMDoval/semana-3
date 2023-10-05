
#este progama va a calcular la posicion final de un objeto en caida libre
#aquí pedimos las variables (altura, gravedad, velocidad y tiempo en ese orden)

height = float(input("insert the height: "))
gravity = float(input("insert the gravity: "))
velocity = float(input("initial velocity: "))
time = float(input("time: "))

#aquí aplicamos la fórmula (altura final=velocidad inicial * tiempo − 1/2 gravedad(aceleración) * tiempo^2 + altura inicial)

final_position = ( velocity * time - 1 ) / ( 2 * gravity * time**2 + height )

print (final_position)

