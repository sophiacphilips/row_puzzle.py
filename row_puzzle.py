#Name: Sophia Philips
#GitHub UserName: sophiacphilips
#Date: 02/14/2023
#This code is designed to take a list (row) of non-negative integers, with 0 as the right most position.
#taken from git instructions: "You have a token that starts on the leftmost square. On each turn,
#the token can shift left or right a number of squares exactly equal to the value in its current square,
# but is not allowed to move off either end. "


def row_puzzle_helper(pos, row):
    if pos<0: #base case
        return False
    if pos>=len(row): #base case
        return False
    if row[pos]==-1: #base case
        return False
    if pos==(len(row)-1): #if value of number in row is less than the length of the row then puzzle is possible
        return True
    place_holder = row[pos] #place_holder used to hold current position of integer in row
    row[pos]=-1
    return row_puzzle_helper(pos+place_holder,row)|row_puzzle_helper(pos-place_holder,row) #adds or subtracts place holder from its
#current value to move left or right, + for right, - for left movement along row

def row_puzzle(row):
    """
    row_puzzle takes a list of positive integers (row parameter) and calls the helper function to play square row game via recursion
    """
    return row_puzzle_helper(0,row)

