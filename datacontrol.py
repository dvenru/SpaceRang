from os import path, listdir


class DataControl:
    def __init__(self):
        self.game_folder = path.dirname(__file__)
        self.resources_folder = path.join(self.game_folder, 'resources')
        self.game_font = None
        self.settings = {}
        self.system_type = []

    def load_setting(self) -> dict:
        with open(path.join(self.game_folder, 'settings.srset')) as file:
            setting = [item.rstrip() for item in file.readlines()]
            for item in setting:
                self.settings[item.split("=")[0]] = item.split("=")[1]
        return self.settings

    def load_font(self) -> str:
        load_font = listdir(path.join(self.resources_folder, 'fonts'))
        self.game_font = path.join(path.join(self.resources_folder, 'fonts'), load_font[0]) if len(load_font) != 0 else None
        return self.game_font
