import pygame

pygame.init()

field_sizes = (500, 400)
app = pygame.display.set_mode(field_sizes)
pygame.display.set_caption("My first game")

square_1_x = 0
square_1_y = 0

game_over: bool = False
while not game_over:
    pygame.display.update()

    app.fill((0, 0, 0))
    print(square_1_x, square_1_y)
    pygame.draw.rect(app, (255, 255, 255), (square_1_x, square_1_y, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if square_1_y < field_sizes[1] - 20:
                    square_1_y += 20
            if event.key == pygame.K_UP:
                if square_1_y > 0:
                    square_1_y -= 20
            if event.key == pygame.K_LEFT:
                if square_1_x > 0:
                    square_1_x -= 20
            if event.key == pygame.K_RIGHT:
                if square_1_x < field_sizes[0] - 20:
                    square_1_x += 20

        elif event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()