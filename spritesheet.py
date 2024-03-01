

import fusionengine as fusion


window = fusion.Window("asd", 800, 600)
player = fusion.Node(window, 200, 200, 100, 100)
anima = fusion.SpriteSheet("./ground_arrows.png",16,16)
anim = fusion.Animation(window, tuple([fusion.Image(f"./ground arrows/{x}.png", 100, 100, 120, 120) for x in range(1, 9)]), 15)

# player.set_frame(15)
# def window_inputs(self):
#    if fusion.key_down(fusion.KEY_E):
#       arr(fileobj, namehint="")


@window.loop
def loop():
    window.set_fps(60)
    player.load_animation(anim)
    player.update()
