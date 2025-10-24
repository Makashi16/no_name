
class lanchingItem:
    def __init__(self, x, y, spd, sens, size_x, size_y, owner):
        self.x = x
        self.y = y
        self.owner = owner
        self.size = (size_x, size_y)
        self.collide = False
        self.spd = spd
        self.goToLeft = sens
        self.hitbox = [self.x, self.y, self.size[0], self.size[1]]
    def move(self, bool):
        if bool is True:
            self.x -= self.spd
        else:
            self.x += self.spd

    def posx(self):
        return self.x
    def posy(self):
        return  self.y
    def update(self):
        self.hitbox = [self.x, self.y, self.size[0], self.size[1]]

