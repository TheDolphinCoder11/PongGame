import pygame as pg
import random as r

# Important for line 88 - 97! https://sigon.gitlab.io/post/2018-10-10-pygame-rect/

WIDTH = 1720
HEIGHT = 1200
black = (0, 0, 0)
white = (255, 255, 255)




def main():
    pg.init()
    pg.RESIZABLE = True
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Pong Game")
    clock = pg.time.Clock()
    running = True
    started = False

    paddle_1 = pg.Rect(30, HEIGHT // 2 - 50, 7, 100)
    paddle_2 = pg.Rect(WIDTH - 30, HEIGHT // 2 - 50, 7, 100)
    ball = pg.Rect(WIDTH // 2 - 12, HEIGHT // 2 - 12, 25, 25)
    paddle_1_move = 0
    paddle_2_move = 0

    if r.randint(1, 2) == 1:
        ball_accel_x = r.randint(2, 4) * 0.1
    else:
        ball_accel_x = r.randint(2, 4) * 0.1 * -1
    if r.randint(1, 2) == 1:
        ball_accel_y = r.randint(2, 4) * 0.1
    else:
        ball_accel_y = r.randint(2, 4) * 0.1 * -1

    bot_speed = 3

    while running:
        screen.fill(black)
        if not started:
            font = pg.font.SysFont('Consolas', 30)
            text = font.render('Press Space to Start', True, white)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, text_rect)

            pg.display.flip()
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                         started = True
            continue

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    paddle_1_move = - 0.5
                if event.key == pg.K_s:
                    paddle_1_move =  0.5 
                if event.key == pg.K_UP:
                    paddle_2_move = -0.5
                if event.key == pg.K_DOWN:
                    paddle_2_move = +0.5
            if event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_s:
                    paddle_1_move = 0.0
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    paddle_2_move = 0.0       
            
        #Time elapse between now and the last frame   
        delta_time = clock.tick(60)
        paddle_1.top += paddle_1_move * delta_time
        paddle_2.top += paddle_2_move * delta_time

        #Setting Limits to the paddle
        if paddle_1.top < 0:
            paddle_1.top = 0
        elif paddle_1.bottom > 1200:
            paddle_1.bottom = 1200

        if paddle_2.top < 0:
            paddle_2.top = 0
        elif paddle_2.bottom > 1200:
            paddle_2.bottom = 1200

        if started:
            ball.left += ball_accel_x * delta_time
            ball.top += ball_accel_y * delta_time

        if ball.top < 0 or ball.bottom > HEIGHT:
            ball_accel_y *= -1
        
        #Check if the ball left the screen.
        if ball.left <= 0 or ball.right >= WIDTH:
            return
        if paddle_1.colliderect(ball) and paddle_1.left < ball.right:
            ball_accel_x *= -1
            ball.left += 5
        
        if paddle_2.colliderect(ball) and paddle_2.left < ball.right:
            ball_accel_x *= -1
            ball.left -= 5

        pg.draw.rect(screen, white, paddle_1)
        pg.draw.rect(screen, white, paddle_2)
        pg.draw.rect(screen, white, ball)
        pg.display.update()


if __name__ == '__main__':
    main() 