import re
def calculator(equation_string):
    numbers = re.split('\+|-|\*|\/|\^|\(|\)|%', equation_string)
    operators = ["START"]+re.findall('\+|-|\*|\/|\^|\(|\)|%', equation_string)
    
    def calcualte(A, B, operator): 
        A, B = float(A),float(B)
        if   operator=="+":
            return A+B
        elif operator=="-":
            return A-B
        elif operator=="*":
            return A*B
        elif operator=="/":
            return A/B
        elif operator=="%":
            return A%B
        elif operator=="^":
            return pow(A, B)
        
    def list_calculation(list):
        numb = [list[i] for i in range(len(list)) if i%2==0]
        oper = [list[i] for i in range(len(list)) if i%2!=0]
        for idx,o in enumerate(oper):
            if o != "+" and o != "-":
                tmp = calcualte(numb[idx], numb[idx+1], o)
                numb[idx], numb[idx+1] = "pop", tmp
                oper[idx]="pop"
        numb = [element for element in numb if element!="pop"]
        oper = [element for element in oper if element!="pop"]
        for idx,o in enumerate(oper):
            tmp = calcualte(numb[idx], numb[idx+1], o)
            numb[idx], numb[idx+1] = 0, tmp
        return numb[-1]
    
    def parse_parentheses(numbers, operators):
        lists = [[] for i in range(operators.count("(")+1)]
        count,last_count, list_idx = 0, 0, 0
        for num, op in zip(numbers, operators):
            last_count=count
            if op=="(":
                count+=1
            elif op==")":
                count-=1
            if count>last_count:
                list_idx+=1
                if lists[list_idx]!=[]:
                    lists[list_idx]=[]
                if num!="":
                    lists[list_idx].append(num)
            elif count<last_count:
                list_idx=count
                lists[list_idx].append(list_calculation(lists[list_idx+1]))
            elif count==last_count:
                lists[list_idx].append(op)
                if num!="":
                    lists[list_idx].append(num)
        lists[0].remove("START")  
        return list_calculation(lists[0])
    
    return parse_parentheses(numbers, operators)