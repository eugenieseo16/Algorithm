function solution(array) {
    var answer = [0,0];
    for (let idx in array){
        if (array[idx] > answer[0]) {
            answer[0] = array[idx]
            answer[1] = Number(idx)
        }
    }
    return answer;
}