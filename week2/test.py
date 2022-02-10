import random

def random_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet[ random.randint(0,26) ]

def random_text(length):
    random_string = ""
    for i in range(length):
        random_string += random_letter()
    return random_string

def score(random_string,goal_string):
    if len(random_string)==len(goal_string):
        score=0
        for i in range(len(goal_string)):
            if goal_string[i]==random_string[i]:
                score+=1
        return score

def monkey_experiment(test_string,iterations):
    best_string=""
    best_score=0
    for i in range(iterations):
        print(i%10,end='\r')
        text=random_text(len(test_string))
        text_score=score(text,test_string)
        if text_score>best_score:
            best_string=text
            best_score=text_score
        if len(test_string)==best_score:
            print(i+1)
            break

    return best_string,best_score


print(monkey_experiment("hio",5000000))