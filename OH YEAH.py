# more strings and text

# i am setting the shortcuts that will help me to type stories or equations

x = "there are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

# i used the shortcut i made to tell the computer to type something like what i told it to

print(x)
print(y)

# i used the shortcut words/signs to type out a statement easier

print("I said: %r.:" %x)
print("I also said: '%s'" % y)

# i am setting the words i dont want to type out as a smaller easier word to type

hilarious = True
jokeEvaluation = "Isn't that joke so funny?! %r"

w = "This is the left side of..."
e = "a string with a right side"
print(w+e)

# More Printing fun
# I am telling the computer to write these things though the word PRINT

print("Mary had a little lamb.")
print("its fleece was white as %s." % 'snow')
print("and everywhere that mary went.")
# in this line i am telling the computer to say the word/phrase/symbol withing the "" to say it 10 times or multiply it by 10.
print("." * 10)

#below i am setting each end into a letter

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end52 = "e"
end6 = "b"
end7 = "u"
end8 = "r"
end9 = "g"
end10 = "e"
end11 = "r"

# i am now adding all the ends together but now they equal a letter and they all spell out Cheeseburger

print(end1+end2+end3+end4+end5+end52)
print(end6+end7+end8+end9+end10+end11)

# the %r is used to put all values instead of putting %d or %s which would cause an error.
# It is used to tell the computer to write both values.
# the %r prints everything that is in the shortcut even the \n which is not put in with the %s


days = "monday tuesday wednesday thursday friday saturday sunday"
months = "Jan\nfeb\nmarch\napril\nmay\njune\njuly\naug\nsept\nnov\ndec"
print("here are the days: ", days)
print("here are the months: ", months)

print("""when using the triple quotation marks we are 
able to use mas many lines as we need/want.
 it can be 3 or 
 4 lines.""")

print("here are the months: %r " % months)

tabbycat = "\tI'm tabbed in."
persiancat = "i'm split\non a line"
backslashcat = "i'm \\ a \\ cat"
topcat = """ill do a list
\t*cat food
\t*fishies
\t*catnip\n\t*grass"""

print(tabbycat)
print(persiancat)
print(backslashcat)
print(topcat)

# escape seq         what it does
# \\         1    Divides the amount of the symbols by 2
# \'         2    It takes the slash away and puts the ' by its self
# \"         3    It takes the slash away and puts the " by its self
# \a         4
# \b         5
# \f         6
# \n         7
# \n(name)   8
# \r         9
# \t         10
# \XXXXX     11
# \XXXXXXXX  12
# \v         13
# \ooo       14
# \xhh       15


print("1 \\\\\\\\\\\\\\\\\\\\\\\\")
print("2 \'")
print("3 \"")
print("4 \a")


age = input("How old are you?")
height = input("How tall are you?")
print("So, you are %r old and %r tall" %(age, height))


favoriteClass = input("Whats your favorite class?")
favoriteColor = input("Whats your favorite color?")
favoriteAnimal = input("Whats your favorite animal?")
favoriteFood = input("Whats your favorite food?")
print("You like going to %r" % favoriteClass)
print("You like looking at %r" % favoriteColor)
print("You like petting %r" % favoriteAnimal)
print("You like eating %r" % favoriteFood)

# Make a story with the question thingy

FavoriteAnimal = input("Whats your favorite animal?")
FavoriteBird = input("Whats your favorite bird?")
FavoriteFlavorSnowcone = input("Whats your favorite snowcone flavor?")
FavoriteSnake = input("Whats your favorite type of snake?")
FamilySize = input("How many people do you have in your family?")
ScaredOfWhat = input("What animal are you scared of?")
ScaredOfSpiders = input("Do spiders scare you?")

print("One day while you were at the zoo with %r people" % FamilySize)
print("You walk by the %r, your favorite animal, and stay there for a while." % FavoriteAnimal)
print("Next, you walk further down and see a %r, your favorite bird.\n The bird lands on you hand while you feed it." % FavoriteBird)
print("You walk inside the reptile exhibit and find the %r cage. \nYou decide to sit there watching it for a while then you move on." % FavoriteSnake)
print("Right next to the snake exhibit you find the %r cage. \nThis animal has haunted your dreams for many nights." % ScaredOfWhat)
print("""Just when you think your safe your Mom sees a spider crawling on your arm. 
She asks if spiders scare you and you answer %r as you jump and wildly slap the spider off.
Your whole family starts laughing including you.
Everyone goes on finding all their favorite animals.""" % ScaredOfSpiders)
print("""As a treat your parents allow you and your sibling(s) to get a snow cone. 
You get the %r flavor as it is your favorite.""" % FavoriteFlavorSnowcone)
print("""Going home is the worst part of the trip but you had fun, even with the jump scares.""")