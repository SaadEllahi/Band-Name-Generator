#Hello User
#What is your name?
#Welcome to your Band Name Generator <name>
#Lets Get started! What is the name of the city you grew up in?
#<cityname> is a great place!
#What is the name of your pet?
#<petname> sound like lovely name <name>!
#Thanks for the information, this makes your band name <cityname> + <petname>

print("Hello User")
name = input("What is your name?")
print("Welcome to your Band Name Generator " + name)
city = input("Lets Get started! What is the name of the city you grew up in? ")
print("I heard " + city + " is a great place!")
pet = input("What is your pet's name? ")
print(pet + " sounds like a lovely name " + name)
print("Thanks for providing the information, your band name is " + city + " " + pet)