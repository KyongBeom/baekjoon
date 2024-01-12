def solution(board, h, w):
    answer = 0
    color = board[h][w]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(len(dx)):
        di = h + dx[i]
        dj = w + dy[i]
        if 0 <= di < len(board) and 0 <= dj < len(board):
            if board[di][dj] == color:
                answer += 1
    return answer