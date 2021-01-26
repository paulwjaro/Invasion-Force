from enemies import Enemy, Paths
from gamefx import CustomSprite

paths = {
    # Horizontal Zigzags
    '0': [[-64, 32], [10, 32], [110, 96], [210, 32], [310, 96], [410, 32], [510, 96], [610, 32], [664, 32]],
    '1': [[-64, 128], [10, 128], [110, 192], [210, 128], [310, 192], [410, 128], [510, 192], [610, 128], [664, 128]],
    '2': [[-64, 224], [10, 224], [110, 288], [210, 224], [310, 288], [410, 224], [510, 288], [610, 224], [664, 224]]
}

path_system = Paths()

for path in paths:
    path_system.create_path(paths[path])


enemies = {
    'Drone_1': {
        'spd': 2,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Drone_1.png', 64)
    },
    'Drone_2': {
            'spd': 2,
            'collision_layer': 'enemies',
            'collision_mask': ['player', 'projectiles'],
            "c_width": 64,
            'c_height': 64,
            'sprite': CustomSprite('Assets/Drone_2.png', 64)
    },
    'Bot_1': {
        'spd': 3,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Bot_1.png', 64)
    },
    'Bot_2': {
        'spd': 3,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Bot_2.png', 64)
    },
    'Ship_1': {
        'spd': 4,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Ship_1.png', 64)
    },
    'Ship_2': {
        'spd': 4,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Ship_2.png', 64)
    }
}

levels = {
    '1': {
        'waves': {
            '0': {
                'strands': {
                    '0': {
                        'length': 6,
                        'enemy': enemies['Drone_1'],
                        'path': path_system.path_list[0]
                    },
                    '1': {
                        'length': 6,
                        'enemy': enemies['Drone_2'],
                        'path': path_system.path_list[1]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 7,
                        'enemy': enemies['Drone_1'],
                        'path': path_system.path_list[0]
                    },
                    '1': {
                        'length': 7,
                        'enemy': enemies['Bot_1'],
                        'path': path_system.path_list[1]
                    },
                    '2': {
                        'length': 7,
                        'enemy': enemies['Drone_2'],
                        'path': path_system.path_list[2]
                    }
                }
            },
        }
    },
    '2': {
        'waves': {
            '0': {
                'strands': {
                    '0': {
                        'length': 6,
                        'enemy': enemies['Drone_1'],
                        'path': path_system.path_list[0]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 7,
                        'enemy': enemies['Drone_2'],
                        'path': path_system.path_list[0]
                    }
                }
            },
        }
    },
    '3': {
        'waves': {
            '0': {
                'strands': {
                    '0': {
                        'length': 6,
                        'enemy': enemies['Drone_1'],
                        'path': path_system.path_list[0]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 7,
                        'enemy': enemies['Drone_2'],
                        'path': path_system.path_list[0]

                    }
                }
            },
        }
    }
}
