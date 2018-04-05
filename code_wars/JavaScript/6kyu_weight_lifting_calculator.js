// Problem:Weight Lifting Calculator (6kyu)
/*
As a keen weightlifter you are constantly working out how much weight to put on each end of the bar in order to make it even.

You do this by taking your total weight w, which is always a multiple of 2.5, and dividing it by 2 and then working out which weights to put on each end of the bar based on those available to you. Don't forget that the bar already weighs 20kg and shouldn't factor into your final calculation.

Your gym is well stocked, you have an unlimited number of each of these weights:

20kg
15kg
10kg
5kg
2.5kg
1.25kg
Working this out every time is getting tiresome. Create a function that returns an array showing the smallest combination of weights you can put on to reach the total weight w. Return a false error for any weight that cannot be split evenly on the bar or is <20.

For example:

your total weight is w = 175

175 - 20kg bar weight = 155 = 77.5kg on each side of the bar

so the expected output would be:

[20, 20, 20, 15, 2.5]

Finally, if the input is exactly 20kg then the function should return an empty array as that is the result for a bar without any weight.
*/


/* A trick to generate an array with one element duplicated at many indexes like in Python

Array.from(new Array(numberOfTime), (x, i) => element), [element, element, element....]

*/
//My Solution:
function liftingCalc(w){

	let bar_w = [20, 15, 10, 5, 2.5, 1.25];
	let half_bar = (w - 20) / 2; let w_combination = [];  

	for(let i = 0; i < bar_w.length; i++){

		while(half_bar >= bar_w[i]){
    
      		let ocurrence = parseInt(half_bar / bar_w[i]);
			let same_w = Array.from(new Array(ocurrence),(x,y) =>bar_w[i]);			
        	w_combination = w_combination.concat(same_w);
        	half_bar -= (bar_w[i] * ocurrence);
    	}
    	if(half_bar === 0){break;}
  	}
  	return half_bar ? false : w_combination;
}

function liftingCalc(w){

	let stock = [20, 15, 10, 5, 2.5, 1.25];
	let weight = (w - 20) / 2; 
	let res = [];  

	for(let i = 0; i < stock.length; i++){

		while(weight >= stock[i]){
    
      		let ocurrence = parseInt(weight / stock[i]);
			let pack = Array.from(new Array(ocurrence),(x,y) =>stock[i]);			
        	res = res.concat(pack);
        	weight -= (stock[i] * ocurrence);
    	}
    	if(weight === 0){break;}
  	}
  	return weight ? false : res;
}



function liftingCalc(w){

	let stock = [20, 15, 10, 5, 2.5, 1.25];
	let weight = (w - 20) / 2; 
	let res = [];  

	stock.forEach(item => {

		while(weight >= item){
			
        	res.push(item);
        	weight -= item;
    	}

  	})
  	return weight? false : res;
}

console.log(liftingCalc(250))


// Test.assertSimilar(liftingCalc(250), [20, 20, 20, 20, 20, 15]);
// Test.assertSimilar(liftingCalc(175), [20, 20, 20, 15, 2.5]);
// Test.assertSimilar(liftingCalc(95), [20, 15, 2.5]);
// Other Solutions:

// Solution: By warriors

function liftingCalc(w){
  let storage = [20, 15, 10, 5, 2.5, 1.25];
  let weight = w/2-10;
  let result = [];
  
  storage.forEach(item =>{
    while(weight >= item){
      result.push(item);
      weight -= item;
    }

  })
  
  return weight ? false : result;
}

