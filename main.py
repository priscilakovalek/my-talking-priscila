import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Talking Priscila")

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

# Carregar imagens da Priscila
priscila_normal = pygame.image.load("priscila1.png")  # Priscila normal
priscila_roupa = pygame.image.load("priscila2.png")  # Priscila com roupa
priscila_chapeu = pygame.image.load("priscila3.png")  # Priscila com chapéu
priscila_oculos = pygame.image.load("priscila4.png")  # Priscila com óculos

# Redimensionar imagens
priscila_normal = pygame.transform.scale(priscila_normal, (200, 300))
priscila_roupa = pygame.transform.scale(priscila_roupa, (200, 300))
priscila_chapeu = pygame.transform.scale(priscila_chapeu, (200, 300))
priscila_oculos = pygame.transform.scale(priscila_oculos, (200, 300))

# Carregar sons
meow_sound = pygame.mixer.Sound("meow.wav")  # Som de miado
troca_roupa_sound = pygame.mixer.Sound("troca.wav")  # Som ao trocar roupa

# Banco de falas da Priscila
falas = ["Oi!", "Que dia lindo!", "Me dá comida!", "Vamos brincar?", "Me adore!"]

# Variáveis do jogo
moedas = 0
acessorio_atual = 0  # 0 = normal, 1 = roupa, 2 = chapéu, 3 = óculos

# Fonte do texto
font = pygame.font.Font(None, 36)

# Tela inicial
def tela_inicial():
    screen.fill((255, 182, 193))  # Fundo rosa claro
    font_title = pygame.font.Font(None, 64)
    font_button = pygame.font.Font(None, 40)

    titulo = font_title.render("My Talking Priscila", True, WHITE)
    screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 150))

    botao = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
    pygame.draw.rect(screen, GREEN, botao)
    texto_botao = font_button.render("Iniciar", True, WHITE)
    screen.blit(texto_botao, (WIDTH // 2 - 40, 310))

    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if botao.collidepoint(x, y):
                    esperando = False  # Começa o jogo

# Função para exibir falas da Priscila
def mostrar_fala(texto):
    fala_texto = font.render(texto, True, (0, 0, 0))
    screen.blit(fala_texto, (WIDTH // 2 - fala_texto.get_width() // 2, 50))

# Loop principal do jogo
tela_inicial()  # Exibir tela de abertura

running = True
while running:
    screen.fill(WHITE)

    # Escolher qual imagem mostrar
    if acessorio_atual == 0:
        screen.blit(priscila_normal, (300, 200))
    elif acessorio_atual == 1:
        screen.blit(priscila_roupa, (300, 200))
    elif acessorio_atual == 2:
        screen.blit(priscila_chapeu, (300, 200))
    elif acessorio_atual == 3:
        screen.blit(priscila_oculos, (300, 200))

    # Exibir moedas
    texto_moedas = font.render(f"Moedas: {moedas}", True, (0, 0, 0))
    screen.blit(texto_moedas, (10, 10))

    # Exibir botões para trocar acessórios
    pygame.draw.rect(screen, GREEN, (550, 500, 200, 50))
    texto_botao = font.render("Trocar Acessório (-10)", True, WHITE)
    screen.blit(texto_botao, (560, 515))

    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Se clicar na Priscila, ela mia e ganha moedas
            if 300 < x < 500 and 200 < y < 500:
                meow_sound.play()
                moedas += random.randint(1, 5)
                mostrar_fala(random.choice(falas))  # Exibir fala aleatória
            # Se clicar no botão, troca o acessório
            elif 550 < x < 750 and 500 < y < 550 and moedas >= 10:
                troca_roupa_sound.play()
                moedas -= 10
                acessorio_atual = (acessorio_atual + 1) % 4  # Alterna entre os acessórios

    pygame.display.flip()

pygame.quit()