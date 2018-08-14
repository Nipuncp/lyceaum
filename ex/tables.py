def tables(a):
    for i in range(1, a+1):
        for j in range(1, a+1):
            m = str(j*i)
            print (m.ljust(4), end = '')
            # print (j*i, end = '')
            # for k in range(4-len(str(j*i))):
            #     print (' ', end = '')
        print ('')


def tables2(a):
    table = []
    for i in range(1, a+1):
        row = []
        for j in range(1, a+1):
            m = str(j*i)
            row.append((m.ljust(4)))
        table.append("".join(row))
    return "\n".join(table)


t = []

def adder(q):
    t.append(q)
    return sum(t)
