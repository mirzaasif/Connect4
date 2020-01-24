import unittest
from game import ConnectFour, GAME_STATUS_WIN, GAME_STATUS_DRAW, GAME_INCOMPLETE, PLAYER_1, PLAYER_2

class TestGame(unittest.TestCase):

    def test_game_draw(self):
       connect_four = ConnectFour()
       connect_four.board = [
           [1, 2, 1, 2, 1, 2, 1],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
       ]
       self.assertTrue(connect_four.is_game_draw())
       self.assertEqual(connect_four.check_game_status(PLAYER_1, 1, 1), GAME_STATUS_DRAW)

    def test_game_incomplete(self):
        connect_four = ConnectFour()
        connect_four.board = [
           [1, 2, 1, 0, 1, 2, 1],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        self.assertFalse(connect_four.is_game_draw())
        self.assertEqual(connect_four.check_game_status(PLAYER_1, 1, 1), GAME_INCOMPLETE)

    def test_row_win(self):
        connect_four = ConnectFour()
        connect_four.board = [
           [1, 2, 1, 0, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        #self.assertFalse(connect_four.row_win(PLAYER_1, 5, 0))

        connect_four.board = [
           [1, 2, 1, 1, 1, 1, 2],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 1, 1, 1, 1, 1, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        self.assertTrue(connect_four.row_win(PLAYER_1, 0, 3))
        self.assertTrue(connect_four.row_win(PLAYER_1, 0, 2))
        self.assertTrue(connect_four.row_win(PLAYER_1, 0, 4))
        self.assertTrue(connect_four.row_win(PLAYER_1, 0, 5))

        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 0))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 1))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 2))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 3))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 4))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 5))
        self.assertTrue(connect_four.row_win(PLAYER_1, 4, 6))

    def test_col_win(self):
        connect_four = ConnectFour()
        connect_four.board = [
           [1, 2, 1, 0, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        self.assertFalse(connect_four.col_win(PLAYER_1, 5, 0))

        connect_four.board = [
           [1, 2, 1, 1, 1, 1, 1],
           [1, 1, 2, 1, 2, 1, 1],
           [1, 2, 1, 2, 1, 2, 1],
           [1, 1, 2, 1, 2, 1, 1],
           [2, 1, 1, 1, 1, 1, 1],
           [2, 1, 2, 1, 2, 1, 1],
        ]
        self.assertTrue(connect_four.col_win(PLAYER_1, 0, 0))
        self.assertTrue(connect_four.col_win(PLAYER_1, 1, 0))
        self.assertTrue(connect_four.col_win(PLAYER_1, 2, 0))
        self.assertTrue(connect_four.col_win(PLAYER_1, 3, 0))

        self.assertTrue(connect_four.col_win(PLAYER_1, 0, 6))
        self.assertTrue(connect_four.col_win(PLAYER_1, 1, 6))
        self.assertTrue(connect_four.col_win(PLAYER_1, 2, 6))
        self.assertTrue(connect_four.col_win(PLAYER_1, 3, 6))
        self.assertTrue(connect_four.col_win(PLAYER_1, 4, 6))
        self.assertTrue(connect_four.col_win(PLAYER_1, 5, 6))

    def test_horizontal_win_down(self):
        connect_four = ConnectFour()
        connect_four.board = [
           [1, 2, 1, 0, 1, 2, 1],
           [1, 2, 1, 0, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 0, 1, 2, 1],
           [1, 2, 1, 0, 1, 2, 1],
        ]
        self.assertFalse(connect_four.horizontal_win_down(PLAYER_1, 5, 0))

        connect_four.board = [
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 0, 0))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 1, 1))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 2, 2))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 3, 3))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 4, 4))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 5, 5))

        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 0, 1))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 1, 2))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 2, 3))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 3, 4))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 4, 5))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 5, 6))

        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 0, 2))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 1, 3))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 2, 4))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 3, 5))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 4, 6))

        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 0, 3))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 1, 4))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 2, 5))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 3, 6))

        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 1, 0))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 2, 1))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 3, 2))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 4, 3))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_2, 5, 4))

        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 2, 0))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 3, 1))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 4, 2))
        self.assertTrue(connect_four.horizontal_win_down(PLAYER_1, 5, 3))  

    def test_horizontal_win_down(self):
        connect_four = ConnectFour()
        connect_four.board = [
           [1, 2, 1, 0, 1, 2, 1],
           [1, 2, 1, 0, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 0, 1, 2, 1],
           [1, 2, 1, 0, 1, 2, 1],
        ]
        self.assertFalse(connect_four.horizontal_win_up(PLAYER_1, 5, 0))

        connect_four.board = [
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
           [1, 2, 1, 2, 1, 2, 1],
           [2, 1, 2, 1, 2, 1, 2],
        ]
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 5, 0))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 4, 1))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 3, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 2, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 1, 4))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 0, 5))

        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 5, 1))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 4, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 3, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 2, 4))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 1, 5))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 0, 6))

        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 5, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 4, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 3, 4))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 2, 5))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 1, 6))

        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 5, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 4, 4))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 3, 5))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 2, 6))

        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 4, 0))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 3, 1))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 2, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 1, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_1, 0, 4))

        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 3, 0))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 2, 1))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 1, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 0, 3)) 

        connect_four.board = [
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 2, 0, 0],
            [1, 0, 0, 2, 2, 0, 0],
            [2, 0, 2, 2, 2, 0, 0],
            [1, 2, 2, 2, 1, 0, 0],
        ]
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 2, 4))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 3, 3))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 4, 2))
        self.assertTrue(connect_four.horizontal_win_up(PLAYER_2, 5, 1)) 
        

if __name__ == '__main__':
    unittest.main()