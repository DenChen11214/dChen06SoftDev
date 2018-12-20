/* Team SmallFish - Addison Huang and Dennis Chen
SoftDev1 pd6
K30 -- Sequential Progression III: Season of the Witch
2018-12-20*/

var fibonacci = function(n) {
  var sum = [0,1]
  for (var i = 2; i <= n; i++) {
    sum.push(sum[i-2] + sum[i-1]);
  }
  return sum[sum.length - 1]
};

