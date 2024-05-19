winmap = {'MAX': 100, 'MIN': -100, 'DRAW': 0, None: 0}

def minmax(game, depth):
    winner = game.winner()
    if winner is not None:
        return winmap[game.winner()], game
    if depth == 0:
        return game.estimate(), game
    player = game.nextplayer
    if player == 'MAX':
        val, bestState = 2*winmap['MIN'], None
        for state in game.nextStates():
            val, bestState = max([(val, bestState), (minmax(state[0], depth - 1)[0], state)], key=lambda x: x[0])
        return val, bestState
    val, bestState = 2*winmap['MAX'], None
    for state in game.nextStates():
        val, bestState = min([(val, bestState), (minmax(state[0], depth - 1)[0], state)], key=lambda x: x[0])
    return val, bestState

def alphabeta(game, depth, alpha=-100, beta=100):
    winner = game.winner()
    if winner is not None:
        return winmap[game.winner()], game
    if depth == 0:
        return game.estimate(), game
    player = game.nextplayer
    if player == 'MAX':
        val, bestState = 2*winmap['MIN'], None
        for state in game.nextStates():
            val, bestState = max([(val, bestState), (alphabeta(state[0], depth - 1)[0], state)], key=lambda x: x[0])
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val, bestState
    val, bestState = 2*winmap['MAX'], None
    for state in game.nextStates():
        val, bestState = min([(val, bestState), (alphabeta(state[0], depth - 1)[0], state)], key=lambda x: x[0])
        beta = min(beta, val)
        if alpha >= beta:
            break
    return val, bestState