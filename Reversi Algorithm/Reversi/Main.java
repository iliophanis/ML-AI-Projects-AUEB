import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import Helpers.Move;
import Models.Board;
import Models.Player;

public class Main {

    public static void main(String[] args) {

        System.out.println("Reversi Game Starting!\n");
        Scanner scan = new Scanner(System.in);
        System.out.print("Choose a number between 1 and 6 to set the depth of the algorithm: \n");
        int depth = Integer.parseInt(scan.next());
        while (depth < 1 || depth > 6) {
            System.out.print("Invalid number. Choose another between 1 and 6: \n");
            depth = Integer.parseInt(scan.next());
        }

        System.out.print("Do you want to play first?(y/n):");
        int playerLetter = 1; // first player is always X
        if (scan.next().trim().equals("n")) {
            playerLetter = -1;
        }

        Board board = new Board();
        Player pcPlayer = new Player(depth, -playerLetter);

        System.out.println();
        board.print();
        System.out.println();
        int playedLast = -1;

        while (!board.isTerminal()) {
            // pc move
            if (playedLast == playerLetter) {
                if (board.hasMoves(-playerLetter)) {
                    Move move = pcPlayer.MiniMax(board);
                    board.makeMove(-playerLetter, move);
                    System.out.println("I played " + move + "\n");
                    board.print();
                    playedLast = board.getLastLetterPlayer();
                } else
                    playedLast = -playedLast;
            }
            // player move
            if (playedLast == -playerLetter) {
                if (board.hasMoves(playerLetter)) {
                    System.out.print("\nIt's your turn! row,col: ");
                    Map<String, Integer> coordinates = getDirections(scan);
                    while (coordinates.isEmpty()
                            || board.isValidMove(playerLetter, coordinates.get("x"), coordinates.get("y"))
                                    .equals("INVALID")) {
                        System.out.print("Please check your input and try again: ");
                        coordinates = getDirections(scan);
                    }
                    board.makeMove(playerLetter, coordinates.get("x"), coordinates.get("y"));
                    System.out.println();
                    board.print();
                    System.out.println("\n");
                    playedLast = board.getLastLetterPlayer();
                } else
                    playedLast = -playedLast;
            }
        }
        scan.close();

        System.out.println("\nThe game has finished." + board.getGameWinner());

    }

    private static Map<String, Integer> getDirections(Scanner scan) {
        Map<String, Integer> coordinates = new HashMap<>();
        String input = scan.next().trim();
        if (input.length() != 3 || !input.contains(","))
            return coordinates;
        coordinates.put("x", Integer.parseInt(input.substring(0, 1)));
        coordinates.put("y", Integer.parseInt(input.substring(2)));
        return coordinates;
    }

}
