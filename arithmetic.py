import re
def calculator(equation_string):
    numbers = re.split('\+|-|\*|\/|\^|\(|\)|%', equation_string)
    operators = ["START"]+re.findall('\+|-|\*|\/|\^|\(|\)|%', equation_string)
    
    def get_negative_numbers(numbers, operators):
        remove_num_idx = []
        remove_op_idx = []
        for idx, (num, op) in enumerate(zip(numbers, operators)):
            if idx > 0 and op=="-":
                if numbers.copy()[idx-1] == "":
                    numbers[idx] = "-"+num
                    remove_num_idx.append(idx-1)
                    remove_op_idx.append(idx)
        return [i for j, i in enumerate(numbers) if j not in remove_num_idx], [i for j, i in enumerate(operators) if j not in remove_op_idx]
    
    def calcualte(A, B, operator): 
        if   operator=="+":
            return float(A)+float(B)
        elif operator=="-":
            return float(A)-float(B)
        elif operator=="*":
            return float(A)*float(B)
        elif operator=="/":
            return float(A)/float(B)
        elif operator=="%":
            return float(A)%float(B)
        elif operator=="^":
            return pow(float(A), float(B))
        
    def list_calculation(list):
        numb = [list[i] for i in range(len(list)) if i%2==0]
        oper = [list[i] for i in range(len(list)) if i%2!=0]
        for idx, o in enumerate(oper):
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
        numbers, operators = get_negative_numbers(numbers, operators)
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
