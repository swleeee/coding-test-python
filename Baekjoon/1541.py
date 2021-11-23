data = input()

str = ''
count = 0
first = True
mode = "+"

for i in range(len(data)):    
    print(i, data[i], count, mode)
    if(data[i] >= '0' and data[i] <= '9'):        
        str += data[i] 
    else:
        if(first):
            count += int(str)
            first = False
            if(data[i]) == "-":
                mode="-"

        else: 
            if(data[i]=='+'):
                if(mode == '+'):
                    count += int(str)
                else:
                    count -= int(str)
            else: 
                print("-")
                
                if(mode == '+'):
                    count += int(str)
                else:                          
                    count -= int(str)
                mode = "-"           
        str=""

if(mode=="+") : 
    count += int(str)
else:
    count -= int(str)

print(count)

