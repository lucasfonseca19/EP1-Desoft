def faixa_notas(*args):
    l=[*args]
    cinco=[]
    cincset=[]
    sete=[]
    for i in l:
        if(l[i]<5):
            cinco.insert(i,i)
        elif(l[i]>=5 and l[i]<7):
            cincset.append(i)
        else:
            sete.insert(i,i)
        
    print(cinco)
    
            
faixa_notas(3, 4, 5, 5.5, 6, 9)