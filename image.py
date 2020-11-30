import discord
import os
import random

class Image:
    __image_path = "image/BrahmanTrident{0}"
    __image_ext = [".jpg", ".png"]
    __file_count = 5
    __file_path_list = []

    def __init__(self):
        for i in range(1, self.__file_count + 1):
            path = self.__image_path.format(i)
            for ext in self.__image_ext:
                if os.path.exists(path + ext):
                    self.__file_path_list.append(path + ext)

    def File(self):
        return discord.File(random.choice(self.__file_path_list))
