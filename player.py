class Player:
    def __init__(self, Name):
        self.name = Name
        self.components = {}
    def getName(self):
        return self.name
    def addComponent(self, Component):
        self.components[Component.getName()] = Component
    def getComponent(self, ComponentName):
        return self.components[ComponentName]
    def sufferDamage(self, Damage):
        self.components["health"].damage(Damage)
    def isAlive(self):
        if self.components["health"].getHealth() == 0:
            return False
        return True
