import pgzrun

def draw():
    screen.clear()
    screen.draw.text("Teste de Música", center=(400, 300), fontsize=50, color="white")

def update():
    pass

def on_key_down():
    music.play('game_music')
    music.set_volume(1.0)

pgzrun.go()
