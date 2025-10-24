import pyxel

pyxel.init(128, 128, title="Mon premier programme Pyxel")
pyxel.load('ressources.pyxres')
pyxel.cls(0)
x = 10
y = 10
pyxel.text(x, y, "Mon premier programme avec", 7)
pyxel.text(x, y + 10, "Pyxel!", 8)
pyxel.blt(self.robot.x, self.robot.y, 0, self.robot.originX, self.robot.originY, self.robot.size_x, self.robot.size_y, 0)
pyxel.show()