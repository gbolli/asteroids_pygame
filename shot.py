from typing import override
import pygame # type: ignore
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    @override
    def update(self, dt):
        self.position += self.velocity * dt