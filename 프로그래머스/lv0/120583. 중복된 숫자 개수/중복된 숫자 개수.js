function solution(array, n) {
    var answer = 0;
    for(i = 0; i < array.length; i++){
      if(array[i] == n){
        answer += 1
    }
    }
    return answer;
}