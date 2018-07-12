num = input()
try:    
    num = int(num)
    if num%2==0:
        print('Even')
    else:
        print('Odd')
except e:
    print('invalid')