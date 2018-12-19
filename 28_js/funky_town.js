/* Team SmallFish - Addison Huang and Dennis Chen
SoftDev1 pd6
K28 -- Sequential Progression
2018-12-19*/

var fibonacci = function(n) {
    if (n <= 1) {
	return n;
    }
    else {
	return fibonacci(n-1) + fibonacci(n-2);
    }
}

var gcd = function(a,b) {
    if (a > b) {
	for (i = b; i > 0; i--) {
	    if ((a%i==0) && (b%i==0)) {
		console.log(i);
		break
	    }
	}
    }
    else {
	for (i = a; i > 0; i--) {
	    if ((a%i==0) && (b%i==0)) {
		console.log(i);
		break
	    }
	}
    }
}
var students = ['joe','bob','mary','addison','dennis','andrew','tyler','jessica','karen','vincent','allen']
var randomStudent = function(){
    console.log(students[parseInt(Math.random() * students.length)]);
}
f = document.getElementById('fibb')
g = document.getElementById('gcd')
r = document.getElementById('randomS')
r.addEventListener('click',randomStudent)
g.addEventListener('click',gcd(4,8))
var displayFibb = function(){
    console.log(fibonacci(5))
}
