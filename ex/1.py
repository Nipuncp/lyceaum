#a = 1234
#b = "YOu just missed the train"
#c = """India is my country. All Indias are my brothers and sisters. 
#I love my country, and am proud of its rich and varied heritage. """


def digits(a):
    s = str(a)
    l = len(s)
    return l

def nwords(a):
    s = a.split(" ")
    l = len(s)
    return l

def nsentence(a):
    s = a.count(".")
    return s

#print (digits(a))
#print (nwords(b))
#print (nsentence(c))
 

