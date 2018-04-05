// Problem:Pascal Triangle (4kyu)
/*
Pascal's Triangle


Pascal's Triangle

Wikipedia article on Pascal's Triangle: http://en.wikipedia.org/wiki/Pascal's_triangle

Write a function that, given a depth (n), returns a single-dimensional array representing Pascal's Triangle to the n-th level.

For example:

pascalsTriangle(4) == [1,1,1,1,2,1,1,3,3,1]
*/
// My Solution PatrickSile:

function pascalsTriangle(n) {

	var pasTriDict = {'1':[1],'2':[1,1]}; // Initial 2 rows of Pascal Triangle.
	var temp = []; // Temporary rows
	if(n > 2){
		let x = 3; // Setting x to 3 to go backward and increment.
		while(x <= n){
			for(let i = 0; i < x-2; i++){
				temp.push(pasTriDict[String(x-1)][i] + pasTriDict[String(x-1)][i+1])
			}
			temp.push(1);temp.unshift(1);
			pasTriDict[String(x)] = temp;
			temp = []; // reset temporary value
			++x;
		}
	}
	let y = 1; var pasTri = [];
	while(y <= n){
		pasTri = pasTri.concat(pasTriDict[String(y)]);
		++y;
	}
	return pasTri;
}

console.log(pascalsTriangle(6))
// Other Solutions:

// Solution: By warriorsdanielmcq, mrlinn69, suva, testtest123, Sagobunny, jwong483 (plus 12 more warriors)

function pascalsTriangle(n) {
  var pascal = [];
  var idx = 0;
  
  for ( var i = 0; i < n; i++ ) {
    idx = pascal.length - i;
    for ( var j = 0; j < i+1; j++ ) {
      if ( j === 0 || j === i ) {
        pascal.push(1);
      } else {
        pascal.push( pascal[ idx+j ] + pascal[ idx+j-1 ] );
      }
    }
  }
  
  return pascal;
}


// Solution: Bytjwudi, matrixorz, Ulisses

function pascalsTriangle(n) {
  if (n === 1) {
    return [1];
  }
  var prev = pascalsTriangle(n - 1), len = prev.length;
  prev.push(1);
  for (var i = len - n + 1; i < len - 1; i ++) {
    prev.push(prev[i] + prev[i + 1]);
  }
  prev.push(1);
  return prev;
}

// Solution: By afonsomatos

function f(n) {
  if(n<2) return 1;
  return n * f(n - 1);
}

function pascalsTriangle(n) {
 var r = [];
 for(var i = 0; i < n; i++)
   for(var e = 0; e <= i; e++)
     r.push( Math.round(f(i)/(f(e)*f(i - e))));
 return r;
}


// Solution: By maldan_rv

function pascalsTriangle(n) {
    for (var i = 0, ret = []; i < n; i++) for (var j = 0; j <= i; j++) ret.push(row(i, j));
    return ret;
}
function row(n, k) { return (k == 0 || n == k) ?1 :row(n - 1, k - 1) + row(n - 1, k); }


