import sys
import time

print("DumbSAT-style Coin Combination Solver\n")

#inputs got here
coins = input("Provide the coins you would like to use with spaces inbetween (max 5 coins and 20 of each coin): ")
goal = int(input("\nEnter your goal numerical amount: "))

#turns coins into a reverse sorted list
list_of_coins = list(map(int, coins.split()))
list_of_coins.sort(reverse=True)

#case if to many coins
if len(list_of_coins) > 5:
    print("MAX of 5 different coins.")
    sys.exit(1)

start_time = time.time() #start timing here, end time depends on end

#case for 0
if goal == 0:
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nWorking Combo [] gets the goal of {goal} in {duration:.9f} seconds with {list_of_coins} coins.")
    sys.exit(0)

def rec_search(total, coin_combo, index):
    
    #base case
    if total == goal:
        end_time = time.time()
        duration = end_time - start_time
        print(f"\nWorking Combo {coin_combo} gets the goal of {goal} in {duration:.9f} seconds with {list_of_coins} coins.")
        sys.exit(0)  
        
    #fail case
    if total > goal:
        return
    
    #recurssive case
    for i in range(index, len(list_of_coins)): #does the next not done coin
        coin = list_of_coins[i]
        
        coin_MAX = min((goal - total) // coin, 20)
        for count in range(coin_MAX, 0, -1): #this will find all possible number of a specic coin that could be in the ideal combo. It will start with the most, and go down to the least. Makes it so we dont have to recheck a coin, because all possible options are ran in this for loop.
        
            rec_search(total + (coin * count), coin_combo + ([coin] * count), index + 1) #recursion
            
rec_search( 0 , [] , 0)

end_time = time.time()
duration = end_time - start_time
print(f"\nNo Solution found in {duration:.9f} seconds for goal {goal} with {list_of_coins} coins.")
sys.exit(1)  
    
