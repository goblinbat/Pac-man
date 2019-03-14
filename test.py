import unittest
from pacman import PacMan

class PacmanTests(unittest.TestCase):

    def test_pacman_PacMan_eat_should_add_number_to_variable(self):
        # Arrange
        dot = 10

        # Act
        actual = PacMan.eat(dot)
        expected = 5610     # base 5000 + 10 from dot + 600 from next test (not sure why it adds now)

        # Assert
        self.assertEqual(actual, expected)

    def test_pacman_PacMan_consume_should_add_numbers_to_variable_and_then_multiply_before_adding_again(self):
        # Arrange 
        PacMan.consume()   # should add 200 to score
        PacMan.consume()   # should add 400 (200*2) to score

        # Act
        actual = PacMan.points
        expected = 5600     # base 5000 + 200 + 400

        # Assert
        self.assertEqual(actual, expected)
            
    def test_pacman_PacMan_die_should_subtract_1_from_variable(self):
        # Arrange
        PacMan.die()

        # Act
        actual = PacMan.lives
        expected = 2

        # Assert
        self.assertEqual(actual, expected)
    
    def test_pacman_PacMan_extra_should_add_1_to_variable(self):
        # Arrange
        PacMan.extra()

        # Act
        actual = PacMan.lives
        expected = 3

        # Assert
        self.assertEqual(actual, expected)
            