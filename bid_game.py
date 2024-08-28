print("Bidding is now open!")
import os
logo=''' |\
         /  |         
        |  /          
        _\|__         
       |     |        
   __X-|     |-X__    
 /~    |     |     \  
X      |     |      X
       |     |     /
   _X-----X----X ~    
 /     |     |
X      |     |      X 
 \     |     |    _/  
   X~--|     |-X~~    
       |_    |        
         ~--_|'''
print(logo)
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
list_of_bids = []
makebids="yes"
makebids=input("Do you want to make a bid? Type 'yes' or 'no'")
while makebids == "yes":
  clear_screen()
  print(logo)
  name=input("enter your name: ")
  bid=int(input("enter your bid: "))
  list_of_bids.append({"name": name, "bid": bid})
  makebids=input("Are there any other bidders Type yes or no: ")
highest_bid = max(list_of_bids, key=lambda x: x["bid"])#takes max from list of bids in terms of bid
clear_screen()
print(f"The winner is {highest_bid['name']} with a bid of ${highest_bid['bid']}")