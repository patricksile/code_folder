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
pascalsTriangle = (n) ->
	pasTriDict = {'1':[1],'2':[1,1]} temp = []
	if n > 2
		x = 3
		while x <= n
			for i = 0; i < x-2 i++
				temp.push(pasTriDict[String(x-1)][i] + pasTriDict[String(x-1)][i+1])
			temp.push(1);temp.unshift(1)
			pasTriDict[String(x)] = temp;
			temp = [] 
			++x
	y = 1 pasTri = []
	while y <= n
		pasTri = pasTri.concat(pasTriDict[String(y)])
		++y 
	return pasTri