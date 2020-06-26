import __main__ as main

# position will be the value of the position
def minimax(position, depth, alpha, beta, maximizing_player):
    # print(position, depth, alpha, beta, maximizing_player)
    if depth == 0 or main.winner in (0, 1):
        for loop_piece in main.pieces:
            print(loop_piece.move_piece(ai_player=True))
    
    if maximizing_player:
        max_eval = -main.math.inf
    else:
        min_eval = main.math.inf



# function minimax(position, depth, alpha, beta, maximizingPlayer)
#     if depth == 0 or game over in position
#         return static evaluation of position
 
#     if maximizingPlayer
#         maxEval = -infinity
#         for each child of position
#             eval = minimax(child, depth - 1, alpha, beta false)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha
#                 break
#         return maxEval
 
#     else
#         minEval = +infinity
#         for each child of position
#             eval = minimax(child, depth - 1, alpha, beta true)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha
#                 break
#         return minEval
 
 
# // initial call
# minimax(currentPosition, 3, -∞, +∞, true)