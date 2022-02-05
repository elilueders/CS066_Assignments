from binascii import Incomplete
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
    if len(random_string) == len(goal_string):
        score = 0
        for i in range(len(goal_string)):
            if goal_string[i] == random_string[i]:
                score += 1
        return score

def monkey_experiment(test_string, iterations):
    best_string = ""
    best_score = 0
    for i in range(iterations):
        print_loop_progress(i,iterations)
        # print(i, end='\r')
        text = random_text(len(test_string))
        text_score = score(text, test_string)
        if text_score > best_score:
            best_string = text
            best_score = text_score
        if len(test_string) == best_score:
            # print(i+1)
            break
    return best_string, best_score

def print_loop_progress(index,iterations):
    progress_bar = "|"
    bar_segments = 20
    complete = index//(iterations//bar_segments)
    remain = bar_segments-complete
    for i in range(complete):
        progress_bar += "X"
    for j in range(remain):
        progress_bar += "-"
    progress_bar += "|"
    print(progress_bar,index/iterations*100, end='\r')

    if complete+1 == bar_segments:
        progress_bar="  "
        for i in range(bar_segments):
            progress_bar += " "
        print(progress_bar,end='\r')
        
# print(monkey_experiment("methinks it is like a weaselmethinks it is like a weaselmethinks it is like a weasel",100))
# print(monkey_experiment("methinks it is like a weasel",100))
# print(monkey_experiment("methinks it is like a weasel",1000))
# print(monkey_experiment("brevity is the soul of wit",100000))
# print(monkey_experiment("to be",10000))
# print(monkey_experiment("to be",200000))
# print(monkey_experiment("to be",500000))
print('\n',monkey_experiment("a",100))
print('\n',monkey_experiment("a",100))
print('\n',monkey_experiment("a",100))
print('\n',monkey_experiment("ab",1000))
print('\n',monkey_experiment("ab",1000))
print('\n',monkey_experiment("ab",1000))
print('\n',monkey_experiment("abc",100000))
print('\n',monkey_experiment("abc",100000))
print('\n',monkey_experiment("abc",100000))
print('\n',monkey_experiment("abcd",500000))
print('\n',monkey_experiment("abcd",500000))
print('\n',monkey_experiment("abcd",500000))
