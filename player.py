from pgzero.actor import Actor
from settings import *
from pgzero.builtins import Rect

class Player:
    def __init__(self, pos, walls):
        self.actor = Actor('player', pos)
        self.speed = 2
        self.walls = walls

    def draw(self):
        self.actor.draw()

    def update(self, keys):
        if keys.left:
            self.try_move(-self.speed, 0)
        if keys.right:
            self.try_move(self.speed, 0)
        if keys.up:
            self.try_move(0, -self.speed)
        if keys.down:
            self.try_move(0, self.speed)

    def try_move(self, dx, dy):
        new_rect = Rect(
            (self.actor.left + dx, self.actor.top + dy),
            self.actor.size
        )
        for wall in self.walls:
            wall_rect = Rect(wall.left, wall.top, wall.width, wall.height)
            if new_rect.colliderect(wall_rect):
                return     
        self.actor.x += dx
        self.actor.y += dy
