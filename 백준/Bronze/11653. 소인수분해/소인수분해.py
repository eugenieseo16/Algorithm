N = int(input())
div = 2

while N != 1 :
    if N % div == 0: 
        print(div) 
        N = N//div
  
    else:
        div += 1