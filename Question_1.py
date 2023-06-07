#Question 1 
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]
#Here i have implimented selection sort

def seleg(l1):
    for i in range(len(l1)):
        minx = i
        for j in range(i+1, len(l1)):
            if l1[j] < l1[minx]:
                minx = j
        l1[i], l1[minx] = l1[minx], l1[i]
    return l1

lst1 = [5, 416, 54, 21, 6135, 15, 741]
sl = seleg(lst1)
print(sl)



# Time complexity of this code is O(n^2). This is best time comlexity by selection sort.


