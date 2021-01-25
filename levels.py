from player import Player
from enemies import Enemy, Paths
from gamefx import CustomSprite
from misc import Timer, timer_list


enemy_list = ["Assets/Drone_1.png", "Assets/Drone_2.png", "Assets/Bot_1.png", "Assets/Bot_2.png",
              "Assets/Ship_1.png", "Assets/Ship_2.png"]
paths = {
    # Horizontal Zigzags
    '0': [[-64, 32], [10, 32], [110, 96], [210, 32], [310, 96], [410, 32], [510, 96], [610, 32], [664, 32]],
    '1': [[-64, 128], [10, 128], [110, 192], [210, 128], [310, 192], [410, 128], [510, 192], [610, 128], [664, 128]],
    '2': [[-64, 224], [10, 224], [110, 288], [210, 224], [310, 288], [410, 224], [510, 288], [610, 224], [664, 224]]
}

path_system = Paths()

for path in paths:
    path_system.create_path(paths[path])
        
    
    # new_path_length = len(paths[path])
    # new_nodex = paths[path][0][0]
    # new_nodex = paths[path][0][1]





class ObjectHandler:
    def __init__(self, _screen):
        self.screen = _screen
        self.active_objects = []
        self.player = None

    def create(self):
        self.player = Player(self.screen, 320, 420, 64, 64, 3, 'player', ['enemies'], _sprite=CustomSprite('Assets/Player_1.png', 64))
        self.add_object_to_game(self.player)
        new_enemy = Enemy(self.screen, 2, 'enemies', ['player', 'projectiles'], 64, 64, path_system.path_list[1], _sprite=CustomSprite('Assets/Drone_2.png', 64))
        self.add_object_to_game(new_enemy)

    def object_handler(self, _screen):
        if len(self.active_objects) > 0:
            for _object in self.active_objects:
                if _object.destroyed:
                    self.active_objects.pop(self.active_objects.index(_object))

                else:
                    _object.play()
                    if _object.collision_layer != 'none':
                        for collisions in self.active_objects:
                            if _object != collisions:
                                if _object.rect.colliderect(collisions.rect):
                                    if collisions.collision_layer in _object.collision_mask:
                                        _object.hit()
                                        collisions.hit()




        # if len(self.collision_objects) > 0:
        #     for _object in self.collision_objects:
        #         if _object.destroyed:
        #             self.collision_objects.pop(self.collision_objects.index(_object))
        #         else:
        #             for collisions in self.collision_objects:
        #                 if _object != collisions:
        #                     if _object.rect.colliderect(collisions.rect):
        #                         if _object.collision_type in collisions.can_hit:
        #                             _object.hit()
        #                             collisions.hit()

    def add_object_to_game(self, _object):
        self.active_objects.append(_object)

