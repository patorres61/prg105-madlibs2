#Accept User Input Variables


print("I need you to enter some words for this Madlib. There will be prompts for eight variables. ")
print("If you can't come up with something, just hit enter and I will supply a variable for you.")


print("Enter an adjective that descibes how one behaves, for example, timid, aggressive, loving, angry, etc.: ") #prompt for input of an adjective
adjective = raw_input()
if adjective == "":
    adjective = "aggressive"

print("Enter a person's job, e.g., policeman: ") #prompt for input of a person's job
job = raw_input()
if job == "":
    job = "librarian"

print("Enter a type of insect: ") #prompt for input of an insect
insect = raw_input()
if insect == "":
    insect = "cockroach"

print("Enter a type of flying animal: ") #prompt for a flying animal
flyingAnimal = raw_input()
if flyingAnimal == "":
    flyingAnimal = "bat"

print("Enter a type of pet: ") #prompt for a pet
pet = raw_input()
if pet == "":
    pet = "chinchilla"

print("Enter a regular action word that can end with -ed, e.g., kiss, but don't add the -ed: ") #prompt for an action
action = raw_input()
if action == "":
    action = "lick"

print("Enter a very large animal: ") #prompt for a very large animal
largeAnimal = raw_input()
if largeAnimal == "":
    largeAnimal = "whale"

print("Enter another action word that can end with -ed, e.g., walk: ") #prompt for another action
action2 = raw_input()
if action2 == "":
    action2 = "explode"

#Load remaining variables
animal = "porcupine"
arachnid = "scorpion"
pet2 = "pot-belly pig"

print("\nGood Job! That was a lot of variables!")

print("\nHere is your Madlib!")

#poem
print("\nMadlib: There was a(n) " + adjective + " " + job + " who " + action + "ed a " + insect + "\n")
print("There was a(n)"
      " " + adjective + " " + job + " who " + action + "ed a " + insect + ",")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + arachnid + ",")
print("That wriggled and wiggled and tickled inside her;\n")

print("She " + action + "ed the " + arachnid + " to catch the " + insect + ",")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + flyingAnimal + ";")
print("How absurd to " + action + " a " + flyingAnimal + "!\n")

print("She " + action + "ed the " + flyingAnimal + " to catch the " + arachnid + ",")
print("She " + action + "ed the " + arachnid + " to catch the " + insect + ";")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + pet + ";")
print("Fancy that to " + action + " a " + pet + "!\n")

print("She " + action + "ed the " + pet + " to catch the " + flyingAnimal + ",")
print("She " + action + "ed the " + flyingAnimal + " to catch the " + arachnid + ",")
print("She " + action + "ed the " + arachnid + " to catch the " + insect + ";")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + pet2 + ";")
print("What a hog to " + action + " a " + pet2 + "!\n")

print("She " + action + "ed the " + pet2 + " to catch the " + pet + ",")
print("She " + action + "ed the " + pet + " to catch the " + flyingAnimal + ",")
print("She " + action + "ed the " + flyingAnimal + " to catch the " + arachnid + ",")
print("She " + action + "ed the " + arachnid + " to catch the " + insect + ";")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + animal + ";")
print("I don't know how she " + action + "ed a " + animal + "!\n")

print("She " + action + "ed the " + animal + " to catch the " + pet2 + ",")
print("She " + action + "ed the " + pet2 + " to catch the " + pet + ",")
print("She " + action + "ed the " + pet + " to catch the " + flyingAnimal + ",")
print("She " + action + "ed the " + flyingAnimal + " to catch the " + arachnid + ",")
print("She " + action + "ed the " + arachnid + " to catch the " + insect + ";")
print("I don't know why she " + action + "ed a " + insect + " - perhaps she'll " + action2 + "!\n")

print("There was a(n) " + adjective + " " + job + " who " + action + "ed a " + largeAnimal + "...;")
print("...She's dead, of course!")
