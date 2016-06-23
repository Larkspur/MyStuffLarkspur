print "This is a game of survival."
print

character = raw_input("Is your character a girl or a boy?")
character = character.lower()

if character == "boy" or character == "girl":
    print
    print "Your character is a %s." %(character)
    name = raw_input("What is your character's name?")
else:
    print
    print "Please select girl or boy."
    
if len(name) != 0 and name.isalpha():
    capitalized = name[:1]
    capitalized = capitalized.upper()
    name = name[1:]
    name = capitalized + name
    print
    print "Your character's name is %s." %(name)
elif len(name) != 0:
    print
    print "Please enter a name for your character."
else:
    print
    print "Please enter a name that consists of only the English alphabet."
    
print
print "You are in the middle of a dense pine forest. Your only shelter is a small"
print "dirt cave. You also have several items, which can be used for different"
print "purposes. Without any protection, you will be hunted by fierce wild animals."
print "Without any food, you will die in two days. Without any drink, you will die"
print "in one day. Without any rest, you can only survive for 18 hours."
    
