# Problem: Largest Elements (7kyu)
"""
Write a program that outputs the top `n` elements from a list.

Example:

largest(2, [7,5,5,4,3,2,1]) => [6,7]
"""
# My Solution:

def largest(n,xs):
  """Find the n highest elements in a list"""
  return sorted(xs)[-n:]

print(largest(2, [7,5,6,4,3,2,1]))