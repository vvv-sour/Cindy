def compare_two_list(list_a,list_b):
    result=[]
    for a,b in zip(list_a,list_b):
        if a>b:
            result.append(f"{a}>{b}")
        if a<b:
            result.append(f"{a}<{b}")
        if a==b:
            result.append(f"{a}={b}")
    return result