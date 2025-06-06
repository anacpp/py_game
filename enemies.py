from pgzero.actor import Actor
from pgzero.builtins import Rect


class Enemy:
    def __init__(self, pos, walls):
        self.actor = Actor("enemy_0", pos)
        self.speed = 3
        self.walls = walls
        self.direction = (self.speed, 0)
        self.frames = [
            "enemy_0",
            "enemy_1",
            "enemy_2",
            "enemy_3",
            "enemy_4",
            "enemy_5",
            "enemy_6",
            "enemy_7",
        ]
        self.frame_index = 0
        self.frame_timer = 0

    def draw(self):
        """Draw the enemy actor."""
        self.actor.draw()

    def try_move(self, dx, dy):
        """Try to move enemy by dx and dy, changing direction if blocked."""
        new_rect = Rect((self.actor.left + dx, self.actor.top + dy), self.actor.size)
        for wall in self.walls:
            wall_rect = Rect(wall.left, wall.top, wall.width, wall.height)
            if new_rect.colliderect(wall_rect):
                self.change_direction()
                return

        self.actor.x += dx
        self.actor.y += dy

    def update(self):
        """Update enemy animation and position."""
        self.animate()
        self.try_move(*self.direction)

    def change_direction(self):
        """Change enemy direction clockwise when hitting a wall."""
        if self.direction == (self.speed, 0):
            self.direction = (0, self.speed)
        elif self.direction == (0, self.speed):
            self.direction = (-self.speed, 0)
        elif self.direction == (-self.speed, 0):
            self.direction = (0, -self.speed)
        else:
            self.direction = (self.speed, 0)

    def animate(self):
        """Animate enemy sprite frames."""
        self.frame_timer += 1
        if self.frame_timer >= 3:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.actor.image = self.frames[self.frame_index]
            self.frame_timer = 0
