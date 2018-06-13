# Various algorithms written using dynamic programming
import numpy as np

def fibonacci(x):
    f = [0,1]
    if x == 0: return 0
    elif x == 1: return 1
    else:
        for i in range(2,x+1):
            f.append(f[i-1]+f[i-2])
    return f[-1]

def lis(sequence):
    # Longest Increasing Subsequence
    try:
        if len(sequence) < 1:
            return 0
    except:
        print("Invalid argument passed to function.  Requires a sequence.")
    n = len(sequence)
    steps = 0
    longest=[1]
    ans = 1
    for i  in range(1,len(sequence)):
        for j in range(len(longest)):
            l = 1
            steps += 1
            if sequence[i] > longest[j] and l < longest[j] + 1:
                l = longest[j] + 1
        longest.append(l)
        if l > ans:
            ans = l
    print ("Took {} iterations for a sequence of length {}".format(steps,n))
    return ans

def lcs(x,y):
    # Finds the length of the longest string which is a subsequence of both x and y
    L = np.zeros((len(x)+1,len(y)+1))
    try:
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                # print(x[i-1],y[j-1])
                if x[i-1] == y[j-1]:
                    # print("{} == {} at i = {} and j = {}".format(x[i-1],y[j-1],i,j))
                    L[i,j] = 1 + L[i-1,j-1]
                else:
                    L[i,j] = max(L[i,j-1],L[i-1,j])
        return L[-1][-1]
    except Exception as e:
        print("Encounted an issue {!s}".format(e))
        return -1

if __name__=="__main__":
    # Fibonacci Test
    for i in range(11):
        print("Fibonacci number for {} is {}".format(i,fibonacci(i)))

    print("""

    """)

    # Longest Increasing Subsequence Test
    x = [5,7,4,-3,9,1,10,4,5,8,9,3]
    print(x)
    print(lis(x))

    print("""

    """)

    # Longest Recurring Subsequence Test
    X = ["B","C","D","B","C","D","A"]
    Y = ["A","B","E","C","B","A","B"]

    print(X)
    print(Y)
    print(lcs(X,Y))
