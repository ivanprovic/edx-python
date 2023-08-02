# valid for python 3.10

name = input("Whats your name?")

match name:
	case "Harry" | "Hermione" | "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _: # anything else
		print("Who?")
