import random
def cpgenerator():
    l=["Rock","Paper","Scissor"]
    return random.choice(l)
def checker(cpd,inp):
    if cpd.lower()==inp.lower():
        return("You have Guessed Correct ")
    else:
        return("Oops you have guessed Wrong ")

print("Welcome to the Game ")
print("If  you like to Start the Game Enter Start ")
command= input("Enter command :")
command.lower()
while command=="start":
    a=cpgenerator()
    b=input("Guess the item :")
    print(a)
    c=checker(a,b)
    print(c)
    n=input("Do you want to continue(Yes/No) : ")
    if n.lower()=="yes":
        command="start"
    else:
        break
print("Thank you!")
print("Hope you enjoyed the Game")