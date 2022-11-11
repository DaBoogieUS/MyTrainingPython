import unittest
import cool_game

class CoolGameFunctionsTest(unittest.TestCase):

    def test_greet(self):
        """greet() have to return "How are you?" if isEnemy == false"""
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        """greet() have to return "I will kill you, bastard!" if isEnemy == true"""
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard!')

    def test_eat_burgers(self):
        """eat_burgers() have to return "Mmm! That was excellent!" if number <= 3"""
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was excellent!')

    def test_too_much_burgers(self):
        """eat_burgers() have to return "Oh! I am overate!" if number > 4"""
        self.assertEqual(cool_game.eat_burgers(4), 'Oh! I am overate!')

    def test_can_fly_batman(self):
        self.assertTrue(cool_game.can_fly('Batman'), 'Batman have to be able to fly')

    def test_can_fly_anyone_else(self):
        self.assertEqual(cool_game.can_fly('Bob'), False)
        self.assertEqual(cool_game.can_fly('Jim'), False)
        self.assertEqual(cool_game.can_fly('Kevin'), False)
        # self.assertFalse(cool_game.can_fly('Bob'), 'Anyone else don\'t have to be able to fly')
        # self.assertFalse(cool_game.can_fly('Jim'), 'Anyone else don\'t have to be able to fly')
        # self.assertFalse(cool_game.can_fly('Kevin'), 'Anyone else don\'t have to be able to fly')



if __name__ == "__main__":
    unittest.main()