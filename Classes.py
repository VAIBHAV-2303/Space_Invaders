# Class declaration
class Ship:
    'My ship Class'

    def __init__(self):
        self.posx = 320
        self.posy = 560

    def mleft(self):
        if self.posx != 0:
            self.posx -= 80

    def mright(self):
        if self.posx != 560:
            self.posx += 80


class missile:
    'Parent missile class'

    def __init__(self, x, y):
        self.posx = x
        self.posy = y


class alieni:
    'Initial alien class'

    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.timer = 8

    def dectime(self):
        self.timer -= 1


class alienl:
    'Hit alien class'

    def __init__(self, x, y, time):
        self.posx = x
        self.posy = y
        self.timer = time

    def dectime(self):
        self.timer -= 1


class imiss(missile):
    'Slow missile class'

    def __init__(self, x, y):
        missile.__init__(self, x, y)
        self.speed = 0.8

    def move(self):
        self.posy -= self.speed


class lmiss(missile):
    'Fast missile class'

    def __init__(self, x, y):
        missile.__init__(self, x, y)
        self.speed = 1.6

    def move(self):
    	self.posy -= self.speed
