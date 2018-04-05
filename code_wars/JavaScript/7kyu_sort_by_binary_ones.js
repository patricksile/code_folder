// Problem:Sort by binary ones (7kyu)
/*
"""
Sort by binary ones

Instructions
Output
In this example you need to implement a function that sort a list of integers based on it's binary representation.

The rules are simple:

1 - sort the list based on the amount of 1's in the binary representation of each number.
2 - if two numbers have the same amount of 1's, the shorter string goes first. (ex: "11" goes before "101" when sorting 3 and 5 respectively)
3 - if the amount of 1's is same, lower decimal number goes first. (ex: 21 = "10101" and 25 = "11001", then 21 goes first as is lower)
Examples:

Input: [1,15,5,7,3]
( in binary strings is: ["1", "1111", "101", "111", "11"])
Output: [15, 7, 3, 5, 1]
(and after sortByBinaryOnes is: ["1111", "111", "11", "101", "1"])
*/
// My Solution:

const sortFunction = (a, b) => {
  let count = x => [...x].filter(y => y === '1').length;
  let res = [];
  if(count(a) > count(b)){res.push(a);}
  else if(count(a) === count(b) && a.length < b.length){res.push(a);}
  return res
}

const sortByBinaryOnes = (list) => {
  let binary = list.map(x => (x).toString(2));
  let sortedList = binary.sort((a,b) => sortFunction(a,b))
  return sortedList.reverse().map(x => parseInt(x,2))
}



numbers = [[1,15,5,7,3], [12,30,4,2,9],[12,19,1,0,8,4]]
console.log(sortByBinaryOnes(numbers[2]))
// Other Solutions:

// Solution: By warriors