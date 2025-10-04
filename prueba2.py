import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con misiones y obstáculos")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 200, 0)
AMARILLO = (255, 255, 0)
ROJO = (200, 0, 0)
NEGRO = (0, 0, 0)

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
    pygame.Rect(500, 250, 120, 80),
]

# Objetos (estrellas)
def generar_objetos(cantidad):
    objetos = []
    for _ in range(cantidad):
        pos=[(300, 300), (100, 100), (300, 200), (500, 500), (400, 400)]
        x, y = pos.pop(random.randrange(len(pos)))
        objetos.append(pygame.Rect(x, y, 25, 25))
    return objetos

# Estado del juego
mision_activa = False
mision_completada = False
objetos = []
objetos_restantes = 0

# Fuente para texto
fuente = pygame.font.SysFont(None, 32)
reloj = pygame.time.Clock()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False


    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    
      # Guardar posición anterior del jugador (por si choca)
    pos_anterior = jugador.copy()
    
    if teclas[pygame.K_UP]: jugador.y -= velocidad
    if teclas[pygame.K_DOWN]: jugador.y += velocidad
    if teclas[pygame.K_LEFT]: jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]: jugador.x += velocidad

    # Colisiones con obstáculos → regresar a posición anterior
    for obs in obstaculos:
        if jugador.colliderect(obs):
            jugador = pos_anterior.copy()

    # Interacción con NPC → activa misión
    if jugador.colliderect(npc) and not mision_activa and not mision_completada:
        mision_activa = True
        objetos = generar_objetos(3)
        objetos_restantes = len(objetos)

    # Colisión con objetos (recolectar)
    if mision_activa:
        for objeto in objetos[:]:
            if jugador.colliderect(objeto):
                objetos.remove(objeto)
                objetos_restantes -= 1
        if objetos_restantes <= 0:
            mision_activa = False
            mision_completada = True

    # Dibujar en pantalla
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, AZUL, jugador)  # jugador
    pygame.draw.rect(ventana, VERDE, npc)     # npc

    # Dibujar obstáculos
    for obs in obstaculos:
        pygame.draw.rect(ventana, ROJO, obs)

    # Dibujar objetos si hay misión activa
    for objeto in objetos:
        pygame.draw.circle(ventana, AMARILLO, (objeto.x + 12, objeto.y + 12), 12)

    # Mostrar texto de misión
    if not mision_activa and not mision_completada:
        texto = fuente.render("Habla con el NPC (verde) para aceptar la misión", True, NEGRO)
    elif mision_activa:
        texto = fuente.render(f"Misión: recoge las estrellas ({objetos_restantes} restantes)", True, NEGRO)
    else:
        texto = fuente.render("¡Misión completada! 🎉", True, NEGRO)

    ventana.blit(texto, (20, 20))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

