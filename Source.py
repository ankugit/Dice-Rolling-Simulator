import random
import time 
min=1
max=6

roll_again="yes"
while roll_again=="yes" or roll_again=="Yes" or roll_again=="Y" or roll_again=="y":
    print("Rolling the dice....")
    time.sleep(3)
    print("The values are....")
    time.sleep(1)
    print(random.randint(min, max))
    print(random.randint(min,max))
    time.sleep(1)
    roll_again=input("Roll the dices again ")
