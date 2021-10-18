// 숫자 문자열과 영단어(leve1)

String.prototype.replaceAll = function(org, dest) {
    return this.split(org).join(dest);
}

function solution(s) {
    s = s.replaceAll('zero', '0');
    s = s.replaceAll('one', '1');
    s = s.replaceAll('two', '2');
    s = s.replaceAll('three', '3');
    s = s.replaceAll('four', '4');
    s = s.replaceAll('five', '5');
    s = s.replaceAll('six', '6');
    s = s.replaceAll('seven', '7');
    s = s.replaceAll('eight', '8');
    s = s.replaceAll('nine', '9');
    return parseInt(s);
}

console.log(solution("one4seveneight"))