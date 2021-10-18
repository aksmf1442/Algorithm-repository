function solution(new_id) {
    const ic = "1234567890qwertyuiopasdfghjklzxcvbnm-_.";
    let result = '';
    new_id = new_id.toLowerCase();
    let length = new_id.length;

    for (i = 0; i < length; i++) {
        if (ic.includes(new_id[i])) {
            result += new_id[i];
        }
    }

    length = result.length;
    new_id = result;
    result = '';
    check = false;
    for (i = 0; i < length; i++) {
        if (new_id[i] !== '.') {
            result += new_id[i];
            check = false;
            continue;
        }

        if (new_id[i] === '.' && !check) {
            result += new_id[i];
            check = true;
        }
    }

    while (result[0] === '.' || result[result.length - 1] === '.' || result.length <= 2 || result.length >= 16) {

        if (result[0] === '.') {
            result = result.substring(1, result.length);
        }

        if (result[result.length - 1] === '.') {
            result = result.substring(0, result.length - 1);
        }

        if (result.length === 0) {
            result = 'a';
        }

        if (result.length >= 16) {
            result = result.substring(0, 15);
        }

        if (result.length <= 2) {
            while (result.length <= 2) {
                result += result[result.length - 1];
            }
        }
    }
    return result;
}

console.log(solution("abcdefghijklmn.p"));