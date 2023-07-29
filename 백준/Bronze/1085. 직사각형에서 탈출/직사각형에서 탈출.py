x,y,w,h = map(int, input().split())
min_x = 0
if x < w-x:
    min_x = x
else:
    min_x = w-x
min_y = 0
if y < h-y:
    min_y = y
else:
    min_y = h-y
if min_x <= min_y:
    print(min_x)
else:
    print(min_y)