function solution(slice, n) {
  let answer = 1;
  let s = slice
  if (slice >= n) {
    return 1;
  } else {
    while (slice < n) {
      slice += s;
      answer += 1;
    }

    return answer;
  }
}