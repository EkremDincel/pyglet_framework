import math
from pygame import Vector2 as V

class DotDict():
    __slots__ = ()
    
    __setitem__ = object.__setattr__
    __getitem__ = object.__getattribute__

    def __repr__(self):
        s = self.__class__.__name__ + "("
        for i in self.__slots__:
            s += i + "=" + repr(getattr(self, i)) + ", "
        s = s[:-2]
        return s + ")"


class BaseComponent(DotDict):
    __slots__ = ()
    
    components = set()

    def disable(self):
        self.components.remove(self)

    def enable(self):
        self.components.add(self)

class Vector(DotDict):
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def _iterater(self):
        yield self.x
        yield self.y
        
    def __iter__(self):
        return self._iterater()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        assert other.__class__ != Vector
        return Vector(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __pow__(self, other):
        return Vector(self.x ** other, self.y ** other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)
        
    def lenght(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lenghtsq(self):
        return self.x ** 2 + self.y ** 2

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_sqto(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def is_normalized(self):
        return self.x ** 2 + self.y ** 2 == 1

    def normalize(self):
        return self / math.sqrt(self.x ** 2 + self.y ** 2)

    def set_magnitude(self, magnitude):
        m = magnitude / math.sqrt(self.x ** 2 + self.y ** 2)
        self.x *= m
        self.y *= m

class RenderLayer(dict):
    layers = []

    def __init__(self, name, order):
        ...
        

class Transform(BaseComponent):
    __slots__ = ("transform", "rotation", "scale")

    def __init__(self):
        self.transform = Vector()
        self.rotation = 0
        self.scale = Vector()

class RigidBody(BaseComponent):
    __slots__ = ("velocity", "rotational_velocity")

    def __init__(self):
        self.velocity = Vector()
        self.rotational_velocity = 0

class ShapeRenderer(BaseComponent):
    __slots__ = ("shape", "layer", "order")

    def __init__(self, shape, layer = "default", order = 0):
        self.shape = shape
        self.layer = layer
        self.order = order

class SpriteRenderer(BaseComponent):
    __slots__ = ("sprite", "layer", "order")

    def __init__(self, sprite, layer = "default", order = 0):
        self.sprite = sprite
        self.layer = layer
        self.order = order

class BaseObject():
    objects = set()

##    def __init__(self):
##        self.components = {}


    def disable(self):
        self.objects.remove(self)

    def enable(self):
        self.objects.add(self)

    
