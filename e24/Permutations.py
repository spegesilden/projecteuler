def isPerm(x):
    a = str(x)
    lst = []

    for i in range(0,len(a)):
        if not lst.__contains__(a[i]):
            lst.append(a[i])
        else:
            return False
    return True

def containsZero(x):
    string = str(x)

    for s in string:
        if s == '0':
            return True
    return False

def switch(a, i, j):
    x = a
    xi = 0
    xj = 0

    if containsZero(a):
        s = str(a)
    
        xi = (int(s[j]) - int(s[i])) * (10 ** (9-i))
        xj = (int(s[i]) - int(s[j])) * (10 ** (9-j))
    else:
        s = "0" + str(a)
    
        xi = (int(s[j]) - int(s[i])) * (10 ** (9-(i)))
        xj = (int(s[i]) - int(s[j])) * (10 ** (9-(j)))

    x += xi + xj

    return x

def add(A,x):
    A.add(x)

def perms(index, x):
    #permset = [123456789]
    permset = set([])

    if len(index) == 2:
        for i in index:
            for j in [k for k in index if k != i]:
                xperm = switch(x, i, j)
                #add(permset, xperm)
                permset.add(xperm)
    else:
        for i in index:
            index2 = [j for j in index if j != i]
            for j in index2:
                xperm = switch(x, i, j)
                index3 = [k for k in index2 if k != j]
                add(permset, xperm)
                tmpSet = perms(index3, x)
                permset.union(tmpSet)
                #tmpSet = perms(index3, xperm)
                #permset.union(tmpSet)

    return permset

def permString(strings):
    permutations = []

    for x in strings:
        tmp = ""
        perm = x
        strings2 = [i for i in strings if i != x]
        for x2 in strings2:
            tmp2 = perm
            perm += x2
            strings3 = [i for i in strings2 if i != x2]
            for x3 in strings3:
                tmp3 = perm
                perm += x3
                strings4 = [i for i in strings3 if i != x3]
                for x4 in strings4:
                    tmp4 = perm
                    perm += x4
                    strings5 = [i for i in strings4 if i != x4]
                    for x5 in strings5:
                        tmp5 = perm
                        perm += x5
                        strings6 = [i for i in strings5 if i != x5]
                        for x6 in strings6:
                            tmp6 = perm
                            perm += x6
                            strings7 = [i for i in strings6 if i != x6]
                            for x7 in strings7:
                                tmp7 = perm
                                perm += x7
                                strings8 = [i for i in strings7 if i != x7]
                                for x8 in strings8:
                                    tmp8 = perm
                                    perm += x8
                                    strings9 = [i for i in strings8 if i != x8]
                                    for x9 in strings9:
                                        tmp9 = perm
                                        perm += x9
                                        strings10 = [i for i in strings9 if i != x9]
                                        for x10 in strings10:
                                            tmp10 = perm
                                            perm += x10
                                            permInt = int(perm)
                                            #print(permInt)
                                            permutations.append(permInt)
                                            perm = tmp10
                                        perm = tmp9
                                    perm = tmp8
                                perm = tmp7
                            perm = tmp6
                        perm = tmp5
                    perm = tmp4
                perm = tmp3
            perm = tmp2
        perm = tmp

    return permutations

index = range(0,10)
a = 123456789
strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

lexicon = permString(strings)
lexicon.sort()
print(lexicon[0], len(lexicon))
#tmp = perms(index, a)
#tmp.add(a)
#
#print("Appending to lexicon")
#
#for x in tmp:
#    lexicon.append(x)

#for x in range(123456789,987643211):
#    if len(lexicon) >= 1000000:
#        break
#    elif isPerm(x):
#        lexicon.append(x)
#        #print(len(lexicon))
#
#
#print("Now for the sorting")
#
#lexicon.sort()
#
#print(len(lexicon))
#print(lexicon)
#print(lexicon[999999])

#print(perms(permutations, a))
#for item in perms(a):
#    print(isPerm(item))

#a = 0
# #print(containsZero(a), switch(a,0,8))

    #for i in index:
    #    index2 = [k for k in index if k != i]
    #    for i2 in index2:
    #        x2 = switch(x, i, i2)
    #        add(perms, x2)
    #        index3 = [k for k in index2 if k != i2]
    #        for i3 in index3:
    #            add(perms, switch(x, i, i3))
    #            index4 = [k for k in index3 if k != i3]
    #            for i4 in index4:
    #                index5 = [k for k in index4 if k != i4]
    #                for i5 in index5:
    #                    index6 = [k for k in index5 if k != i5]
    #                    for i6 in index6:
    #                        index7 = [k for k in index6 if k != i6]
    #                        for i7 in index7:
    #                            index8 = [k for k in index7 if k != i7]
    #                            for i8 in index8:
    #                                index9 = [k for k in index8 if k != i8]
    #                                for i9 in index9:
    #                                    xperm = switch(x, i9, i8)
    #                                    add(perms, xperm)
