import time

def run():
    # main program
    # find sum to first 1 million numbers
    sum_x = 0
    for i in range(1000000):
        sum_x += i

    # wait for 3 seconds
    time.sleep(3)
    print('Sum of first 1 million numbers is:', sum_x)