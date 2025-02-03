tup=(1,4,9,16,25,36,49,64,81,100)
idx=0
while idx<len(tup):
    if(16==tup[idx]):
        print("element found at index", idx, ":", tup[idx])
    else:
        print("element not found at index", idx)
    idx+=1
