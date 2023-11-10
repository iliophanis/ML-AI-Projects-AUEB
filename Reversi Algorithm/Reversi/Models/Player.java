package Models;

import java.util.ArrayList;
import java.util.Random;

import Helpers.Move;

public class Player {

    private int maxDepth;
    private int playerLetter;

    public Player(int maxDepth, int playerLetter) {
        this.playerLetter = playerLetter;
        this.maxDepth = maxDepth;
    }

    public Move MiniMax(Board board) {
        if (playerLetter == Board.X) {
            // If the X plays then it wants to maximize the heuristics value
            return max(new Board(board), 0);
        } else {
            // If the O plays then it wants to minimize the heuristics value
            return min(new Board(board), 0);
        }
    }

    // The max and min functions are called one after another until a max depth is
    // reached or game reaches end.
    // We create a tree using backtracking DFS.
    private Move max(Board board, int depth) {
        Random r = new Random();
        /*
         * If MAX is called on a state that is terminal or after a maximum depth is
         * reached,
         * then a heuristic is calculated on the state and the move returned.
         */
        if ((board.isTerminal()) || (depth == this.maxDepth)) {
            return new Move(board.getLastMove().getRow(), board.getLastMove().getCol(), board.heuristic());
        }
        // The children-moves of the state are calculated
        ArrayList<Board> children = board.getChildren(Board.X);
        Move maxMove = new Move(Integer.MIN_VALUE);

        for (Board child : children) {
            // And for each child min is called, on a lower depth
            Move move = min(child, depth + 1);
            // The child-move with the greatest value is selected and returned by max
            // check if this.move is max
            if (move.getValue() >= maxMove.getValue()) {
                if ((move.getValue() == maxMove.getValue())) {
                    // If the heuristic has the same value then we randomly choose one of the two
                    // moves
                    if (r.nextInt(2) == 0) {
                        maxMove.setRow(child.getLastMove().getRow());
                        maxMove.setCol(child.getLastMove().getCol());
                        maxMove.setValue(move.getValue());
                    }
                } else {
                    maxMove.setRow(child.getLastMove().getRow());
                    maxMove.setCol(child.getLastMove().getCol());
                    maxMove.setValue(move.getValue());
                }
            }

            if (move.getValue() < maxMove.getValue()) { // alpha- beta pruning
                return maxMove;
            }
        }

        return maxMove;

    }

    private Move min(Board board, int depth) {

        Random r = new Random();

        if ((board.isTerminal()) || (depth == this.maxDepth)) {
            return new Move(board.getLastMove().getRow(), board.getLastMove().getCol(), board.heuristic());
        }

        ArrayList<Board> children = board.getChildren(Board.O);
        Move minMove = new Move(Integer.MAX_VALUE);

        for (Board child : children) {
            Move move = max(child, depth + 1);
            if (move.getValue() <= minMove.getValue()) {
                if ((move.getValue() == minMove.getValue())) {
                    if (r.nextInt(2) == 0) {
                        minMove.setRow(child.getLastMove().getRow());
                        minMove.setCol(child.getLastMove().getCol());
                        minMove.setValue(move.getValue());
                    }
                } else {
                    minMove.setRow(child.getLastMove().getRow());
                    minMove.setCol(child.getLastMove().getCol());
                    minMove.setValue(move.getValue());
                }
            }

            if (move.getValue() > minMove.getValue()) { // alpha- beta pruning
                return minMove;
            }
        }
        return minMove;
    }
}