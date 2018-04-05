// Problem:Roman Numerals Decoder (4kyu)
/*
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI'); // should return 21
Courtesy of rosettacode.org
*/
// My Solution:
function solution(roman){
	let romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	let units = [1000,  500,  100,  50,  10,  5,  1]
	let idx = x => romans.indexOf(roman[x]);
	let number = 0; let i = 0
	while(i < romans.length){
		while(roman[i]){

			if(idx(i) > idx(i+1) && roman[i + 1] != undefined){number -= units[idx(i)];}

			else{number += units[idx(i)];}

			roman = roman.slice(i + 1, roman.length);
		}
		++i
	}
	return number;
}


console.log(solution('MMMCMLXXVIII')) 
// Other Solutions:

// Solution: By warriors

// solution = (roman) ->
// 	romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
// 	units = [1000,  500,  100,  50,  10,  5,  1]
// 	idx = (x) -> romans.indexOf(roman[x])
//   	number = 0
//   	i = 0
//   	while i < romans.length
//     	while roman[i]
//       	if idx(i) > idx(i + 1) and roman[i + 1] != undefined
//         	number -= units[idx(i)]
//       	else
//         	number += units[idx(i)]
//       	roman = roman.slice(i + 1, roman.length)
//     	++i
//   	number