from consts import *


class Entity:

    def __init__(self, entity_type, sprites, x, y):
        self.entity_type = entity_type
        self.sprites = sprites
        self.x = x
        self.y = y
        self.bottom_x = x + TILE_SIZE
        self.bottom_y = y + TILE_SIZE
        pass

    def convert_entity_type(self, entity_type):
        entity_type_dictionary = {"player": 0, "enemy": 1, "environment": 2}
        sprite_set = entity_type_dictionary[entity_type]
        return sprite_set

    #def collision_detection(self):