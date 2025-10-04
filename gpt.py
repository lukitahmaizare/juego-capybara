import pygame

# Inicializar pygame
pygame.init()

# Configuración de ventana
ancho, alto = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con misiones")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 200, 0)
amarillo = (255, 255, 0)

# Jugador
jugador = pygame.Rect(50, 50, 40, 40)
velocidad = 5

# NPC
npc = pygame.Rect(300, 200, 40, 40)

#Imagen de la estrella
img_estrella = pygame.image.load("star.png")

# Objeto de misión (estrella)
estrella = pygame.Rect(500, 300, 30, 30)
mostrar_estrella = False

# Sistema de misión
mision_activa = False
mision_completada = False
fuente = pygame.font.SysFont(None, 30)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]: jugador.y -= velocidad
    if teclas[pygame.K_DOWN]: jugador.y += velocidad
    if teclas[pygame.K_LEFT]: jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]: jugador.x += velocidad

    # Colisión con NPC → activa misión
    if jugador.colliderect(npc) and not mision_activa and not mision_completada:
        mision_activa = True
        mostrar_estrella = True

    # Colisión con estrella → completa misión
    if jugador.colliderect(estrella) and mision_activa:
        mision_completada = True
        mostrar_estrella = False
        mision_activa = False

    # Dibujar en pantalla
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)   # jugador
    pygame.draw.rect(ventana, verde, npc)      # npc

    # Mostrar estrella solo si la misión está activa
    if mostrar_estrella:
        pygame.surface.blit(ventana, star, (100, 300))

    # Mostrar estado de misión
    if mision_completada:
        texto = fuente.render("Misión completada 🎉", True, (0, 0, 0))
    elif mision_activa:
        texto = fuente.render("Misión: recoge la estrella ⭐", True, (0, 0, 0))
    else:
        texto = fuente.render("Habla con el NPC (cuadro verde)", True, (0, 0, 0))

    ventana.blit(texto, (20, 20))

    # Actualizar pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(30)


pygame.quit()
