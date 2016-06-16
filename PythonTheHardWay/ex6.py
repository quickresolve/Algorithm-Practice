#Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e


# %r displays raw data of the variable - good for debugging
# %s is good for displaying to variables to the users

# you can use single quotes inside of strings that have double quotes, using either independently is a stylistic choice







#If you want multiple formats in your string to print multiple variables, you need to put them inside () parenthesis separated by , commas
