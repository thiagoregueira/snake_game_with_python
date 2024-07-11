import random
import sys

import pygame

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
screen_width = 400
screen_height = 400

# Configura a exibição
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title='Jogo da Cobrinha', icontitle='🐍')

# Cores
light_gray = (200, 200, 200)
dark_blue = (0, 0, 139)
orange = (255, 165, 0)
red = (213, 50, 80)

# Objeto de relógio
clock = pygame.time.Clock()

# Tamanho do bloco da cobra
snake_block = 10
snake_speed = 15


# Função para desenhar a cobra
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(
            game_display, dark_blue, [x[0], x[1], snake_block, snake_block]
        )


# Função para exibir mensagens na tela
def message(msg, color):
    font_style = pygame.font.SysFont(None, 16)
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [screen_width / 12, screen_height / 2])


# Função principal do jogo
def game_loop():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Mudança de posição da cobra
    x1_change = 0
    y1_change = 0

    # Lista para armazenar o corpo da cobra
    snake_list = []
    length_of_snake = 1

    # Posição inicial da comida
    foodx = (
        round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    )
    foody = (
        round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    )

    while not game_over:
        while game_close is True:
            game_display.fill(light_gray)
            message(
                'Você Perdeu! Pressione Q para Sair ou C para Jogar Novamente',
                red,
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Verifica se a cobra bateu nas bordas da tela
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(light_gray)
        pygame.draw.rect(
            game_display, orange, [foodx, foody, snake_block, snake_block]
        )
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Verifica se a cobra colidiu consigo mesma
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x1 == foodx and y1 == foody:
            foodx = (
                round(random.randrange(0, screen_width - snake_block) / 10.0)
                * 10.0
            )
            foody = (
                round(random.randrange(0, screen_height - snake_block) / 10.0)
                * 10.0
            )
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


# Inicia o jogo
game_loop()
