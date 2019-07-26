i = 2
while i <= 3:
    j = 0
    while j <= 3:
        j += 1
        if j == 2:
            break
            #continue
        print("======")
        print("i=%dj=%d" % (i, j))
    i += 1
