##########
# UtilsN.py
# Utility functions
##########

# getUserChoice()
# Displays a list of options, prompts for an option, and returns it
# Pass it a list of lists in format [["Letter","Display text"]]
# Example: [["A","Option A"],["B","Option B"],["C","Option C"]]
# Returns selected letter
def getUserChoice(options):
    # Create a variable to hold valid inputs
    validInputs = ""
    # Loop through the options
    for opt in options:
        # Add this one to the valid letters list
        validInputs += opt[0]
        # And display it
        print(opt[0], "-", opt[1])
    # Create the prompt
    prompt = "What do you want to do? [" + validInputs + "]: "
    # Initialize variables
    choice = ""
    done = False
    # Main loop
    while not done:
        # Get a single upper case character
        choice = input(prompt).strip().upper()
        # If the user entered more than 1 character
        if len(choice) > 1:
            # Just use the first
            choice = choice[0]
        # Do we have 1 valid input?
        if len(choice) == 1 and choice in validInputs:
            # We do, outa here!
            done = True
    # Return the selected option
    return choice

# Numeric input function
def inputNumber(prompt):
    # Input variable
    inp = ""
    # Loop until variable is a valid number
    while not inp.isnumeric():
        # Prompt for input
        inp = input(prompt).strip()
    # Return the number
    return int(inp)

# Yes / No choice function
def inputYesNo(prompt):
    print(prompt)
    # Input variable
    ynchoice = " "
    # Determine if input is valid
    while ynchoice not in ["Y","N"]:
        ynchoice = input(print("Enter your choice as Y or N")).strip().upper()
    return ynchoice
