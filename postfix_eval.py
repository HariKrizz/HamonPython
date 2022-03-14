
def postfix_calc(expr):
    nums = []      
    
    if not len(expr):
        return None

    if expr.isalpha(): 
        return None

    for i in expr:   
        if i.isdigit(): 
            nums.append(int(i))

        elif i == '+': 
            n1 = nums.pop()
            n2 = nums.pop()
            nums.append(n1 + n2)

        elif i == '-': 
            n1 = nums.pop()
            n2 = nums.pop()
            nums.append(n1 - n2)

        elif i == '*':
            n1 = nums.pop()
            n2 = nums.pop()
            nums.append(n1 * n2)
            
        elif i == '/': 
            n1 = nums.pop()
            n2 = nums.pop()
            nums.append(n1 / n2)       
    return nums

if __name__ == '__main__':
    expr = "acd"  
    print(postfix_calc(expr))     