import os
import configparser

def load_config(config_file="config.ini"):
    # Read config file
    config = configparser.ConfigParser()
    config.read(config_file)

    token = config["BOT"]["Token"]
    id_channel = int(config["BOT"]["ID_channel"])
    message_for_using = config["BOT"]["Message_for_using"]
    map_folder = config["FOLDER"]["Scrap_Mechanic_map_folder"]

    # Verification
    if not os.path.exists(map_folder):
        raise FileNotFoundError(f"The folder {map_folder} doesn't exist.")

    if "\\" in map_folder:
        raise ValueError("The path of the folder is not correct. It can't contain backslash.")

    return token, id_channel, map_folder, message_for_using
