import pygame
import random
import os
import time
import math

pygame.font.init()

WIDTH, HEIGHT = 1200, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYER_IMG = pygame.image.load(os.path.join('Blue_Triangle_V3.png'))
SQUARE_IMG = pygame.image.load(os.path.join('Greensquare.png'))

BLACK = (0, 0, 0)

FPS = 60


class Collidable():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


def main():
    lost = False
    player_vel = 5
    score = 0
    player = Collidable(600, 500, PLAYER_IMG)
    run = True
    clock = pygame.time.Clock()
    squares = []
    main_font = pygame.font.SysFont('sfnsmono', 30)
    lost_font = pygame.font.SysFont('sfnsmono', 50)
    countdown_font = pygame.font.SysFont('sfnsmono', 100)

    def draw_window():
        if lost == False:
            score_label = main_font.render(f"Score: {score}", 1, (0, 255, 0))
            WIN.fill(BLACK)
            WIN.blit(score_label, (40, 50))

            player.draw(WIN)
            for square in squares:
                square.draw(WIN)

            if score < 75:
                cd_label_3 = countdown_font.render('3', 1, (255, 255, 255))
                WIN.blit(cd_label_3, (600, 200))
            elif 150 > score > 75:
                cd_label_2 = countdown_font.render('2', 1, (255, 255, 255))
                WIN.blit(cd_label_2, (600, 200))
            elif 225 > score > 150:
                cd_label_3 = countdown_font.render('1', 1, (255, 255, 255))
                WIN.blit(cd_label_3, (600, 200))
            elif 300 > score > 225:
                cd_label_4 = countdown_font.render('GO!', 1, (255, 255, 255))
                WIN.blit(cd_label_4, (580, 200))
            pygame.display.update()
        if lost == True:

            lost_label = lost_font.render(f'GAME OVER', 1, (0, 255, 0))
            lost_label2 = lost_font.render(f'Final Score: {score}', 1, (0, 255, 0))
            lost_label3 = lost_font.render(' Play Again(y/n)', 1, (0, 255, 0))
            WIN.fill(BLACK)
            WIN.blit(lost_label, (460, 100))
            WIN.blit(lost_label2, (370, 200))
            WIN.blit(lost_label3, (350, 300))
            pygame.display.update()
            key = pygame.key.get_pressed()
            if key[pygame.K_y]:
                main()
            elif key[pygame.K_n]:
                pygame.quit()

    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def main_menu():
        run = True

        while run:
            key = pygame.key.get_pressed()
            menu_font = pygame.font.SysFont('snsnmono', 50)
            menu_label = menu_font.render('Press SpaceBar to Start Game', 1, (0, 255, 0))

            WIN.fill(BLACK)
            WIN.blit(menu_label, (600, 100))
            pygame.display.update()

            if key[pygame.K_SPACE]:
                break

    while run:

        score += 1
        clock.tick(FPS)
        draw_window()
        square_vel = 4 + math.log(score, 7)
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.x -= player_vel
        if key[pygame.K_w]:
            player.y -= player_vel
        if key[pygame.K_d]:
            player.x += player_vel
        if key[pygame.K_s]:
            player.y += player_vel

        square_x = random.randrange(1200)
        square = Collidable(square_x, 0, SQUARE_IMG)

        while len(squares) < 10:
            squares.append(square)
        for square in squares:
            square.draw(WIN)
            # if square.y in collide_y and square.x in collide_x:
            #     run = False
            if square.y > 800:
                squares.remove(square)
            if collide(player, square) and score > 200:
                lost = True
        if lost:
            score -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for square in squares:
            square.y += square_vel

    pygame.quit()


if __name__ == '__main__':
    main()




