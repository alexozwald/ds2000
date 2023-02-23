'''
DS2K: Example code from 9/14

This code shows one way of printing out the number of thousands,
hundreds, tens, ones in an integer provided by the user.
'''

# Input: 4321 
# Output: “thousands = 4, hundreds=3, tens=2, ones=1”
def main():
    orig = int(input('Enter a non-negative integer\n'))

    # Note that ‘//’ is integer division
    thousands = orig // 1000
    print("thousands =", thousands)
    
    leftover = orig - thousands*1000
    hundreds = leftover // 100
    print("hundreds =", hundreds)

    # Update leftover portion by subtracting
    # away the hundreds
    leftover = leftover - hundreds*100
    tens = leftover // 10
    print("tens =", tens)
    leftover = leftover - tens*10

    # At this point all we have are the ones!
    ones = leftover
    print("ones =", ones)
    
main()
