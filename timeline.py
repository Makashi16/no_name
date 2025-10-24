import enemies

class TIMELINE:
    def __init__(self):
        self.robot = enemies.ENEMY(10, 1, 100, 0, 24, 15, 15)
        self.goblin = enemies.ENEMY(10, 1, 50, 0, 88, 15, 15)
        self.soldier = enemies.ENEMY(20, 2, 50, 16, 88, 15, 15)
        self.general = enemies.ENEMY(50, 3, 90, 32, 88, 15, 15)
        self.challenger = enemies.ENEMY(100, 3, 80, 48, 88, 15, 15)
        self.god_challenger = enemies.ENEMY(300, 3, 110, 48, 104, 15, 15)
        self.breakTime = None
        self.phase_index = [self.robot,self.breakTime,self.goblin, self.breakTime,self.soldier, self.breakTime,self.general, self.breakTime,self.challenger, self.god_challenger]
        self.actual_phase = self.phase_index[0]
        self.actual_ennemi = self.phase_index[0]
    def change_phase(self):
        if len(self.phase_index) != 0:
            self.phase_index.pop(0)
            self.actual_phase = self.phase_index[0]


