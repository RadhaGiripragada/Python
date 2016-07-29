#this is a file operations demostration
from sys import argv




def file_read_write_operations(filename):
	#either open with just "open" and close. or do with "with....as" 
	#we don't have to close the file

	fd = open(filename,"w+") 
	fd.write("this is open...close file")
	fd.close() #you have to close file to flush buffers 

	with open("file1.txt","w") as my_file_fd:
		my_file_fd.write("This is my file")
		my_file_fd.write("No need to close this file")

	#check if this is closed
	if not my_file_fd.closed:
		my_file_fd.close()
	if not fd.closed:
		fd.close()	

	#now read the file
	with open("file1.txt","r") as r_rd:
		print r_rd.readline() #reads one line
		print r_rd.readline()

	r1=open(filename,"r")
	print r1.read() #reads whole file
	r1.close()

	#empty the file
	"""r1=open(filename,"w")
	r1.truncate()
	"""

script, filename=argv
file_read_write_operations(filename)


