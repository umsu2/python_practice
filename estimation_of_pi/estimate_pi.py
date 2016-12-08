
import math
from random import uniform


AREA_OF_SQUARE = 2 * 2
class PiEstimator:
    # Area of Circle is pi*r*r, given r = 1, the area of circle = pi.
    # Assume a square of 2 x 2 size. drawing a circle in the center with r = 1.
    # the probability of a point chosen randomly from range of (-1, 1) in both x and y axis. will result in either inside the circle or outside the circle
    # the probability inside the circle * area of square = estimate of pi

    def run(self):
        trial = 0
        point_inside_circle = 0

        while True:

            if self.run_single_trial():
                point_inside_circle += 1
            trial += 1

            yield (self._calc_probability(trial, point_inside_circle) * AREA_OF_SQUARE , trial)


    def run_single_trial(self):
        point = self._pick_random_point()
        return self._validate(point)

    @staticmethod
    def _calc_probability(trials, point_inside_circle ):
        return point_inside_circle / trials if point_inside_circle > 0 else 0

    @staticmethod
    def _pick_random_point(): # picking a random point from -1, 1 range
        return Point(x = uniform(-1,1), y = uniform(-1,1))

    @staticmethod
    def _validate(point):
        return True if point.distance_from_origin() <= 1 else False



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x*self.x +self.y*self.y)


def run_pi_estimator():
    sim = PiEstimator()

    for result in sim.run():
        print(result)

if __name__ == '__main__':
    run_pi_estimator()