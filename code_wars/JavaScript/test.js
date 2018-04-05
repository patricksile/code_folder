if (!Array.prototype.first) {
  Array.prototype.first = function() {
    return this[0];
  }
}

c = ['this','that','the']

console.log(c.first())

console.log(c.entries())