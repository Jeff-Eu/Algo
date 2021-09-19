# 657. Judge Route Circle

```javascript
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    var upCount = 0;
    var downCount = 0;
    var leftCount = 0;
    var rightCount = 0;
    
    for (var i in moves) {
        if (moves[i] === 'U') upCount++;
        else if(moves[i] === 'D') downCount++;
        else if(moves[i] === 'L') leftCount++;
        else rightCount++;
    }
    
    return (Math.abs(upCount - downCount) + Math.abs(leftCount - rightCount) === 0) 
};
```