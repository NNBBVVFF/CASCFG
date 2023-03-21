import toml

# Читаем конфигурационный файл
def readingTemplate():
    with open('config.toml', 'r') as config_toml_template:
        config = toml.load(config_toml_template)
        return config




if __name__ == '__main__':
    print(readingTemplate()["vbu"][1])



