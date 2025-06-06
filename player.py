from pgzero.actor import Actor
from pgzero.builtins import Rect
from settings import *


class Player:
    def __init__(self, pos, walls):
        self.actor = Actor('player_rt_1', pos)
        self.speed = 2
        self.walls = walls
        self.frames_right = ['player_rt_1', 'player_rt_2', 'player_rt_3', 'player_rt_2']
        self.frames_left = ['player_lf_1', 'player_lf_2', 'player_lf_3', 'player_lf_2']
        self.frames_up = ['player_up_1', 'player_up_2', 'player_up_3', 'player_up_2']
        self.frames_down = ['player_down_1', 'player_down_2', 'player_down_3', 'player_down_2']
        self.frame_index = 0
        self.frame_timer = 0
        self.current_direction = 'right'
        self.idle_frames = {
            'right': self.frames_right,
            'left': self.frames_left,
            'up': self.frames_up,
            'down': self.frames_down
        }

    def draw(self):
        """Draw the player actor."""
        self.actor.draw()

    def update(self, keys):
        """Update position and animation based on keys pressed."""
        if keys.left:
            self.try_move(-self.speed, 0)
            self.current_direction = 'left'
        elif keys.right:
            self.try_move(self.speed, 0)
            self.current_direction = 'right'
        elif keys.up:
            self.try_move(0, -self.speed)
            self.current_direction = 'up'
        elif keys.down:
            self.try_move(0, self.speed)
            self.current_direction = 'down'

        self.animate()

    def try_move(self, dx, dy):
        """Try moving player by dx, dy if no collision."""
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

    def animate(self):
        """Animate player sprite cycling frames per direction."""
        self.frame_timer += 1
        if self.frame_timer >= 5:
            self.frame_index = (
                self.frame_index + 1
            ) % len(self.idle_frames[self.current_direction])
            self.actor.image = self.idle_frames[self.current_direction][
                self.frame_index
            ]
            self.frame_timer = 0

