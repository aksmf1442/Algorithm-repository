// [1차 비밀지도]

function solution(n, arr1, arr2) {
    var answer = [];
    let arr = new Array(n).fill("");
    
    for (let i = 0; i < n; i++) {
        let num1 = arr1[i].toString(2);
        let num2 = arr2[i].toString(2);
        while (num1.length < n) {
            num1 = "0" + num1;
        }
        while (num2.length < n) {
            num2 = "0" + num2;
        }

        for (let j = 0; j < n; j++) {
            if (num1[j] === "1" || num2[j] === "1") {
                arr[i] += "#";
            } else {
                arr[i] += " ";
            }
        }
    }
    
    return arr;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));