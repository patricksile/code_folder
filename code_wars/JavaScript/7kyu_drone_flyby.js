/*
The other day is saw an amazing video where a guy hacked some wifi controlled lightbulbs by flying a drone past them. Brilliant.

In this kata we will recreate that stunt... sort of.

You will be given two strings: lamps and drone. Lamps represents a row of lamps, currently off, each represented by 'x'. When these lamps are on, they should be represented by 'o'.

The drone string represents the position of the drone 'T' (any better suggestion for character??) and its flight path up until this point '='. The drone always flies left to right, and always begins at the start of the row of lamps. Anywhere the drone has flown, including its current position, will result in the lamp at that position switching on.

Return the resulting lamps string. See example tests for more clarity.

Test.describe("Example tests",_=>{
Test.assertEquals(flyBy('xxxxxx', '====T'), 'ooooox');
Test.assertEquals(flyBy('xxxxxxxxx', '==T'), 'oooxxxxxx'); 
Test.assertEquals(flyBy('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx'); 
})
*/
function flyBy(lamps, drone){

        // x's lenght
        let x = 'x'.repeat(lamps.length - drone.length)
        let o = 'o'.repeat(drone.length)
        return o + x
    }


function flyBy2(l, d) {
    return 'o'.repeat(d.length) + 'x'.repeat(l.length - d.length)
}
function flyBy3(l, d) {
    let ll = l.length;
    let ld = d.length;
    
    if ( ll <= ld ) return 'o'.repeat(ld);
    return 'o'.repeat(ld) + 'x'.repeat(ll - ld)
}

flyBy4 = (l, d) => 'o'.repeat(d.length) + 'x'.repeat(l.length - d.length)

function flyBy5(l, d){
    return [...l].fill('o', 0, d.length).join(``);
  }
// Test zone:

l = "xxxxxxxx"
d = "===========T"

console.log(flyBy5(l,d))
