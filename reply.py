from image import Image
import discord
import random

patterns = [Reply(["機炎方陣", "破壊"], ["機炎方陣！？", "破壊！？"]),
            Reply(["機炎方陣・破壊", "機炎方陣破壊"], "機炎方陣・破壊！？"),
            Reply(["ブラフマントライデント", "シヴァ槍"], Image.Files())]

class Reply:
    __pattern = None
    __reply = None

    def __init__(self, pattern, reply):
        self.__pattern = pattern
        self.__reply = reply

    def predicate(self, message):
        if type(self.__pattern) is str:
            return __pattern in message.text

        for pattern in self.__pattern:
            if pattern in message.text:
                return True

        return False

    def reply_message(self, message):
        # 配列以外なら
        if type(self.__reply) is not "array":
            return self.__reply

        # リストが空なら
        if not self.__reply:
            return ""

        # 配列の中から一つを返す
        return random.choices(self.__reply)
