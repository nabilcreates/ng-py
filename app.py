import random

# Create a class
class NumberGenerator():

    def filter(self,length,startnum):
        # final result of number
        currentstr = ''
        
        # repeat loop until it reaches the range
        for x in range(0,length):

            # generate a random number
            num = random.randint(0,9)

            # concat with the currentstr
            currentstr += str(num)

        # if first digit == the start num
        if(int(currentstr[:1]) == startnum):

            # print it out
            print(currentstr)


# loop
for x in range(0,100000):
    # print
    newin = NumberGenerator().filter(8,8)