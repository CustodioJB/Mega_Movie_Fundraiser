# import statements

# functions go here

# checks that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response

        # if name is blank, show error (& repeat loop)
        else:
            print(error_message)


# checks for an integer between two values
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:
        
        # ask user for number and check it is valid
        try:
            response = int(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response
                
            if low_num <= response <= high_num:
                return response
            else:
                print(error)
            
        except ValueError:
            print(error)

# ************ Main Routine ************


# Set up dictionaries / list needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# start of loop

# initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats " "left".format (MAX_TICKETS - count))

    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left! ***")

    # Get details...

    # Get name (can't be blank)
    name = not_blank("Name: ", 
            "Sorry - this can't be blank, please enter your name")
    count += 1
    print()

    # Get age (between 12 and 130)
    age = int_check("Age:", 12, 130)

if count == MAX_TICKETS:
    print("You havee sold all the available tickets!")
else:
    print ("You have sold al {} tickets. \n"
        "There are {} places still availalbe"
        .format (count, MAX_TICKETS - count))

    

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method (and apply surcharge if necessary)

# Calculate Total Sales and profit


# Output data to text file
