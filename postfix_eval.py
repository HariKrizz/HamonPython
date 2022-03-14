
def postfix_calc(expr):
    nums = [] 
   
    if not len(expr):
        return None

    for i in expr:   
        if i.isdigit(): 
            nums.append(int(i))

        elif expr.isalpha(): 
            return None
        
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
    expr = "123abc++"  
    print(postfix_calc(expr))     