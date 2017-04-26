#Clone this file from the command line, add a comment and push it back up



#Make a function that takes a string (something in quote marks, like "Hello") and returns the reverse
def reverseString(word):
    #reverse the string here
    #assign it to a variable
    #return it
    return word

#Make a function that takes two numbers #(either integers/whole numbers or decimals,
#python doesn't care, it figures out which it's dealing with) and divides the first by the second
#returns the answer
def divide(a, b):
    return 0
    #do something here
    #return the answer here

#Find the first element in the list and return it
def findFirstFriend(listOfFriends):
    return "Jim"

##these are the test functions, functions to test that functions work - yep. meta.
def testReverseString():
    answer = reverseString("hello")
    if answer is "olleh":
        print "The reverse of hello is olleh"
    else:
        print "Something went wrong, '%s' isn't the reverse of hello" % answer

def testDivide():
    answer = divide(15, 3)
    if answer is 5:
        print "15 divided by 3 is 5"
    else:
        print "Try again, 15 divided by three is not %d" % answer

def testFirstFriend():
    answer = findFirstFriend(["Callum", "Daniel Cuzens", "Jim", "Gus"])
    if answer is "Callum":
        print "callum is number one etc etc"
    else:
        print "%s is not the favourite friend" % answer

testReverseString()
testDivide()
testFirstFriend()
