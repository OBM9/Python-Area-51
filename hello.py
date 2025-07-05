print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play!") 
score = 0   

answer = input("What does gpu stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
    score = score + 1
else:
    print("Incorrect!")
    score -= 1
    score + score - 1
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")

