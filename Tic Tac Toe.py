import random

tictactoe = [[0,0,0], [0,0,0], [0,0,0]]
row = 0
column = 0
gameon = 0
player = 0
playeron = 0
retry = 0
low = 1
high = 2
headortail = 0
usrnumber = 0

print ("Columns")
print (" 1  2  3 ")
print (tictactoe[0], str(1))
print (tictactoe[1], str(2), " Rows")
print (tictactoe[2], str(3))

print ("\n")

while (playeron == 0):
	player = str(input("Which player are you? X or O? \nOr would you like to press R for roll? "))

	if player == 'x':
		player = 'X'
		playeron = 1
	elif player == 'o':
		player = 'O'
		playeron = 1
	elif player == 'O':
		playeron = 1
	elif player == 'X':
		playeron = 1
	elif player == 'R' or 'r':
            headortail = str(input("Heads(H) or Tails(T)? "))
           	
            if headortail == 'H' or 'h' or 'heads' or 'Heads':
                usrnumber = random.randint(low, high)
                if usrnumber == 1:
                    print ("Heads! \n You will go first with X")
                    player = 'X'
                    playeron = 1
                else:
                    print ("Tails! \n You will go second with O")
                    player = 'O'
                    playeron = 1
            elif headortail == 'T' or 't' or 'tails' or 'Tails':
                usrnumber = random.randint(low, high)
                if usrnumber == 1:
                    print ("Tails! \n You will go first with X")
                    player = 'X'
                    playeron = 1
                else:
                    print ("Heads! \n You will go second with O")
                    player = 'O'
                    playeron = 1
            else:
           	    playeron = 0
           	    print ("Invalid Input\n")
	else:
		print ("Invalid Input\n")

	print ("\n")

while (gameon == 0):
	retry = 0
	if player == 'X':
		print ("Go player X")
	elif player == 'O':
		print ("Go player O")
	
	row = int(input("What row would you like? \n"))
	column = int(input("What column would you like? \n"))
	
	if (1 > column or 3 < column):
           retry = 1
           print ("Wrong Number for Column")
	if (1 > row or 3 < row):
           retry = 1
           print ("Wrong Number for Row")
           


	while (retry == 0): 
   	    row = row - 1
   	    column = column - 1
   	    print ("\n")
   	    if (tictactoe[row][column] == 'O' or tictactoe[row][column] == 'X'):
           	print ("Someone is already there!")
           	retry = 1
   	    else:
           	tictactoe[row][column] = player
        
   	    print ("Columns")
   	    print (" 1  2  3 ")
   	    print (tictactoe[0], str(1))
   	    print (tictactoe[1], str(2), " Rows")
   	    print (tictactoe[2], str(3))
        
   	    print ("\n")
   	    if (tictactoe[0][0] == 'X' and tictactoe[0][1] == 'X' and tictactoe[0][2] =='X'):
                print ("Player " + player + " Wins!")
                gameon = 1		
   	    elif (tictactoe[0][0] == 'O' and tictactoe[0][1] == 'O' and tictactoe[0][2] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[1][0] == 'X' and tictactoe[1][1] == 'X' and tictactoe[1][2] =='X'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[1][0] == 'O' and tictactoe[1][1] == 'O' and tictactoe[1][2] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[2][0] == 'O' and tictactoe[2][1] == 'O' and tictactoe[2][2] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[2][0] == 'X' and tictactoe[2][1] == 'X' and tictactoe[2][2] =='X'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][0] == 'O' and tictactoe[1][0] == 'O' and tictactoe[2][0] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][0] == 'X' and tictactoe[1][0] == 'X' and tictactoe[2][0] =='X'):
           	print (" Player" + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][1] == 'X' and tictactoe[1][1] == 'X' and tictactoe[2][1] =='X'):
           	print (" Player" + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][1] == 'O' and tictactoe[1][1] == 'O' and tictactoe[2][1] =='O'):
           	print (" Player" + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][2] == 'X' and tictactoe[1][2] == 'X' and tictactoe[2][2] =='X'):
           	print (" Player" + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][2] == 'O' and tictactoe[1][2] == 'O' and tictactoe[2][2] =='O'):
           	print (" Player" + player + " Wins!")
           	gameon = 1
        
   	    elif (tictactoe[0][0] == 'O' and tictactoe[1][1] == 'O' and tictactoe[2][2] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[0][0] == 'X' and tictactoe[1][1] == 'X' and tictactoe[2][2] =='X'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[2][0] == 'O' and tictactoe[1][1] == 'O' and tictactoe[0][2] =='O'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
   	    elif (tictactoe[2][0] == 'X' and tictactoe[1][1] == 'X' and tictactoe[0][2] =='X'):
           	print ("Player " + player + " Wins!")
           	gameon = 1
	if player == 'X':
	    if (retry == 0):
	        player = 'O'
	    else:
 	       player = 'X'
	elif player == 'O':
 	   if (retry == 0):
	        player = 'X'
 	   else:
	        player = 'O'
            