#Use some encoding, probably like base64 to convert saved binary from picke to ascii text or save the
#datatypes as they are to save all progress and level  dictionary together with this script while being
#able to update them as needed as well

#Use terminal background coloring with blank spaces instead of the solid blocks used to print the level
#matrix
#Utilize blessed.Terminal.center(string)
from pickle import dump,load #To read/write level dictionary, save or load progress
from os import path #To save or load progress from a file
from copy import deepcopy #To create an independent copy of avariable
from blessed import Terminal #To take key input and use UI elements
from time import sleep #To show save message and animation on tiles match
level_dictionary={} #LEVEL DICTIONARY
level_dictionary={
	1: [['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']],
	2: [['R', 'R', 'Y', 'R'], ['Y', 'Y', '0', 'R'], ['Y', 'B', '0', '0'], ['B', 'B', '0', 'B']],
	3: [['R', 'Y', 'Y', 'R'], ['0', 'Y', 'R', 'B'], ['Y', '-1', 'R', '0'], ['0', 'B', 'B', 'B']],
	4: [['R', 'R', 'R', '-1'], ['0', 'B', 'B', 'Y'], ['-1', 'B', 'Y', 'R'], ['Y', '0', 'B', 'Y']],
	5: [['B', '-1', 'R', 'Y'], ['B', '-1', 'R', 'R'], ['B', 'Y', 'Y', '0'], ['0', 'B', 'Y', 'R']],
	6: [['0', 'B', 'B', '0', '0'], ['0', 'B', 'O', 'R', '0'], ['B', '-1', 'R', 'Y', '-1'], ['-1', 'O', 'Y', '0', 'Y'], ['O', 'O', 'R', 'R', 'Y']],
	7: [['B', 'B', 'O', 'O', '0'], ['O', '-1', 'B', 'B', 'R'], ['0', 'Y', 'O', '0', 'R'], ['Y', 'Y', 'R', '-1', 'R'], ['0', '0', 'Y', '-1', '0']],
	8: [['0', '0', 'C', 'C', '0', 'Y'], ['0', 'O', 'O', '0', 'O', 'Y'], ['O', 'B', 'Y', 'B', 'Y', '-1'], ['B', 'C', 'B', '-1', '0', '0'], ['C', '-1', '-1', '0', '0', '0'], ['R', 'R', '0', 'R', 'R', '0']],
	9: [['0', '0', 'Y', '0', 'Y', '0'], ['-1', '0', '0', 'Y', '0', 'Y'], ['B', '-1', 'B', '0', '0', 'C'], ['B', 'B', 'C', 'R', 'O', 'O'], ['R', 'C', 'C', '-1', '0', 'O'], ['R', 'R', '0', '-1', 'O', '0']],
	10: [['0', '0', 'O', 'O', 'V', '0', '0'], ['0', 'V', '0', '0', '0', '0', 'O'], ['0', '0', '-1', '0', 'Y', 'O', '0'], ['B', 'B', 'V', 'C', '0', '-1', '-1'], ['B', '0', 'V', 'R', 'Y', 'Y', 'R'], ['0', 'B', 'R', '0', 'Y', '-1', 'R'], ['0', '0', '-1', '0', 'C', 'C', 'C']],
	11: [['-1', 'C', 'C', 'B', '-1', '0', '0'], ['O', 'C', '-1', '0', '-1', '0', '0'], ['0', 'O', '0', 'C', 'B', '0', 'B'], ['0', '0', 'Y', 'O', 'B', '0', '0'], ['Y', 'Y', 'R', 'O', '-1', '0', '0'], ['0', '0', 'Y', 'R', 'V', 'V', 'V'], ['R', '0', '0', 'V', 'R', '0', '0']],
	12: [['Y', 'G', 'G', '-1', 'B', '0', 'O', '0'], ['0', '0', '0', '0', '0', 'B', 'Y', 'O'], ['Y', 'C', 'G', '-1', 'B', 'B', 'O', 'O'], ['0', '0', 'Y', '0', 'R', 'C', 'C', 'G'], ['V', '-1', '0', 'R', '0', 'R', 'C', '0'], ['0', '0', '0', '0', 'R', 'V', 'V', '0'], ['V', '-1', '-1', '-1', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']],
	13: [['0', '0', '0', '0', '0', 'G', 'O', '0'], ['0', '0', '0', 'G', '0', 'G', 'V', '0'], ['0', 'R', 'B', '0', 'G', 'O', 'Y', '-1'], ['0', '0', '0', '0', '0', 'Y', '0', 'V'], ['0', 'B', 'B', '0', '-1', 'Y', 'Y', 'V'], ['0', '0', 'R', 'R', 'C', '0', 'V', 'O'], ['R', '0', '0', '0', 'C', '0', 'C', 'C'], ['-1', '-1', '0', '0', 'C', '-1', '-1', 'O']]
	}
	# mapping formats the level matrix
mapping = {
	'R':  "\033[31m{0}\033[0m",       # Red
	'Y':  "\033[33m{0}\033[0m",       # Yellow
	'B':  "\033[34m{0}\033[0m",       # Blue
	'C':  "\033[36m{0}\033[0m",       # Cyan
	'V':  "\033[38;5;129m{0}\033[0m", # Violet (256-color code 129)
	'G':  "\033[38;5;244m{0}\033[0m", # Grey (256-color code 244)
	'O':  "\033[38;5;208m{0}\033[0m", # Orange (256-color code 208)
	'-1': "\033[37m{0}\033[0m",       # White
	'0':  " " #"{0}"                  # No color (Space)
	} # If making changes to mapping, do update mappings string
filename="/sdcard/level_dictionary.dict" #Level dictionary in a file
if path.exists(filename): #Load level dictionary from file
    with open(filename, 'rb') as file:
        level_dictionary = load(file)
#else:
#    with open(filename, 'wb') as file:
#        dump(level_dictionary,file)
#        exit()
def check_for_integer(string): #Check if 'string' is an integer
	try:
		integer=int(string)
		return integer
	except ValueError:
		return string
def matrix_length_breadth_handler(): #Interactively takes new matrix length and breadth
	while True:
		print("\rEnter Board Length (0 to exit): ",end="",flush=True)
		matrix_length=input()
		matrix_length=check_for_integer(matrix_length)
		if type(matrix_length)!=int:
			continue
		elif matrix_length<3: #Seperate condition statement as the if condition ensures other statements get only an integer to check
			print("Board Length should be at least 3.")
			continue
		else:
			if matrix_length==0:
				exit()
			break
	while True:
		print("\rEnter Board Breadth (0 to exit) [",matrix_length,"]: ",sep="",end="",flush=True)
		matrix_breadth=input()
		if len(matrix_breadth.split())==0: #Split function is used because the script should not care if the input only contains blank spaces
			matrix_breadth=int(matrix_length)
			break
		matrix_breadth=check_for_integer(matrix_breadth)
		if type(matrix_breadth)!=int:
			continue
		elif matrix_breadth<3:
			print("Board Breadth should be at least 3.")
			continue
		else:
			if matrix_breadth==0:
				exit()
			break
	return (matrix_length,matrix_breadth)
def make_level_matrix(level,ml,mb): #Older, non-interactive implementation to make level matrix
	#Make it directly interactive, allow and show changes to the matrix in real time, with current selection highlighting
	global m #LEVEL MATRIX
	while True:
		m=[]
		for column in range(ml):
			line=[0]*mb
			for element in range(mb):
				print("Enter positional color for",column+1,"x",element+1,": ",end="")
				pn=(input())
				if pn.isalpha():
					pn=pn.upper()
				line[element]=pn
			m.append(line)
		cont=""
		while True:
			for element in m:
				print(element)
			cont=input("Continue(Y) Retry(N) ? ")
			if cont.isalpha():
				cont=cont.upper()
			if cont=="Y":
				level_dictionary[level]=m
				with open(filename, 'wb') as file:
					dump(level_dictionary, file)
				break
			elif cont=="N":
				break
		if cont=="Y":
			break
def read_levels(level_dictionary): #Old implementation to print the matrix
	for level in level_dictionary.keys():
		print("LEVEL:",level)
		for row in level_dictionary[level]:
			print("-"*(len(row)*5+1),"\n|",end="")
			for element in row:
				print("",mapping[element]*2,"|",end="")
			print()
		print("-"*(len(row)*5+1))
def add_level(): #Level matrix addition entry point
	read_levels(level_dictionary)
	while True:
		level=int(input("Enter Level Number (0 to exit): "))
		if level==0:
			break
		ml=int(input("Board Length: "))
		mb=int(input("Board Breadth: "))
		make_level_matrix(level,ml,mb)
def new_read_levels(level,matrix_dimensions,pointer_location,input_alphabet,level_matrix): #Print live changes to the level matrix
#	if matrix_length==0 and matrix_breadth==0:
	term=Terminal()
	matrix_length,matrix_breadth=matrix_dimensions
	if input_alphabet.isalpha():
		input_alphabet=input_alphabet.upper()
	print(term.clear + term.home) # Clear the screen and move to Top-Left
#	print("\033c",end="",flush=True)
	print("Use the arrow keys to navigate between rows, columns and special options")
	if level in level_dictionary.keys():
		print("EDITING: Level",level)
	else:
		print("ADDING: New Level",level)
	print("Board Dimensions (LENGTH×BREADTH) : ",matrix_length,"×",matrix_breadth,sep="")
	mappings="""Available Keys and their Mapping:
R :  \033[31m██\033[0m    # Red
Y :  \033[33m██\033[0m    # Yellow
B :  \033[34m██\033[0m    # Blue
C :  \033[36m██\033[0m    # Cyan
V :  \033[38;5;129m██\033[0m    # Violet (256-color code 129)
G :  \033[38;5;244m██\033[0m    # Grey (256-color code 244)
O :  \033[38;5;208m██\033[0m    # Orange (256-color code 208)
-1:  \033[37m██\033[0m    # White
0 :  " "   # No color (Space)"""
#	block="▒" #"▓"
	print(mappings)
	len_row=len(level_matrix[0])
	for row in range(len(level_matrix)):
		print("-"*(len_row*5+1),"\n|",end="")
		for column in range(len_row):
			if (row,column)==pointer_location:
				if input_alphabet not in mapping.keys():
					print("",(mapping[level_matrix[row][column]].format("▒"))*2,"|",end="")
				else:
					print("",(mapping[input_alphabet].format("▒"))*2,"|",end="")
			else:
				print(" ",(mapping[level_matrix[row][column]].format("█"))*2," |",sep="",end="")
		print()
	print("-"*(len_row*5+1))
#	print("[SAVE]"," "*((len_row-2)*3//2),"[RESET]"," "*((len_row-2)*3//2),"[EXIT]",sep="")
#	print(" "*((len_row-2)*3//2),"[SAVE]"," "*((len_row-2)*3//2),"[EXIT]",sep="")
	if pointer_location==(len_row+1,0):
		print("\033[47;30m","[SAVE]","\033[0m"," "*((len_row-2)*3//2),"[RESET]"," "*((len_row-2)*3//2),"[BACK]",sep="")
	elif pointer_location==(len_row+1,1):
		print("[SAVE]"," "*((len_row-2)*3//2),"\033[47;30m","[RESET]","\033[0m"," "*((len_row-2)*3//2),"[BACK]",sep="")
	elif pointer_location==(len_row+1,2):
		print("[SAVE]"," "*((len_row-2)*3//2),"[RESET]"," "*((len_row-2)*3//2),"\033[47;30m","[BACK]","\033[0m",sep="")
'''for level in level_dictionary.keys():
	for inp in range(3):
		new_read_levels(level,(len(level_dictionary[level]),len(level_dictionary[level][0])),(0,0),(0,0),"",level_dictionary[level]) #len(level_dictionary[level][-1])+1,inp),"",level_dictionary[level])
		input()
		break
exit()'''
def trim_matrix(level,keep_rows,keep_cols,level_matrix): #To trim an already existing matrix
    term=Terminal()
    # Total Matrix Dimensions
    max_rows = len(level_matrix)
    max_cols = len(level_matrix[0])
    # Selection Window Origin (Top-Left Corner)
    # Ensuring the window fits within the matrix
    curr_r = 0
    curr_c = 0
    # Keep dimensions (clamped to matrix size just in case)
    k_rows = min(keep_rows, max_rows)
    k_cols = min(keep_cols, max_cols)
    focus = 'matrix' # 'matrix' or 'buttons'
    btn_idx = 0      # 0 for TRIM, 1 for BACK
    tab_count=0
    get_back="n"
    return_trimmed="n"
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
             print(term.clear + term.home) # Clear the screen and move to Top-Left
#            print("\033c",end="",flush=True)
             print("TRIMMING LEVEL BOARD: Level",level)
             print("Original Board Dimensions (LENGTH×BREADTH) : ",max_rows,"×",max_cols,sep="")
             print("New Board Dimensions (LENGTH×BREADTH) : ",keep_rows,"×",keep_cols,sep="")
             print("Use The Arrow Keys to Select The Area to Keep After Trimming, Press TAB key to choose among the Options, Press ENTER key to select\n")
#            print("Arrows: Move Window | TAB: Toggle Focus | ENTER: Select\n")
            # --- Render Matrix ---
             for row in range(max_rows):
                 print("-" * ((max_cols *5)+1),"\n|",end="")
                 line = ""
                 for column in range(max_cols):
                     val = (mapping[level_matrix[row][column]])
                     # Check if current cell is within the selection window
                     is_in_window = (curr_r <= row < curr_r + k_rows and curr_c <= column < curr_c + k_cols)
                     if is_in_window:
                          line += " "+(val.format("█"))*2+" |"
                     else:
                          if level_matrix[row][column]=="0":
                              line += " ░░ |"
                          else:
                              line += " "+(val.format("▒"))*2+" |"
                 print(line)

             print("-" * ((max_cols * 5)+1))

            # --- Render Buttons ---
             btns = ["TRIM", "BACK"]
             btn_line = "   "
             for index in range(len(btns)):
                 if focus == 'buttons' and btn_idx == index:
                     btn_line+=" "*((max_cols*1)-2)
                     btn_line += term.black_on_white("[" + btns[index] + "]")
                 else:
                     btn_line += " "*((max_cols*1)-2) + btns[index]
             print(btn_line.center(max_cols*2))
             if get_back=="y":
                 print("CONFIRMATION: The Current Changes Won't Be Saved, Do you still want to go to the previous menu (Y/N) ? ")
             elif return_trimmed=="y":
                 print("CONFIRMATION: Do you want to save the changes (Y/N) ? ")
            # --- Input Handling ---
             key = term.inkey()

             if key.name == 'KEY_TAB':
                 tab_count+=1
                 if focus == "matrix":
                     focus = 'buttons'
                 else:
                     if tab_count ==1:
                         focus="buttons"
                         btn_idx=0
                         continue
                     elif tab_count == 2:
                     	focus="buttons"
                     	if btn_idx == 1:
                     	    focus = "matrix"
                     	    btn_idx=0
                     	    tab_count=0
                     	else:
                     	    btn_idx=1
                     	continue
                     elif tab_count == 3:
                         focus = 'matrix'
                         btn_idx=0
                         tab_count=0

             elif focus == 'matrix':
                 # Move the selection window origin
                 if key.name == 'KEY_UP':
                     curr_r = max(0, curr_r - 1)
                 elif key.name == 'KEY_DOWN':
                     curr_r = min(max_rows - k_rows, curr_r + 1)
                 elif key.name == 'KEY_LEFT':
                     curr_c = max(0, curr_c - 1)
                 elif key.name == 'KEY_RIGHT':
                     curr_c = min(max_cols - k_cols, curr_c + 1)
             elif focus == 'buttons':
                 if get_back=="y" or return_trimmed=="y":
                     if str(key).isalpha():
                         if str(key).upper() == "Y":
                             if get_back=="y":
                                 return []
                             elif return_trimmed=="y":
                                 return trimmed
                         elif str(key).upper() == "N":
                             get_back="n"
                             return_trimmed="n"
                             continue
                 elif key.name == 'KEY_LEFT':
                     btn_idx = 0
                 elif key.name == 'KEY_RIGHT':
                     btn_idx = 1
                 elif key.name == 'KEY_ENTER' or key == '\n':
                     if btns[btn_idx] == "TRIM":
                         # Extract the windowed area
                         trimmed = [row[curr_c : curr_c + k_cols] for row in level_matrix[curr_r : curr_r + k_rows]]
                         return_trimmed="y"
                     else:
                         get_back="y"
#print(interactive_sliding_matrix(13,6,6,level_dictionary[13]))
def new_make_level_matrix(level,matrix_length,matrix_breadth): #Takes matrix information and lets choose the next operation
	global level_dictionary
	#Make it directly interactive, allow and show changes to the matrix in real time
	if level in level_dictionary.keys():
#		matrix_length=len(level_matrix)
#		matrix_breadth=len(level_matrix[0])
		level_matrix=deepcopy(level_dictionary[level])
		if matrix_length!=len(level_matrix) or matrix_breadth!=len(level_matrix[0]):
#			trim_matrix_length=matrix_length
#			trim_matrix_breadth=matrix_breadth
			while True:
				if level_matrix!=[]:
					print("\rEnter Y to Create a New & Empty Level Board Or N to Trim The Saved Board to The New Dimensions (Y/n) ? ",end="",flush=True)
				else:
					print("Enter Y to Create a New & Empty Level Board Or N to Trim The Saved Board to The New Dimensions (Y/n) ? ",end="")
				choice=input()
				if choice.isalpha():
					if len(choice.split())==0 or choice=="Y" or choice=="y":
						level_matrix=[(["0"]*matrix_breadth)]*matrix_length #create empty matrix
						break
					elif choice=="N" or choice=="n":
						trim_matrix_dimensions=(matrix_length,matrix_breadth)
						level_matrix=trim_matrix(trim_matrix_dimensions,level_matrix)
						if level_matrix!=[]:
							break
		"""elif matrix_length=0 and matrix_breadth=0:
			matrix_length=len(level_matrix)
			matrix_breadth=len(level_matrix[0])"""
	else:
		level_matrix=[(["0"]*matrix_breadth)]*matrix_length #create empty matrix
	term=Terminal()
	pointer_location=(0,0)
	original_matrix_dimensions=(matrix_length,matrix_breadth)
	trim_matrix_dimensions=(0,0)
	input_alphabet=""
	curr_r,curr_c=0,0
	orig_level_matrix=deepcopy(level_matrix)
	message=""
	with term.cbreak(), term.hidden_cursor():
		while True:
			new_read_levels(level,original_matrix_dimensions,pointer_location,input_alphabet,level_matrix)
			if message!="":
				print("Message: ",message)
			message=""
			key=term.inkey()
			if key.is_sequence:
				if key.name=="KEY_UP" and curr_r > 0:
					curr_r-=1
				elif key.name=="KEY_DOWN" and curr_r < (matrix_length):
					curr_r+=1
				elif key.name=="KEY_LEFT" and curr_c > 0:
					curr_c-=1
				elif key.name=="KEY_RIGHT" and curr_c < (matrix_breadth-1):
					curr_c+=1
				if curr_r==matrix_length and curr_c > 2: #Prevent Out-Of-Boundary on the three options
					curr_c=2
				pointer_location=(curr_r,curr_c)
				if curr_r==(matrix_length+1):
					if curr_c==0 and key.name=="KEY_ENTER":
						message="Saved The Level Board"
						level_dictionary[level]=level_matrix
						with open(filename,"wb") as file:
							dump(level_dictionary,file)
						#Write the updated dictionary to the file as well
					elif curr_c==1 and key.name=="KEY_ENTER":
						print(term.normal_cursor,end="",flush=True)
						with term.cooked():
							while True:
								print("\rCONFIRMATION: The Current Changes Won't Be Saved, Do you still want to reset the board (Y/n) ? ",end="",flush=True)
								choice=input()
								if choice.isalpha():
									if len(choice.split())==0 or choice=="Y" or choice=="y":
										message="Reset Complete"
										level_matrix=deepcopy(orig_level_matrix)
										break
						print(term.hidden_cursor,end="",flush=True)
					elif curr_c==2 and key.name=="KEY_ENTER":
						print(term.normal_cursor,end="",flush=True)
						with term.cooked():
							while True:
								print("\rCONFIRMATION: The Current Changes Won't Be Saved, Do you still want to go to the previous menu (Y/n) ? ",end="",flush=True)
								choice=input()
								if choice.isalpha():
									if len(choice.split())==0 or choice=="Y" or choice=="y":
										choice="Y"
										break
									elif choice=="N" or choice=="n":
										choice="N"
										break
						print(term.hidden_cursor,end="",flush=True)
						if choice=="Y":
							break #Get back to level selection menu
			elif key and not key.is_sequence: # and str(key).upper() in mapping.keys(): #Probably has an error
				key=str(key)
				if key.isalpha() and key.upper() in mapping.keys():
					level_matrix[curr_r][curr_c]=key.upper()
					input_alphabet=key.upper()
				elif key in ("0","-1"):
					level_matrix[curr_r][curr_c]=key
					input_alphabet=key
	while True:
		m=[]
		for column in range(ml):
			line=[0]*mb
			for element in range(mb):
				print("Enter positional color for",column+1,"x",element+1,": ",end="")
				pn=(input())
				if pn.isalpha():
					pn=pn.upper()
				line[element]=pn
			m.append(line)
		cont=""
		while True:
			for element in m:
				print(element)
			cont=input("Continue(Y) Retry(N) ? ")
			if cont.isalpha():
				cont=cont.upper()
			if cont=="Y":
				level_dictionary[level]=m
				with open(filename, 'wb') as file:
					dump(level_dictionary, file)
				break
			elif cont=="N":
				break
		if cont=="Y":
			break
def new_add_level():
	while True:
		print("\033c",end="",flush=True)
		print("\rEnter The Level Number, which needs to be added or edited (0 to exit): ",end="",flush=True)
		level=input()
		level=check_for_integer(level)
		if type(level)!=int:
			continue
		if level==0:
			break
		elif level in level_dictionary.keys():
			while True:
				print("\rLevel",level,"already exists. Do you want to change the board dimensions (Y/n) ?",end="",flush=True)
				choice=input()
				if choice.isalpha():
					if len(choice.split())==0 or choice=="Y" or choice=="y":
						matrix_length,matrix_breadth=matrix_length_breadth_handler()
						break
					elif choice=="N" or choice=="n":
						matrix_length=matrix_breadth=0
						break
			new_make_level_matrix(level,matrix_length,matrix_breadth)
		else:
			matrix_length,matrix_breadth=matrix_length_breadth_handler()
			new_make_level_matrix(level,matrix_length,matrix_breadth)
#new_add_level()
#exit()
"""
def print_board(level,level_matrix):
	print("LEVEL:",level)
	for row in level_matrix:
		print("-"*(len(row)*5+1),"\n|",end="")
		for element in row:
			print("",(mapping[element].format("█"))*2,"|",end="")
		print()
	print("-"*(len(row)*5+1))
"""
def reverse_columnwise(level_matrix):
	for row in range(len(level_matrix)):
		level_matrix[row]=level_matrix[row][::-1]
	return level_matrix
def move_blocks(direction,level_matrix):
	global old_level_matrices
	try:
		if old_level_matrices[-1]!=level_matrix:
			old_level_matrices.append(deepcopy(level_matrix))
	except IndexError:
		old_level_matrices.append(deepcopy(level_matrix))
	if direction=="W":
		for row in range(len(level_matrix)-1):
			for index in range(len(level_matrix[row])):
				if (level_matrix[row][index]=="0") and (level_matrix[row+1][index] not in ["0","-1"]):
					level_matrix[row][index]=level_matrix[row+1][index]
					level_matrix[row+1][index]="0"
	if direction=="S": #Same operation as a W operation if the list is flipped without flipping sub elements
		#Reversing row-wise
		level_matrix=level_matrix[::-1]
		for row in range(len(level_matrix)-1):
			for index in range(len(level_matrix[row])):
				if (level_matrix[row][index]=="0") and (level_matrix[row+1][index] not in ["0","-1"]):
					level_matrix[row][index]=level_matrix[row+1][index]
					level_matrix[row+1][index]="0"
		#Reversing row-wise
		level_matrix=level_matrix[::-1] #Re-fliping to get correct Level Matrix as it should after a S operation
	if direction=="A":
		for row in range(len(level_matrix)):
			for index in range(len(level_matrix[row])-1):
				if (level_matrix[row][index]=="0") and (level_matrix[row][index+1] not in ["0","-1"]):
					level_matrix[row][index]=level_matrix[row][index+1]
					level_matrix[row][index+1]="0"
	if direction=="D": #Same operation as an A operation if the matrix is reversed column wise
#		def reverse_columnwise(level_matrix):
#			for row in range(len(level_matrix)):
#				level_matrix[row]=level_matrix[row][::-1]
		level_matrix=reverse_columnwise(level_matrix)
		for row in range(len(level_matrix)):
			for index in range(len(level_matrix[row])-1):
				if (level_matrix[row][index]=="0") and (level_matrix[row][index+1] not in ["0","-1"]):
					level_matrix[row][index]=level_matrix[row][index+1]
					level_matrix[row][index+1]="0"
		level_matrix=reverse_columnwise(level_matrix)
def check_for_match(level,moves,focus,btn_idx,message,moves_message,level_matrix):
	global old_level_matrices
	old_level_matrix=deepcopy(level_matrix)
	moves_message=""
#	matched=False
	if not level_matrix: # If level matrix is empty, do not make any changes
		return (moves_message,moves,level_matrix) #No Changes
	rows = len(level_matrix)
	cols = len(level_matrix[0])
	# 1. Count total occurrences of every unique element in the matrix
	# This acts as our "target" size for a perfect continuation
	total_counts = {}
	for r in range(rows):
		for c in range(cols):
			val = level_matrix[r][c]
			if val not in ("0", "-1"):
				total_counts[val] = total_counts.get(val, 0) + 1
	visited = set()
	match_count = 0
	# We need to track which cells to turn into '0' after checking all matches
	to_be_replaced = {}
	for r in range(rows):
		for c in range(cols):
			char = level_matrix[r][c] # Got the current element
			# Rule: Skip 0, -1, and already visited cells
			if char in ("0", "-1") or (r, c) in visited:
				continue
			# Start a search for a new connected group
			group = [] # Stores the coordinates of the group of element if they are connected and of same type
			stack = [(r, c)] #Saving the current element coordinates
			visited.add((r, c)) #Ensuring no recheck for already checked element
			while stack: #True till stack is not empty
				curr_r, curr_c = stack.pop() #Get coordinates of curently selected element, coordinates change as more connected elements are found
				group.append((curr_r, curr_c)) # Saving the coordinates as the element belongs to the group of currently selected element
				# Check 4 neighbors (Up, Down, Left, Right)
				for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
					nr, nc = curr_r + dr, curr_c + dc
					if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and level_matrix[nr][nc] == char): # check if the found element was not visited before and is within the matrix
						visited.add((nr, nc)) #Saving so that we do not revisit
						stack.append((nr, nc)) #Appended to stack to further check the neighbours of the found element, the for loop helps with checking for a T shaped or L shaped group
			# 3. CHECK CONDITION:
			# Does the size of this connected group match the total count in the matrix?
			if len(group) == total_counts[char]:
				match_count += 1
				#print(char,group)
				to_be_replaced[char]=group
				#sleep(1)
	# Replace all matched elements with "0"
	for char in to_be_replaced.keys():
		for row_idx in range(rows):
			for col_idx in range(cols):
				if (row_idx,col_idx) in to_be_replaced[char]:
					level_matrix[row_idx][col_idx] = "0"
					sleep(0.2)
					print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
		if len(to_be_replaced)>1:
			sleep(0.5)
		for r, c in to_be_replaced[char]:
			level_matrix[r][c] = "0"
	# 5. Return moves changes and the edited level matrix
	if match_count > 0:
#		matched=True
		old_level_matrices.append(old_level_matrix)
		if match_count > 1:
			s="s"
		else:
			s=""
#		moves_message="Moves: {0} + {1}  = {2} \n\033[31m{1} \033[92mBlock{3} Matched ! \033[0m\n".format(moves,match_count,moves+match_count+1,s)
		moves_message="Moves: {0} + {1} = {2} \n\033[31m{1} \033[92mBlock{3} Matched ! \033[0m\n".format(moves,match_count,moves+match_count,s)
#		return (moves_message,moves+match_count+1,level_matrix)
		return (moves_message,moves+match_count,level_matrix)
#	elif match_count == 1:
#		moves_message="+"
#		return (moves+match_count+1,level_matrix) # +1 is to account for move loss for the key press
	else:
		moves_message=""
		return (moves_message,moves,level_matrix) #no changes

def undo_last_action(): #while_deducting_one_move
	#No level downgrade with undo allowed
	global moves,undo_calls
	message=""
	undo_calls+=1
	"""try: # probably not needed, causes two moves loss
		if old_level_matrices[-1]!=level_matrix:
			moves=moves-1
	except IndexError:
		pass"""
#	print(old_level_matrices)
	if (old_level_matrices==[] or level_matrix in level_dictionary.values()) or moves==0:
		message="UNDO operation not possible\n"
		undo_calls=0
		return (level_matrix,message)
#	elif level_matrix==old_level_matrices[-1]: #never true
#		return level_matrix
#	elif level_matrix in level_dictionary.values():
#		undo_calls=0
#		return (level_matrix)
	else:
		message="Undid last move\n"
		if undo_calls==1: #Deduct 1 move only if called continuously
			moves=moves-1
		last_level_matrix=old_level_matrices.pop() #remove last element from old_level_matrices and save the last element to last_level_matrix becuase undo is possible but redo is not
		return (last_level_matrix,message)
def save_progress(level,moves,level_matrix,old_level_matrices):
	if level<1:
		raise ValueError("Level ValueError: level can't be less than 1, "+str(level)+" given")
	return
	print("Check for proper level and moves change with changing level")
	progress=(level,moves,level_matrix,old_level_matrices)
	with open("color-tiles-google-game.progress","wb") as file:
		dump(progress,file)
def load_progress(filename="color-tiles-google-game.progress"):
	if path.exists(filename):
		with open(filename, 'rb') as file:
			progress = load(file)
	else:
#		progress = (1,10,level_dictionary[1],[]) #moves set to 10 for testing
		progress = (1,3,level_dictionary[1],[]) #[['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']])
	return progress
def print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix):
	try:
		term=Terminal()
#		print("\033c",end="",flush=True) #Clear Screen at each prompt
		print(term.clear+term.home)
#		print_board(level,level_matrix)
		print("LEVEL:",level)
#		print("Press W or Arrow Up key to swipe UP, S or Arrow Down key to swipe DOWN,")
#		print("A or Arrow Left to swipe LEFT, D or Arrow Right to swipe RIGHT")
#		for row in level_matrix:
#			print("-"*(len(row)*5+1),"\n|",end="")
#			for element in row:
#				print("",(mapping[element].format("█"))*2,"|",end="")
#			print()
#		print("-"*(len(row)*5+1))
		if message!="":
			print(message,end="")
#		message=""
		if moves_message!="":
			print(moves_message,end="")
#		moves_message=""
		if moves<=3:
			print("Moves Remaining:\033[31m",moves,"\033[0m")
		else:
			print("Moves Remaining:\033[92m",moves,"\033[0m")
		"""if moves==0:
			print("\033[31mGAME OVER ! you are out of moves.\033[0m")
#			while True:
#				print("\r",end="",flush=True)
#				print("\r(R)etry or (E)xit ? ",end="",flush=True)
#			choice=input("(R)etry or (E)xit ? ")
#				if ((choice.isalpha()) and (choice.upper() in "RE")) and len(choice)==1:
#				if choice.upper()=="R" or choice.upper()=="E":
			print("Press R key to Retry or E key to Exit")
#			if choice.isalpha():
			if choice=="E" or choice=="e":
				choice="E"
				print("Saving current progress before exiting...")
				save_progress(level,moves,level_matrix,old_level_matrices)
				print("Progress saved, exiting...")
#				break
			elif choice=="R" or choice=="r":
				level=0 # level gets +1 at each loop iteration
				moves=3
				level_matrix=deepcopy(level_dictionary[1])
				old_level_matrices=[]
#				break
			break"""
		print("Press W or Arrow Up key to swipe UP, S or Arrow Down key to swipe DOWN,")
		print("Press A or Arrow Left to swipe LEFT, D or Arrow Right to swipe RIGHT")
		print("Press TAB to Choose the options, Enter to Select an option")
		for row in level_matrix:
			row_sep=("-"*(len(row)*5+1)).center(72)
			print(row_sep)
			for index in range(len(row_sep)):
				if row_sep[index]=="-":
					centralise_row=" "*index
					break
			row_line="|"
			for element in row:
				row_line+=" "+(mapping[element].format("█")*2)+" |"
			print(centralise_row+row_line)
		print(("-"*(len(row)*5+1)).center(72))
		print("-"*72)
		btns=["UNDO","RESTART","EXIT"]
		if level_matrix==level_dictionary[level] or moves==0:
			btns[0]="\u001b[9mUNDO\u001b[0m"
		btn_line = "   "
		for index in range(len(btns)):
			if focus == 'buttons' and btn_idx == index:
				btn_line+=" "*(12+(len(level_matrix[0])*1)-2)
				btn_line += term.black_on_white("[" + btns[index] + "]")
			else:
				btn_line += " "*(12+(len(level_matrix[0])*1)-2) + btns[index]
		print(btn_line.center(72))
	except KeyboardInterrupt:
		print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
		return
'''		print(term.clear+term.home)
		print("LEVEL:",level)
		if moves<=3:
			print("Moves Remaining:\033[31m",moves,"\033[0m")
		else:
			print("Moves Remaining:\033[92m",moves,"\033[0m")
		print("Press W or Arrow Up key to swipe UP, S or Arrow Down key to swipe DOWN,")
		print("Press A or Arrow Left to swipe LEFT, D or Arrow Right to swipe RIGHT")
		print("Press TAB to Choose the options, Enter to Select an option")
		print(("-"*72))
		for row in level_matrix:
			row_sep=("-"*(len(row)*5+1)).center(72)
			print(row_sep)
			for index in range(len(row_sep)):
				if row_sep[index]=="-":
					centralise_row=" "*index
					break
			row_line="|"
			for element in row:
				row_line+=" "+(mapping[element].format("█")*2)+" |"
			print(centralise_row+row_line)
		print(("-"*(len(row)*5+1)).center(72))
		print("-"*72)
		btns=["UNDO","Restart","EXIT"]
		if level_matrix==level_dictionary[level]:
			btns[0]="\u001b[9mUNDO\u001b[0m"
		btn_line = "   "
		for index in range(len(btns)):
#			if focus == 'buttons' and btn_idx == index:
#				btn_line+=" "*(12+(len(level_matrix[0])*1)-2)
#				btn_line += term.black_on_white("[" + btns[index] + "]")
#			else:
			btn_line += " "*(12+(len(level_matrix[0])*1)-2) + btns[index]
		print(btn_line.center(72))
'''
def play_game(ctrl_c=False):
	global level,moves,undo_calls,level_matrix,old_level_matrices
	term=Terminal()
	focus="matrix" # "matrix" or "buttons"
	btn_idx=0 # 0 to undo, 1 to Restart, 2 to exit
	tab_count=0
	get_back="n"
	restart_game="n"
	undo="n"
	empty=False
	choice=""
	direction=""
	message=""
	moves_message=""
	undo_calls=0
#	empty=False
	level,moves,level_matrix,old_level_matrices=load_progress("color-tiles-google-game.progress")
	saved_level_matrix=deepcopy(level_matrix)
	saved_level=int(level)
#	level=level-1
	while True:
#		level+=1
		if empty==True:
			level+=1
			empty=False
		if level==14: #level not in level_dictionary.keys():
			save_progress(1,3,level_dictionary[1],[]) #[['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']])
			level=1
			moves=3
			level_matrix=deepcopy(level_dictionary[level])
			old_level_matrices=[]
			print("print game complete and ask if player wants to restart")
		if saved_level_matrix==level_dictionary[1] or saved_level!=level:
			level_matrix=deepcopy(level_dictionary[level])
		uniq_elements=[] # Stores the number of unique elements except "0" and "-1"
#		level_matrix=level_dictionary[5]
#		for l in level_dictionary.keys():
		if level_matrix==level_dictionary[level]:
			for row in level_matrix:
				for element in row:
					if element not in ("0","-1") and element not in uniq_elements:
						uniq_elements.append(element)
#			break
		level_initial_moves=int(moves)
		if level!=1:
			moves_message+="Promoted to Level {0} \n".format(level)
#		print(uniq_elements)
#		print(level_matrix)
#		exit()
#		moves_message=""
#		if choice=="R" or direction=="R":
#			level=1
#			moves=3
#			level_matrix=deepcopy(level_dictionary[level])
#			old_level_matrices=[]
#		choice=""
		with term.fullscreen(), term.cbreak(), term.hidden_cursor():
			while True: #This while loop (statement only) can be removed and level promotion be handed to if empty==True block

				"""
#UI LOGIC STARTS###############################################################################################################

#				print("\033c",end="",flush=True) #Clear Screen at each prompt
				print(term.clear+term.home)
#				print_board(level,level_matrix)
				print("LEVEL:",level)
#				print("Press W or Arrow Up key to swipe UP, S or Arrow Down key to swipe DOWN,")
#				print("A or Arrow Left to swipe LEFT, D or Arrow Right to swipe RIGHT")
#				for row in level_matrix:
#					print("-"*(len(row)*5+1),"\n|",end="")
#					for element in row:
#						print("",(mapping[element].format("█"))*2,"|",end="")
#					print()
#				print("-"*(len(row)*5+1))
				if message!="":
					print(message,end="")
				message=""
				if moves_message!="":
					print(moves_message,end="")
				moves_message=""
				if moves<=3:
					print("Moves Remaining:\033[31m",moves,"\033[0m")
				else:
					print("Moves Remaining:\033[92m",moves,"\033[0m")
				if moves==0:
					print("\033[31mGAME OVER ! you are out of moves.\033[0m")
#					while True:
#						print("\r",end="",flush=True)
#						print("\r(R)etry or (E)xit ? ",end="",flush=True)
#					choice=input("(R)etry or (E)xit ? ")
#						if ((choice.isalpha()) and (choice.upper() in "RE")) and len(choice)==1:
#						if choice.upper()=="R" or choice.upper()=="E":
					print("Press R key to Retry or E key to Exit")
#					if choice.isalpha():
					if choice=="E" or choice=="e":
						choice="E"
						print("Saving current progress before exiting...")
						save_progress(level,moves,level_matrix,old_level_matrices)
						print("Progress saved, exiting...")
#						break
					elif choice=="R" or choice=="r":
						level=0 # level gets +1 at each loop iteration
						moves=3
						level_matrix=deepcopy(level_dictionary[1])
						old_level_matrices=[]
#						break
					break
				print("Press W or Arrow Up key to swipe UP, S or Arrow Down key to swipe DOWN,")
				print("Press A or Arrow Left to swipe LEFT, D or Arrow Right to swipe RIGHT")
				print("Press TAB to Choose the options, Enter to Select an option")
				print(("-"*72))
				for row in level_matrix:
					row_sep=("-"*(len(row)*5+1)).center(72)
					print(row_sep)
					for index in range(len(row_sep)):
						if row_sep[index]=="-":
							centralise_row=" "*index
							break
					row_line="|"
					for element in row:
						row_line+=" "+(mapping[element].format("█")*2)+" |"
					print(centralise_row+row_line)
				print(("-"*(len(row)*5+1)).center(72))
				print("-"*72)
				btns=["UNDO","Restart","EXIT"]
				if level_matrix==level_dictionary[level]:
					btns[0]="\u001b[9mUNDO\u001b[0m"
				btn_line = "   "
				for index in range(len(btns)):
					if focus == 'buttons' and btn_idx == index:
						btn_line+=" "*(12+(len(level_matrix[0])*1)-2)
						btn_line += term.black_on_white("[" + btns[index] + "]")
					else:
						btn_line += " "*(12+(len(level_matrix[0])*1)-2) + btns[index]
				print(btn_line.center(72))
				"""
#				if level==0:
#					print_board(1,moves,focus,btn_idx,message,moves_message,level_matrix)
#				else:
				print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
				message=""
				moves_message=""
				if moves==0:
					print("\033[31mGAME OVER ! you are out of moves.\033[0m")
#					while True:
#						print("\r",end="",flush=True)
#						print("\r(R)etry or (E)xit ? ",end="",flush=True)
#					choice=input("(R)etry or (E)xit ? ")
#						if ((choice.isalpha()) and (choice.upper() in "RE")) and len(choice)==1:
#						if choice.upper()=="R" or choice.upper()=="E":
					print("Choose between Restart and Exit")
#					continue
					"""
#					if choice.isalpha():
					if choice=="E" or choice=="e":
						choice="E"
						print("Saving current progress before exiting...")
						save_progress(level,moves,level_matrix,old_level_matrices)
						print("Progress saved, exiting...")
#						break
					elif choice=="R" or choice=="r":
						level=0 # level gets +1 at each loop iteration
						moves=3
						level_matrix=deepcopy(level_dictionary[1])
						old_level_matrices=[]
#						break
					break
					"""
				if get_back=="y":
					print("COMFIRMATION : Exit the Game (Y/N) ?")
				elif restart_game=="y":
					print("By Restarting the game, you will loose your current progress. \nRestart the Game (Y/N) ?")
#				if ctrl_c==True:
#					direction="E"
#					print("Saving current progress before exiting...")
#					save_progress(level,moves,level_matrix,old_level_matrices)
#					print("Progress saved, exiting...")
#					break
#				sleep(1)
#				continue
#				if get_back=="y":
#					direction="E"
#				elif restart_game=="y":
#					print("CONFIRMATION: Do you want to Restart the Game (Y/N) ? ")
#				if level_matrix==level_dictionary[level]:
#					print("Enter\u001b[9m U to Undo,\u001b[0m E to Exit, R to Restart the Game") #UNDO option disabled at game start
#				else:
#					print("Enter U to Undo, E to Exit, R to Restart the game")
				direction=""
				try:
					key=term.inkey()
				except KeyboardInterrupt:
					print("Saving current progress before exiting...")
					save_progress(level,moves,level_matrix,old_level_matrices)
					print("Progress saved, exiting...")
					sleep(1) #To display save message
#					exit()
					ctrl_c=True
					break
#				direction=input("Enter Your Choice: ")
				if key.name == 'KEY_TAB': # and (get_back!="y" or restart_game!="y"):
					if get_back=="y" or restart_game=="y":
						continue
					tab_count+=1
					if focus == "matrix":
						focus = 'buttons'
						btn_idx=0
						continue
					else:
#						if tab_count ==1:
#							focus="buttons"
#							btn_idx=0
#							continue
						if tab_count == 2:
#							focus="buttons"
#							btn_idx=1
#							continue
							if btn_idx == 1:
								focus = "buttons"
								btn_idx=2
#								tab_count=0
							elif btn_idx == 2:
#								btn_idx=1
								focus="matrix"
								tab_count=0
								btn_idx=0
							else: # if btn_idx==0
								btn_idx=1
								focus="buttons"
							continue
						elif tab_count == 3:
							btn_idx=2
							focus="buttons"
							continue
#							if btn_idx==2:
#								focus="buttons"
#								btn_idx=0
#							elif btn_idx==1:
#								btn_idx=0
#							else:
						elif tab_count == 4:
							focus = 'matrix'
							btn_idx=0
							tab_count=0
							continue
				elif key.name=="KEY_ESCAPE":
					get_back="y"
#					focus="buttons"
					continue
				if focus == 'matrix' and moves!=0:
					if key.name=="KEY_UP":
						direction="W"
					elif key.name=="KEY_LEFT":
						direction="A"
					elif key.name=="KEY_DOWN":
						direction="S"
					elif key.name=="KEY_RIGHT":
						direction="D"
					elif str(key).isalpha():
						if str(key).upper()=="W":
							direction="W"
						elif str(key).upper()=="A":
							direction="A"
						elif str(key).upper()=="S":
							direction="S"
						elif str(key).upper()=="D":
							direction="D"
				if focus == 'buttons' or get_back=="y":
					if get_back=="y" or restart_game=="y":
#						print("CONFIRMATION: EXIT ?")
						if str(key).isalpha():
							if str(key).upper() == "Y":
								if get_back=="y":
#									ctrl_c=True
#									get_back="n"
									direction="E"
									print("Saving current progress before exiting...")
									save_progress(level,moves,level_matrix,old_level_matrices)
									print("Progress saved, exiting...")
									sleep(1) #To display save message
									break
								elif restart_game=="y": #Probably has some issues with level promotion
									level=1
									moves=3
									level_matrix=deepcopy(level_dictionary[1])
									old_level_matrices=[]
									restart_game="n"
									break
#								elif undo=="y":
#									level_matrix,message=deepcopy(undo_last_action())
							elif str(key).upper() == "N":
								get_back="n"
								restart_game="n"
								undo="n"
								continue
#					elif undo=="y":
#						level_matrix,message=deepcopy(undo_last_action())
#						undo="n"
					elif key.name=="KEY_LEFT":
						focus="buttons"
						if btn_idx==2:
							btn_idx=1
						else:
							btn_idx=0
						continue
					elif key.name=="KEY_RIGHT":
						focus="buttons"
						if btn_idx==0:
							btn_idx=1
						else:
							btn_idx=2
						continue
					elif key.name=="KEY_ENTER" or key=='\n': #or key.name=="KEY_ESCAPE":
						focus="buttons"
						if btn_idx==0:
							level_matrix,message=deepcopy(undo_last_action())
#							undo="y"
						elif btn_idx==1:
							restart_game="y"
						else:
							get_back="y"
						continue
					elif str(key).isalpha():
						if str(key).upper()=="A":
							if btn_idx==2:
								btn_idx=1
							else:
								btn_idx=0
						elif str(key).upper()=="D":
							if btn_idx==0:
								btn_idx=1
							else:
								btn_idx=2
						continue
#UI LOGIC COMPLETE##############################################################################################################################

#				if direction.upper()=="W" or direction.upper()=="A" or direction.upper()=="S" or direction.upper()=="D":
#				continue
				if direction in "WASD":
#					direction=direction.upper()
					try:
						if old_level_matrices[-1]!=level_matrix:
							undo_calls=0
					except IndexError:
						pass
					move_blocks(direction,level_matrix)
					if old_level_matrices[-1]!=level_matrix:
						moves=moves-1
						print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
						sleep(0.2)
						moves_message,moves,level_matrix=check_for_match(level,moves,focus,btn_idx,message,moves_message,level_matrix)
#						if matched==True:
#							print_board(level,moves,focus,btn_idx,message,moves_message,old_level_matrices[-1])
#							sleep(0.5)
#							print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
#							matched=False
						empty=True
						for row in level_matrix:
							for element in row:
								if element not in ("0","-1"):
									empty=False
									break
#								if empty==False:
#									break
							if empty==False:
								break
						if empty==True:
							print_board(level,moves,focus,btn_idx,message,moves_message,level_matrix)
							sleep(0.2)
#							level+=1
							# This save progress block should move to the line next to level+=1
							# The code below will save a non existing level if the current level is last
							if next(reversed(level_dictionary))!=level: #level_dictionary.keys())[-1]!=level:
								save_progress(level+1,moves,level_dictionary[level+1],old_level_matrices)
#							if len(uniq_elements)==(moves - level_initial_moves):
							if moves==level_initial_moves: #Doesn't works if two blocks match simultaneously
								moves_message+="Perfect +1 move\n"
								moves+=1
#							if len(uniq_elements)==(moves - level_initial_moves):
#								moves_message+="Perfect \n"
							old_level_matrices=[]
#							empty=False
							break
						else:
							save_progress(level,moves,level_matrix,old_level_matrices)
				elif direction=="E":
					direction="E"
					print("Saving current progress before exiting...")
					save_progress(level,moves,level_matrix,old_level_matrices)
					print("Progress saved, exiting...")
					sleep(1) #Sleep to show save message
					break
#				elif direction=="R" or direction=="r": #Has some issues with level promotion
#					confirm=""
#					while confirm.lower() not in ("y","n"):
#						print("\r",end="",flush=True)
#						print("By Restarting the game, you will loose your current progress. \nRestart the Game (Y/n) ? ") #,end="") #Ask for reset confirmation
#						confirm=input()
#						if len(confirm.split())==0:
#							confirm="y"
#						if not confirm.isalpha():
#							confirm=""
#					if confirm.lower()=="y":
#						level=0 #level gets +1 at each loop iteration
#						moves=3
#						level_matrix=deepcopy(level_dictionary[1])
#						old_level_matrices=[]
#						break
#				elif direction=="U" or direction=="u":
#					level_matrix,message=deepcopy(undo_last_action())
#					if old_level_matrices[-1]!=level_matrix:
#						moves=moves-1
			if choice=="E" or direction=="E" or ctrl_c==True:
				break
def menu():
	options=["Play","Add or Edit level","Automatic play","Quit"]
	return
def choose_between_edit__play_or_auto_play():
	return
def auto_play():
	return

play_game()
exit()
#try:
#	play_game()
#	pass
#except KeyboardInterrupt:
#	play_game(ctrl_c=True)
#	print("Saving current progress before exiting...")
#	save_progress(level,moves,level_matrix,old_level_matrices)
#	print("Progress saved, exiting...")
#	exit()

old_level_matrices=[]
# --- Test Cases ---

matrix1 = [['0', 'R', 'R'],
           ['Y', 'Y', 'Y'],
           ['Y', 'R', 'R']]
#print(f"Matches found: {check_for_match(3,matrix1)}")
# Output: 1 (The Y's form a group of 4)

matrix2 = [['R', 'R', 'Y', 'R'],
           ['0', 'Y', 'Y', 'R'],
           ['0', 'Y', 'B', '0'],
           ['0', 'B', 'B', 'B']]
t=check_for_match(2,3,"matrix",0,"","",matrix2)
print(f"Matches found: {t}")
exit()
# Output: 2 (Y and B both have groups of 4)

level_matrix=[["Y","R","R"],["0","Y","Y"],["Y","R","R"]]
print(check_for_match(2,3,"matrix",0,"","",level_matrix)) #[["Y","Y","0","0"],["Y","Y","Y","0"],["0","Y","0","0"],["Y","0","Y","0"]])) #level_dictionary[1])

print(check_for_match(3,[["Y","R","R"],["Y","Y","0"],["Y","R","R"]])) #level_dictionary[1])

exit()
