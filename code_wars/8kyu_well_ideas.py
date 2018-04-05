# Problem: Well of Ideas_Easy version(8kyu)
"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
"""
# My Solution:

def well(x):
    good = x.count('good')
    if good == 1 or good == 2:
        return 'Publish!'
    elif good > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'

# Other Solutions:
# Solution 1: By daddepledge, zShark

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'

# Solution 2: By lechevalier

def well(a):c=a.count('good');return['Fail!','Publish!','I smell a series!'][(c>0)+(c>2)]

# Solution 3: By maipatana

def well(x):
    good = x.count('good')
    print (good)
    if good == 0:
        return 'Fail!'
    elif good > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'
