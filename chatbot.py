#pregunto por el nombre
nombre = input("¿Cómo te llamas?: ")

#pregunto de donde es 
residencia = input(f"{nombre}, encantado de conocerte. ¿De dónde eres?: ")

#pido que me recomiende un sitio para visitar en el lugar que vive
visitar = input(f"¡Qué sitio más bonito! Recomiéndame algún lugar bonito para visitar en {residencia}: ")

#pregunto por sus aficiones en el tiempo libre
hobbie = input(f"Perfecto, me acordaré de visitar {visitar} cuando vaya a {residencia}. {nombre}, ¿qué te gusta hacer en tu tiempo libre?: ")

#abro un bucle con la funcion de que si me responde algo que no sea ninguna de las 2 opciones que propongo repita la pregunta
while True:
    quedar = input(f"¡Qué guay! A mí también me gusta {hobbie}. Cuando visite {residencia}, ¿podemos quedar para {hobbie} juntos? ¿Qué te parece si después de {hobbie} vamos a {visitar}?  ok/me viene mal : ")

#si responde algunauna de las opciones el bucle se cierra 
    if quedar == "ok":
        print(f"Guay, te aviso cuando esté por {residencia}. {nombre}, un placer haberte conocido.")
        break
    elif quedar == "me viene mal":
        print(f"Bueno, no te preocupes. Quedamos otro día. Un placer haberte conocido, {nombre}.")
        break

#si no responde ninguna de las opciones el bucle te devuelve a la linea donde empieza
    else:
        print("No entendí tu respuesta. Por favor, responde 'ok' o 'me viene mal'.")