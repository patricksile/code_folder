// Problem:Roman Numerals Encoder (4kyu)
/*
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000); // should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
*/

// My Solution:
function solution(number){
  let romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  let units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  let roman_str = ''; let i = 0
  while(i < romans.length){
    while(number >= units[i]){
      roman_str += romans[i];
      number -= units[i];
    }
    ++i
  }
  return roman_str;
}
console.log(solution(254))
// Other Solutions:

// Solution: By warriors