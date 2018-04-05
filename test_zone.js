// var noRepeat = list => [... new Set(list)].reduce((a,b)=>a+b) * 2 - list.reduce((x,y)=>x+y);
function makeNegative(int) {
	return int < 0 ? int : -int;
}
var makeNegative = int => int < 0 ? int : -int;
// Test Zone
var digit = 96669;
console.log(makeNegative( digit )); // -> 6