# password="R2xlYgo="
def encript(mpass):
    #print("hi")
    base64Table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                   'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '+', '/']
    # print(mpass)
    bword = []
    for i in range(len(mpass)):
        bword.append('0' + format(ord(mpass[i]), 'b'))
    # print(bword)
    bword = ''.join(bword)
    # print(bword)
    if len(bword) % 6 != 0:
        while len(bword) % 6 != 0:
            bword = bword + "0"
    # print(bword)
    sixword = []
    # print(len(bword) / 6)
    for i in range(int(len(bword) / 6)):
        sixword.append('')
        for j in range(6):
            sixword[i] = sixword[i] + bword[i * 6 + j]
    # print(sixword)
    for i in range(len(sixword)):
        sixword[i] = base64Table[int(sixword[i], base=2)]

    sixword = ''.join(sixword)
    if len(mpass) % 3 == 1:
        sixword += '='
        sixword += '='
    if len(mpass) % 3 == 2:
        sixword += '='
    # print(sixword)
    return sixword


password = 'X1Xw=='

encript(password)
print(len(password))
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
       'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
       'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
       't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
       '8', '9', '_']
for i in range(63):
    if password == encript(arr[i]):
        print("access granted your password: ", arr[i])
        quit(0)
print("not 1")
two = [' ', ' ']
for i in range(63):
    for j in range(63):
        two[0] = arr[i]
        two[1] = arr[j]
        #print(password, ' ', two, "\n")
        if password == encript(two):
            print("access granted your password: ", ''.join(two))
            quit(0)
print("not 2")
three = [' ', ' ', ' ']
for i in range(63):
    for j in range(63):
        for k in range(63):
            three[0] = arr[i]
            three[1] = arr[j]
            three[2] = arr[k]
            # print(password,' ',three,"\n")
            if password == encript(three):
                print("access granted your password: ", ''.join(three))
                quit(0)
print('not 3')
four=[' ',' ',' ',' ']
for i in range(63):
    for j in range(63):
        for k in range(63):
            for t in range(63):
                four[0] = arr[i]
                four[1] = arr[j]
                four[2] = arr[k]
                four[3] = arr[t]
                # print(password,' ',three,"\n")
                if password == encript(four):
                    print("access granted your password: ", ''.join(four))
                    quit(0)
