a = {'I': 1 , 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def b(value):
    res = 0
    key = value[-1]
    for i in value[::-1]:
        if a[i] >= a[key]:
            res += a[i]
            kei = i
        else:
            res -= a[i]
    return res


print(b('VI'))
