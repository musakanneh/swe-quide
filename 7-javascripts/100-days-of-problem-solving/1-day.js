/**
 * leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
 * @param {number[][]} moves
 * @return {string}
 */
const tictactoe = (moves) => {
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]];

    const matrix = new Array(3);
    for (let i = 0; i < 3; i++) {
        matrix[i] = Array(3);
    }

    for (let i = 0; i < moves.length; i++) {
        if (i % 2 == 0) {
            matrix[moves[i][0]] [moves[i][1]] = "A";
        } else {
            matrix[moves[i][0]] [moves[i][1]] = "B";
        }
    }

    const check_row_col = (row) => {
        if (matrix[row][0] && matrix[row][1] && matrix[row][2] &&
            new Set(matrix[row][0], matrix[row][1], matrix[row][2]).size === 1) {
            return matrix[row][0];
        }

        if (matrix[0][row] && matrix[1][row] && matrix[2][row] &&
            new Set(matrix[0][row], matrix[1][row], matrix[2][row]).size === 1) {
            return matrix[0][row];
        }

        if (matrix[0][0] && matrix[1][1] && matrix[2][2] &&
            new Set(matrix[0][0], matrix[1][1], matrix[2][2]).size === 1) {
            return matrix[0][0];
        }

        if (matrix[0][2] && matrix[1][1] && matrix[2][0] &&
            new Set(matrix[0][2], matrix[1][1], matrix[2][0]).size === 1) {
            return matrix[0][2];
        }
    }

    for (let i = 0; i < matrix.length; i++) {
        if (check_row_col(i)) {
            return check_row_col(i);
        }
    }
    
    return moves.length === 9 ? "Draw" : "Pending";
};
console.log(tictactoe());