#1  Mine :)
def bubble_sort(array):
    length=len(array)-1
    for j in range (length):
        for i in range(length-j):

        # This swap(boolean) veriable is used to nothing but optimize the code [In case your array is given sorted already]
            swap=False
            if array[i]>array[i+1]:    

                # by swapping variable                                                    
                array[i],array[i+1]=array[i+1],array[i]     
                swap=True

        if not swap:
            break



#2  Using Temp var
def bubble_sort(array):
    length=len(array)-1
    for j in range (length):
        for i in range(length-j):

    # This swap(boolean) veriable is used to nothing but optimize the code [In case your array is given sorted already]
            swap=False
            
            if array[i]>array[i+1]:     

                #using temp var                                     
                temp=array[i]                            
                array[i]=array[i+1]
                array[i+1]=temp
                swap=True
            
        if not swap:
            break






if __name__=='__main__':
    array=[-2, 45, 0, 11, -9]


    bubble_sort(array)
    print (array)