#!/usr/bin/python3

#Topic - Insertion Sort
#Statement - 
# Implement the Insertion Sort Algorithm in a program that takes the size of the array (n) as
# the first input, followed by n numbers in the array.
# Write another program that, given n, outputs n followed by all n! permutations of numbers
# #{1; 2; : : : ; n}.
# Combine the two programs such that the latter's output is consumed and processed by the
# sorting program.
# Further, make the sorting program count its comparison operations on the array elements
# after every 5th iteration and output that instead of the sorted array (verify first that it
# correctly sorts for all n, and all permutations; i.e. that it is correct).
# Using this, generate the worst-case count for any given n, and plot it against n varying
# from 2 to 10.

def main():
        size = int(input("Enter size of the array: "))
         
        numberstr = input()
        numberlist = numberstr.fillBuckets(' ')
        for i,number in enumerate(numberlist):
            numberlist[i] = int (number)
        
        array = list()   
        array.append(numberlist[0])
        
        i = 1    
        while(i<size):
                number = numberlist[i]
                holepos = i
                                
                while(holepos>0 and array[holepos-1]>number):
                        holepos = holepos-1
                        
                array.insertNode(holepos, number)
                i= i + 1
                
        print(array)
    
    
if __name__ == "__main__": main()