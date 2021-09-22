#Osama Hussain
#This is my week 2 assignment

#Object 1
subway = {
    "train_name": "A",
	"terminal": "Inwood_207_st",
	"destination": "168_st",
	"stop_duration": 2,
	"speed": 200,
	"fuel_type": "electric",
	"delay": false,
	"carriage": "3016",
	"capacity": 56,
	"passengers": 35,
	"no_mask": 4,
	"seat_availability": "Low"
}

#This is the MadLib activity
# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
favoriteBorough = input("Enter your favorite borough in NYC: ")
favoriteActor = input("What is your favorite actor or actress?: ")
favoriteSinger = input("Name your favorite sinder: ")
favoriteNeighbourhood = input("Enter your favorite neighbourhood in NYC: ")
favoriteStreet = input("Which street do you like the best: ")
favoriteFastFood = input("Your goto fastfood chain: ")
food = input("What food do you love making? ")
car = input("What car do you wanna drive when you're rich?: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "Yeah, I'm out that" + " " + favoriteBorough + " " + ", now I'm down in Tribeca" \
"Right next to" + " " + favoriteActor + " " + ", but I'll be hood forever" \
"I'm the new" + " " + favoriteSinger + " " + ", and since I made it here" \
"I can make it anywhere, yeah, they love me everywhere" \
"I used to cop in" + " " + favoriteNeighbourhood + " " + ", hola, my Dominicanos" \
"Right there up on" + " " + favoriteStreet + " " + ", brought me back to that" + " "
+ favoriteFastFood + "Took it to my stash spot, 560 State Street" \
"Catch me in the kitchen, like a Simmons whippin'" + " " \
+ food + "Cruisin' down 8th Street, off-white" + " " + car \

# finally we print the story
print (story)
