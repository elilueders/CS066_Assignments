import random


def random_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet[random.randint(0, 26)]


def random_text(length):
    random_string = ""
    for i in range(length):
        random_string += random_letter()
    return random_string


def score(random_string, goal_string):
    score = 0
    for i in range(len(goal_string)):
        if goal_string[i] == random_string[i]:
            score += 1
    return score


def monkey_experiment(test_string, iterations):
    best_string = ""
    best_score = 0
    for i in range(iterations):
        text = random_text(len(test_string))
        text_score = score(text, test_string)
        if text_score > best_score:
            best_string = text
            best_score = text_score

    return best_string, best_score


"""
# test cases
print(monkey_experiment("methinks it is like a weasel",10000))
print(monkey_experiment("methinks it is like a weasel",100))
print(monkey_experiment("brevity is the soul of wit",50000))
print(monkey_experiment("to be",100000))
print(monkey_experiment("to be",200000))
print(monkey_experiment("a", 50000))
print(monkey_experiment("ab", 50000))
print(monkey_experiment("abc", 50000))
print(monkey_experiment("abcd", 50000))
print(monkey_experiment("testing one two three", 1000000))

# test results
('zebhyxirqqtoiagjtdj aujwawxd', 7)
('vzwoqahszigfyhalotkdyqbyxnb ', 3)
('rkecithjrf twhjqdulimri hd', 7)
('tq be', 4)
('ho be', 4)
('a', 1)
('ab', 2)
('abc', 3)
('azcd', 3)
('zestnncchneyeyxxqkrjk', 7)
"""