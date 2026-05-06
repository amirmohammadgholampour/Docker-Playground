import random 

link = "https://github.com/amirmohammadgholampour/"

print("================================================================")
print("Welcome to this game!🎮")
print("My name is AmirMohammad.🙃\nIf possible, follow my Github!🤗🤗")
print(f"My github link: {link}")
print("================================================================\n\n")

try:
    user = int(input("Do you want to continue? Yes: 1, No: 0\nHa? "))
except EOFError: 
    print("Message not received")

if user == 1: 
    system_number = random.randint(1, 10) 
    score = 5

    while True: 
        try: 
            user_number = int(input("\nEnter your guess: ")) 
        except EOFError: 
            print("Message not recieved")
        
        if user_number == system_number: 
            print("Winner!🎉🎉") 
            print(f"Your score is {score}") 
            break
        
        elif user_number > system_number: 
            score -= 1 
            print("Go Down!🤨🤨")
            print(f"Score: {score}") 
        
        elif user_number < system_number: 
            score -= 1 
            print("Go Up!😑😑")
            print(f"Score: {score}") 
        
        if score == 0:
            print("\nLooser!😐😐") 
            print(f"Score: {score}") 
            break
else:
    print("Ok, Fuck you!🖕")