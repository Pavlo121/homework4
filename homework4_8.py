import configparser

class ConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()

    def __enter__(self):
        self.config.read(self.file_path)
        return self.config

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)


config_file_path = 'config.ini'

with ConfigManager(config_file_path) as config:
    if 'Settings' not in config:
        config.add_section('Settings')
    config['Settings']['theme'] = 'dark'
    config['Settings']['font_size'] = '12'

print(f"Конфігурація успішно змінена в файлі {config_file_path}.")
