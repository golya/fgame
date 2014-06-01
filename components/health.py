class Health:
    def __init__(self, Health):
        self.name = "health"
        self.health = Health
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def damage(self, Damage):
        self.health -= Damage
        if self.health < 0:
            self.health = 0
