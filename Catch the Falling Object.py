import pygame
import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BASKET_WIDTH, BASKET_HEIGHT = 100, 50
OBJECT_WIDTH, OBJECT_HEIGHT = 20, 20
FPS = 60
OBJECT_FALL_SPEED = 3
LIVES = 3


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")


class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BASKET_WIDTH, BASKET_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect.y = 0

    def update(self):
        self.rect.y += OBJECT_FALL_SPEED


def game():
    basket = Basket()
    falling_objects = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(basket)
    
    score = 0
    lives = LIVES
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        
        
        if random.randint(1, 20) == 1:
            falling_object = FallingObject()
            falling_objects.add(falling_object)
            all_sprites.add(falling_object)
        
        
        caught_objects = pygame.sprite.spritecollide(basket, falling_objects, True)
        score += len(caught_objects)
        
        
        for obj in falling_objects:
            if obj.rect.top > SCREEN_HEIGHT:
                obj.kill()
                lives -= 1
                if lives == 0:
                    running = False
        

        screen.fill(WHITE)
        all_sprites.draw(screen)
        
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        lives_text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    
    screen.fill(WHITE)
    game_over_text = font.render("Game Over", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    game()
