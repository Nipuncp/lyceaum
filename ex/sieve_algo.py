def sieve(n):
    list_n = [ i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if list_n[i]%(j+1) == 0:
                list_n.pop(i)
    print (list_n)
