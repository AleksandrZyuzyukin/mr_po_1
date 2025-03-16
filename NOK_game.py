import math
import random

from games_engine import play_game


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_three_numbers():
    numbers = [random.randint(1, 100) for _ in range(3)]
    correct_answer = lcm(lcm(numbers[0], numbers[1]), numbers[2])
    return " ".join(map(str, numbers)), correct_answer


def play_lcm_game():
    play_game(lcm_three_numbers, "Find the smallest common multiple of given numbers.", max_rounds=3)


if __name__ == "__main__":
    play_lcm_game()
