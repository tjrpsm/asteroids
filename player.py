from circleshape import *
from shot import *
from constants import *

class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer: float = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt) -> None:
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer > 0:
                pass
            else:
                self.shoot()
                self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.cooldown_timer -= dt
        self.move(dt)


    def move(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
            self.position += rotated_with_speed_vector
        if keys[pygame.K_s]:
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * -dt
            self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        rotated_shot_with_speed_vector = rotated_shot * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_shot_with_speed_vector
