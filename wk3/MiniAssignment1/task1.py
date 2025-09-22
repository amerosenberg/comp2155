#1) Ask the user for a filename. Assume that the user will input the extension. (1 mark)
#2) Create a file with the name the user inputted in step 1) (1 mark)
#3) Ask the user for content. (1 mark)
#4) APPEND the data entered in step 3) to the file the user inputted in step 1) (1 mark)

file = input("Please enter a file name (including extension): ")
open(file,"a").close()

content = input("Please enter content: ")
with open(file, "a") as file:
    file.write(content + "\n")

