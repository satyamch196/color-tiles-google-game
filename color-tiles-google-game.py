#Use some encoding, probably like base64 to convert saved binary from picke to ascii text or save the
#datatypes as they are to save all progress and level  dictionary together with this script while being
#able to update them as needed as well

#Use terminal background coloring with blank spaces instead of the solid blocks used to print the level
#matrix
from pickle import dump,load
from os import path
from copy import deepcopy
from blessed import Terminal
level_dictionary={} #LEVEL DICTIONARY
#level_dictionary={1: [['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']], 2: [['R', 'R', 'Y', 'R'], ['Y', 'Y', '0', 'R'], ['Y', 'B', '0', '0'], ['B', 'B', '0', 'B']], 3: [['R', 'Y', 'Y', 'R'], ['0', 'Y', 'R', 'B'], ['Y', '-1', 'R', '0'], ['0', 'B', 'B', 'B']], 4: [['R', 'R', 'R', '-1'], ['0', 'B', 'B', 'Y'], ['-1', 'B', 'Y', 'R'], ['Y', '0', 'B', 'Y']], 5: [['B', '-1', 'R', 'Y'], ['B', '-1', 'R', 'R'], ['B', 'Y', 'Y', '0'], ['0', 'B', 'Y', 'R']], 6: [['0', 'B', 'B', '0', '0'], ['0', 'B', 'O', 'R', '0'], ['B', '-1', 'R', 'Y', '-1'], ['-1', 'O', 'Y', '0', 'Y'], ['O', 'O', 'R', 'R', 'Y']], 7: [['B', 'B', 'O', 'O', '0'], ['O', '-1', 'B', 'B', 'R'], ['0', 'Y', 'O', '0', 'R'], ['Y', 'Y', 'R', '-1', 'R'], ['0', '0', 'Y', '-1', '0']], 8: [['0', '0', 'C', 'C', '0', 'Y'], ['0', 'O', 'O', '0', 'O', 'Y'], ['O', 'B', 'Y', 'B', 'Y', '-1'], ['B', 'C', 'B', '-1', '0', '0'], ['C', '-1', '-1', '0', '0', '0'], ['R', 'R', '0', 'R', 'R', '0']], 9: [['0', '0', 'Y', '0', 'Y', '0'], ['-1', '0', '0', 'Y', '0', 'Y'], ['B', '-1', 'B', '0', '0', 'C'], ['B', 'B', 'C', 'R', 'O', 'O'], ['R', 'C', 'C', '-1', '0', 'O'], ['R', 'R', '0', '-1', 'O', '0']], 10: [['0', '0', 'O', 'O', 'V', '0', '0'], ['0', 'V', '0', '0', '0', '0', 'O'], ['0', '0', '-1', '0', 'Y', 'O', '0'], ['B', 'B', 'V', 'C', '0', '-1', '-1'], ['B', '0', 'V', 'R', 'Y', 'Y', 'R'], ['0', 'B', 'R', '0', 'Y', '-1', 'R'], ['0', '0', '-1', '0', 'C', 'C', 'C']], 11: [['-1', 'C', 'C', 'B', '-1', '0', '0'], ['O', 'C', '-1', '0', '-1', '0', '0'], ['0', 'O', '0', 'C', 'B', '0', 'B'], ['0', '0', 'Y', 'O', 'B', '0', '0'], ['Y', 'Y', 'R', 'O', '-1', '0', '0'], ['0', '0', 'Y', 'R', 'V', 'V', 'V'], ['R', '0', '0', 'V', 'R', '0', '0']], 12: [['Y', 'G', 'G', '-1', 'B', '0', 'O', '0'], ['0', '0', '0', '0', '0', 'B', 'Y', 'O'], ['Y', 'C', 'G', '-1', 'B', 'B', 'O', 'O'], ['0', '0', 'Y', '0', 'R', 'C', 'C', 'G'], ['V', '-1', '0', 'R', '0', 'R', 'C', '0'], ['0', '0', '0', '0', 'R', 'V', 'V', '0'], ['V', '-1', '-1', '-1', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']], 13: [['0', '0', '0', '0', '0', 'G', 'O', '0'], ['0', '0', '0', 'G', '0', 'G', 'V', '0'], ['0', 'R', 'B', '0', 'G', 'O', 'Y', '-1'], ['0', '0', '0', '0', '0', 'Y', '0', 'V'], ['0', 'B', 'B', '0', '-1', 'Y', 'Y', 'V'], ['0', '0', 'R', 'R', 'C', '0', 'V', 'O'], ['R', '0', '0', '0', 'C', '0', 'C', 'C'], ['-1', '-1', '0', '0', 'C', '-1', '-1', 'O']]}
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
	}
filename="/sdcard/level_dictionary.dict"
if path.exists(filename):
    with open(filename, 'rb') as file:
        level_dictionary = load(file)
#else:
#    with open(filename, 'wb') as file:
#        dump(level_dictionary,file)
#        exit()
def check_for_integer(string):
	try:
		integer=int(string)
		return integer
	except ValueError:
		return string
def matrix_length_breadth_handler():
	while True:
		print("\rEnter Board Length (0 to exit): ",end="",flush=True)
		matrix_length=input()
		matrix_length=check_for_integer(matrix_length)
		if type(matrix_length)!=int:
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
		else:
			if matrix_breadth==0:
				exit()
			break
	return (matrix_length,matrix_breadth)
def make_level_matrix(level,ml,mb):
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
def read_levels(level_dictionary):
	for level in level_dictionary.keys():
		print("LEVEL:",level)
		for row in level_dictionary[level]:
			print("-"*(len(row)*5+1),"\n|",end="")
			for element in row:
				print("",mapping[element]*2,"|",end="")
			print()
		print("-"*(len(row)*5+1))
def add_level():
	read_levels(level_dictionary)
	while True:
		level=int(input("Enter Level Number (0 to exit): "))
		if level==0:
			break
		ml=int(input("Board Length: "))
		mb=int(input("Board Breadth: "))
		make_level_matrix(level,ml,mb)
def new_read_levels(level,original_matrix_dimensions,trim_matrix_dimensions,pointer_location,input_alphabet,level_matrix):
#	if matrix_length==0 and matrix_breadth==0:
	matrix_length,matrix_breadth=original_matrix_dimensions
	trim_matrix_length,trim_matrix_breadth=trim_matrix_dimensions
	if input_alphabet.isalpha():
		input_alphabet=input_alphabet.upper()
	print(Terminal.clear + Terminal.home) # Clear the screen and move to Top-Left
#	print("\033c",end="",flush=True)
	print("Use the arrow keys to navigate between rows, columns and special options")
	if level in level_dictionary.keys():
		print("EDITING: Level",level)
	elif level==-1:
		print("TRIMMING LEVEL BOARD: Level",level)
	else:
		print("ADDING: New Level",level)
	print("Board Dimensions (LENGTH×BREADTH) : ",matrix_length,"×",matrix_breadth,sep="")
#	for level in level_dictionary.keys():
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
	if level!=-1:
		print(mappings)
	else:
		print("New Board Dimensions (LENGTH×BREADTH) : ",trim_matrix_length,"×",trim_matrix_breadth,sep="")
		print("Use The Arrow Keys to Select The Area to Keep After Trimming")
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
"""def trim_matrix(trim_matrix_dimensions,level_matrix):
	def print_trimmed_level_matrix(trim_matrix_dimensions,pointer_location,level_matrix):
		matrix_length=len(level_matrix)
		matrix_breadth=len(level_matrix[0])
		trim_matrix_length,trim_matrix_breadth=trim_matrix_dimensions
#	if input_alphabet.isalpha():
#		input_alphabet=input_alphabet.upper()
		print(Terminal.clear + Terminal.home) # Clear the screen and move to Top-Left
#	print("\033c",end="",flush=True)
		print("TRIMMING LEVEL BOARD: Level",level)
		print("Original Board Dimensions (LENGTH×BREADTH) : ",matrix_length,"×",matrix_breadth,sep="")
		print("New Board Dimensions (LENGTH×BREADTH) : ",trim_matrix_length,"×",trim_matrix_breadth,sep="")
		print("Use The Arrow Keys to Select The Area to Keep After Trimming, Press TAB key to select among the Options")
		removed_part_=(matrix_length-trim_matrix_dimensions[0],matrix_breadth-trim_matrix_dimensions[1])
		len_row=len(level_matrix[0])
		for row in range(len(level_matrix)):
			print("-"*(len_row*5+1),"\n|",end="")
			for column in range(len_row):
				if row >= matrix_length-trim_matrix_dimensions[0]: #(row,column)==pointer_location:
#					if input_alphabet not in mapping.keys():
					print("",(mapping[level_matrix[row][column]].format(▒))*2,"|",end="")
#					else:
#						print("",(mapping[input_alphabet].format(▒))*2,"|",end="")
				else:
					print(" ",(mapping[level_matrix[row][column]].format(""█))*2," |",sep="",end="")
			print()
		print("-"*(len_row*5+1))
		if pointer_location==(len_row+1,0):
			print(" "*((len_row-2)*3//2),"\033[47;30m","[TRIM]","\033[0m"," "*((len_row-2)*3//2),"[BACK]",sep="")
		elif pointer_location==(len_row+1,1):
			print(" "*((len_row-2)*3//2),"[TRIM]"," "*((len_row-2)*3//2),"\033[47;30m","[BACK]","\033[0m",sep="")
	pointer_location=(0,0)
	matrix_length=len(level_matrix)
	matrix_breadth=len(level_matrix[0])
	curr_r,curr_c=0,0
	active_part="upper"
	with Terminal.cbreak(), Terminal.hidden_cursor():
		while True:
			print_trimmed_level_matrix(trim_matrix_dimensions,pointer_location,level_matrix)
			key=Terminal.inkey()
			if key.is_sequence:
				if key.name=="KEY_UP" and curr_r > 0:
					curr_r-=1
				elif key.name=="KEY_DOWN" and curr_r < (matrix_length - trim_matrix_dimensions[0] - 1):
					curr_r+=1
				elif key.name=="KEY_LEFT" and curr_c > 0:
					curr_c-=1
				elif key.name=="KEY_RIGHT" and curr_c < (matrix_breadth - trim_matrix_dimensions[1] - 1):
					curr_c+=1
				if curr_r==matrix_length and curr_c > 1: #Prevent Out-Of-Boundary on the two options
					curr_c=1
#				pointer_location=(curr_r,curr_c)
				if curr_r==(matrix_length+1):
					if curr_c==0 and key.name=="KEY_ENTER":
						#Add proper logic to return correct level matrix
						return level_matrix
					elif curr_c==1 and key.name=="KEY_ENTER"::
						print(Terminal.normal_cursor,end="",flush=True)
						with Terminal.cooked():
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
						print(Terminal.hidden_cursor,end="",flush=True)
						if choice=="Y":
							level_matrix=[]
							return level_matrix
							break #Get back to trim selection menu
			if key and not key.is_sequence:
				if key.name=="KEY_TAB":
					if active_part=="upper":
						active_part="lower"
						curr_r+=matrix_length
					elif active_part=="lower":
						active_part="lower"
						curr_r-=matrix_length
			if curr_r==matrix_length and curr_c > 1:
				curr_c=1
			pointer_location=(curr_r,curr_c)"""
def interactive_sliding_matrix(level,keep_rows,keep_cols,level_matrix):
    term=Terminal()
    # Total Matrix Dimensions
    max_rows = len(level_matrix)
    max_cols = len(level_matrix[0]) #if max_rows > 0 else 0
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
                     val = (mapping[level_matrix[row][column]]) #.center(4)
                     # Check if current cell is within the selection window
                     is_in_window = (curr_r <= row < curr_r + k_rows and curr_c <= column < curr_c + k_cols)
                     if is_in_window:
#                     	val+="|"
#                         if focus == 'matrix':
#                             line += term.black_on_green(val)+"|"
#                         else:
#                             line += term.green(val)+"|"
                          line += " "+(val.format("█"))*2+" |"
                     else:
#                         line += term.white(val)+"|"
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
                     btn_line += term.black_on_white("[" + btns[index] + "]") #+ "    "
                 else:
                     btn_line += " "*((max_cols*1)-2) + btns[index] #+ " "*(max_cols-2)
             print(btn_line.center(max_cols*2))

            # --- Input Handling ---
             key = term.inkey()

             if key.name == 'KEY_TAB':
                 tab_count+=1
                 if focus == "matrix":
                     focus = 'buttons'
                 else:
                     if tab_count >2:
                         focus = 'matrix'
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
                 else:
                     print("Unsupported Key:",key.name)

             elif focus == 'buttons':
                 if key.name == 'KEY_LEFT':
                     btn_idx = 0
                 elif key.name == 'KEY_RIGHT':
                     btn_idx = 1
                 elif key.name == "KEY_TAB":
                     if btn_idx == 0:
                         btn_idx=1
                     else:
                         btn_idx=0
                 elif key.name == 'KEY_ENTER' or key == '\n':
                     if btns[btn_idx] == "TRIM":
                         # Extract the windowed area
                         trimmed = [row[curr_c : curr_c + k_cols] for row in level_matrix[curr_r : curr_r + k_rows]]
                         return trimmed
                     else:
                         return []
                 else:
                     print("Unsupported Key:",key.name)
print(interactive_sliding_matrix(13,6,6,level_dictionary[13]))
def create_empty_matrix(matrix_length,matrix_breadth):
	level_matrix=[]
	for row in range(matrix_length):
		line=[0]*matrix_breadth
		level_matrix.append(line)
	return level_matrix
def new_make_level_matrix(level,matrix_length,matrix_breadth):
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
						level_matrix=create_empty_matrix(matrix_length,matrix_breadth)
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
		level_matrix=create_empty_matrix(matrix_length,matrix_breadth)
	pointer_location=(0,0)
	original_matrix_dimensions=(matrix_length,matrix_breadth)
	trim_matrix_dimensions=(0,0)
	input_alphabet=""
	curr_r,curr_c=0,0
	orig_level_matrix=deepcopy(level_matrix)
	message=""
	with Terminal.cbreak(), Terminal.hidden_cursor():
		while True:
			new_read_levels(level,original_matrix_dimensions,trim_matrix_dimensions,pointer_location,input_alphabet,level_matrix)
			if message!="":
				print("Message: ",message)
			message=""
			key=Terminal.inkey()
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
						print(Terminal.normal_cursor,end="",flush=True)
						with Terminal.cooked():
							while True:
								print("\rCONFIRMATION: The Current Changes Won't Be Saved, Do you still want to reset the board (Y/n) ? ",end="",flush=True)
								choice=input()
								if choice.isalpha():
									if len(choice.split())==0 or choice=="Y" or choice=="y":
										message="Reset Complete"
										level_matrix=deepcopy(orig_level_matrix)
										break
						print(Terminal.hidden_cursor,end="",flush=True)
					elif curr_c==2 and key.name=="KEY_ENTER":
						print(Terminal.normal_cursor,end="",flush=True)
						with Terminal.cooked():
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
						print(Terminal.hidden_cursor,end="",flush=True)
						if choice=="Y":
							break #Get back to level selection menu
			elif key and not key.is_sequence: #and str(key) in mapping.keys():
				level_matrix[curr_r][curr_c]=str(key)
				input_alphabet=str(key)
				
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
def print_board(level,level_matrix):
	print("LEVEL:",level)
	for row in level_matrix:
		print("-"*(len(row)*5+1),"\n|",end="")
		for element in row:
			print("",(mapping[element].format("█"))*2,"|",end="")
		print()
	print("-"*(len(row)*5+1))
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
		def reverse_columnwise(level_matrix):
			for row in range(len(level_matrix)):
				level_matrix[row]=level_matrix[row][::-1]
		reverse_columnwise(level_matrix)
		for row in range(len(level_matrix)):
			for index in range(len(level_matrix[row])-1):
				if (level_matrix[row][index]=="0") and (level_matrix[row][index+1] not in ["0","-1"]):
					level_matrix[row][index]=level_matrix[row][index+1]
					level_matrix[row][index+1]="0"
		reverse_columnwise(level_matrix)
def check_for_match(moves,level_matrix):
	old_moves=int(moves)
	uniq_elements=[] #Stores the unique elements in the level matrix
#	occurrences=0 #Used to store occurrences of a unique element
#	matches=[] #Stores the location and thus the total number of matching elements
	for row in level_matrix:
		for element in row:
			if (element not in ["0","-1"]) and (element not in uniq_elements):
				uniq_elements.append(element)
	for uniq_element in uniq_elements:
		matches=[] #Stores the location and thus the total number of matching elements
		occurrences=0 #Used to store occurrences of a unique element
		for row in range(level_matrix):
			for column in level_matrix[row]:
				if uniq_element==level_matrix[row][column]:
					occurrences+=1
					if (row,column) not in matches:
						matches.append((row,column))
					if row > 0: # Next if conditions are useless as the above if statement adds all positional tuple to the matches list
						if (uniq_element==level_matrix[row-1][column]) and ((row-1,column) not in matches):
							matches.append((row-1,column))
					if row < len(level_matrix): #Useless
						if (uniq_element==level_matrix[row+1][column]) and ((row+1,column) not in matches):
							matches.append((row+1,column))
					if column > 0: #Useless
						if (uniq_element==level_matrix[row][column-1]) and ((row,column-1) not in matches):
							matches.append((row,column-1))
					if column < len(level_matrix[0]): #Useless
						if (uniq_element==level_matrix[row][column+1]) and ((row,column+1) not in matches):
							matches.append((row,column+1))
		if len(matches)==occurrences:
			moves+=1
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
	if old_level_matrices==[] or level_matrix in level_dictionary.values():
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
def play_game():
	global level,moves,undo_calls,level_matrix,old_level_matrices
	choice=""
	direction=""
	message=""
	undo_calls=0
	level,moves,level_matrix,old_level_matrices=load_progress("color-tiles-google-game.progress")
	saved_level_matrix=deepcopy(level_matrix)
	saved_level=int(level)
	level=level-1
	while True:
		level+=1
		if level not in level_dictionary.keys():
			save_progress(1,3,level_dictionary[1],[]) #[['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']])
			level=1
			moves=3
			level_matrix=deepcopy(level_dictionary[level])
			old_level_matrices=[]
			print("print game complete and ask if player wants to retry")
		if saved_level_matrix==level_dictionary[1] or saved_level!=level:
			level_matrix=deepcopy(level_dictionary[level])
#		if choice=="R" or direction=="R":
#			level=1
#			moves=3
#			level_matrix=deepcopy(level_dictionary[level])
#			old_level_matrices=[]
#		choice=""
		while True:
			print("\033c",end="",flush=True) #Clear Screen at each prompt
			print_board(level,level_matrix)
			print(message,end="")
			message=""
			if moves<=3:
				print("Moves Remaining:\033[31m",moves,"\033[0m")
			else:
				print("Moves Remaining:\033[92m",moves,"\033[0m")
			if moves==0:
				print("\033[31mGAME OVER ! you are out of moves.\033[0m")
				while True:
#					print("\r",end="",flush=True)
#					print("\r(R)etry or (E)xit ? ",end="",flush=True)
					choice=input("(R)etry or (E)xit ? ")
#					if ((choice.isalpha()) and (choice.upper() in "RE")) and len(choice)==1:
#					if choice.upper()=="R" or choice.upper()=="E":
					if choice.isalpha():
						if choice=="E" or choice=="e":
							choice="E"
							print("Saving current progress before exiting...")
							save_progress(level,moves,level_matrix,old_level_matrices) #[['Y', 'R', 'R'], ['0', 'Y', 'Y'], ['Y', 'R', 'R']])
							print("Progress saved, exiting...")
							break
						elif choice=="R" or choice=="r":
							level=0 # level gets +1 at each loop iteration
							moves=3
							level_matrix=deepcopy(level_dictionary[1])
							old_level_matrices=[]
							break
				break
			print("Enter W to swipe UP, S to swipe DOWN, A to swipe LEFT, D to swipe RIGHT")
			if level==1 and level_matrix==level_dictionary[1]:
				print("Enter\u001b[9m U to Undo,\u001b[0m E to Exit, R to Reset the Game") #UNDO option disabled at game start
			else:
				print("Enter U to Undo, E to Exit, R to Restart the game")
			direction=input("Enter Your Choice: ")
#			if ((direction.isalpha()) and (direction.upper() in "WASD")) and len(direction)==1 :
			if direction.upper()=="W" or direction.upper()=="A" or direction.upper()=="S" or direction.upper()=="D":
				direction=direction.upper()
#				old_level_matrices.append(deepcopy(level_matrix))
				try:
					if old_level_matrices[-1]!=level_matrix:
						undo_calls=0
				except IndexError:
					pass
				move_blocks(direction,level_matrix)
				if old_level_matrices[-1]!=level_matrix:
					moves=moves-1
				check_for_match(level_matrix)
				save_progress(level,moves,level_matrix,old_level_matrices)
			elif direction=="E" or direction=="e":
				direction="E"
				print("Saving current progress before exiting...")
				save_progress(level,moves,level_matrix,old_level_matrices)
				print("Progress saved, exiting...")
				break
			elif direction=="R" or direction=="r":
				confirm=""
				while confirm.lower() not in ("y","n"):
#					print("\r",end="",flush=True)
					print("By Restarting the game, you will loose your current progress. \nRestart the Game (Y/n) ? ",end="") #Ask for reset confirmation
					confirm=input()
					if len(confirm.split())==0:
						confirm="y"
					if not confirm.isalpha():
						confirm=""
				if confirm.lower()=="y":
					level=0 #level gets +1 at each loop iteration
					moves=3
					level_matrix=deepcopy(level_dictionary[1])
					old_level_matrices=[]
					break
			elif direction=="U" or direction=="u":
				level_matrix,message=deepcopy(undo_last_action())
#				if old_level_matrices[-1]!=level_matrix:
#					moves=moves-1
		if choice=="E" or direction=="E":
			break
try:
#	play_game()
	pass
except KeyboardInterrupt:
	print("Saving current progress before exiting...")
	save_progress(level,moves,level_matrix,old_level_matrices)
	print("Progress saved, exiting...")
	exit()
