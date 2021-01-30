from enemies import *

paths = {
    # Horizontal Zigzags
    '0': [[-64, 32], [10, 32], [110, 96], [210, 32], [310, 96], [410, 32], [510, 96], [610, 32], [664, 32]],
    '1': [[-64, 128], [10, 128], [110, 192], [210, 128], [310, 192], [410, 128], [510, 192], [610, 128], [664, 128]],
    '2': [[-64, 224], [10, 224], [110, 288], [210, 224], [310, 288], [410, 224], [510, 288], [610, 224], [664, 224]],
    '3': [[60, -64], [60, 300], [580, 300], [580, -64]],
    '4': [[-64, 160], [100, 160], [180, 460], [220, 160], [380, 160], [460, 460], [540, 160], [704, 160]],
    '5': [[20, -64], [20, 20], [620, 340], [20, 340], [620, 20], [620, -64]],
    '6': [[-64, 300], [20, 300], [320, 60], [620, 300],[704, 300]]
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
                        'length': 10,
                        'enemy': enemies_data['Drone_1'],
                        'path': path_system.path_list[0]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 12,
                        'enemy': enemies_data['Drone_2'],
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
                        'length': 15,
                        'enemy': enemies_data['Bot_1'],
                        'path': path_system.path_list[5]
                    },
                    '1': {
                        'length': 15,
                        'enemy': enemies_data['Drone_2'],
                        'path': path_system.path_list[1]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 15,
                        'enemy': enemies_data['Drone_1'],
                        'path': path_system.path_list[4]
                    },
                    '1': {
                        'length': 15,
                        'enemy': enemies_data['Bot_2'],
                        'path': path_system.path_list[3]
                    }
                }
            },
            '2': {
                'strands': {
                    '0': {
                        'length': 12,
                        'enemy': enemies_data['Bot_1'],
                        'path': path_system.path_list[6]
                    },
                    '1': {
                        'length': 15,
                        'enemy': enemies_data['Ship_1'],
                        'path': path_system.path_list[5]
                    }
                }
            }
        }
    },
    '3': {
        'waves': {
            '0': {
                'strands': {
                    '0': {
                        'length': 20,
                        'enemy': enemies_data['Ship_1'],
                        'path': path_system.path_list[2]
                    },
                    '1': {
                        'length': 18,
                        'enemy': enemies_data['Bot_2'],
                        'path': path_system.path_list[5]
                    }
                }
            },
            '1': {
                'strands': {
                    '0': {
                        'length': 18,
                        'enemy': enemies_data['Ship_2'],
                        'path': path_system.path_list[0]

                    },
                    '1': {
                        'length': 20,
                        'enemy': enemies_data['Drone_2'],
                        'path': path_system.path_list[3]
                    }
                }
            },
            '2': {
                'strands': {
                    '0': {
                        'length': 20,
                        'enemy': enemies_data['Bot_1'],
                        'path': path_system.path_list[6]

                    },
                    '1': {
                        'length': 22,
                        'enemy': enemies_data['Bot_2'],
                        'path': path_system.path_list[5]
                    },
                    '2': {
                        'length': 18,
                        'enemy': enemies_data['Ship_1'],
                        'path': path_system.path_list[1]
                    }
                }
            },
            '3': {
                'strands': {
                    '0': {
                        'length': 22,
                        'enemy': enemies_data['Ship_2'],
                        'path': path_system.path_list[4]

                    },
                    '1': {
                        'length': 24,
                        'enemy': enemies_data['Drone_1'],
                        'path': path_system.path_list[2]
                    },
                    '2': {
                        'length': 24,
                        'enemy': enemies_data['Ship_1'],
                        'path': path_system.path_list[3]
                    }
                }
            }
        }
    }
}
