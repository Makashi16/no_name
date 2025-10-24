import random, player, pyxel

from pyxel.cli import play_pyxel_app


class BREAKTIME:
    def __init__(self):
        self.article = [['hp', 5, 10, 20], ['atk', 5, 15, 25], ['def', 5, 10, 25], ['cr', 15, 25, 50], ['cd', 50, 100, 200], ['jump', 1, 2, 3], ['spd', 10, 20, 30], ['weight', 10, 20, 50]]
        self.buffs = [0 for _ in range(3)]

    def buff(self):
        ans = []
        for i in range(3):
            a = random.randint(0, len(self.buffs)) # quel type bonus on prend ???
            b = random.randint(1, 10)           # quel rareté de bonus on prend ??? proba en % :
            # 1 = 50%
            # 2 = 40%
            # 3 = 10%
            if b <= 5:
                raretyBuff = 1
            elif b != 10:
                raretyBuff = 2
            else:
                raretyBuff = 3
            ans.append([self.article[a][0], self.article[a][raretyBuff]])
        return ans
    def choose_buff(self, buff):
        chosen = None
        if pyxel.btn(pyxel.KEY_K) is True:
            chosen = 0
        elif pyxel.btn(pyxel.KEY_L) is True:
            chosen = 1
        elif pyxel.btn(pyxel.KEY_M) is True:
            chosen = 2
        if chosen is not None:
            return buff[chosen]


