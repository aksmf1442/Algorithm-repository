// 크레인 인형뽑기 게임

function solution(board, moves) {
    var result = 0;
    let crainStack = [];
    
    for (let y of moves) {
        y -= 1;
        for (let x = 0; x < board[0].length; x++) {
            if (board[x][y] !== 0) {
                crainStack.push(board[x][y]);
                board[x][y] = 0;
                break;
            }
        }
        if (crainStack.length >= 2 && crainStack[crainStack.length - 1] === crainStack[crainStack.length - 2]) {
            result += 2;
            crainStack.pop();
            crainStack.pop();
        }
    }
    return result;
}