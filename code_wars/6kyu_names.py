# Problem:
"""

"""
# My Solution:
def likes(n):
    ln = len(n)
    if ln <= 1:
        return '{} likes this'.format(n[0] if ln else 'no one')
    if ln == 2:
        return '{} and {} like this'.format(n[0], n[1])
    if ln == 3:
        return '{}, {} and {} like this'.format(n[0], n[1], n[2])
    if ln > 3:
        return '{}, {} and {} others like this'.format(n[0], n[1],len(n[2:]))
# Other Solutions:
# Solution 1: By
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
