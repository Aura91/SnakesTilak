import pygame
import random

pygame.init()

# Colors
white = (100, 255, 200)
red = (255, 0, 0)
green = (0, 100, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes testing OwO")
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("WELCOME TO SNAKES OWO", red, 190, 250)
        text_screen("Press Enter To Play", (255,255,255), 230, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

clock = pygame.time.Clock()
# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    fps = 30
    score = 0
    init_velocity = 9
    snk_list = []
    snk_length = 1
    food_x = random.randint(30, screen_width/2)
    food_y = random.randint(20, screen_height/5)

    with open("highscore\hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue...", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<20:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                if score>int(hiscore):
                    hiscore = score
                    with open('hiscore.txt', "w") as f1:
                        f1.write(str(score))

                snk_length +=4

            gameWindow.fill(white)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                    game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
            text_screen("Score: " + str(score)+ "  High score: "+str(hiscore), red, 5, 5)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
