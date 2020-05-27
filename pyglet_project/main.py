import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()

image = pyglet.resource.image('.png')
image.anchor_y = image.width/2
image.anchor_x = image.height/2
sprite = pyglet.sprite.Sprite(image, 200, 200)
print(sprite.opacity)
##label = pyglet.text.Label('Hello, world',
##                          font_name='Times New Roman',
##                          font_size=36,
##                          x=window.width//2, y=window.height//2,
##                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    sprite.draw()
##    print("çiz")

@window.event
def on_key_press(symbol, modifiers):
    print(symbol, modifiers)

    sprite.opacity -= 10

    if sprite.rotation == 360:
        sprite.rotation = 0

@window.event
def on_key_release(symbol, modifiers):
    print(symbol, modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button, modifiers)


pyglet.app.run()
