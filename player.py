import pyxel, random

class PLAYER:
    def __init__(self, x, y, hp, spd, weight):
        self.x = x
        self.y = y
        self.size = (10, 14)
        self.hitbox = [self.x, self.y, self.size[0], self.size[1]]
        self.lookingAtLeft = False
        self.collide = False
        self.jumpCount = 0
        self.platform = [((46, 120), (192, 128))]
#################################################################################
# STATS
#################################################################################
        self.hp = hp
        self.atk = 100
        self.Def = 10
        self.cr = 5
        self.cd = 10
        self.spd = spd
        self.weight = weight
        self.jumpMax = 2
#################################################################################
    def stats(self):
        return self.hp, self.atk, self.Def, self.cr, self.cd, self.spd, self.weight, self.jumpMax
#################################################################################
# DMG methods
#################################################################################
    def dmgDeal(self):
        critRate = random.randint(1, 100)
        if critRate <= self.cr:
            crit = self.cd / 100 * self.atk
        else:
            crit = 1
        return round(self.atk * crit / 100)

    def dmgTaken(self, a):
        b = a-self.Def*0.1
        if b < 1:
            b = 1
        self.hp -= b

    def fallen(self):
        self.hp = 0
#################################################################################
# Moving Methods
#################################################################################
    def gravity(self, a):
        if self.collide is False:
            self.y += a

    def move(self):
        #############################################################
        ##LEFT
        if pyxel.btn(pyxel.KEY_Q) and self.x > 0:
            self.x -= self.spd * 2
            self.lookingAtLeft = True
        elif self.x < 0:
            self.x = 0
        #############################################################
        ##RIGHT
        if pyxel.btn(pyxel.KEY_D) and self.x < 240:
            self.x += self.spd * 2
            self.lookingAtLeft = False
        elif self.x > 240:
            self.x = 240
        #############################################################
        ##JUMP
        if pyxel.btnr(pyxel.KEY_Z) and self.y > 8:
            if self.jumpCount < self.jumpMax:
                self.y -= self.spd * (0.4 * self.weight)
                self.jumpCount += 1
            if self.y > 240:
                self.y = 240

        #############################################################
        ##GRAVITY
        if self.collide is False:
            # if pyxel.btn(pyxel.KEY_S):
            self.gravity(2)
        if pyxel.btn(pyxel.KEY_J):
            print(self.x, ",", self.y)

#############################################################
    def collider(self, co):
        if self.y + 8 >= co[0][1] and self.x + 8 > co[0][0] and self.x - 8 < co[1][0] and self.y - 8 < co[1][1]:
            self.collide = True
            self.y -= self.y - co[0][1] + 8
        else:
            self.collide = False

    def jumpCountReset(self):
        if self.collide is True:
            self.jumpCount = 0
    def update(self):
        self.move()
        self.jumpCountReset()
        self.hitbox = [self.x, self.y, self.size[0], self.size[1]]
        self.gravity(1)
        for i in range(len(self.platform)):
            self.collider(self.platform[i])
        if 256 - self.y < 10:
            self.fallen()
            pyxel.quit()
