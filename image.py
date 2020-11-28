import discord
import random

class Image:
    __image_path = "image/BrahmanTrident{0}.png"
    __file_count = 3
    __file_path_list = []

    def __init__(self):
        for i in range(1, self.__file_count + 1):
            self.__file_path_list.append(self.__image_path.format(i))

    def File(self):
        return discord.File(random.choice(self.__file_path_list))
