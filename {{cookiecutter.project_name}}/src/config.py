import json
import os


class Config(object):
    """Get the config file for the current env"""
    def __init__(self, test, test2):
        self.test = test
        self.test2 = test2



def read_config() -> str:
    with open('appsettings.json') as appsettings:
        appsettings_string = appsettings.read()

    return appsettings_string


def get_config(env) -> Config:
    appsettings = read_config()
    json_string = json.loads(appsettings)
    config = Config(**json_string[env])
    return config

