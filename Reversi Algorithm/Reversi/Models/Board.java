package Models;

import java.util.ArrayList;
import java.util.StringTokenizer;

import Helpers.Heuristic;
import Helpers.Move;

public class Board {

    public static final int X = 1; // black
    public static final int O = -1; // white
    public static final int EMPTY = 0;

    // Immediate move that lead to this board
    private Move lastMove;

    /*
     * Variable containing who played last; whose turn resulted in this board
     * Even a new Board has lastLetterPlayed value; it denotes which player will
     * play first
     */
    private int lastPlayer;

    private int[][] gameBoard;

    private int movesCounter;

    public Board() {
        this.lastMove = new Move();
        this.lastPlayer = O;
        movesCounter = 0;
        this.gameBoard = new int[8][8];
        for (int i = 0; i < this.gameBoard.length; i++) {
            for (int j = 0; j < this.gameBoard.length; j++)
                gameBoard[i][j] = EMPTY;
        }
        this.gameBoard[3][3] = X;
        this.gameBoard[3][4] = O;
        this.gameBoard[4][3] = O;
        this.gameBoard[4][4] = X;
    }

    public Board(Board board) {
        this.lastMove = board.lastMove;
        this.lastPlayer = board.lastPlayer;
        this.movesCounter = board.getMoveCounter();
        this.gameBoard = new int[8][8];
        for (int i = 0; i < this.gameBoard.length; i++) {
            for (int j = 0; j < this.gameBoard.length; j++) {
                this.gameBoard[i][j] = board.gameBoard[i][j];
            }
        }
    }

    public int getBoard(int x, int y) {
        return gameBoard[x][y];
    }

    public ArrayList<Board> getChildren(int letter) {
        ArrayList<Board> children = new ArrayList<>();
        ArrayList<Move> moves = this.acceptableMoves(letter);
        for (Move move : moves) {
            Board child = new Board(this);
            child.makeMove(letter, move.getRow(), move.getCol());
            move.setValue(child.heuristic());
            children.add(child);
        }
        return children;
    }

    public void makeMove(int player, int x, int y) {
        // directions is a string which contains all the possible cells this player can
        // go
        String directions = isValidMove(player, x, y);
        StringTokenizer splitter = new StringTokenizer(directions); // split the string (by spaces)
        // if there are more than 2 available moves, we keep 2
        int numOfMoves = splitter.countTokens(); // count the tokens of the string (how many moves are available)
        if (numOfMoves > 1)
            numOfMoves = 2; // 2 == multiple moves
        else
            numOfMoves = 0; // 0 == a single move

        while (splitter.hasMoreTokens()) { // if there are still more available moves

            String direction = splitter.nextToken();

            if (direction.equals("RIGHT")) {
                int j = y;
                if (numOfMoves == 1) // if there is only one available move
                {
                    j++; // go to the right column
                }
                if (numOfMoves > 0) {
                    numOfMoves--; // decrease the available moves (bc you will go right)
                }
                while (gameBoard[x][j] != player) { // if to the right cell you don't see the player letter
                    gameBoard[x][j++] = player; // put player letter to the next right cell
                }
            }
            if (direction.equals("LEFT")) {
                int j = y;
                if (numOfMoves == 1)
                    j--;
                if (numOfMoves > 0)
                    numOfMoves--;
                while ((gameBoard[x][j] != player) && ((j - 1) < 8 && (j - 1) >= 0)) {
                    gameBoard[x][j--] = player;
                }
            }
            if (direction.equals("DOWN")) {
                int i = x;
                if (numOfMoves == 1)
                    i--;
                if (numOfMoves > 0)
                    numOfMoves--;
                while (gameBoard[i][y] != player) {
                    gameBoard[i--][y] = player;
                }
            }
            if (direction.equals("UP")) {
                int i = x;
                if (numOfMoves == 1) // the first cell
                    i++;
                if (numOfMoves > 0)
                    numOfMoves--;
                while (gameBoard[i][y] != player) {
                    gameBoard[i++][y] = player;
                }
            }
            if (direction.equals("UP_RIGHT")) { // fill the between cells with the player's letter
                int j = y;
                int i = x;
                if (numOfMoves == 1) { // if there is only one available move
                    j++; // move right the col
                    i++; // move down the row
                }
                if (numOfMoves > 0)
                    numOfMoves--; // reduce the number of moves
                while (gameBoard[i][j] != player) { // while you don't find the player's letter into the cells
                    gameBoard[i++][j++] = player; // put the player's letters into the cells
                }
            }
            if (direction.equals("UP_LEFT")) {
                int j = y;
                int i = x;
                if (numOfMoves == 1) {
                    j--;
                    i++;

                }
                if (numOfMoves > 0)
                    numOfMoves--;
                while (gameBoard[i][j] != player) {
                    gameBoard[i++][j--] = player;
                }
            }
            if (direction.equals("DOWN_RIGHT")) {
                int j = y;
                int i = x;
                if (numOfMoves == 1) {
                    j++;
                    i--;
                }
                if (numOfMoves > 0)
                    numOfMoves--;
                while (gameBoard[i][j] != player) {
                    gameBoard[i--][j++] = player;
                }
            }
            if (direction.equals("DOWN_LEFT")) {
                int j = y;
                int i = x;
                if (numOfMoves == 1) {
                    j--;
                    i--;
                }
                if (numOfMoves > 0)
                    numOfMoves--;
                while (gameBoard[i][j] != player) {
                    gameBoard[i--][j--] = player;
                }
            }
        }
        lastMove = new Move(x, y);
        lastPlayer = player;
        movesCounter++;
    }

    public String isValidMove(int letter, int x, int y) {

        // check if move is out of bounds
        if (x < 0 || y < 0)
            return "INVALID";
        if (x > 7 || y > 7)
            return "INVALID";
        // check if move leads to a non empty cell
        if (gameBoard[x][y] != EMPTY)
            return "INVALID";

        int oppositeLetter = -letter;
        String directions = ""; // create an empty string
        boolean inside = false; // if there is enemy inside

        int row = x; // the row the player wants to go
        int col = y; // the column the player wants to go
        // check the board down
        while (row - 1 > 0 && gameBoard[row - 1][col] == oppositeLetter) {
            row--;
            inside = true;
        }
        row--;

        if (row == -1)
            directions += ""; // we are out of bounds
        else if (gameBoard[row][col] == letter && inside) {
            directions += " DOWN";
        }

        // new direction -> up
        inside = false;
        row = x;
        col = y;
        // check the cells of the board
        // see if there is enemy down the same column
        while (row + 1 < 7 && gameBoard[row + 1][col] == oppositeLetter) {
            row++; // while DOWN this column there is the enemy
            inside = true; // enemy inside == true (the cell of the column)
        }
        row++;
        // if there is enemy at every cell to this specific column (down of that cell)
        if (row == 8)
            directions += ""; // don't add to the directions the DOWN option (there is no cell left)
        // if at the row we've reached, i.e. 5, between them there is enemy letter
        // (in==true)
        else if (gameBoard[row][col] == letter && inside) { // if at this cell we have letter & enemy contained
            directions += " UP"; // between this cell and the desirable row that the player entered
        }

        // explore new direction -> right
        inside = false;
        row = x;
        col = y;
        while (col + 1 < 7 && gameBoard[row][col + 1] == oppositeLetter) {
            col++;
            inside = true;
        }
        col++;

        if (col == 8)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " RIGHT";
        }

        // new direction -> left
        inside = false;
        row = x;
        col = y;
        while (col - 1 > 0 && gameBoard[row][col - 1] == oppositeLetter) {
            col--;
            inside = true;
        }
        col--;

        if (col == -1)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " LEFT";
        }

        // new direction
        inside = false;
        row = x;
        col = y; // down right
        while (row + 1 < 7 && col + 1 < 7 && gameBoard[row + 1][col + 1] == oppositeLetter) {
            row++;
            col++;
            inside = true;
        }
        if (++col == 8 || ++row == 8)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " UP_RIGHT";
        }
        // new direction
        inside = false;
        row = x;
        col = y; // down left
        while (row + 1 < 7 && col - 1 > 0 && gameBoard[row + 1][col - 1] == oppositeLetter) {
            row++;
            col--;
            inside = true;
        }

        if (--col == -1 || ++row == 8)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " UP_LEFT";
        }
        // new direction
        inside = false;
        row = x;
        col = y; // up right
        while (row - 1 > 0 && col + 1 < 7 && gameBoard[row - 1][col + 1] == oppositeLetter) {
            row--;
            col++;
            inside = true;
        }

        if (++col == 8 || --row == -1)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " DOWN_RIGHT";
        }
        // new direction
        inside = false;
        row = x;
        col = y; // up left
        while (row - 1 > 0 && col - 1 > 0 && gameBoard[row - 1][col - 1] == oppositeLetter) {
            row--;
            col--;
            inside = true;
        }

        if (--col == -1 || --row == -1)
            directions += "";
        else if (gameBoard[row][col] == letter && inside) {
            directions += " DOWN_LEFT";
        }

        if (directions.equals("")) {
            directions = "INVALID";
        }
        // it returns all the moves that the specific player can make at this point
        return directions;
    }

    public ArrayList<Move> acceptableMoves(int player) {
        ArrayList<Move> allMoves = new ArrayList<>(); // all the moves the player can make
        Move temp;
        for (int i = 0; i < gameBoard.length; i++) {
            for (int j = 0; j < gameBoard.length; j++) { // only if the specific move is not forbidden
                if (!isValidMove(player, i, j).equals("INVALID")) {
                    temp = new Move(i, j); // add this move to our list
                    allMoves.add(temp);
                }
            }
        }
        return allMoves;
    }

    public void makeMove(int player, Move move) {
        makeMove(player, move.getRow(), move.getCol());
    }

    // count how many disks this player has
    public int countLetters(int player) {
        int sum = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (gameBoard[i][j] == player) {
                    sum++;
                }
            }
        }
        return sum;
    }

    public double heuristic() {
        Heuristic val = new Heuristic(this);
        return val.heuristic_evaluation();
    }

    public String getGameWinner() {
        int sum = 0;
        for (int i = 0; i < gameBoard.length; i++) {
            for (int j = 0; j < gameBoard.length; j++) { // count the letters on the board
                sum = sum + gameBoard[i][j];
            }
        }
        if (sum < 0)
            return "The winner is O!";
        if (sum > 0)
            return "The winner is X!";

        return "It is a dead hit!";

    }

    public void print() {
        System.out.println("  0 1 2 3 4 5 6 7  ");
        for (int i = 0; i < 8; i++) {
            System.out.print(i);
            for (int j = 0; j < 8; j++) {
                if (gameBoard[i][j] > 0) {
                    System.out.print(" X");
                } else if (gameBoard[i][j] < 0) {
                    System.out.print(" O");
                } else
                    System.out.print(" -");
            }
            System.out.println();
        }

    }

    public boolean hasMoves(int player) {
        return acceptableMoves(player).size() != 0;
    }

    public int getLastLetterPlayer() {
        return lastPlayer;
    }

    public boolean isTerminal() {
        return (acceptableMoves(X).size() + acceptableMoves(O).size() == 0);
    }

    public int getMoveCounter() {
        return movesCounter;
    }

    public Move getLastMove() {
        return lastMove;
    }

}
