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
def multiple_write():
    with open("mylife.txt", "w") as input_mylife:
        while True:
            print("____________________________________________________________________________________________________________________________________")
            input_line=str(input("Enter your line: "))
            # Write input to 'mylife.txt'
            input_mylife.write(str(input_line)+"\n")
            # Iterate input texts
            while True:
                input_question=str(input("Would you like to add more lines? (y or n only)\n"))
                if input_question=='y':
                    break
                elif input_question=='n':
                    print("\nThank you for using the method.")
                    break
                else: 
                    print("Invalid")
                    print("___________________________________________________________________________________________________________________________")
                    continue
            if input_question=='n':
                break
def view_input():
    with open("mylife.txt", "r") as view_file:
        view_mylife=str(input("Would you like to view all of your input? (y or n):\n"))
        if view_mylife=='y':
            for line in view_file:
                print(line.strip().rjust(50)+'\n')
        elif view_mylife=='n':
            print("Thank You.")
            exit()
        else:
            print("Invalid")
            print("_______________________________________________________________________________________________________________________")
# Execute the code
multiple_write()
view_input()

# Sample lines to put:
# My life is all but simple
# Normal days, normal events
# But deep within my 'ole heart
# is a longing, unrelenting.

# HONTIVEROS JEROME ANDREI O.
# BSCPE 1-5