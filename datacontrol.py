from os import path, listdir


class DataControl:
    def __init__(self):
        self.game_folder = path.dirname(__file__)
        self.resources_folder = path.join(self.game_folder, 'resources')
        self.settings_file_name = "settings.srset"

    def load_setting(self) -> dict:
        settings = {}
        with open(path.join(self.game_folder, self.settings_file_name)) as file:
            setting = [item.rstrip() for item in file.readlines()]
            for item in setting:
                settings[item.split("=")[0]] = item.split("=")[1]
        return settings

    def load_font(self) -> str:
        load_font = listdir(path.join(self.resources_folder, 'fonts'))
        game_font = path.join(path.join(self.resources_folder, 'fonts'), load_font[0]) if len(load_font) != 0 else None
        return game_font
