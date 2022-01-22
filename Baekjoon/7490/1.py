def eval(s) :
    A = None
    B = ""
    # sum = 0
    for c in s :
        if c == '+' :
            A = int(A) + int(B)
            B = ""
                
        elif  c == '-' :
            A = int(A) - int(B)
            B = ""
        elif c.isdigit() :
            if A is None : # 처음이면 
                A = int(c)
            else :
                B +=c
        # elif c == " " :
            
    print(A)
    return A


eval("1+2-3+4-5-6+7")