import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Load assets
font = pygame.font.SysFont("Arial", 24)

# Helper functions
def wrap_around(pos):
    """Wrap position around screen edges."""
    x, y = pos
    return [x % WIDTH, y % HEIGHT]

def distance(p1, p2):
    """Calculate the distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Classes
class Ship:
    def __init__(self):
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, WHITE, [(20, 0), (0, 30), (40, 30)])
        self.position = [WIDTH // 2, HEIGHT // 2]
        self.angle = 0
        self.velocity = [0, 0]

    def rotate(self, direction):
        self.angle += direction * 5

    def thrust(self):
        rad_angle = math.radians(self.angle)
        self.velocity[0] += math.cos(rad_angle) * 0.5
        self.velocity[1] += math.sin(rad_angle) * 0.5

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position = list(wrap_around(self.position))

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect.topleft)

class Asteroid:
    def __init__(self):
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]
        self.radius = random.randint(20, 40)

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position = list(wrap_around(self.position))

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.position[0]), int(self.position[1])), self.radius)

class Bullet:
    def __init__(self, position, angle):
        self.position = list(position)
        rad_angle = math.radians(angle)
        self.velocity = [math.cos(rad_angle) * 5, math.sin(rad_angle) * 5]
        self.lifespan = 60

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position = list(wrap_around(self.position))
        self.lifespan -= 1

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.position[0]), int(self.position[1])), 3)

# Game setup
ship = Ship()
asteroids = [Asteroid() for _ in range(5)]
bullets = []
score = 0
running = True

# Main game loop
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.rotate(-1)
    if keys[pygame.K_RIGHT]:
        ship.rotate(1)
    if keys[pygame.K_UP]:
        ship.thrust()
    if keys[pygame.K_SPACE]:
        bullets.append(Bullet(ship.position[:], ship.angle))

    ship.update()
    ship.draw()

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw()

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw()
        if bullet.lifespan <= 0:
            bullets.remove(bullet)

    for asteroid in asteroids[:]:
        if distance(ship.position, asteroid.position) < asteroid.radius:
            print("Game Over!")
            running = False
        for bullet in bullets[:]:
            if distance(bullet.position, asteroid.position) < asteroid.radius:
                asteroids.remove(asteroid)
                bullets.remove(bullet)
                score += 10

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
