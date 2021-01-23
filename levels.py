from enemies import Enemy, Paths
from misc import Timer, timer_list
from movement_entities import collision_types


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
    new_path = path_system.create_path(len(path), paths[path])


class Level:
    def __init__(self, _screen):
        self.screen = _screen
        self.started = False
        self.squads = []
        self.add_list = []
        
    
    def start(self):
        self.started = True
        self.create_squad()
        
    def run(self):
        if self.started:
            for enemy in self.squads[0].squad_members:
                self.add_list.append(enemy)
            print(self.add_list)
            

    def load_enemy(self, _enemy):
        return _enemy

    def create_squad(self):
        new_squad = Squad(1, self.screen)
        new_squad.initialize_squad()
        self.squads.append(new_squad)


class Squad:
    def __init__(self, _size, _screen):
        self.size = _size
        self.screen = _screen
        self.squad_members = []
        
    def initialize_squad(self):
        for i in range(self.size):
            self.add_member(self.screen, 2)
        
    def add_member(self, _screen, _spd):
        new_member = Enemy(_screen, _spd, _collision_type=collision_types[2], _hitlist=collision_types[:1], _path=path_system.path_list[0])
        self.squad_members.append(new_member)

