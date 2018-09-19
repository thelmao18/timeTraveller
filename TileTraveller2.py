#   Reitur 1,3     Reitur 2,3    Reitur 3,3
#   Reitur 1,2    |Reitur 2,2|   Reitur 3,2
#   Reitur 1,1    |Reitur 2,1|   Reitur 3,1
# Notandanum er gefið upplýsingar í hvaða átt hann getur fært sig í byrjun og
# eftir hverja hreyfingu. Þegar notandi færir sig slær hann inn fyrsta stafinn í þeirri
# átt sem hann ætlar í. Þá ætti hann að vera kominn á annan reit. Ef notandinn slær inn
# eitthvað vitlaust þá á kóðinn að prenta út "Not a valid direction!" og leyfir
# notandanum að reyna aftur. Þegar notandinn er kominn á reit 3,1 þá á kóðinn að láta
# hann vita að hann hefur unnið leikinn og á síðan að hætta.
# 1. Which implementation was easier and why?
    # For me the first implementation was way easier to make because I 
    # could make it from scratch without having to think about another code, 
    # which I had to do with the second implementation.
# 2. Which implementation is more readable and why?
    # I would think that the second implementation is more readable because 
    # it has a function in it and isn't all chrushed together in one loop.
# 3. Which problems in the first implementations were you able to solve with the latter implementation?
    # None. I did not solve anything in the first implementation with the latter implementation. Read question one.

x = 1
y = 1
valid_directions = 'n'
victory = False

def Directions(direction, valid_directions):  
    if direction in valid_directions:
        global x
        global y
        if direction == "n":
            y = y + 1
            return y
        elif direction == "s":
            y = y - 1
            return y
        elif direction == "e":
            x = x + 1
            return x
        elif direction == "w":
            x = x - 1
            return x

print("You can travel: (N)orth.")

while not victory:  
    direction = input("Direction: ")
    direction = direction.lower()
    Directions(direction, valid_directions)
    if direction not in valid_directions:
        print("Not a valid direction!")
    else:    
        if direction == "n":
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nes'
            elif (x,y) == (1,3):
                print("You can travel: (E)ast or (S)outh.")
                valid_directions = 'es'
            else:
                print("You can travel: (S)outh or (W)est.")
                valid_directions = 'sw'
        elif direction == "s":
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nes'
            elif (x,y) == (3,2):
                print("You can travel: (N)orth or (S)outh.")  
                valid_directions = 'ns'
            elif (x,y) == (3,1):
                victory = True
            else:
                print("You can travel: (N)orth.")
                valid_directions = 'n'
        elif direction == "e":
            if (x,y) == (2,3):
                print("You can travel: (E)ast or (W)est.")
                valid_directions = 'ew'
            else:
                print("You can travel: (S)outh or (W)est.")
                valid_directions = 'sw'
        elif direction == "w":
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nes'
            elif (x,y) == (1,3):
                print("You can travel: (E)ast or (S)outh.")
                valid_directions = 'es'
            elif (x,y) == (2,3):
                print("You can travel: (E)ast or (W)est.")
                valid_directions = 'ew'
print("Victory!")