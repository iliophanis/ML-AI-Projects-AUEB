package Helpers;

import Models.Board;

public class Heuristic {
    Board board;

    public Heuristic(Board board) {
        if (board == null)
            return;
        this.board = board;
    }

    public double heuristic_evaluation() {

        double coin_parity;
        double mobility;
        double corners_captured;
        double stability;

        // Number of player's letter
        int X = board.countLetters(1);
        int O = board.countLetters(-1);
        // coin parity
        if (X + O != 0)
            coin_parity = 100 * (X - O) / (X + O);
        else
            coin_parity = 0;

        // mobility
        X = board.acceptableMoves(1).size();
        O = board.acceptableMoves(-1).size();
        if (X + O != 0)
            mobility = 100 * (X - O) / (X + O);
        else
            mobility = 0;

        // corners captured
        X = O = 0;
        if (board.getBoard(0, 0) == 1)
            X++;
        else if (board.getBoard(0, 0) == -1)
            O++;
        if (board.getBoard(0, 7) == 1)
            X++;
        else if (board.getBoard(0, 7) == -1)
            O++;
        if (board.getBoard(7, 0) == 1)
            X++;
        else if (board.getBoard(7, 0) == -1)
            O++;
        if (board.getBoard(7, 7) == 1)
            X++;
        else if (board.getBoard(7, 7) == -1)
            O++;

        if (X + O != 0)
            corners_captured = 100 * (X - O) / (X + O);
        else
            corners_captured = 0;

        // Stability
        X = O = 0;
        // 1st row
        if (board.getBoard(0, 0) == 1)
            X += 4;
        if (board.getBoard(0, 0) == -1)
            O += 4;
        if (board.getBoard(0, 1) == 1)
            X -= 3;
        if (board.getBoard(0, 1) == -1)
            O -= 3;
        if (board.getBoard(0, 2) == 1)
            X += 2;
        if (board.getBoard(0, 2) == -1)
            O += 2;
        if (board.getBoard(0, 3) == 1)
            X += 2;
        if (board.getBoard(0, 3) == -1)
            O += 2;
        if (board.getBoard(0, 4) == 1)
            X += 2;
        if (board.getBoard(0, 4) == -1)
            O += 2;
        if (board.getBoard(0, 5) == 1)
            X += 2;
        if (board.getBoard(0, 5) == -1)
            O += 2;
        if (board.getBoard(0, 6) == 1)
            X -= 3;
        if (board.getBoard(0, 6) == -1)
            O -= 3;
        if (board.getBoard(0, 7) == 1)
            X += 4;
        if (board.getBoard(0, 7) == -1)
            O += 4;
        // 2nd row
        if (board.getBoard(1, 0) == 1)
            X -= 3;
        if (board.getBoard(1, 0) == -1)
            O -= 3;
        if (board.getBoard(1, 1) == 1)
            X -= 4;
        if (board.getBoard(1, 1) == -1)
            O -= 4;
        if (board.getBoard(1, 2) == 1)
            X -= 1;
        if (board.getBoard(1, 2) == -1)
            O -= 1;
        if (board.getBoard(1, 3) == 1)
            X -= 1;
        if (board.getBoard(1, 3) == -1)
            O -= 1;
        if (board.getBoard(1, 4) == 1)
            X -= 1;
        if (board.getBoard(1, 4) == -1)
            O -= 1;
        if (board.getBoard(1, 5) == 1)
            X -= 1;
        if (board.getBoard(1, 5) == -1)
            O -= 1;
        if (board.getBoard(1, 6) == 1)
            X -= 4;
        if (board.getBoard(1, 6) == -1)
            O -= 4;
        if (board.getBoard(1, 7) == 1)
            X -= 3;
        if (board.getBoard(1, 7) == -1)
            O -= 3;
        // 3rd row
        if (board.getBoard(2, 0) == 1)
            X += 2;
        if (board.getBoard(2, 0) == -1)
            O += 2;
        if (board.getBoard(2, 1) == 1)
            X -= 1;
        if (board.getBoard(2, 1) == -1)
            O -= 1;
        if (board.getBoard(2, 2) == 1)
            X += 1;
        if (board.getBoard(2, 2) == -1)
            O += 1;
        if (board.getBoard(2, 3) == 1)
            X += 0;
        if (board.getBoard(2, 3) == -1)
            O += 0;
        if (board.getBoard(2, 4) == 1)
            X += 0;
        if (board.getBoard(2, 4) == -1)
            O += 0;
        if (board.getBoard(2, 5) == 1)
            X += 1;
        if (board.getBoard(2, 5) == -1)
            O += 1;
        if (board.getBoard(2, 6) == 1)
            X -= 1;
        if (board.getBoard(2, 6) == -1)
            O -= 1;
        if (board.getBoard(2, 7) == 1)
            X += 2;
        if (board.getBoard(2, 7) == -1)
            O += 2;
        // 4th row
        if (board.getBoard(3, 0) == 1)
            X += 2;
        if (board.getBoard(3, 0) == -1)
            O += 2;
        if (board.getBoard(3, 1) == 1)
            X -= 1;
        if (board.getBoard(3, 1) == -1)
            O -= 1;
        if (board.getBoard(3, 2) == 1)
            X += 0;
        if (board.getBoard(3, 2) == -1)
            O += 0;
        if (board.getBoard(3, 3) == 1)
            X += 1;
        if (board.getBoard(3, 3) == -1)
            O += 1;
        if (board.getBoard(3, 4) == 1)
            X += 1;
        if (board.getBoard(3, 4) == -1)
            O += 1;
        if (board.getBoard(3, 5) == 1)
            X += 0;
        if (board.getBoard(3, 5) == -1)
            O += 0;
        if (board.getBoard(3, 6) == 1)
            X -= 1;
        if (board.getBoard(3, 6) == -1)
            O -= 1;
        if (board.getBoard(3, 7) == 1)
            X += 2;
        if (board.getBoard(3, 7) == -1)
            O += 2;
        // 5th row
        if (board.getBoard(4, 0) == 1)
            X += 2;
        if (board.getBoard(4, 0) == -1)
            O += 2;
        if (board.getBoard(4, 1) == 1)
            X -= 1;
        if (board.getBoard(4, 1) == -1)
            O -= 1;
        if (board.getBoard(4, 2) == 1)
            X += 0;
        if (board.getBoard(4, 2) == -1)
            O += 0;
        if (board.getBoard(4, 3) == 1)
            X += 1;
        if (board.getBoard(4, 3) == -1)
            O += 1;
        if (board.getBoard(4, 4) == 1)
            X += 1;
        if (board.getBoard(4, 4) == -1)
            O += 1;
        if (board.getBoard(4, 5) == 1)
            X += 0;
        if (board.getBoard(4, 5) == -1)
            O += 0;
        if (board.getBoard(4, 6) == 1)
            X -= 1;
        if (board.getBoard(4, 6) == -1)
            O -= 1;
        if (board.getBoard(4, 7) == 1)
            X += 2;
        if (board.getBoard(4, 7) == -1)
            O += 2;
        // 6th row
        if (board.getBoard(5, 0) == 1)
            X += 2;
        if (board.getBoard(5, 0) == -1)
            O += 2;
        if (board.getBoard(5, 1) == 1)
            X -= 1;
        if (board.getBoard(5, 1) == -1)
            O -= 1;
        if (board.getBoard(5, 2) == 1)
            X += 1;
        if (board.getBoard(5, 2) == -1)
            O += 1;
        if (board.getBoard(5, 3) == 1)
            X += 0;
        if (board.getBoard(5, 3) == -1)
            O += 0;
        if (board.getBoard(5, 4) == 1)
            X += 0;
        if (board.getBoard(5, 4) == -1)
            O += 0;
        if (board.getBoard(5, 5) == 1)
            X += 1;
        if (board.getBoard(5, 5) == -1)
            O += 1;
        if (board.getBoard(5, 6) == 1)
            X -= 1;
        if (board.getBoard(5, 6) == -1)
            O -= 1;
        if (board.getBoard(5, 7) == 1)
            X += 2;
        if (board.getBoard(5, 7) == -1)
            O += 2;
        // 7th row
        if (board.getBoard(6, 0) == 1)
            X -= 3;
        if (board.getBoard(6, 0) == -1)
            O -= 3;
        if (board.getBoard(6, 1) == 1)
            X -= 4;
        if (board.getBoard(6, 1) == -1)
            O -= 4;
        if (board.getBoard(6, 2) == 1)
            X -= 1;
        if (board.getBoard(6, 2) == -1)
            O -= 1;
        if (board.getBoard(6, 3) == 1)
            X -= 1;
        if (board.getBoard(6, 3) == -1)
            O -= 1;
        if (board.getBoard(6, 4) == 1)
            X -= 1;
        if (board.getBoard(6, 4) == -1)
            O -= 1;
        if (board.getBoard(6, 5) == 1)
            X -= 1;
        if (board.getBoard(6, 5) == -1)
            O -= 1;
        if (board.getBoard(6, 6) == 1)
            X -= 4;
        if (board.getBoard(6, 6) == -1)
            O -= 4;
        if (board.getBoard(6, 7) == 1)
            X -= 3;
        if (board.getBoard(6, 7) == -1)
            O -= 3;
        // 8th row
        if (board.getBoard(7, 0) == 1)
            X += 4;
        if (board.getBoard(7, 0) == -1)
            O += 4;
        if (board.getBoard(7, 1) == 1)
            X -= 3;
        if (board.getBoard(7, 1) == -1)
            O -= 3;
        if (board.getBoard(7, 2) == 1)
            X += 2;
        if (board.getBoard(7, 2) == -1)
            O += 2;
        if (board.getBoard(7, 3) == 1)
            X += 2;
        if (board.getBoard(7, 3) == -1)
            O += 2;
        if (board.getBoard(7, 4) == 1)
            X += 2;
        if (board.getBoard(7, 4) == -1)
            O += 2;
        if (board.getBoard(7, 5) == 1)
            X += 2;
        if (board.getBoard(7, 5) == -1)
            O += 2;
        if (board.getBoard(7, 6) == 1)
            X -= 3;
        if (board.getBoard(7, 6) == -1)
            O -= 3;
        if (board.getBoard(7, 7) == 1)
            X += 4;
        if (board.getBoard(7, 7) == -1)
            O += 4;

        if (X + O != 0)
            stability = 100 * (X - O) / (X + O);
        else
            stability = 0;

        return (coin_parity + mobility + corners_captured + stability);

    }

}
