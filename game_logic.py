import pgzrun
from settings import *
from player import Player
from enemies import Enemy
from pgzero.builtins import music

WIDTH = TILE_SIZE * MAP_WIDTH
HEIGHT = TILE_SIZE * MAP_HEIGHT

player = None
coins = []
enemies = []
door = None
walls = []

game_over = False
game_win = False
game_state = "menu"
background = Actor('background', (WIDTH // 2, HEIGHT // 2))
current_music = None
sound_on = True

def play_game_music(track_name):
       global current_music

       if current_music != track_name:
        print(f"Tocando música: {track_name}")
        music.set_volume(0.7)
        music.play(track_name)
        current_music = track_name

def play_effect(track_name):
       
        music.set_volume(1.0)
        music.play_once(track_name)


def on_mouse_down(pos):
    global game_state, sound_on

    if game_state == "menu":
        if start_button.collidepoint(pos):
            game_state = "playing"
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on
        elif exit_button.collidepoint(pos):
            print("Exit selected")
            quit() 

def load_map():
    global player, coins, enemies, door, walls
    coins.clear()
    enemies.clear()
    walls.clear()

    for y in range(len(map_grid)):
        for x in range(len(map_grid[y])):
            val = map_grid[y][x]
            pos = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)

            if val == 1:
                walls.append(Actor('wall', pos))
            elif val == 'P':
                player = Player(pos, walls)
            elif val == 'C':
                coins.append(Actor('coin', pos))
            elif val == 'E':
                enemies.append(Enemy(pos, walls))
            elif val == 'D':
                door = Actor('door', pos)
load_map()
play_game_music('game_music')

def draw():
    screen.clear()
    if game_state == "menu":
        

        background.draw()
        screen.draw.text('WHERE IS MY SNACK', center=(400, 80), fontsize=60, color="white")
        screen.draw.filled_rect(start_button, "blue")
        screen.draw.text('Start Game', center=start_button.center, color="white")

        screen.draw.filled_rect(sound_button, "blue")
        screen.draw.text(f"Sound: {'ON' if sound_on else 'OFF'}", center=sound_button.center, color="white")

        screen.draw.filled_rect(exit_button, "blue")
        screen.draw.text("Exit", center=exit_button.center, color="white")

    elif game_state == "playing":
        
        for wall in walls:
            wall.draw()
        for coin in coins:
            coin.draw()
        for enemy in enemies:
            enemy.draw()
        if door:
            door.draw()
        if player:
            player.draw()
        if game_over:
            screen.draw.text("GAME OVER!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")
        elif game_win:
            screen.draw.text("YOU WIN!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="green")

def update():
    global game_over, game_win

    if game_over or game_win:
        return 

    if player:
        player.update(keyboard)

    for enemy in enemies:
        enemy.update()

    for coin in coins[:]: 
        if player.actor.colliderect(coin):
            play_effect('points_sound')
            coins.remove(coin)

    for enemy in enemies:
        if player.actor.colliderect(enemy.actor):
            play_effect('game_over')
            print("Game Over!")
            game_over = True

    if len(coins) == 0 and door:
        if player.actor.colliderect(door):
            print("You win!")
            play_effect('win')
            game_win = True

pgzrun.go()
