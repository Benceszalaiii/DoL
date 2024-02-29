import fusionengine as fusion

arrow = fusion.SpriteSheet("./ground_arrows.png", 16, 16)
window = fusion.Window("asd", 300, 200)
player =fusion.Node(window, 0, 0, 200, 200)
print(arrow)
anim = fusion.Animation(window, arrow,15)
player.load_animation(anim)
player.set_frame(0)
@window.loop
def loop():
    window.set_fps(60)
    player.get_frame()
    player.update()