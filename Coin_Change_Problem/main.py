
import fontstyle
import time
from easygui import *
# format text
count = 0
while True:    
    list = ["Coin Change Problem","Enter your target goal: ","Enter your available coin denominations: ","Current time is :"]
    coin_change_problem = fontstyle.apply(list[count], 'red')
    print(coin_change_problem)
    time.sleep(1)    
    def user_input():
       coin_change_problem = fontstyle.apply(list[count+1], 'green')
       target_amount = input(coin_change_problem)
       coin_change_problem = fontstyle.apply(list[count+2], 'green')
       available_coin_denominations = input(coin_change_problem)
       import time
       curr = time.time()
       csurr = time.ctime(curr)
       coin_change_problem = fontstyle.apply(list[count+3], 'purple')
       coin_change_problems = fontstyle.apply(csurr, 'yellow')
       print(coin_change_problem,coin_change_problems)
      
       user_input()
   