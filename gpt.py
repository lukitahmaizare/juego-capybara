import pygame

# Inicializar pygame
pygame.init()

# Configuración de ventana
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Juego con misiones y obstáculos")

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

# Obstáculos
obstaculos = [
    pygame.Rect(200, 100, 80, 200),
    pygame.Rect(400, 50, 50, 150),
    pygame.Rect(100, 300, 150, 50),
    pygame.Rect(500, 250, 120, 80)
]

# Imagen de la estrella
img_estrella = pygame.image.load("star.png")

# Objeto de misión (estrella)
def generar_objetos(cantidad):
    objetos=[]
    for i in range(cantidad):
        pos = [(300, 300), (100, 100), (300, 200), (500, 500), (400, 400)]
        x, y = pos.pop(random.randrange(len(pos)))
        objetos.append(pygame.Rect(x, y, 25, 25))
    return objetos

# Sistema de misión
mision_activa = False
mision_completada = False
objetos = []
objetos_restantes = 0
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
        objetos = generar_objetos(3)
        objetos_restantes = len()
        mostrar_estrella = True

    # Colisión con estrella → completa misión
    if mision_activa:
        for objeto in objetos[:]:
            if jugador.colliderect(objeto):
                objetos.remove(objeto)
                objetos_restantes -= 1
        if objetos_restantes = 0:
            mision_activa = False
            mision_completada = True
            
    # Dibujar en pantalla
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)   # jugador
    pygame.draw.rect(ventana, verde, npc)      # npc

    # Dibujar obstáculos
    for obs in obstaculos:
        pygame.draw.rect(ventana, rojo, obs)

    #Mostrar estrellas
    for objeto in objetos:
        pygame.Surface.blit(ventana, objeto, (objeto.x + 12, objeto.y + 12))

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


