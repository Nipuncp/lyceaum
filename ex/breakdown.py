def breakdown(amount):
    br = {}
    denom_1000 = amount//1000
    remain_1000 = amount%1000
    denom_500 = remain_1000//500
    remain_500 = remain_1000%500
    denom_100 = remain_500//100
    remain_100 = remain_500%100
    denom_50 = remain_100//50
    remain_50 = remain_100%50
    denom_20 = remain_50//20
    remain_20 = remain_50%20
    denom_10 = remain_20//10
    remain_10 = remain_20%10
    denom_5 = remain_10//5
    remain_5 = remain_10 %5
    denom_1 = remain_5
    br[1000] = denom_1000
    br[500] = denom_500
    br[100] = denom_100
    br[50] = denom_50
    br[20] = denom_20
    br[10] = denom_10
    br[5] = denom_5
    br[1] = denom_1
    return br

def breakdown(amount):
    br = {}
    for i in [1000, 500, 100, 50, 20, 10, 5, 1]:
        count = amount // i
        sub_total = count * i
        amount = amount - sub_total
        br[i] = count
    return br
        
    # br = {}
    # denom_1000 = amount//1000
    # remain_1000 = amount%1000
    # denom_500 = remain_1000//500
    # remain_500 = remain_1000%500
    # denom_100 = remain_500//100
    # remain_100 = remain_500%100
    # denom_50 = remain_100//50
    # remain_50 = remain_100%50
    # denom_20 = remain_50//20
    # remain_20 = remain_50/20
    # denom_10 = remain_20//10
    # remain_10 = remain_20%10
    # denom_5 = remain_10//5
    # remain_5 = remain_10 %5
    # denom_1 = remain_5
    # br[1000] = denom_1000
    # br[500] = denom_500
    # br[100] = denom_100
    # br[50] = denom_50
    # br[20] = denom_20
    # br[10] = denom_10
    # br[5] = denom_5
    # br[1] = denom_1
    # return br


def breakdown2(n,d):
    denom_500 = n/500
    remain_500 = n%500
    d[500] -= denom_500
    
