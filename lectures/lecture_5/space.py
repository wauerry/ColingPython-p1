class SpaceObject:
    def __init__(self, name):
        self.name = name

class Star(SpaceObject):
    def __init__(self, name, brightness=None):
        super().__init__(name)
        self.brightness = brightness
