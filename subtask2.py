
def arit_func():
    #start values
        n = 0
        s = 0
        m = 0
        a = 0
        #set of values for x
        num = [5,3,6,30,76,-1]

        x = num[n]
        m = x
        while x != -1:
            s = s + x
            if m > x:
                m = x
            n = n + 1   #select next value
            x = num [n]

        if n == 0:
            a = -1
            m = -1
        else:
            a = s/n     #mean
        print (n,s,m,a) #output
arit_func()             #call function 
# it looks like I learned how to use git today