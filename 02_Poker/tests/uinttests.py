import unittest
import main as mn
import constants as con
import combinations as cmb


class PokerTest(unittest.TestCase):

    def test_get_value(self):
        """
        Test that the numbers 1, 29 and 52 get correctly translated to a value
        :return: 14, 3 and 13
        """
        # initialize data
        data = [1, 29, 52]
        for i in range(len(data)):
            data[i] = mn.get_value(data[i], con.SYMBOLS)

        # assertion
        self.assertEqual(data, [14, 3, 13])

    def test_royal_flush(self):
        """
        Test that a *royal-flush-hand* of 5 cards gets detected as such.

        **royal-flush:** highest possible straight (10, J, Q, K, A) with everything in the same color
        :return: True
        """
        # initialize data
        card1 = mn.card(10, con.SYMBOLS)  # 10 of clubs
        card2 = mn.card(11, con.SYMBOLS)  # Jack of clubs
        card3 = mn.card(12, con.SYMBOLS)  # Queen of clubs
        card4 = mn.card(13, con.SYMBOLS)  # King of clubs
        card5 = mn.card(1, con.SYMBOLS)  # Ace of clubs
        data = [card1, card2, card3, card4, card5]
        # assertion
        self.assertTrue(cmb.royal_flush(data))

    def test_straight_flush(self):
        """
        Test that a *straight-flush-hand* gets detected as such

        **straight-flush:** all 5 cards with values in a seamless row and same color
        :return: True
        """
        # initialize data
        card1 = mn.card(19, con.SYMBOLS)  # 6 of diamonds
        card2 = mn.card(20, con.SYMBOLS)  # 7 of diamonds
        card3 = mn.card(21, con.SYMBOLS)  # 8 of diamonds
        card4 = mn.card(22, con.SYMBOLS)  # 9 of diamonds
        card5 = mn.card(23, con.SYMBOLS)  # 10 of diamonds
        data = [card1, card2, card3, card4, card5]
        # assertion
        self.assertTrue(cmb.straight_flush(data))

    def test_four_of_a_kind(self):
        """
        Test that a hand with 4 different cards sharing the same value gets detected
        :return: True
        """
        # initialize data
        card1 = mn.card(42, con.SYMBOLS)  # 3 of spades
        card2 = mn.card(16, con.SYMBOLS)  # 3 of diamonds
        card3 = mn.card(21, con.SYMBOLS)  # 8 of diamonds
        card4 = mn.card(29, con.SYMBOLS)  # 3 of hearts
        card5 = mn.card(3, con.SYMBOLS)  # 3 of clubs
        data = [card1, card2, card3, card4, card5]
        # assertion
        self.assertTrue(cmb.four_of_a_kind(data))

    def test_full_house(self):
        """
        Test that a full-house-hand gets detected

        **full-house:** a pair and another three of a kind
        :return: True
        """
        # initialize data
        card1 = mn.card(50, con.SYMBOLS)  # Jack of spades
        card2 = mn.card(16, con.SYMBOLS)  # 3 of diamonds
        card3 = mn.card(37, con.SYMBOLS)  # Jack of hearts
        card4 = mn.card(42, con.SYMBOLS)  # 3 of spades
        card5 = mn.card(11, con.SYMBOLS)  # Jack of clubs
        data = [card1, card2, card3, card4, card5]
        # assertion
        self.assertTrue(cmb.full_house(data))


if __name__ == '__main__':
    unittest.main()
