import random
class ENEMY:
    def __init__(self, hp, spd, weight, originX, originY, size_x, size_y):
        self.x = 190
        self.y = 60
        self.originX = originX
        self.originY = originY
        self.size_x = size_x
        self.size_y = size_y
        self.hidden = False
        self.goToLeft = False
        self.collide = False
        self.hitbox = [self.x, self.y, self.size_x, self.size_y]
        self.platform = [((46,120),(192,128))]
        self.jumpCount = 0
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
    def dmgTaken(self, a):
        b = a-self.Def*0.1
        if b < 1:
            b = 1
        self.hp -= b
    def dmgDeal(self):
        critRate = random.randint(1, 100)
        if critRate <= self.cr:
            crit = self.cd / 100 * self.atk
        else:
            crit = 1
        return round(self.atk * crit / 100)
    def fallen(self):
        self.hp = 0
    def gravity(self, a):
        if self.collide is False:
            self.y += a
    def fall(self):
        self.gravity(2)
    def collider(self, co):
        if self.y + 8 >= co[0][1] and self.x + 8 > co[0][0] and self.x - 8 < co[1][0] and self.y - 8 < co[1][1]:
            self.collide = True
            self.y -= self.y - co[0][1] + 8
        else:
            self.collide = False
    def jump(self):
        if self.collide == False and self.y > 120:
            if self.jumpCount < self.jumpMax:
                self.y -= self.spd * (0.4*self.weight)
                self.jumpCount += 1

    def update(self):
        self.fall()
        self.hitbox = [self.x, self.y, self.size_x, self.size_y]
        for i in range(len(self.platform)):
            self.collider(self.platform[i])