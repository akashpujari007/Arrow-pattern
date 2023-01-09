n = int(input())
increasing = (n + 1) // 2
decreasing = n - increasing

i = 1
while i <= increasing:
    s = 1
    while s <= i - 1:
        print(' ', end='')
        s = s + 1
        
    j = 1
    while j <= i:
        print('* ', end='')
        j = j + 1
    print()
    i = i + 1
    
i = 1
while i <= decreasing:
    s = 1
    while s <= decreasing - i:
        print(' ', end='')
        s = s + 1
    j = 1
    while j <= decreasing - i + 1:
        print('* ', end='')
        j = j + 1
    print()
    i = i + 1