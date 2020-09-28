import random

moves = ['rock', 'paper', 'scissors']


def getInput():
    answer = input("Please select, 'Rock', 'Paper', or 'Scissors'  ").lower()
    if answer in moves:
        return answer
    else:
        return getInput()


def getLearnedSolution(previousMove):
    if previousMove == 'rock':
        return 'paper'
    elif previousMove == 'paper':
        return 'scissors'
    else:
        return 'rock'


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        return getInput()

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.savedMove = ''

    def move(self):
        if self.savedMove:
            return getLearnedSolution(self.savedMove)
        else:
            return (random.choice(moves))

    def learn(self, my_move, their_move):
        self.savedMove = my_move


class CyclePlayer(Player):
    def __init__(self):
        self.cycleMove = 0

    def move(self):
        currentMove = moves[self.cycleMove]
        if self.cycleMove == len(moves) - 1:
            self.cycleMove = 0
        else:
            self.cycleMove += 1
        return currentMove

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.savedMove = ''

    def move(self):
        if self.savedMove:
            return self.savedMove
        else:
            return (random.choice(moves))

    def learn(self, my_move, their_move):
        self.savedMove = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        print(p2)
        self.p1 = p1
        self.p2 = p2
        self.win = 0
        self.loss = 0
        self.tie = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}  Opponent played: {move2}")

        if beats(move1, move2):
            print('** You win this round **')
            self.win += 1
        elif beats(move2, move1):
            print('** You lost this round **')
            self.loss += 1
        else:
            print('** This round ended in a Tie **')
            self.tie += 1

        print(f'Player 1 wins: {self.win}')
        print(f'Player 1 losses: {self.loss}')
        print(f'Ties: {self.tie}')

        # self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def print_results(self):
        print('Player 1 wins: ', self.win)
        print('Player 1 losses: ', self.loss)
        print('ties: ', self.tie)

        if self.win > self.loss:
            print('Player 1 wins!!!')
        elif self.win < self.loss:
            print('Player 1 loses!!!')
        else:
            print('Tie')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        self.print_results()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
