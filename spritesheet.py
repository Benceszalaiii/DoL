

import fusionengine as fusion


window = fusion.Window("asd", 800, 600)
player = fusion.Node(window, 200, 200, 100, 100)
anima = fusion.SpriteSheet("./ground_arrows.png", 16, 16)
anim = fusion.Animation(window, anima, 1/2)


@window.loop
def loop():
    window.set_fps(60)
    player.load_animation(anim)
    player.set_frame(player.get_frame() + 1)
    player.update()
