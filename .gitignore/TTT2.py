

                                                 #***TIC_TAC_TOE GAME CODED BY : RIYAZ UL HAQUE***


import socket

class CONNECTION():

	#DEFINED CLASS FOR GAME  WHICH INCLUDES CONNECTION ESTABLISHMENT REQUIREMENTS
	def __init__(self):
		self.serversock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		
	#BINDING SOCKET TO A PARTICULAR PORT IN HOST MACHINE
	def bind(self):
		port = 1234
		self.serversock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)
		self.serversock.bind(('0.0.0.0' , port))
		self.serversock.listen(2)
		
	
	#ACCEPT THE CONNECTION REQUEST
	def accept(self):
		(clientsocket , address) = self.serversock.accept()
		return clientsocket
		
		
	#CONNECT TO THE HOST AND PORT OF THE OTHER
	def connect(self , host , port):
		self.serversock.connect((host , port))
		
		
	#SEND METHOD
	def send(self , msg):
		self.serversock.send(msg)
		
		
	#RECEIVE METHOD
	def receive(self):
		return self.serversock.recv(1024)
		
		
	#STOP 
	def stop(self):
		print "**GAME OVER**"
		print "THANK YOU FOR PLAYING TIC_TAC_TOE GAME"
		self.serversock.close()
		
		
		
	#BASIC FUNCTION REQUIREMENTS
	def Instruction(self):    #DISPLAYS THE GAME INSTRUCTIONS
		print(
    """

    **WELCOME TO THE**
         	
 
 ________   _   ______             _________   ______    ______             _________    _______    ________
/___  ___\ / \ /   ___/           /___   ___\ /  __  \  /  ____/           /___   ___\  /  ___  \  /   _____\  
   / \     | | |  /       _____       / \     |  __  | |  /        ______      / \     |  /   \  | |   \     
   | |     | | |  \___    \_____\     | |     | |  | | |  \____    \_____\     | |     |  \___/  | |   /____
   \_/     \_/ \______\               \_/     \_/  \_/  \______\               \_/      \_______/   \________\
   
   
    **GAME** CODED BY: RIYAZ-UL-HAQUE					 
    THIS IS A MULTIPLAYER TIC_TAC_TOE GAME   	
      
    INSTRUCTIONS:
	1: YOU CAN MAKE YOUR MOVE BY ENTERING A NUMBER IN BETWEEN 0-8. 
	2: THE NUMBER WILL CORRESPOND TO THE BOARD POSITION AS ILLUSTRATED.
    
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
	
	3: CONDITION OF WINNING THE GAME:
	   WINNER WILL BE DECIDED ON THE BASIS OF WHOEVER SO FIRST FILL THEIR RESPECTIVE SIGN ON THE BOARD'S POSITION
	   THREE CONSECUTIVE IN A ROW OR IN COLUMN OR EITHER IN DIAGONAL.
	4: PLAY WITH YOUR BEST MOVES.
					
		   
    """
		)
	
	



	#DECLARATION OF VARIABLE GLOBALLY
	X="X"
	O="O"
				
	
	def CHOOSE_PLAYER_1(self,Board):   #FUNCTION ALLOW THE PLAYER(1) TO CHOOSE THEIR SPOT ON THE BOARD
		global select
		valid_move=False
		valid = [0,1,2,3,4,5,6,7,8]   
		while(not valid_move):
				select=int(raw_input("PLEASE SELECT YOUR CHOICE TO MAKE A MOVE BETWEEN 0 To 8 :\n>"))
				if (select) not in valid:
					print "PLEASE ENTER VALID INPUT PLAYER(1)"
					continue
				if (Board[select]=='X' and Board[select]=='O'):
					print "SORRY THE POSITION ON THE BOARD HAS ALREADY BEEN TAKEN!! TRY OTHER"	
					continue
				if (Board[select]!='X' and Board[select]!='O'):
					Board[select]='X'
					valid_move=True
				

	def CHOOSE_PLAYER_2(self,Board):   #FUNCTION ALLOW THE PLAYER(2) TO CHOOSE THEIR SPOT ON THE BOARD
		global reply
		valid_move=False
		valid = [0,1,2,3,4,5,6,7,8]
		while(not valid_move):
			reply=int(raw_input("PLEASE SELECT YOUR CHOICE TO MAKE A MOVE BETWEEN 0 To 8 :\n>"))
			if (reply) not in valid:
				print "PLEASE ENTER VALID INPUT PLAYER(2)"
				continue
			if (Board[reply]=='X' and Board[reply]=='O'):
				print "SORRY THE POSITION ON THE BOARD HAS ALREADY BEEN TAKEN!! TRY OTHER"	
				continue
			if (Board[reply]!='X' and Board[reply]!='O'):
				Board[reply]='O'
				valid_move=True
			




#MAIN_BODY OF THE GAME
def main():
	Board=[0,1,2,
		   3,4,5,
		   6,7,8]
	def show(Board): 	#DISPLAY_GAME BOARD
		
		print  "-- -- -- -- -- -- "
		print '||' , Board[0] , '||' , Board[1] , '||' , Board[2] , '||'
		print  "-- -- -- -- -- -- "	
		print '||' , Board[3] , '||' , Board[4] , '||' , Board[5] , '||'
		print  "-- -- -- -- -- -- "
		print '||' , Board[6] , '||' , Board[7] , '||' , Board[8] , '||'
		print  "-- -- -- -- -- -- "
	
	
	def WON(x,y):       #FUCTION THAT DEFINES ALL CONDITION OF WINNING THE GAME
		return ((x[0] == y and x[1] == y and x[2] == y) or 
		(x[3] == y and x[4] == y and x[5] == y) or
		(x[6] == y and x[7] == y and x[8] == y) or
		(x[0] == y and x[3] == y and x[6] == y) or
		(x[1] == y and x[4] == y and x[7] == y) or
		(x[2] == y and x[5] == y and x[8] == y) or
		(x[0] == y and x[4] == y and x[8] == y) or
		(x[2] == y and x[4] == y and x[6] == y))
	  
	  
	player1=CONNECTION()#CLASS OBJECT CREATED    
	first=raw_input("DO YOU WANT TO BE THE SERVER **YES(Y)\NO(N)**\n>")
	if first=="Y":
		print" WAITING FOR THE CLIENT TO CONNECT"
		player1.bind()  
		p2=player1.accept()
		player1.Instruction()
		reply ='init'		
		
		
		#ASKING FOR WHO WANTS TO GO FIRST		
		
		FIRST=raw_input(" START THE GAME BY PRESSING : **Y** \n>")
		if FIRST=="Y":
			print "**GREAT YOU ARE THE PLAYER(1) AND YOU ARE PLAYING WITH Xs**"
	
		show(Board)
		p2.send(str(FIRST))
				
				
			#FUNCTION ALLOW THE PLAYER(HUMAN) TO CHOOSE THEIR SPOT ON THE BOARD
		if FIRST =="Y":
			global select
			valid_move=False
			turn = 0
			
			while (turn < 9) and (not valid_move):			
					player1.CHOOSE_PLAYER_1(Board)
				
					turn+=1
					show(Board)
					if WON( Board , 'X' ):
						print "CONGRATULATIONS PLAYER(1) ** YOU WON**"
						break ;
					elif turn == 5:
						print "WELL TRIED ITS A TIE"
						break ;
		
		
					p2.send(str(select))
					print "WAITING FOR THE PLAYER(2) TO MAKE A MOVE..."	
					reply=p2.recv(1024)
				 
					reply = int(reply)
					Board[reply]="O"
				
					print 'PLAYER(2) MADE A MOVE AT:' + str(reply)
					show(Board)
				
					if WON(Board , 'O'):
						print "BETTER LUCK NEXT TIME PLAYER(2)**WON**"
						break ;
					elif turn == 5:
						print "WELL TRIED ITS A TIE"
						break ;
		
			p2.send(str(select))
			p2.close()
			player1.stop()
	
	elif first =="N":
		p2=raw_input("ENTER THE ADDRESS OF THE HOST TO WHICH YOU WANT TO CONNECT:")
		player1.connect(p2, 1234)
		player1.Instruction()
			
	
		FIRST = player1.receive()
	
		if FIRST == "Y":
			print " PLAYER(1) WILL START THE GAME AND GOING TO PLAY WITH **Xs**"

		show(Board)	
		
		
		
		global reply
		turn = 0
		valid_move = False
		while (turn < 9 ) and (not valid_move):
			turn +=1
			print "WAITING FOR THE PLAYER(1) TO MAKE A MOVE ..."
			select = player1.receive()
			select=int(select)
			print "PLAYER(1) MADE A MOVE AT :" + str(select)
			Board[select]= "X"
		
			show(Board)
	
			if WON(Board , 'X'):
				print "PLAYER(1) WON"
				break ;
			elif turn == 5:
				print "WELL TRIED ITS A TIE"
				break ;
	 
			player1.CHOOSE_PLAYER_2(Board)
			show(Board)
			
			
			if WON(Board , 'O'):
				print "CONGRATULATIONS PLAYER(2) **YOU WON**"
				break;
			elif turn == 5:
				print 'WELL TRIED ITS A TIE'
				break;
		
			
			reply = str(reply)
			player1.send(reply)
		reply = str(reply)	
		player1.send(reply)
		player1.stop()
			
	else:
		print "PLEASE ENTER THE VALID REQUIRE INPUT"
		main()
	def ask():     #FUNCTION CREATED TO ASK IF YOU TO PLAY AGAIN
		print"FOR PLAYING AGAIN **PLEASE READ THE FOLLOWING INSTRUCTIONS**"
		QUESTION=raw_input("DO YOU WANT TO PLAY AGAIN IF YES PRESS 'Y' ELSE PRESS 'N': \n>")
		if QUESTION=="Y":
			main()             #CALL TO MAIN FUNCTION
		elif QUESTION=="N":
			input("QUIT BY PRESSING ENTER")
	ask()
	
	
main()        #CALLING OF MAIN FUCTION


			
