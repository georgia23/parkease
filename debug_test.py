# ParkEase Parking Fee Calculator
# Homework: Debugging using pdb, Python shell tests, and VS Code debugger


def calculate_fee(hours, vehicle_type):

    breakpoint()  
    # breakpoint() pauses the program so we can inspect variables using pdb.
    # When the program reaches this line, the debugger opens in the terminal.

    rates = {
        "car": 2000,
        "bike": 1000,
        "truck": 3000
    }

    # FIX: Found using Python shell testing.
    # Root cause: If the vehicle type does not exist in the rate table,
    # Python throws a KeyError and crashes.
    # Tool used: Python shell tests and pdb variable inspection.
    # Solution: Check if the vehicle exists before calculating the fee.

    if vehicle_type not in rates:
        return "Invalid vehicle type"

    # FIX: Found using Python shell testing with edge case input.
    # Root cause: If hours is None or negative, multiplication causes an error
    # or incorrect parking fee.
    # Tool used: Python shell testing.
    # Solution: Validate hours before calculating.

    if hours is None or hours < 0:
        return "Invalid number of hours"

    fee = hours * rates[vehicle_type]

    return fee


# ---- PROGRAM INPUT ----

hours = int(input("Enter number of parking hours: "))
vehicle = input("Enter vehicle type (car/bike/truck): ")

result = calculate_fee(hours, vehicle)

print("Parking fee:", result)


# -------------------------------------------------------
# DEBUGGING NOTES
# -------------------------------------------------------

# 1. PDB COMMANDS USED
# These commands were used after the breakpoint() paused execution.

# n
# Moves to the next line of code.
# Revealed how the program executed step by step.

# p hours
# Printed the value of the hours variable.
# Confirmed the input value was correctly passed to the function.

# p vehicle_type
# Displayed the vehicle type entered by the user.

# l
# Listed the surrounding lines of code to understand program flow.

# c
# Continued execution until the program finished.


# -------------------------------------------------------
# 2. PYTHON SHELL TESTING RESULTS
# These tests were performed directly in the Python shell.

# Test 1: Normal input
# calculate_fee(2,"car")
# Result: 4000

# Test 2: Zero hours (edge case)
# calculate_fee(0,"car")
# Result: 0

# Test 3: Motorcycle
# calculate_fee(3,"bike")
# Result: 3000

# Test 4: Vehicle not in rate table
# calculate_fee(2,"bus")
# Result: "Invalid vehicle type"

# Test 5: None hours (edge case)
# calculate_fee(None,"car")
# Result: "Invalid number of hours"


# -------------------------------------------------------
# 3. VS CODE DEBUGGER (F5)
# Steps performed:
#
# 1. Opened the ParkEase Python file in VS Code.
# 2. Added breakpoint() inside calculate_fee().
# 3. Pressed F5 to start debugging.
# 4. Entered test inputs in the terminal.
# 5. The program paused at breakpoint().
# 6. Observed variables in the Variables panel:
#       hours
#       vehicle_type
#       rates
