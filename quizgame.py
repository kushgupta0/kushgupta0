

print("Hello Welcome to my game")
points = 0
playing = input("Would you like to play ? :) ")

if playing != "yes":
    quit()

print("Lets play!!!")

answer1 = input("Who is the quarterback of the Kansas City Chiefs? ")
if answer1!= "Patrick Mahomes" :
    print("You are incorrect")
else: 
    print("You are correct. +1 Point")
    points+=1

answer2 = input("Who won the superbowl last year ? ")
if answer2!= "Kansas City Cheifs":
    print("You are incorrect")
else:
    print("You are correct. +1 Point") 
    points+=1

answer3 = input("Who is the running back for the Dallas Cowboys ? ")
if answer3!= "Tony Pollard":
    print("You are incorrect")
else: 
    print("You are correct. +1 Point")
    points+=1

answer4 = input("What college did CeeDee Lamb attend? ")
if answer4!= "Oklahoma":
    print("You are incorrect")
else: 
    print("You are correct. +1 Point")
    points+=1

answer5 = input("Who was the Cheifs Quarterback before Patrick Mahomes ? ")
if answer5!= "Alex Smith":
    print("You are incorrect")
else:
    print("You are correct. +1 Point") 
    points+=1

if points == 5:
    print("you got all of the questions correct")

if points == 4:
    print("Good job, you missed one but almost got them all correct")

if points == 3:
    print("You got three questions correct. good job")

if points == 2:
    print("You only got two questions correct. Tune into NFL Redzone on sundays!")

if points == 1:
    print("You only got one question correct. Oh no. Watch some youtube highlights.")

if points == 0:
    print("If youre a beginner to football there are many videos for you to learn!")