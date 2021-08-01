#Goal: maximize value while limiting total weight
T = {}
def Knapsack(w,v,u):
    #Check if unit already in bag and initialize
    if u not in T:
        T[u] = 0
    #Check all the weights in range of w and Recursively call knapsack
        for i in range(len(w)):
            if w[i] <= u:
                T[u] = max(T[u],Knapsack(w,v,u-w[i])+v[i])
                
    #Store results in the dictionary
    return T[u]



#Driver function
print(Knapsack(w=[6, 3, 4, 2], v=[30, 14, 16, 9], u=10))