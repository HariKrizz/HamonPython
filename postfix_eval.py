
def postfix_calc(expr):
    nums = []   
    if not len(expr):
        return None
    else:
        for i in expr:   
            if i.isdigit(): 
                nums.append(int(i))
            else:
                n1 = nums.pop()
                n2 = nums.pop()
                if i == '+': 
                    nums.append(n1 + n2)
                elif i == '-': 
                    nums.append(n1 - n2)
                elif i == '*':
                    nums.append(n1 * n2)
                elif i == '/': 
                    nums.append(n1 / n2)       
        return nums.pop()
    

if __name__ == '__main__':
    expr = "123++"  
    print(postfix_calc(expr))     