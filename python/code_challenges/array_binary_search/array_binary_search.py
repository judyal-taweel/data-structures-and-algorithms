def binarysearch(list,num):
    firstidx = 0
    lastidx = len(list)-1

    while firstidx <= lastidx:         
        if firstidx <= lastidx:
            middle = firstidx + (lastidx-firstidx) // 2
            middlenum = list[middle]
            if middlenum == num:
               return middle
            elif middlenum <= num:  
                lastidx = middle-1
            elif middlenum >= num:  
                firstidx = middle+1
        
            return -1        
    


