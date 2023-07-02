import random
rock = '''
    ---------
----`   _ _ _)
       (_ _ _)
       (_ _ _)
       (_ _)
    `---(_)
'''

'huihjk'
"hgkjhkjl"
'''
kjbkui
lihoi
'''
# kugiup

paper = '''
     -------
----`    _ _ _)_ _
           _ _ _ _ _ _)
              _ _ _ _  _)
            _ _ _ _ _ _)
 ----` _ _ _ _ _ _ _ )          
'''
siccors='''
      _ _ _ _ _
-----`   _ _ _ )_ _ _
              _ _ _ _ )
        _ _ _ _ _ _ _ _ )
        (_ _ _ )
'''
game_images=[rock,paper,siccors]
user_choice=int(input("Enter your choice: type 0 for Rock, type 1 for Paper,type 2 for Scissor"))
if user_choice >= 3 or user_choice <0:
    print("You entered invalid number ,you lose.")
else:
     print(game_images[user_choice])
     computer_choice=random.randint(0,2)
     print("Computer Choice:")
     print(game_images[computer_choice])
     if computer_choice == user_choice:
         print("Its Draw")
     elif computer_choice==0 and user_choice==2:
          print("You won!!")
     elif computer_choice==2 and user_choice==0:
         print("You loose!")
     elif computer_choice > user_choice:
         print("You Lose!!")
     elif computer_choice < user_choice:
         print("You WON !!!")

