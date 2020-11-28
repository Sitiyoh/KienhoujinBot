import discord

class Image:
    __image_path = "image/BrahmanTrident{}.png"
    __file_count = 3

    @classmethod
    def Files(cls, id):
        files = []

        for i in range(__file_count):
            files[i] = discord.File(__image_path.format(id))

        return files
