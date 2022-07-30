from project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):
    USERNAME = "hero username"
    HEALTH = 100
    DAMAGE = 11
    LEVEL = 10

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_init__expect_correct_input(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_battle_same_usernames__expect_to_raise(self):
        enemy_hero = Hero(self.USERNAME, 7, 90, 3)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_hero_negative_health__expect_to_raise(self):
        enemy_hero = Hero("Enemy username", 7, 90, 3)

        self.hero.health = -3
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

        self.hero.health = 0
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_enemy_negative_health__expect_to_raise(self):
        enemy_hero = Hero("Enemy username", 7, -3, 3)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(error.exception))

        enemy_hero = Hero("Enemy username", 7, 0, 3)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(error.exception))

    def test_battle_draw_expect_correct_result(self):
        enemy_hero = Hero("Enemy username", self.LEVEL, self.HEALTH, self.DAMAGE)
        actual_result = self.hero.battle(enemy_hero)
        expected_result = "Draw"
        self.assertEqual(expected_result, actual_result)
        expected_health = self.HEALTH - (self.DAMAGE * self.LEVEL)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, enemy_hero.health)

    def test_battle__you_win__expect_win(self):
        enemy_level, enemy_health, enemy_damage = 5, 10, 2
        enemy_hero = Hero("Enemy username", enemy_level, enemy_health, enemy_damage)

        actual_result = self.hero.battle(enemy_hero)

        expected_result = "You win"
        hero_expected_health = self.HEALTH - (enemy_hero.damage * enemy_hero.level) + 5
        hero_expected_level = self.LEVEL + 1
        hero_expected_damage = self.DAMAGE + 5
        enemy_expected_health = enemy_health - (self.DAMAGE * self.LEVEL)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(hero_expected_health, self.hero.health)
        self.assertEqual(hero_expected_level, self.hero.level)
        self.assertEqual(hero_expected_damage, self.hero.damage)
        self.assertEqual(enemy_expected_health, enemy_hero.health)

    def test_battle__you_lose__expect_lose(self):
        hero_level, hero_health, hero_damage = 5, 10, 2
        hero = Hero("Hero username", hero_level, hero_health, hero_damage)
        enemy_hero = Hero("Enemy username", self.LEVEL, self.HEALTH, self.DAMAGE)

        actual_result = hero.battle(enemy_hero)

        expected_result = "You lose"
        enemy_hero_expected_health = self.HEALTH - (hero_damage * hero_level) + 5
        enemy_hero_expected_level = self.LEVEL + 1
        enemy_hero_expected_damage = self.DAMAGE + 5
        hero_expected_health = hero_health - (self.DAMAGE * self.LEVEL)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(enemy_hero_expected_health, enemy_hero.health)
        self.assertEqual(enemy_hero_expected_level, enemy_hero.level)
        self.assertEqual(enemy_hero_expected_damage, enemy_hero.damage)
        self.assertEqual(hero_expected_health, hero.health)

    def test_str__expect_correct_output(self):
        actual_result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
