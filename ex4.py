def main():
	x = int(input("What's x? "))
	if is_even(x): # is it true?
		print("Even")
	else:
		print("Odd")

def is_even(n):
	if n % 2 == 0: # if it's true -> do by True in main
		return True
	else: # if it's false -> do by False in main
		return False

main()