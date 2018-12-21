/* Team SmallFish - Addison Huang and Dennis Chen
SoftDev1 pd6
K30 -- Sequential Progression III: Season of the Witch
2018-12-20*/

// var changeHeading = function(e) {
//     var h = document.getElementById("h")
//     h.innerHTML =
// };

// var removeItem = function(e) {
// };

// var lis = document.getElementsByTagName("li");
//
// for(var i=0; i < lis.length; i++) {
//     lis[i].addEventListener('mouseover', );
//     lis[i].addEventListener('mouseout', );
//     lis[i].addEventListener('click', );
// };
var addItem = function(e) {
    var list = document.getElementById('thelist');
    var item = document.createElement("li");
    item.innerHTML = 'WORD';
    list.appendChild(item);
};
var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var fibIndex = 1
var addFib = function(e){
    var lis = document.getElementById('fiblist');
    var item = document.createElement('li');
    item.innerHTML = fib(fibIndex);
    fibIndex += 1;
    lis.appendChild(item);
    console.log(e);
};

var fibonacci = function(n) {
  var sum = [0,1];
  for (var i = 2; i <= n; i++) {
    sum.push(sum[i-2] + sum[i-1]);
  }
  return sum[sum.length - 1];
};
var addFib2 = function(e){
    var lis = document.getElementById('fiblist');
    var item = document.createElement('li');
    item.innerHTML = fibonacci(fibIndex);
    fibIndex += 1;
    lis.appendChild(item);
    console.log(e);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
