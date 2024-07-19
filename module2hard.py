def rebys(n):
    password = ''
    for i in range(1, 20):
        for j in range(i +1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    print(password)


rebys(11)













