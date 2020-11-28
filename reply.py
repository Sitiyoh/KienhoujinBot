from image import Image
import discord
import random

class Reply:
    __pattern = None
    __reply = None

    def __init__(self, pattern, reply):
        self.__pattern = pattern
        self.__reply = reply

    @classmethod
    def React(cls, message):
        for pattern in patterns:
            if pattern.__predicate(message):
                return pattern.__reply_message(message)

        return None

    def __predicate(self, text):
        if type(self.__pattern) is str:
            return __pattern in text

        for pattern in self.__pattern:
            if pattern in text:
                return True

        return False

    def __reply_message(self, message):
        # 配列以外なら
        if type(self.__reply) is not list:
            return self.__reply

        # リストが空なら
        if not self.__reply:
            return ""

        # 配列の中から一つを返す
        return random.choice(self.__reply)

patterns = [Reply(["機炎方陣", "破壊"], ["機炎方陣！？", "破壊！？"]),
            Reply(["機炎方陣・破壊", "機炎方陣破壊"], "機炎方陣・破壊！？"),
            Reply(["ブラフマントライデント", "シヴァ槍"], Image())]
