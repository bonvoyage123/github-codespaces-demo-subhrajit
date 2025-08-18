# WRITING IN A FILE
f= open('myfile.txt','w')  # Declaring the file name and selecting the mode (w, in this case)
print (f)  # Metadata of the file
text = f.write ("Hello World, My name is Subhrajit !!") # Writing in the file
f.close ()  # This is mandatory

# READING THE FILE CONTENTS
f= open('myfile.txt','r')  # Declaring the file name and selecting the mode (r, in this case)
print (" The file content below :")
readFile = f.read () # Reading in the file
print (readFile)
f.close()

#APPENDING THE FILE :: Basically writing in the existing file
f= open('myfile.txt','a')  # Declaring the file name and selecting the mode (a, in this case)
print (" The appended file content below :")
appendFile = f.write ("""
             I am a Data Engineer""") # Appending in the file
print (appendFile)
f.close()

#READING THE APPENDED FILE
f= open('myfile.txt','r')  # Declaring the file name and selecting the mode (r, in this case)
print (" The file content below :")
readFile = f.read () # Reading in the file
print (readFile)
f.close()