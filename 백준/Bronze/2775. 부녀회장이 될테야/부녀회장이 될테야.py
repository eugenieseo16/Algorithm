TC = int(input())
for _ in range(TC):
    floor = int(input())
    room_num = int(input())
    residents = [i for i in range(room_num + 1)]

    for f in range(floor):
        for num in range(1, room_num + 1):
            residents[num] += residents[num - 1]
    print(residents[-1])
