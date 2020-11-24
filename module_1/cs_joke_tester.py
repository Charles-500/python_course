# this allows my program to sleep for as long as I need it to
import time 


print("Hello. Welcome to the Joke tester. My name is Wally") # conversational prompt
time.sleep(2) # sleeping for x seconds

name = input("Tell me your name: ")
for i in range(2):
    print("Processing...")
    time.sleep(1)

print(f"Welcome, {name}. And thanks for playing today")
time.sleep(3)

print("Ok, so first up, I need your help") # conversational prompt
time.sleep(2) # sleeping for x seconds
print("I've lost my watch")
time.sleep(2) # sleeping for x seconds
print("Can you tell me if it's morning, afternoon or night?") 
answer0 = input("Let me know here: ")
if answer0.lower() == "morning":
    print("Well good morning to you")
elif answer0.lower() == "afternoon":
    print("Thanks. This day has really flown by")
elif answer0.lower() == "night":
    print("Ok, no wonder i'm feeling sleepy!")

time.sleep(2) 
    
print(f"right {name}, I have two jokes to test your skills")    
time.sleep(2)    
    
print("lets get started with joke 1")    
   
wins = 0

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Joke 1! " + "-" * 30)
print("-" * 70)

print("where do beef burgers go to dance?")    
answer2 = input("Please type your answer here: ") 

if answer2.lower() == "the meatball":
        print(f"you are correct, great start {name}!")
        wins += 1
else:
   print("Incorrect. They go to the meatball!")

time.sleep(1)  
print("On to your second joke!")

time.sleep(2) 
print("-" * 70)
print("-" * 30 + " Joke 2! " + "-" * 30)
print("-" * 70)


print("what did Mr and Mrs Hamburger name their daughter?")    
answer3 = input("Please type your answer here: ")

if answer3.lower() == "patty":
    print("that is right, you got it!")
    wins += 1
else:
    print("that's not right. The answer is Patty of course!")
      
time.sleep(2)

print("You got {} correct out of two".format(wins))

if wins == 2:
    print(f"Well done {name}. You got two right, that's a perfect score. Straight to the top of the class!")

elif wins == 1:
    print(f"You got fifty percent {name} so we'll give you a pass mark. Solid effort")      
elif wins == 0:
    print(f"Oh no {name}, you scored a duck egg!! Thanks for playing")

time.sleep(2)
print(f"So that's game over {name}, see you next time")

