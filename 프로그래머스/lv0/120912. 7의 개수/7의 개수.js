function solution(array) {
//     7을 기준으로 문자열을 나눈다음 만들어진 문자열의 개수 -1
    return array.join('').split('7').length - 1;
}