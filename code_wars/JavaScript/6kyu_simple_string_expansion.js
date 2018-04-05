/*
Mini-Problem: 6kyu Simple String Extension
Consider the following expansion:
solve("3(ab)") = "ababab" -- "ab" repeats 3 times
solve("2(a3(b))" = "abbbabbb" -- "a3(b)" == "abbb" repeats twice.
Given a string, return the expansion of that string.
Input will consist of only lowercase letters and numbers in valid parenthesis. There will be no letters or numbers after the last closing parenthesis.
More examples in test cases.
Good luck!
ALGORITHMS
*/

function solve (str) {
    
    
    return undefined;
}
// Test Zone
aString = "a3(b)"
console.log(solve(aString)) // => "abbb"


var str = "a(3a4(rte(4y)))".replace(')','');
var temp_str = ""; 
var previous_char = str.slice(-1); // initialized with the last character, and will be reseted on purpose;

for (let i = str.length - 1; i >= 0; i-- ) {
    if ( str[i] !== '(' && !Number(str[i]) ) { // not '(' and not a number
        temp_str  = str[i] + temp_str;
        previous_char = str[i];
    }
    else if ( !!Number(str[i]) && previous_char !== '(') { // a number and previous_char not '('
        temp_str = previous_char.repeat(str[i] - 1) + temp_str
    } // check if it is a number and previous character is not '(' multiply with the only character at the right
    else if ( parseInt(str[i]) && previous_char === '(') {
        temp_str = temp_str.repeat(str[i]);
        previous_char = str[i]; // resetting to actual char
    }// check if it is a number and 'var previous_char' is '(' multiply with all the most right characters 'var multiplied_chars'
    console.log(str[i]);
}

 
// describe("Basic tests", function () {
//     Test.assertEquals(solve("3(ab)"), "ababab");
//     Test.assertEquals(solve("2(a3(b))"), "abbbabbb");
//     Test.assertEquals(solve("3(b(2(c)))"), "bccbccbcc");
//     Test.assertEquals(solve("k(a3(b(a2(c))))"), "kabaccbaccbacc");
// });
