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
persiancat = " i'm split\non a line"
backslashcat = "i'm \\ a \\ cat"
topcat = """ill do a list
\t*cat food
\t*fishies
\t*catnip\n\t*grass"""

print(tabbycat)
print(persiancat)
print(backslashcat)
print(topcat)

