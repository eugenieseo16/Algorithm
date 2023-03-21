function solution(my_string, n) {
  return [... my_string].map(v => v.repeat(n)).join("")
}

         