from random import choice

DOORS = [1, 2, 3]


class MontyHallSimulator:
    def __init__(self, reselect=True):
        self.reselect = reselect

    def run(self):

        wins = 0
        runs = 0
        while True:
            if self.run_single_game():
                wins += 1
            runs += 1
            yield self._calc_winning_probability(wins, runs)


    def run_single_game(self):

        price_door = self._generate_price_room()
        contestant_choice = self._contestant_pick()
        host_pick = self._host_pick(contestant_picked_door=contestant_choice, price_door=price_door)
        contestant_choice_final = self._contestant_second_choice(host_pick=host_pick,
                                                                 contestant_first_choice=contestant_choice)

        return self._check_contestant_selection(contestant_choice_final, price_door)

    @staticmethod
    def _calc_winning_probability(wins, games):
        return (wins / games, wins, games) if games > 0 else (0, 0, 0)

    @staticmethod
    def _check_contestant_selection(contestant_choice, price_door):
        return True if contestant_choice is price_door else False


    def _contestant_second_choice(self, *, host_pick, contestant_first_choice):
        if self.reselect:
            return next(door for door in DOORS if door is not host_pick and door is not contestant_first_choice)
        else:
            return contestant_first_choice

    @staticmethod
    def _contestant_pick():
        return choice(DOORS)
        # contestant pick a room

    @staticmethod
    def _host_pick(*, contestant_picked_door, price_door):
        # host pick a room with goat
        # another implementation, I don't really like how it searches through the list twice and creates another local variable
        # doors = DOORS[:]
        # doors.pop(contestant_picked_door)
        # doors.pop(price_door)
        # return doors[0]

        host_picked_door = next(door for door in DOORS if door is not contestant_picked_door and door is not price_door)

        return host_picked_door

    @staticmethod
    def _generate_price_room():
        # return the door number that has the price
        return choice(DOORS)


def main():
    sim = MontyHallSimulator(reselect=True)
    sim.run_single_game()
    for probability_result in sim.run():
        print(probability_result)


main()
