#Rock paper scissors game:-
import random
l=['Rock','Paper','Scissors']
while True:
    ccount=0
    ucount=0
    uc=int(input('''
#for satarting the game press the key 1 and for existing press 2
 game start
 1 yes
 2 N0 | exist 
'''))
    if uc==1:
        pass
    for a in range(1,6):
        userinput=int(input('''
#Entering the key and choose option --- 1,2,3.
1 Rock
2 Paper
3 Scissor                          
    '''))
        
        if userinput==1:
            uchoice="Rock"
            
        elif userinput==2:
            uchoice="Paper"
            
        elif userinput==3:
            uchoice="Scissor"
            
        cchoice=random.choice(l)
        if uchoice==cchoice:
            
            print("Computer Value:-",cchoice)
            
            print("User Value:-",uchoice)
            
            print("Game Drow---")
            
            ucount=ucount+1
            ccount=ccount+1
        elif(uchoice=="Rock" and cchoice=="Scissor") or (uchoice=="Paper" and cchoice=="Rock") or (uchoice=="Scissor" and cchoice=="Paper"):
            
            print("Computer Value:-",cchoice)
            
            print("User Value:-",uchoice)
            
            print("You Win")
            ucount=ucount+1
        else:
             print("Computer Value:-",cchoice)
             print("User Value:-",uchoice)
             print("Computer Win")
             ccount=ccount+1
    if ucount==ccount:
        print("Fanaly Game Draw")
        print("User Score",ucount)
        print("Computer Score",ccount)
    elif ucount>ccount:
        print("User Score:-",ucount)
        print("Computer Score:-",ccount)
        print("Fanaly you win the Game!")
        
    else:
        print("User Score:-",ucount)
        print("Computer Score:-",ccount)
        print("Fanaly computer win the game")
        
else:
    pass   