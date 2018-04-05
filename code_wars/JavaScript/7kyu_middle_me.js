function middleMe(N, X, Y){
  if(N % 2 != 0){return X}
  else{return Y.repeat(N/2) + X + Y.repeat(N/2)}
}
middleMe=(N,X,Y)=>N%2?X:Y.repeat(N/2)+X+Y.repeat(N/2)

console.log(middleMe(18,'z','#'))