// 최소직사각형

function solution(sizes) {
    var answer = 0;
    let maxValue = 0;
    for (let i = 0; i < sizes.length; i++) {
        if (maxValue < Math.max(...sizes[i])) {
            maxValue = Math.max(...sizes[i]);
        }
    }
    let minValue = 0;
    for (let i = 0; i < sizes.length; i++) {
        minValue = Math.max(Math.min(...sizes[i]), minValue);
    }
    return maxValue * minValue;
}

console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]]));
console.log(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]));