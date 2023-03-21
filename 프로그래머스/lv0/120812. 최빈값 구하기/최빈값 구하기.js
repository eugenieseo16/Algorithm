function solution(array) {
  // array의 길이가 1일 경우
  let setarray = [...new Set(array)];
  if (array.length === 1 || setarray.length === 1 ) return array[0];
    
  const numbers = {};
  const answer = [];

  // numbers에 값X --> 값을 만들고 1, 있으면 기존 값 +1을 해준다.
  //  {'1': 1, '2': 1, '3': 3, '4': 1 }
  array.forEach(num => {
    numbers[num] = ++numbers[num] || 1;
  });

  // numbers를 array로 바꾼다
  // [[1, 1], [2, 1], [3, 3], [4, 1]]
  for (let key in numbers) {
    answer.push([key, numbers[key]]);
  }

  // 정렬
  answer.sort((a, b) => b[1] - a[1]);

  // 최빈값이 여러 개인지 확인
  if (answer[0][1] === answer[1][1]) {
    return -1;
  } else {
    return Number(answer[0][0]);
  }
}
