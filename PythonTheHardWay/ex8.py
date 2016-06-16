#Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
#this line substitutes the numnbers 1-4 in place of the %rs

print formatter % ("one", "two", "three", "four")
#this line substitutes the strings one - four in place of the %rs

print formatter % (True, False, False, True)
#this line substitutes the boolean values in place of the %rs

print formatter % (formatter, formatter, formatter, formatter)
#this line substitutes the value of the variable formatter in place of each %r

print formatter % ("I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")
#this line substitutes the strings in the parenthesis in place of the %rs.

# %r will give yu the raw programmers version of a variable, aka the "representation"
# Use %s if you want to use non-ASCII characters, otherwise it will print out weird symbols
