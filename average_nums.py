
def AverageofList(arr):

    sum = 0

    for i in arr:
        sum +=  i
        avg = sum/len(arr)

    if len(arr) != 0:
        return avg
    else: 
        return None
       
print(AverageofList([5])) 