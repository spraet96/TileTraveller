#Leikmaður fær upp valmöguleika um átt sem hann getur farið í og hann þarf að reyna að velja rétta átt til að sigra.
#Stundum er bara ein leið í boði en allt að 3 leiðir í einu geta verið í boði.
#Ef leikmaður velur átt sem er ekki í boði, þá fær hann upp "Not a valid direction!"

N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

x_pos,y_pos = 1,1
direction = ""
valid = ('')



def move(x_pos,y_pos,direction):
    if direction.lower() == 'n':
        return x_pos,y_pos +1
    elif direction.lower() == 's':
        return x_pos,y_pos -1
    elif direction.lower() == 'e':
        return x_pos +1,y_pos
    elif direction.lower() == 'w':
        return x_pos -1,y_pos



while True:
    if direction.lower() in valid:

        if (x_pos == 1 and y_pos == 1)  or  (x_pos == 2 and y_pos == 1):
            print("You can travel: {}.".format(N))
            valid = ('n')
        elif (x_pos == 1 and y_pos == 2):
            print("You can travel: {} or {} or {}.".format(N,E,S))
            valid = ('n', 'e', 's')
        elif (x_pos == 2 and y_pos == 2) or (x_pos == 3 and y_pos == 3):
            print("You can travel: {} or {}.".format(S,W))
            valid = ('s', 'w')
        elif (x_pos == 1 and y_pos == 3):
            print("You can travel: {} or {}.".format(S,E))
            valid = ('s', 'e')
        elif (x_pos == 2 and y_pos == 3):
            print("You can travel: {} or {}.".format(W,E))
            valid = ('w', 'e')
        elif (x_pos == 3 and y_pos == 2):
            print("You can travel: {} or {}.".format(N,S))
            valid = ('n', 's')
        elif (x_pos == 3 and y_pos == 1):
            print('Victory!')
            exit()
            


    direction = (input("Direction: "))
    if direction.lower() in valid:
        x_pos,y_pos = move(x_pos,y_pos, direction)
    else:
        print('Not a valid direction')

    
   

     
            


