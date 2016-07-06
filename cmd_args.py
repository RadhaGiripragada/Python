from sys import argv

def addition(first,second):
	return first+second

def subtraction(first,second):
	return second-first

def multiplication(first,second):
	return first*second

def division(first,second):
	return first/second


prg, arg1,arg2=argv
first=int(arg1)
second=int(arg2)


print " 1 Addition"
print " 2 subtraction \n 3 Multiplication \n 4 Division"

choice = int(raw_input("Enter your choice from above list"))
if choice == 1:
	print addition(first,second)
elif choice==2:
	print subtraction(first,second)
elif choice==3:
	print multiplication(first,second)
elif choice==4:
	print division(first,second)
else:
	print "Invalid choice"

  
