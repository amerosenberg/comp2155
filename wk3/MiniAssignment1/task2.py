#1) Ask the user for a filename. (1 mark)
#2) TRY to open the file for reading. (2 marks)
#3) Output an error message if the specified file in Step 1) is not found (2 marks)
#4) If file in Step 1) is found, output its contents (1 mark)

file = input("Enter file name: ")

try:
    with open(file, 'r') as file:
        print(file.read())

except FileNotFoundError:
    print(f"{file} not found.")


