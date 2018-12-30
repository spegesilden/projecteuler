def isLeap(y):
    if y % 400 == 0 and y % 1000 != 0:
        return False
    elif y % 4 == 0:
        return True
    return False

def days(m, y):
    if m == "September" or m == "April" or m == "June" or m == "November":
        return 30
    elif isLeap(y):
        if m == "February":
            return 29
    elif not isLeap(y):
        if m == "February":
            return 28
    return 31

def isSunday(d):
    if d % 7 == 6:
        return True
    return False

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

d = 0
sundays = 0

for m in months:
    d += days(m, 1900)

for y in range(1901, 2001):
    for m in months:
        #if m != "May" and y == 2016:
        #    print(isSunday(d))
        if isSunday(d):
            #print(m, y)
            sundays += 1
        d += days(m, y)

print(sundays)
