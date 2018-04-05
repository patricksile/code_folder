// Problem:
/*
Write the function squareArea(A) (square_area($A) in PHP) that finds the area of the red square when you have the length of the line A.

alt text

Use π = Math.PI (M_PI in PHP)
Round to two decimals.
*/
// My Solution:
function squareArea(A){
  return parseFloat((Math.pow(2 * A / Math.PI , 2)).toFixed(2))
}
// Other Solutions:
// Solution 1: By AntEco, PaulBryan_dev, Hayley1999, The1BRIAN

function squareArea(A){
  var circum = 4 * A;
  var radius = circum / (2 * Math.PI);
  var area = Math.pow(radius, 2);
  return Math.round(area*100)/100
}

// Solution 2: By Mikhail158

squareArea = A => +Math.pow((2 * A / 3.1416), 2).toFixed(2);

// Solution 3: By WompWomp, natashk, Krinjih, petey283, jarvisniu, Ulisses

function squareArea(A){
  return Math.round(Math.pow(A*2/Math.PI,2) * 100) /100
}
