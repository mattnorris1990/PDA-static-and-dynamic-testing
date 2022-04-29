import unittest
from src.card import *
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Spades", 2)
        self.card3 = Card("Spaces", 3)
        
        self.cards = [self.card1, self.card2]
        self.all_cards = [self.card1, self.card2, self.card3]

        self.cardgame = CardGame()

    # @unittest.skip("Delete this line to run the test")
    def test_check_for_ace_true(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    # @unittest.skip("Delete this line to run the test")
    def test_check_for_ace_false(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card2))
    
    # @unittest.skip("Delete this line to run the test")       
    def test_check_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    # @unittest.skip("Delete this line to run the test")
    def test_check_highest_card_switched(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card2, self.card1))

    # @unittest.skip("Delete this line to run the test")
    def test_cards_total_value(self):
        self.assertEqual("You have a total of3", self.cardgame.cards_total(self.cards))

    # @unittest.skip("Delete this line to run the test")
    def test_cards_total_wrong_value(self):
        self.assertNotEqual ("You have a total of3", self.cardgame.cards_total(self.all_cards))