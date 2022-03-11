
def average(arr):
    s = 0
    if not arr:
        return None
    for i in arr:
        s +=  i
    avg = s/len(arr)
    return avg
if __name__ == '__main__':
    print(average([1,2,3,4,5]))