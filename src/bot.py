import os
import configparser
import asyncio
import discord
from src.file_handler import compress_map, decompress_map
from src.config_handler import load_config


def get_bot_parameters():    
    try:
        return load_config()
    
    except (FileNotFoundError, ValueError) as e:
        print(e)
        exit()

class Bot(discord.Client):
    def __init__(self, action, map_name, map_folder, id_channel, message_for_using):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.id_channel = id_channel
        self.channel = None

        @self.event
        async def on_ready():
            print(f'Bot : "{self.user}" started')
            self.channel = self.get_channel(self.id_channel)

            if self.channel is None:
                print(f"Channel with ID {self.id_channel} not found")
                await self.close()
            
            if action == "send":
                compress_map(f"{map_folder}/{map_name}.db")
                await self.channel.send(file=discord.File(f"{map_name}.zip"))
                os.remove(f"{map_name}.zip")

                print(f"Map '{map_name}' has been sent.")
                await self.close()
            
            if action == "download":
                try:                    
                    messages = [message async for message in self.channel.history(limit=1)]
                except:
                    print(f"The last message in the channel '{self.channel.name}' not found")
                    await self.close()
                
                if len(messages[0].attachments) > 0:
                    if messages[0].attachments[0].filename == f"{map_name}.zip":
                        # Download the file
                        await messages[0].attachments[0].save(fp=messages[0].attachments[0].filename)
                    else:
                        print(f"The name of the latest map in the channel {self.channel.name} is {messages[0].attachments[0].filename}. This doesn't correspond to the name of the map to download.")
                        await self.close()
                else:
                    print(f"The last message in the channel '{self.channel.name}' dosen't contain file.")
                    await self.close()
                
                decompress_map(messages[0].attachments[0].filename, map_folder)
                os.remove(messages[0].attachments[0].filename)

                await self.channel.send(message_for_using)
                
                print(f"Map '{map_name}' has been downloaded.")
                await self.close()