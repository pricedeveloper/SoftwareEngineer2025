"""
Paula Rice
Lab Exercise 10
"""
# Define the list of colors
colors = ['red', 'orange', 'olive', 'magenta', 'green']

# Get user input
usercolor = input("Enter a color to search for: ")

# Clean up the input (strip whitespace and convert to lowercase)
usercolor = usercolor.strip().lower()

# Initialize flag to track if color is found
colorfound = False

# Use a for loop to search through the list
for color in colors:
    # Check if the current color matches the user input
    if color == usercolor:
        colorfound = True
        break  # Exit the loop once we find a match

# Print the appropriate message based on whether the color was found
if colorfound:
    print(f"{usercolor} color is in the list")
else:
    print(f"{usercolor} color IS NOT in the list")
