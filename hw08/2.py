week = int(input())
day = int(input())

if week % 2 == 0:
    if day == 2:
        print(f'第{week}周的周{4}')
    elif day == 4:
        print(f'第{week+1}周的周{2}')
else:
    print(f'第{week+1}周的周{2}')
