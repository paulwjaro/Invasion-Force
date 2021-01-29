from enemies import *

paths = {
    # Horizontal Zigzags
    '0': [[-64, 32], [10, 32], [110, 96], [210, 32], [310, 96], [410, 32], [510, 96], [610, 32], [664, 32]],
    '1': [[-64, 128], [10, 128], [110, 192], [210, 128], [310, 192], [410, 128], [510, 192], [610, 128], [664, 128]],
    '2': [[-64, 224], [10, 224], [110, 288], [210, 224], [310, 288], [410, 224], [510, 288], [610, 224], [664, 224]]
}

path_system = Paths()

for path in paths:
    path_system.create_path(paths[path])




levels = {
    '1': {
        'waves': {
            '0': {
                'strands': {
                    '0': {
                        'length': 2,
                        'enemy': enemies_data['Drone_1'],
                        'path': path_system.path_list[0]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 3,
                        'enemy': enemies_data['Drone_2'],
                        'path': path_system.path_list[1]
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
                        'length': 3,
                        'enemy': enemies_data['Bot_1'],
                        'path': path_system.path_list[2]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 4,
                        'enemy': enemies_data['Bot_2'],
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
                        'length': 3,
                        'enemy': enemies_data['Ship_1'],
                        'path': path_system.path_list[2]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 4,
                        'enemy': enemies_data['Ship_2'],
                        'path': path_system.path_list[1]

                    }
                }
            },
        }
    }
}
