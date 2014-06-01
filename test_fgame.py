import unittest
import fgame
import player
import components.health

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = fgame.Game()
        self.game.addPlayer(player.Player("Delrothar"))
        self.game.addPlayer(player.Player("Wussayo"))
        self.game.getPlayerByName("Delrothar").addComponent(components.health.Health(100))
        self.game.getPlayerByName("Wussayo").addComponent(components.health.Health(130))

    def testShouldBeTwoConnectedPlayerInTheGame(self):
        self.assertLivingPlayers(2)

    def testShouldGetPlayerHealths(self):
        self.assertPlayerHealth("Wussayo", 130)
        self.assertPlayerHealth("Delrothar", 100)

    def testPlayerShouldSufferDamage(self):
        self.sufferDamage("Wussayo",31)
        self.assertPlayerHealth("Wussayo", 99)

    def testPlayerShouldDieFromCriticalDamage(self):
        self.sufferDamage("Wussayo", 150)
        self.assertPlayerHealth("Wussayo", 0)
        self.assertLivingPlayers(1)

    def assertLivingPlayers(self, ExpectedNumberOfLivingPlayers):
        self.assertEqual(
            ExpectedNumberOfLivingPlayers,
            self.game.getNumberOfLivingPlayers()
        )

    def assertPlayerHealth(self, Name, Health):
        self.assertEqual(
            Health,
            self.game.getPlayerByName(Name).getComponent("health").getHealth()
        )

    def sufferDamage(self, Name, Damage):
        self.game.getPlayerByName(Name).sufferDamage(Damage)

if __name__ == '__main__':
    unittest.main()
