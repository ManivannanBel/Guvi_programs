alp = raw_input()
alp = alp.split()
if int(alp[0])>int(alp[1]):
    if int(alp[0]>alp[2]):
        print alp[0]
    else:
        print alp[2]
else:
    if int(alp[1])>int(alp[2]):
        print alp[1]
    else:
        print alp[2]
