/* Team BigFish - Jeffrey Wu and Dennis Chen
SoftDev1 pd6
K29 -- Sequential Progression II: Electric Boogaloo...
2018-12-19*/

var fibonacci = function(n) {
  var sum = [0,1]
  for (var i = 2; i <= n; i++) {
    sum.push(sum[i-2] + sum[i-1]);
  }
  console.log(sum[sum.length - 1])
};

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
};
var students = ['joe','bob','mary','addison','dennis','andrew','tyler','jessica','karen','vincent','allen']
var randomStudent = function(){
  console.log(students[parseInt(Math.random() * students.length)]);
};
f = document.getElementById('fibb')
g = document.getElementById('gcd')
r = document.getElementById('randomS')
f.addEventListener('click',function(){
  console.log(fibonacci(13));
  document.getElementById("message").innerHTML = 'Fibonnacci of 13 is ' + fibonacci(13);
});
r.addEventListener('click',function(){
  console.log(randomStudent());
  document.getElementById("message").innerHTML = 'Random student is ' + randomStudent();
});
g.addEventListener('click',function(){
  console.log(gcd(2019,3365));
  document.getElementById("message").innerHTML = 'The GCD of 2019 and 3365 is ' + gcd(2019,3365);
});
