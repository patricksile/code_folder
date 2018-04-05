# Problem:Roman Numerals Decoder (4kyu)
"""
Instructions
"""
# My Solution:
def solution(roman):
	romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	units = [1000,  500,  100,  50,  10,  5,  1]
	idx = lambda x: romans.index(roman[x])
	number, i = (0,0)
	while i < len(romans):
		while len(roman):
			if i != len(roman) - 1 and idx(i) > idx(i+1): number -= units[idx(i)]
			else: number += units[idx(i)]
			roman = roman[i+1:]
		i += 1
	return number

print(solution('DCCCIX'))
# Other Solutions:

# Solution: By warriors

# function solution(roman){
# 	let romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
# 	let units = [1000,  500,  100,  50,  10,  5,  1]
# 	let idx = x => romans.indexOf(roman[x]);
# 	let number = 0; let i = 0
# 	while(i < romans.length){
# 		while(roman[i]){

# 			if(idx(i) > idx(i+1) && roman[i + 1] != undefined){number -= units[idx(i)];}

# 			else{number += units[idx(i)];}

# 			roman = roman.slice(i + 1, roman.length);
# 		}
# 		++i
# 	}
# 	return number;
# }
