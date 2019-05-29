msgs = {3:"Linio",5:"IT",8:"Linianos"}

def q_r(n,d):
    q,r = (n//d,n%d)
    return q,r

def calc_key_component(q_r,d):
    try:
        return (q_r[1]*d)/q_r[1]
    except ZeroDivisionError:
        return 0

    
#n=7
for n in range(1,101):
    q_r_3 = q_r(n,3)
    q_r_5 = q_r(n,5)

    k = (8 - int(calc_key_component(q_r_3,3)+calc_key_component(q_r_5,5))) 

    try:
        print(msgs[k])
    except KeyError:
        print(n)
