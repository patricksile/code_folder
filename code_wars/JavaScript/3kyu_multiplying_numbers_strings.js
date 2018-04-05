// Problem:Multiplying numbers as strings (3kyu)
/*
Multiplying numbers as strings

Instructions
Output
This is the first part. You can solve the second part here when you are done with this. Multiply two numbers! Simple!

The arguments are passed as strings.
The numbers may be way very large
Answer should be returned as a string
The returned "number" should not start with zeros e.g. 0123 is invalid
Note: 100 randomly generated tests!

*/
// My Solution:

function multiply(a,b){

	let temp = '';
	let lb = b.length; let la = a.length;
	let over = '0'; let line = ''; let lines = [];

	for(let i = lb - 1; i >= 0; i--){

		for(let j = la - 1; j >= 0; j--){

			temp = eval(b[i] + '*' + a[j] + '+' + over) + ''

			if(temp.length == 2){

				line += temp[1]; 
				over = temp[0]
			}

			else{

				line += temp; 
				over = '0';
			}

			temp = '';

			if(j === 0){

				lines.push('0'.repeat(b.slice(i + 1, lb).length) + line + over + '0'.repeat(b.slice(0, i).length)); 

				line = ''; over = '0';
			}

		}
	}

	let x = 0; let pretemp = 0; let pre_res = ''; let carry = 0

	for(let k = 0; k < lines[0].length; k++){

		for(let l = 0; l < lines.length; l++){

			pretemp += eval(lines[l][k]); // sum of each columns in lines

			if(l === lines.length - 1){

				pretemp += carry; carry = 0;
				let pre_str = pretemp + '';

				if((pre_str).length > 1){

					pre_res += (pre_str)[pre_str.length - 1]; 
					carry = +(pre_str).slice(0, pre_str.length - 1); pretemp = 0;
				}
				else{

					pre_res += pretemp; pretemp = 0;
				}
			}

		}
	}

	let res = Array.from(pre_res).reverse().join('').replace(/^0+/, '');
	return res != '' ? res : '0'
}

function multiply(a,b){
	let temp = '';
	let lb = b.length; let la = a.length;
	let over = '0'; let line = ''; let lines = [];
	for(let i = lb - 1; i >= 0; i--){
		for(let j = la - 1; j >= 0; j--){
			temp = eval(b[i] + '*' + a[j] + '+' + over) + ''
			if(temp.length == 2){line += temp[1]; over = temp[0]}
			else{line += temp; over = '0';}
			temp = '';
			if(j === 0){
				lines.push('0'.repeat(b.slice(i + 1, lb).length) + line + over + '0'.repeat(b.slice(0, i).length)); 
				line = ''; over = '0';
			}
		}
	}
	let x = 0; let pretemp = 0; let pre_res = ''; let carry = 0
	for(let k = 0; k < lines[0].length; k++){
		for(let l = 0; l < lines.length; l++){
			pretemp += eval(lines[l][k]); 
			if(l === lines.length - 1){
				pretemp += carry; carry = 0;
				let pre_str = pretemp + '';
				if((pre_str).length > 1){
					pre_res += (pre_str)[pre_str.length - 1]; 
					carry = +(pre_str).slice(0, pre_str.length - 1); pretemp = 0;
				}
				else{pre_res += pretemp; pretemp = 0;}
			}
		}
	}
	let res = Array.from(pre_res).reverse().join('').replace(/^0+/, '');
	return res != '' ? res : '0'
}

a = '58608473622772837728372827'
b = '7586374672263726736374'
// c = '444625839871840164201221331016205566214109298'
// expected = '444625839871840560024489175424316205566214109298'
// expectet = '444625839871840560024489175424316205566214109298'
// ll = 48
// console.log(expected.length)
console.log(multiply(a,b))

// x = '0'.repeat(a.slice(0,2).length) + '123' + '0'.repeat(a.slice(2 + 1,4))
// Other Solutions:

// Solution: By warriors alex.budiakov, Pipka94, user2630808

function multiply(a, b) {
  var aa = a.split('').reverse();
  var bb = b.split('').reverse();

  var stack = [];

  for (var i = 0; i < aa.length; i++) {
    for (var j = 0; j < bb.length; j++) {
      var m = aa[i] * bb[j];
      stack[i + j] = (stack[i + j]) ? stack[i + j] + m : m;
    }
  }

  for (var i = 0; i < stack.length; i++) {
    var num = stack[i] % 10;
    var move = Math.floor(stack[i] / 10);
    stack[i] = num;

    if (stack[i + 1])
      stack[i + 1] += move;
    else if (move != 0)
      stack[i + 1] = move;
  }


  return stack.reverse().join('').replace(/^(0(?!$))+/, "");
}

// Solution: By desfero

function multiply(a, b) {
  return a.split('').reduceRight((p, a, i) => 
      b.split('').reduceRight((p, b, j) => {
        const mul = (a - '0') * (b - '0');
        const p1 = i + j;
        const p2 = p1 + 1;
        const sum = mul + valOrZero(p[p2]);
                
        p[p1] = valOrZero(p[p1]) + Math.floor(sum / 10);
        p[p2] = sum % 10;
                
        return p;
      }, p)
    , []).join('').replace(/^0+(?=\d)/, '');
  }

function valOrZero(v) {
  return v || 0;
}

// Solution: By axelboc

/**
 * Multiply two very big numbers passed as string.
 * @param {string} rawA
 * @param {string} rawB
 * @return {string}
 */
function multiply(rawA, rawB) {
  const a = prepareTerm(rawA);
  const b = prepareTerm(rawB);
  
  return formatResult(carryValues(computeSubProducts(a, b)));
}

/**
 * Convert a string to an array of digits, then reverse its order
 * so the least significant digit comes first (to simplify looping).
 * e.g. '13' => [3, 1]
 * @param {string} num
 * @param {array<number>}
 */
function prepareTerm(num) {
  return num.split('').map(digit => parseInt(digit, 10)).reverse();
}

/**
 * Compute the sums of the subproducts of the two terms.
 * e.g. [3, 2] * [5, 4] => [(3 * 5), (3 * 4) + (2 * 5), (2 * 4)] => [15, 22, 8]
 * @param {array<number>} a
 * @param {array<number>} b
 * @return {array<number>}
 */
function computeSubProducts(a, b) {
  const products = [];
  
  for (let i = 0; i < a.length; i++) {
    let da = a[i];
  
    for (let j = 0; j < b.length; j++) {
      let db = b[j];
    
      let k = i + j;
      if (k >= products.length) products.push(0);
      
      products[k] += da * db;
    }
  }
  
  return products;
}

/**
 * Turn the array of sub-products into an array of digits, carrying the values over.
 * Note that the last item in the returned array may be a number rather than a single digit.
 * e.g. [15, 22, 8] => [5, (22 + 1), 8] => [5, 3, (8 + 2)] => [5, 3, 0, 1]
 * @param {array<number>} products
 * return {array<number>}
 */
function carryValues(products) {
  return products.reduce((digits, prod, i) => {
    // Push the current digit
    digits.push(prod % 10);
    
    // Carry the value
    const val = Math.floor(prod / 10);
    if (i + 1 < products.length) {
      products[i + 1] += val;
    } else {
      digits.push(val);
    }
    
    return digits;
  }, []);
}

/**
 * Turn the digits array into the expected result string
 * making sure to strip any leading zeros.
 * e.g. [5, 3, 0, 1] => '1035'
 * @param {array<number>} digits
 * @return {string}
 */
function formatResult(digits) {
  // Reverse digits array and turn it into a string
  const result = digits.reverse().map(d => d.toString()).join('');
  
  // Remove leading zeros
  return result.replace(/^0*(\d+)$/, '$1');
}

// Solution: By marians

function multiply(a, b) {
  if(a=='0' || b=='0') return '0';
  let i = 0;
  let j = a.length -1;
  let nbZeros = 0; 
  while(a[i] == '0' && i <= j) i ++;
  
  // ignore zeros from begining
  if( i == j + 1) return '0';
  // Count zeros from end
  while(a[j] == '0') {
    j--;
    nbZeros++;
  }
  var arrA = [];
  
  // insert in front
  for(; i <= j; i++) arrA.unshift(a[i]);
  i = 0;
  j = b.length -1;
  while(b[i] == '0' && i <= j) i++;
  if(i == j + 1) return '0';
  while(b[j] == '0') {
    j--;
    nbZeros++;
  }
  var arrB = [];
  for(; i <= j; i++) arrB.unshift(b[i]);
  
  var res= Array.from(new Array(arrA.length + arrB.length), () => 0);
  arrB.unshift(0);
  arrA.unshift(0);
  for(let i = 1; i < arrB.length; i++) {
    for(let j = 1; j < arrA.length; j++) {
      res[i + j - 1] += arrB[i] * arrA[j];
    }
  }
  //console.log(res)
  let t=0;
  let number ='';
  for(let i = 1; i < res.length; i++) {
    let nr = res[i] + t;
    number = nr % 10 + number;
    t = Math.floor(nr / 10);
  }
  if(t > 0) {
    number = t + number;
  }
  if(nbZeros){
    var text = Array.from(new Array(nbZeros), () => 0).join('');
    number += text;
  }
  return number;
}



let x = 5;

console.log(toString())
