#CREATING THE SQUARES
Theboard={1:" ",2:" ",3:" ",
          4:" ",5:" ",6:" ",
          7:" ",8:" ",9:" "}

#DRAWING THE BOARD
def drawboard(Theboard):
    print(Theboard[1]+"|"+Theboard[2]+"|"+Theboard[3])
    print("-+-+-")
    print(Theboard[4]+"|"+Theboard[5]+"|"+Theboard[6])
    print("-+-+-")
    print(Theboard[7]+"|"+Theboard[8]+"|"+Theboard[9])


#2-PLAYER MODE
#GAME LOOP
def game():
    global Theboard
    drawboard(Theboard)
    count=0
    turn="X"

#GETTING A SQUARE AS INPUT
    for i in range(1,11):
        a=int(input("Your turn "+ turn +" where would you like to move ? "))
        if a>9:
            print("Square does not exist. Please give a valid square number")
            continue
        if Theboard[a]!=" ":
            print("This square is occupied. Please select another square")
            continue
        Theboard[a]=turn
        count+=1
        drawboard(Theboard)
#OUT OF MOVES CONDITION
        if count >= 9:
            print("Out of moves")
            print("It is tie")
            break
#CHECKING WETHER A PERSON HAS WON
        if count >=5:
            #BOTTOM HORIZONTAL
            if Theboard[7]==Theboard[8]==Theboard[9]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    break
                
            #MIDDLE HORIZONTAL
            elif Theboard[4]==Theboard[5]==Theboard[6]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
            #TOP HORIZONTAL    
            elif Theboard[1]==Theboard[2]==Theboard[3]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
            #RIGHT VERTICAL    
            elif Theboard[1]==Theboard[4]==Theboard[7]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
            #MIDDLE VERTICAL  
            elif Theboard[2]==Theboard[5]==Theboard[8]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
            #LEFT VERTICAL
            elif Theboard[3]==Theboard[6]==Theboard[9]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
            #DIAGONAL 1   
            elif Theboard[1]==Theboard[5]==Theboard[9]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
            #DIAGONAL 2    
            elif Theboard[3]==Theboard[5]==Theboard[7]!=" ":
                print("Game over")
                print("You win",turn)
                playagain=input("Would you like to play again ? Y/N ")
                if playagain=="Y" or playagain=="y":
                    for key in Theboard:
                        Theboard[key]=" "
                    drawboard(Theboard)
                    count=0
                else:
                    print("Thank you for playing")
                    break
                
        #SWITCHING TURNS OF PLAYERS       
        if turn=="X":
            turn="O"
        else:
            turn="X"

        
game()
        
