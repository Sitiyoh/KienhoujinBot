import cv2
import discord

# 画像が一致していると判定される閾値
MATCH_THRESHOLD = 0.8
TEMPLATE_PATH = ["image/BrahmanTrident1.png", "image/BrahmanTrident2.png"]

def Match(num):
    if MATCH_THRESHOLD < num:
        return True

    return False

def JudgeMatching(path):
    image = cv2.imread(path)

    template = []
    for p in TEMPLATE_PATH:
        template.append(cv2.imread(path))

    Judg = False
    maxResult = 0

    for t in template:
        result = cv2.matchTemplate(image, t, cv2.TM_CCORR_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

        if maxResult < maxVal:
            maxResult = maxVal

        #類似度が閾値を超えているか判定（上で作った関数を使用）
        Judg = Match(maxVal)
        if Judg:
            break

    #結果を出力
    print(maxResult)
    # （実行結果→）True or False
    return Judg
