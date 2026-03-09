import random
import math
import time

def create_question(score):
    expression = ""
    answer = 0
    
    # decide addition min and max possible values
    add_min = score // 2
    add_max = 2 * score + 5
    
    # decide operands
    add_1 = random.randint(add_min, add_max)
    add_2 = random.randint(add_min, add_max)
    
    answer = add_1 + add_2
    expression = str(add_1) + " + " + str(add_2)
    
    return expression, answer

#### Main game ####

# Start screen

print("Welcome to the math game!")
print("Try and answer as much questions as you can!")
print("You have 10 seconds per question, so be quick!")
input("Input anything to start: ")

# Initialisations
score = 0
fail = False
expression = ""
answer = 0
start_time = 0.0

# Main game loop
while not fail:
    
    start_time = time.monotonic()
    
    print("\n=========================================\n")
    print(f"Current score: {score}\n")
    
    # Generate question, difficulty is based on points
    expression, answer = create_question(score) 
    
    # Ask the question
    print(f"What is {expression} ?")
    response = input("Your answer: ")
    
    # Check the user's answer
    if (int(response) == answer):
        print("\nCorrect!")
        score += 1 # why not have them have an extra point even if they timeout lol
        
        # Were they too late?
        time_elapsed = time.monotonic() - start_time
        if time_elapsed > 10:
            late_time = round(time_elapsed - 10, 2)
            print(f"But you took {late_time} seconds too long...")
            fail = True
    else:
        print(f"\nIncorrect... the correct answer was {answer} !")
        fail = True

print(f"You finished with {score} score!")