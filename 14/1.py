content_list = [
    {"name": "Taylor Swift", "follower_count": "250", "description": "Musician", "country": "USA"},
    {"name": "Cristiano Ronaldo", "follower_count": "300", "description": "Footballer", "country": "Portugal"},
    {"name": "Elon Musk", "follower_count": "152", "description": "Entrepreneur", "country": "USA"},
    {"name": "Ariana Grande", "follower_count": "230", "description": "Musician", "country": "USA"},
    {"name": "Lionel Messi", "follower_count": "280", "description": "Footballer", "country": "Argentina"},
    {"name": "Kylie Jenner", "follower_count": "220", "description": "Entrepreneur", "country": "USA"},
    {"name": "Dwayne Johnson", "follower_count": "260", "description": "Actor", "country": "USA"},
    {"name": "Selena Gomez", "follower_count": "240", "description": "Musician", "country": "USA"},
    {"name": "Kim Kardashian", "follower_count": "210", "description": "Entrepreneur", "country": "USA"},
    {"name": "Neymar Jr.", "follower_count": "221", "description": "Footballer", "country": "Brazil"},
    {"name": "Beyoncé", "follower_count": "200", "description": "Musician", "country": "USA"},
    {"name": "Justin Bieber", "follower_count": "232", "description": "Musician", "country": "USA"},
    {"name": "Billie Eilish", "follower_count": "190", "description": "Musician", "country": "USA"},
    {"name": "LeBron James", "follower_count": "180", "description": "Basketball Player", "country": "USA"},
    {"name": "Kendall Jenner", "follower_count": "170", "description": "Model", "country": "USA"},
    {"name": "Shakira", "follower_count": "160", "description": "Musician", "country": "Colombia"},
    {"name": "Virat Kohli", "follower_count": "150", "description": "Cricketer", "country": "India"}
]
import random

score = 0

def generate_randoms():
    return random.randint(0, len(content_list) - 1)

def game(first_random=None):
    global score
    if first_random is None:
        first_random = generate_randoms()
    second_random = generate_randoms()
    while second_random == first_random:
        second_random = generate_randoms()

    print(f'Compare A:{content_list[first_random]["name"]}, a {content_list[first_random]["description"]}, from {content_list[first_random]["country"]}')
    print("VS")
    print(f'Against B:{content_list[second_random]["name"]}, a {content_list[second_random]["description"]}, from {content_list[second_random]["country"]}')
    print(content_list[first_random]["follower_count"])
    print(content_list[second_random]["follower_count"])
    print('score:', score)
    get_answer = input('\nWho has more followers? Type A or B ')

    if get_answer == 'A':
        if int(content_list[first_random]["follower_count"]) > int(content_list[second_random]["follower_count"]):
            score += 1
            game(first_random)
        else:
            print(f'you have lost, your score is {score}')
            return True

    if get_answer == 'B':
        if int(content_list[first_random]["follower_count"]) < int(content_list[second_random]["follower_count"]):
            score += 1
            game(second_random)
        else:
            print(f'you have lost, your score is {score}')
            return True

game()