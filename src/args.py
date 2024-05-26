import os
import argparse
from src.bot import Bot, get_bot_parameters


def main():
    # General parser
    parser = argparse.ArgumentParser(description=__doc__)

    sub = parser.add_subparsers(dest="sub")
    
    # Argument
    parser.add_argument(
        "-f",
        "--file",
        help=("The name of the map"),
        dest="map_name",
        required=True,
    )
    
    # Parser for actions
    send = sub.add_parser("send", help="Send the map")
    download = sub.add_parser("download", help="Download the map and move it in the correct folder.")

    args = parser.parse_args()

    token, id_channel, map_folder, message_for_using = get_bot_parameters()

    match args.sub:
        case "send":
            if os.path.isfile(f"{map_folder}/{args.map_name}.db"):
                bot = Bot("send", args.map_name, map_folder, id_channel, message_for_using)
                bot.run(token)
            else:
                print(f"The map {args.map_name} dosen't")
                return

        case "download":
            bot = Bot("download", args.map_name, map_folder, id_channel, message_for_using)
            bot.run(token)

