function solution(numbers) {
    const arr = numbers.sort(function(a, b)  {
        return a - b;
    });
    const idx = arr.length
    return arr[idx-2] * arr[idx-1]
}