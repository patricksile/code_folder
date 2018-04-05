# Problem:
"""
Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
"""
# My Solution:

def reverseWords(str):
    # I unecessaraly used teh for it is not needed
    return " ".join(w for w in str.split()[::-1])
    # return " ".join(str.split()[::-1])

# Other Solutions:

# Solution 1: By jhoffner, yammesicka, SwingKing, BrianDGLS92, laerianna
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


# Solution 2: By jolaf, RM84, michal_niklas, daddepledge

def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))
