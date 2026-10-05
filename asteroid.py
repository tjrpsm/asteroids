from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        r1 = random.uniform(20,50)
        r2 = random.uniform(-50,-20)

        child1 = Asteroid(self.position[0], self.position[1], new_radius)
        c1_vector = self.velocity
        rotated_c1 = c1_vector.rotate(r1)
        rotated_c1_with_speed_vector = rotated_c1 * 1.2
        child1.velocity = rotated_c1_with_speed_vector

        child2 = Asteroid(self.position[0], self.position[1], new_radius)
        c2_vector = self.velocity
        rotated_c2 = c2_vector.rotate(r2)
        rotated_c2_with_speed_vector = rotated_c2 * 1.2
        child2.velocity = rotated_c2_with_speed_vector
        # could also have calcualted new movement with
        # childX.velocity = pygame.math.Vector2.rotate(self.velocity, rX) * 1.2
        # but I interpreted the directions as manipulating the vector "outside"
        # of the object
