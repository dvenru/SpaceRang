from os import path, listdir


class DataControl:
    def __init__(self):
        game_folder = path.dirname(__file__)
        resources_folder = path.join(game_folder, 'resources')

        # установка настроек игры
        self.settings = {}
        with open(path.join(game_folder, 'settings.srset')) as file:
            setting = [item.rstrip() for item in file.readlines()]
            for item in setting:
                self.settings[item.split("=")[0]] = item.split("=")[1]

        # установка шрифта
        load_font = listdir(path.join(resources_folder, 'fonts'))
        self.game_font = path.join(path.join(resources_folder, 'fonts'), load_font[0]) if len(load_font) != 0 else None

        self.system_type = []
