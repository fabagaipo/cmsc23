
def doubledInt(x: int)->int:
    return 2 * x

def largest(x: float, y: float)->float:
    return x if x > y else y

def isVertical(p1: (float, float), p2: (float, float))->bool:
    return p1[0] == p2[0]

def primes(n: int)->[int]:
    z = [1, 2]
    i = 3
    while(len(z) <= n):
        for a in range(3, i + 1, 2):
            if i == a:
                z.append(a)
            if i % a == 0:
                break
        i += 1
    return z[:n]

def fibonacciSequence(n: int)->list:
    z = [0, 1]
    _ = [z.append(z[-1] + z[-2]) for _ in range(n)]
    return z[:n]

def sortedIntegers(l: [int])->[int]:
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i] = l[i] + l[j]
                l[j] = l[i] - l[j]
                l[i] = l[i] - l[j]
    return l

def sublists(x: [int])->[[int]]:
    return [list(a) for a in x]

def fme(b: int, p: int, m: int)->int:
    return b ** p % m