/**
 * @param {string} s
 * @return {string}
 */
const removeDuplicateLetters = (s) => {
    s = "bcabc";
    let stack = [];

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (stack.includes(char)) continue;

        while (stack[stack.length - 1] > char
            && s.substring(i).includes(stack[stack.length - 1])) {
            stack.pop();
        }
        stack.push(char);
    }
    return stack.join('');
};
console.log(removeDuplicateLetters());