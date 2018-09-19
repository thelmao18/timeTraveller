#   Reitur 1,3     Reitur 2,3    Reitur 3,3
#   Reitur 1,2    |Reitur 2,2|   Reitur 3,2
#   Reitur 1,1    |Reitur 2,1|   Reitur 3,1
# Notandanum er gefið upplýsingar í hvaða átt hann getur fært sig í byrjun og
# eftir hverja hreyfingu. Þegar notandi færir sig slær hann inn fyrsta stafinn í þeirri
# átt sem hann ætlar í. Þá ætti hann að vera kominn á annan reit. Ef notandinn slær inn
# eitthvað vitlaust þá á kóðinn að prenta út "Not a valid direction!" og leyfir
# notandanum að reyna aftur. Þegar notandinn er kominn á reit 3,1 þá á kóðinn að láta
# hann vita að hann hefur unnið leikinn og á síðan að hætta.
(x,y) = (1,1)
valid_directions = 'nN'
victory = False

print("You can travel: (N)orth.")

while not victory:
    direction = input("Direction: ")
    if direction not in valid_directions:
        print("Not a valid direction!")
    else:
        if (direction == "n") or (direction == "N"):
            y += 1
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nNeEsS'
            elif (x,y) == (1,3):
                print("You can travel: (E)ast or (S)outh.")
                valid_directions = 'eEsS'
            else:
                print("You can travel: (S)outh or (W)est.")
                valid_directions = 'sSwW'
        elif (direction == "s") or (direction == "S"):
            y = y - 1  
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nNeEsS'
            elif (x,y) == (3,2):
                print("You can travel: (N)orth or (S)outh.")  
                valid_directions = 'nNsS'
            elif (x,y) == (3,1):
                victory = True
            else:
                print("You can travel: (N)orth.")
                valid_directions = 'nN'
        elif (direction == "e") or (direction == "E"):
            x += 1
            if (x,y) == (2,3):
                print("You can travel: (E)ast or (W)est.")
                valid_directions = 'eEwW'
            else:
                print("You can travel: (S)outh or (W)est.")
                valid_directions = 'sSwW'
        elif (direction == "w") or (direction == "W"):
            x = x - 1
            if (x,y) == (1,2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_directions = 'nNeEsS'
            elif (x,y) == (1,3):
                print("You can travel: (E)ast or (S)outh.")
                valid_directions = 'eEsS'
            elif (x,y) == (2,3):
                print("You can travel: (E)ast or (W)est.")
                valid_directions = 'eEwW'
print("Victory!")