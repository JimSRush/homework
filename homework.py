#Clone this file from the command line, add a comment and push it back up

#Make a function that takes a string (something in quote marks, like "Hello") and returns the reverse
def reverseString(word):
    #reverse the string here
    #assign it to a variable
    #return it
    return word #placeholder

#Make a function that takes two numbers #(either integers/whole numbers or decimals,
#python doesn't care, it figures out which it's dealing with) and divides the first by the second
#returns the answer
def divide(a, b):
    return 0 # placeholder
    #do something here
    #return the answer here

#Find the first element in the list and return it
def findFirstFriend(listOfFriends):
    return "Jim"#placeholder

#This function takes a string like Frozen Beard and replaces all the vowels with 'v'
#so in this case, calling/invoking the function with the string "FrozenBeard" should return "FrvzvnBvvrd"
#This is a bit extra for experts and may need a bit of thinking about but i bvlvve vn yvv
#hint: if it seems like a lot of code, remember you can just make a new function to do a little bit of work for you and invoke it when you need it
def replaceStuffWithVees(string):
    return string #placeholder

##these are the test functions, functions to test that functions work - yep. meta.
def testReverseString():
    answer = reverseString("hello")
    if answer == "olleh":
        print "The reverse of hello is olleh, sweet"
    else:
        print "Something went wrong, '%s' isn't the reverse of hello" % answer

def testDivide():
    answer = divide(15, 3)
    if answer is 5:
        print "15 divided by 3 is 5, good job"
    else:
        print "Try again, 15 divided by three is not %d" % answer

def testFirstFriend():
    answer = findFirstFriend(["Callum", "Daniel Cuzens", "Jim", "Gus"])
    if answer is "Callum":
        print "callum is number one etc etc"
    else:
        print "%s is not the favourite friend" % answer

def testVees():
    answer = replaceStuffWithVees("callumisfrozenbeard")
    if answer is "Cvllvmvsfrvzvnbvvrd":
        print "Yes, callum IS Frnznznznvbeard or whater"
    else:
        print "%s isn't the answer you're looking for" % answer

testReverseString()
testDivide()
testFirstFriend()
testVees()
