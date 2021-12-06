from game import Game
from players import Dealer, Player
from decks import CustomDeck
from sheets import log

from multiprocessing import Queue, Process, cpu_count
import time

args_queue = Queue()
results_queue = Queue()

parameters = {
    'rounds': 10000,
    'deck_count': 4,
    'player_count': 2
}

cards = ['A', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'J', 'Q', 'K']


def proc(queue1, queue2):
    while not queue2.empty():
        parameters = queue2.get()
        decks = [CustomDeck(**parameters['deck_params']) for i in range(parameters['deck_count'])]
        players = [Player() for i in range(parameters['player_count'])]
        dealer = Dealer()
        game = Game(decks=decks, players=players, dealer=dealer, rounds=parameters['rounds'])
        game.simulate()
        queue1.put((parameters, game.scores))


if __name__ == '__main__':
    time_start = time.perf_counter()
    processes = []
    simulation_count = 0

    for i in range(8192):
        p = parameters.copy()
        x = format(i, 'b')
        x = ''.join('0' for i in range(13 - len(x))) + x
        p['deck_params'] = {}
        for index, card in enumerate(cards):
            if x[index] == '1':
                p['deck_params'][card] = 40
        args_queue.put(p)
        simulation_count += 1

    for cpu in range(cpu_count()):
        processes.append(Process(target=proc, args=(results_queue, args_queue,)))

    for process in processes:
        process.start()

    def percent(x): return str(100 * x / (params['rounds'] * params['player_count']))[:5] + '%'

    for i in range(simulation_count):
        params, results = results_queue.get()
        wins = 0
        ties = 0
        losses = 0
        for player in results:
            wins += results[player]['wins']
            ties += results[player]['ties']
            losses += results[player]['losses']
        log(str(params['deck_params']), (percent(wins), percent(ties), percent(losses)))

    for process in processes:
        process.join()

    time_end = time.perf_counter()

    print('execution time > ', time_end - time_start)
