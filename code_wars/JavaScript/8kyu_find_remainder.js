// Problem: Find the remainder (8kyu)
/*
Write a function that accepts two arguments and returns the remainder after dividing the larger number by the smaller number. Division by zero should return NaN (in C#, throw a new DivideByZeroException instead). Arguments will both be integers.
*/
// My Solution:

function remainder(a, b){
  // Divide the larger argument by the smaller argument and return the remainder
  return Math.max(a, b) % Math.min(a, b);
}

// Other Solutions:
// Solution 1: By OverZealous, pepkin88, JulianNicholls, mattbache, vmcnabb,

function remainder(a, b){
  return a > b ? a % b : b % a;
}

// Solution 2: By lipenco, glu10, Commy

function remainder(a, b){
  // Divide the larger argument by the smaller argument and return the remainder
  var min = Math.min(a,b);
  var max = Math.max(a,b);

  return min ? max % min : NaN;
}
