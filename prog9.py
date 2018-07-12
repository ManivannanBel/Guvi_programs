try:
    n = (raw_input())
    n = n.split()
    k = int(n[1])
    n = int(n[0])
    arr = raw_input()
    arr = arr.split()
    sum = 0
    for i in range(k):
        sum += int(arr[i])
    print sum
except:
    pass
