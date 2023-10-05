nombre = input("¿Cómo te llamas?: ")
residencia = input(f"{nombre}, encantado de conocerte. ¿De dónde eres?: ")
visitar = input(f"¡Qué sitio más bonito! Recomiéndame algún lugar bonito para visitar en {residencia}: ")
hobbie = input(f"Perfecto, me acordaré de visitar {visitar} cuando vaya a {residencia}. {nombre}, ¿qué te gusta hacer en tu tiempo libre?: ")

while True:
    quedar = input(f"¡Qué guay! A mí también me gusta {hobbie}. Cuando visite {residencia}, ¿podemos quedar para {hobbie} juntos? ¿Qué te parece si después de {hobbie} vamos a {visitar}?: ")

    if quedar == "ok":
        print(f"Guay, te aviso cuando esté por {residencia}. {nombre}, un placer haberte conocido.")
        break
    elif quedar == "me viene mal":
        print(f"Bueno, no te preocupes. Quedamos otro día. Un placer haberte conocido, {nombre}.")
        break
    else:
        print("No entendí tu respuesta. Por favor, responde 'ok' o 'me viene mal'.")