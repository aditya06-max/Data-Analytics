import random 

def game_win(user , computer):
    if user == computer:
        return None
    
    #Snake vs Water
    if user == "s" and computer =="w":
        return True
    if user == "w" and computer =="s":
        return False
    
    #Water vs Gun
    if user == "w" and computer =="g":
        return True
    if user == "g" and computer =="w":
        return False
    
    #Snake vs Gun
    if user == "g" and computer =="s":
        return True
    if user == "s" and computer =="g":
        return False
        

rand_no = random.randint(1,3)#This will generate random integer between 1 and3

print("Computer turn: Snake(s) , Water(w) , Gun(g)  ")
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"

user = input("Your turn: Snake(s) , Water(w) , Gun(g) ").lower()

result = game_win(user,computer)
print(f"\nYou chose: {user}")
print(f"\nComputer chose: {computer}")

if result is None: #whenever we check equality with none we use "is" not "==" becuase none object in the python is in the memory 
    print("It's a draw")
elif(result):
    print("You Win! ")
else:
    print("You loose! ")
     
