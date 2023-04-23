# **PROGRAM 3**
# Write a method in python to write multiple line of text contents into a text file mylife.txt.
# See sample output:
# Enter line: Beautiful is better than ugly.
# Are the more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n

# Define the method/function
with open("mylife.txt", "w") as input_mylife:
    while True:
        print("____________________________________________________________________________________________________________________________________")
        input_line=str(input("Enter your line: "))
        input_mylife.write(str(input_line)+"\n")
        while True:
            input_question=str(input("Would you like to add more lines? (y or n only)\n"))
            if input_question=='y':
                break
            elif input_question=='n':
                print("Thank you for using the method.")
                exit()
            else: 
                print("Invalid")
                print("___________________________________________________________________________________________________________________________")
                continue
# Write into the output file 'mylife.txt'
# Iterate input texts
# Write input to 'mylife.txt'