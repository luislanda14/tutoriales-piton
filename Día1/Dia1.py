a=[]
c=[]
d=[]
b=0
with open('imput.txt') as f:
    for x in f:
        if '\n' in x[0:2]:
            a.append("/")
        else:
            print(x)
            a.append(int(x[:-1]))
    print(a)
    for x in a:
        if x != "/":
            b=x+b
        else:
            c.append(b)
            b=0
    c.append(b)
    max_num = max(c)
    print("Lleva aproximadamente",max_num,"kilos de coca metidos por el culo")
    pos_max = c.index(max_num)
    print("Elfo más robable:", pos_max+1)

    d = c.copy()
    d.sort()
    top3 = max(d)+ int(d[-2]) + int(d[-3])
    print("Tienen",top3,"caramelos antes de convertirse a la sociedad de la nieve")