import time, pyxel
class SPELL1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.lvl = 1
        self.here = False
        self.coulddown = 1.5
        self.time = 0
        self.wait = 0
        self.pressed = False
        self.size = (15, 15)
        self.hitbox = [self.x, self.y, self.size[0], self.size[1]]
    def launch(self, x, y):
        self.here = True
        self.x = x - 4
        self.y = y - 7
        self.time = time.time()




    def dmg(self, p):
            return p.dmgDeal()*lvl

    def KB(self):
            return lvl * 35
    def update(self):
        if pyxel.btnr(pyxel.KEY_K):
            self.pressed = True
        else:
            self.pressed = False
        if self.here is True and time.time() - self.time >= self.coulddown:
                self.here = False


