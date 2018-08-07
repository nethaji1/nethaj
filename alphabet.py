while True:
	print("Enter '0' for exit.")
	cha = input("Enter any character: ")
	if cha == '0':
		break
	else:
		if((cha>='a' and cha<='z') or (cha>='A' and cha<='Z')):
			print(cha, "is an alphabet.\n")
		else:
			print(cha, "is not an alphabet.\n")
