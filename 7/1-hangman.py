import random
name_list = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander',
    'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo',
    'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew',
    'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln',
    'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah',
    'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles', 'Eli',
    'Nolan', 'Christian', 'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca', 'Landon', 'Hunter', 'Jonathan',
    'Santiago', 'Axel', 'Easton', 'Cooper', 'Jeremiah', 'Angel', 'Roman', 'Connor', 'Jameson', 'Robert',
    'Greyson', 'Jordan', 'Ian', 'Carson', 'Jaxson', 'Leonardo', 'Nicholas', 'Dominic', 'Austin', 'Everett',
    'Brooks', 'Xavier', 'Kai', 'Jose', 'Parker', 'Adam', 'Jace', 'Wesley', 'Kayden', 'Silas',
    'Bennett', 'Declan', 'Waylon', 'Weston', 'Evan', 'Emmett', 'Micah', 'Ryder', 'Beau', 'Damian',
    'Brayden', 'Gael', 'Rowan', 'Harrison', 'Bryson', 'Sawyer', 'Amir', 'Kingston', 'Jason', 'Giovanni',
    'Vincent', 'Ayden', 'Chase', 'Myles', 'Diego', 'Nathaniel', 'Legend', 'Jonah', 'River', 'Tyler',
    'Cole', 'Braxton', 'George', 'Milo', 'Zachary', 'Ashton', 'Luis', 'Jasper', 'Kaiden', 'Adriel',
    'Gavin', 'Bentley', 'Calvin', 'Zion', 'Juan', 'Maxwell', 'Max', 'Ryker', 'Carlos', 'Emmanuel',
    'Jayce', 'Lorenzo', 'Ivan', 'Jude', 'August', 'Kevin', 'Malachi', 'Elliott', 'Rhett', 'Archer',
    'Karter', 'Arthur', 'Luka', 'Elliot', 'Thiago', 'Brandon', 'Camden', 'Justin', 'Jesus', 'Maddox',
    'King', 'Theo', 'Enzo', 'Matteo', 'Emiliano', 'Dean', 'Hayden', 'Finn', 'Brody', 'Antonio',
    'Abel', 'Alex', 'Tristan', 'Graham', 'Zayden', 'Judah', 'Xander', 'Miguel', 'Atlas', 'Messiah',
    'Barrett', 'Tucker', 'Timothy', 'Alan', 'Edward', 'Leon', 'Dawson', 'Eric', 'Ace', 'Victor',
    'Abraham', 'Nicolas', 'Jesse', 'Charlie', 'Patrick', 'Walker', 'Joel', 'Richard', 'Beckett', 'Blake',
    'Alejandro', 'Avery', 'Grant', 'Peter', 'Oscar', 'Matias', 'Amari', 'Lukas', 'Andres', 'Arlo',
    'Colt', 'Adonis', 'Kyrie', 'Steven', 'Felix', 'Preston', 'Marcus', 'Holden', 'Emilio', 'Remington',
    'Jeremy', 'Kaleb', 'Brantley', 'Bryce', 'Mark', 'Knox', 'Israel', 'Phoenix', 'Kobe', 'Nash',
    'Griffin', 'Caden', 'Kenneth', 'Kyler', 'Hayes', 'Jax', 'Rafael', 'Beckham', 'Javier', 'Maximus',
    'Simon', 'Paul', 'Omar', 'Kaden', 'Kash', 'Lane', 'Bryan', 'Riley', 'Zane', 'Louis',
    'Aidan', 'Paxton', 'Maximiliano', 'Karson', 'Cash', 'Cayden', 'Emerson', 'Tobias', 'Ronan', 'Brian',
    'Dallas', 'Bradley', 'Jorge', 'Walter', 'Josue', 'Khalil', 'Damien', 'Jett', 'Kairo', 'Zander',
    'Andre', 'Cohen', 'Crew', 'Hendrix', 'Colin', 'Chance', 'Malakai', 'Clayton', 'Daxton', 'Malcolm',
    'Lennox', 'Martin', 'Jaden', 'Kayson', 'Bodhi', 'Francisco', 'Cody', 'Erick', 'Kameron', 'Atticus',
    'Dante', 'Jensen', 'Cruz', 'Finley', 'Brady', 'Joaquin', 'Anderson', 'Gunner', 'Muhammad', 'Zayn',
    'Derek', 'Raymond', 'Kyle', 'Angelo', 'Reid', 'Spencer', 'Nico', 'Jaylen', 'Jake', 'Prince',
    'Manuel', 'Ali', 'Gideon', 'Stephen', 'Ellis', 'Orion', 'Rylan', 'Eduardo', 'Mario', 'Rory',
    'Cristian', 'Odin', 'Tanner', 'Julius', 'Callum', 'Sean', 'Kane', 'Ricardo', 'Travis', 'Wade',
    'Warren', 'Fernando', 'Titus', 'Leonel', 'Edwin', 'Cairo', 'Corbin', 'Dakota', 'Ismael', 'Colson',
    'Killian', 'Major', 'Tate', 'Gianni', 'Elian', 'Remy', 'Lawson', 'Niko', 'Nasir', 'Kade',
    'Armani', 'Ezequiel', 'Marshall', 'Hector', 'Desmond', 'Kason', 'Garrett', 'Jared', 'Cyrus', 'Russell',
    'Cesar', 'Tyson', 'Malik', 'Donovan', 'Jaxton', 'Cade', 'Romeo', 'Nehemiah', 'Sergio', 'Iker',
    'Caiden', 'Jay', 'Pablo', 'Devin', 'Jeffrey', 'Otto', 'Kamari', 'Ronin', 'Johnny', 'Clark',
    'Ari', 'Marco', 'Edgar', 'Bowen', 'Jaiden', 'Grady', 'Zayne', 'Sullivan', 'Jayceon', 'Sterling',
    'Andy', 'Conor', 'Raiden', 'Royal', 'Royce', 'Solomon', 'Trevor', 'Winston', 'Emanuel', 'Finnegan',
    'Pedro', 'Luciano', 'Harvey', 'Frank', 'Noel', 'Troy', 'Princeton', 'Johnathan', 'Erik', 'Fabian',
    'Oakley', 'Rhys', 'Porter', 'Hugo', 'Franklin', 'Clark', 'Dakota', 'Reed', 'Curtis', 'Mohamed'
]
size_list = len(name_list)
random_index = random.randint(0, size_list - 1)
target_name = name_list[random_index]
num_tries = len(target_name)
lives = num_tries
intial_answer = []
final_answer = []
all_guessed =[]
    
for item in range (len(target_name)):
    intial_answer.append('*')    
for item in target_name:
    final_answer.append(item.lower())
    
for item in range (num_tries):    
    guessed_alphabet =input('guess an alphabet :')
    if len(guessed_alphabet) > 2:
        print('please enter only one alphabet')
        lives -=1
        print(f'you have {lives} left')
        print(f'{intial_answer}')
       
        if lives == 0:
            print('you lost')
            print(f'{target_name} was the answer')
            break
        else:
            continue
    else:     
        if guessed_alphabet in target_name:
             for item in range(len(target_name)):
                 if guessed_alphabet == final_answer[item]:
                     intial_answer[item]= guessed_alphabet
                     if '_' in final_answer and lives ==0 : 
                         print('you lost')
                         break
                     if '_' in final_answer and lives >0 :
                         print('one went')
                 else:
                      lives-=1
                      print(f'you have {lives} left')
                      if lives == 0:
                            print('you lost')
                            break
                      else:
                          continue
                     

