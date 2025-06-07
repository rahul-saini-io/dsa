"""
    here we need to find an intuition that how can we find all the change that we can have from the coins we have

    1. here we have an unsorted array of coins
    2. Now we need to find the change we cannot make out of these coins
    3. if we sort the array and the add coins we need to make sure of previous coins sum should not exceed next coin value
    4. eg. [2,4,5] here we cannot have change 1 because if we start from change 0 and add 1 to change(0) the 2 is greater than the sum
    5. so this is the intuition on which we build our logic

"""

def find_non_cons_change(coins):

    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1

        change += coin

    return change+1


coins = [1,2,4]

print(find_non_cons_change(coins))