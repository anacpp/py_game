from pgzero.actor import Actor
from pgzero.builtins import Rect

class Enemy:
    def __init__(self, pos, walls):
        self.actor = Actor('enemy', pos)
        self.speed = 2
        self.walls = walls
        self.direction = (self.speed, 0)

    def draw(self):
        self.actor.draw()

    def update(self):
        self.try_move(*self.direction)

    def try_move(self, dx, dy):
        new_rect = Rect(
            (self.actor.left + dx, self.actor.top + dy),
            self.actor.size
        )

        for wall in self.walls:
            wall_rect = Rect(wall.left, wall.top, wall.width, wall.height)
            if new_rect.colliderect(wall_rect):
                self.change_direction()
                return
      
        self.actor.x += dx
        self.actor.y += dy

    def change_direction(self):
        
        if self.direction == (self.speed, 0):  
            self.direction = (0, self.speed)   
        elif self.direction == (0, self.speed):
            self.direction = (-self.speed, 0)  
        elif self.direction == (-self.speed, 0):
            self.direction = (0, -self.speed)   
        else:
            self.direction = (self.speed, 0)
