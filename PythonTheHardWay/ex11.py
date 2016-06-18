print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#We put a , (comma) at the end of each print line. This is so print doesn't end the line with a newline character and go to the next line.

# raw_input() takes input in as a string
# encapsulate that in int() to convert to a number when necessary - int(raw_input())

#The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.

#if a string prints out with a u in front of it, it is telling you that the string is in unicode. Use %s instead of %r to get them to print normally.
