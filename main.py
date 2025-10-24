import pyxel, player, timeline, breakTime, projectile, enemies, spell1 , random
from projectile import lanchingItem

tl = timeline.TIMELINE()
player = player.PLAYER(60, 60, 100, 1, 100)
brT = breakTime.BREAKTIME()
sp1 = spell1.SPELL1()

class Jeu:
    def __init__(self):
        self.screenSize = 256
        pyxel.init(self.screenSize, self.screenSize, title="game")
        pyxel.load('ressources.pyxres')
#################################################################################
## objects
#################################################################################
        self.robot = None
        self.robot = tl.actual_phase
#################################################################################
        self.size = (10,14)
        self.knife = None
        self.missile = None
        self.platform = [((46,120),(192,128))]
        self.ingame = True
        self.buffs = brT.buff()
        self.chosen_buff = None
        pyxel.run(self.update, self.draw)
    def launch(self):
        """ control the launching of the player's knife """
        if pyxel.btnr(pyxel.KEY_E):
            if self.knife is None:
                self.knife = lanchingItem(player.x + 10, player.y, player.spd*3, player.lookingAtLeft, 15, 7, player)
        if self.knife is not None:
            self.knife.move(self.knife.goToLeft)
            if self.knife.x > self.screenSize or self.knife.x < 0 :
                self.knife = None
#################################################################################
    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.screenSize, self.screenSize)
        if self.ingame is True:
            self.HPdisplay(player.hp, 10, "player")
            self.HPdisplay(self.robot.hp, 20, 'robot')
            if player.lookingAtLeft is False:
                pyxel.blt(player.x, player.y, 0, 16, 0, self.size[0], self.size[1], 7)
            else:
                pyxel.blt(player.x, player.y, 0, 26, 0, self.size[0], self.size[1], 7)
########################################################################################
## --------------------------------------------------------------------------------------
            if self.robot.hidden is False:
                pyxel.blt(self.robot.x, self.robot.y, 0, self.robot.originX, self.robot.originY, self.robot.size_x, self.robot.size_y, 0)

## ----------------------------------------------------------------------------------------
###########################################################################################
            if self.knife is not None:
                if self.knife.goToLeft is True:
                    pyxel.blt(self.knife.x, self.knife.y, 0, 16, 24, self.knife.size[0], self.knife.size[1], 6)
                else:
                    pyxel.blt(self.knife.x, self.knife.y, 0, 16, 32, self.knife.size[0], self.knife.size[1], 6)
            if self.missile is not None and self.robot.hidden is False:
                if self.missile.goToLeft is True:
                    pyxel.blt(self.missile.x, self.missile.y, 0, 33, 26, self.missile.size[0], self.missile.size[1], 6)
                else:
                    pyxel.blt(self.missile.x, self.missile.y, 0, 32, 35, self.missile.size[0], self.missile.size[1], 6)
            if sp1.here is True:
                pyxel.blt(sp1.x, sp1.y, 0, 0, 104, 15, 15, 0)
        else:
            for i in range(len(self.buffs)):
                 pyxel.text(30, 60 + i*10, f"{self.buffs[i][0]} : {self.buffs[i][1]}", 0)
###############################################################################################
    def HPdisplay(self, qqu, h, name):
        pyxel.text(10, h, f"HP {name}: {qqu}", 0)
######################################################################################################
    def hitten(self, obj, who):
        """check in someone is hitten """
        if obj is not None:
                hitb1 = obj.hitbox
                hitb2 = who.hitbox
                collision_x = (hitb1[0] < hitb2[0] + hitb2[2]) and (hitb1[0] + hitb1[2] > hitb2[0])
                collision_y = (hitb1[1] < hitb2[1] + hitb2[3]) and (hitb1[1] + hitb1[3] > hitb2[1])
                if collision_x and collision_y:
                    who.dmgTaken(obj.owner.dmgDeal())
########################################################################################################
    def hittenEX(self, obj, who):
        """check in someone is hitten """
        if obj is not None:
                hitb1 = obj.hitbox
                hitb2 = who.hitbox
                collision_x = (hitb1[0] < hitb2[0] + hitb2[2]) and (hitb1[0] + hitb1[2] > hitb2[0])
                collision_y = (hitb1[1] < hitb2[1] + hitb2[3]) and (hitb1[1] + hitb1[3] > hitb2[1])
                print(collision_x, collision_y)
                if collision_x and collision_y:
                    self.robot.dmgTaken(sp1.dmg())
########################################################################################################
    def getVector(self, p1, p2):
        """ get vector coordinate from object p1 to object p2 """
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        return x2 - x1, y2 - y1
    def getVectorXY(self, x1, y1, x2, y2):
        """ get vector coordinate between 2 points """
        return x2 - x1, y2 - y1
#####################################################################################################
    def robot_move(self):
        """ manage the ennemi movement ( need to change ) """
        if self.robot.hidden is False:
            if 100 > self.getVector(self.robot, player)[0] > -100:
                state = "fight"
            else:
                state = "idle"
            if state == "idle":
                if self.robot.collide is False:
                    obj = self.getVectorXY(self.robot.x, self.robot.y, self.screenSize/2, self.screenSize/2 )
                    if self.robot.x < obj[0]:
                        self.robot.x += self.robot.spd
                    if self.robot.x > obj[0]:
                        self.robot.x -= self.robot.spd
                    if self.robot.y > obj[1]:
                        self.robot.y -= self.robot.spd
            elif state == "fight":
                obj = self.getVector(self.robot, player)
                if obj[0] > 10 or obj[0] < -10:
                    if 0 < obj[0]:
                        self.robot.x += self.robot.spd
                    if 0 > obj[0]:
                        self.robot.x -= self.robot.spd
                if self.missile is None:
                    self.missile = projectile.lanchingItem(self.robot.x, self.robot.y + 5, self.robot.spd*2, self.robot.goToLeft, 15, 6, self.robot)
                    if obj[0] < 0:
                        self.missile.goToLeft = True
                    else:
                        self.missile.goToLeft = False
                else:
                    self.missile.move(self.missile.goToLeft)
                    if self.missile.x > self.screenSize or self.missile.x < 0:
                        self.missile = None

                if self.knife is not None and self.robot.jumpCount == 0:
                    a = random.randint(1, 10)
                    kn = self.getVector(self.robot, self.knife)
                    if kn[0] < a:
                        self.robot.y -= self.robot.spd * (0.4 * self.robot.weight)
                        self.robot.jumpCount = 1
                if self.knife is None:
                    self.robot.jumpCount = 0


##########################################################################################
    def gameover(self):
        """ manage the death """
        if self.robot.hp <= 0 < player.hp:
            self.robot.hidden = True
            tl.change_phase()
            self.buffs = brT.buff()
            self.ingame = False
        if player.hp <= 0:
            pyxel.quit()
##########################################################################################
    def game_check(self):
        if tl.actual_phase is not None:
            self.ingame = True
        else:
            self.ingame = False
##########################################################################################
# Spell 1
##########################################################################################
    def fireball(self):
        if sp1.pressed is True:
            sp1.launch(player.x, player.y)
            self.hittenEX(sp1, self.robot)


##########################################################################################
    def update(self):
        self.game_check()
        if self.ingame is True:
            self.gameover()
            self.robot.update()
            player.update()
            if self.knife is not None:
                self.knife.update()
                self.hitten(self.knife, self.robot)
            sp1.update()
            self.fireball()
            if self.missile is not None:
                self.missile.update()
                self.hitten(self.missile, player)
            self.robot_move()
            self.launch()
            if self.knife is not None:
                self.knife.hitbox = [self.knife.x, self.knife.y, self.knife.size[0], self.knife.size[1]]
        else:
            self.chosen_buff = brT.choose_buff(self.buffs)

            if self.chosen_buff is not None:
                if self.chosen_buff[0] == 'hp':
                    player.hp += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'atk':
                    player.atk += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'def':
                    player.Def += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'cr':
                    player.cr += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'cd':
                    player.cd += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'jump':
                    player.jumpMax += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'spd':
                    player.spd += self.chosen_buff[1]
                elif self.chosen_buff[0] == 'weight':
                    player.weight -= self.chosen_buff[1]
                tl.change_phase()
                self.robot = tl.actual_phase
                self.chosen_buff = None

Jeu()