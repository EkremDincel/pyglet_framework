import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_key_press(symbol, modifiers):
    print(symbol, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    print(symbol, modifiers)

def update(dt):
    sprite.x += sprite.dx * dt

pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz

pyglet.app.run()
