import configparser

config = configparser.ConfigParser()


def get_settings():
    config.read('settings.ini')
    try:
        window_size = config['Settings']['Window size']
        window_size = list(window_size.split(","))
        window_size = int(window_size[0]), int(window_size[1])

        grid_size = config['Settings']['Grid size']
        grid_size = list(grid_size.split(","))
        grid_size = int(grid_size[0]), int(grid_size[1])
    except:
        window_size = 600, 600
        grid_size = 10, 10

    return window_size, grid_size
