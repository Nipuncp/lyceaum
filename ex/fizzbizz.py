def fizzbizz(n):
    for i in range(n+1):
        if(i%15 == 0):
            print("fizzbizz")
        elif(i%5 == 0):
            print("bizz")
        elif(i%3==0):
            print("fizz")
        else:
            print (i)

    
