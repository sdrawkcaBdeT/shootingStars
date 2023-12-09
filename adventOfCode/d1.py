import re

# Open file
with open('adventOfCode/d1_input.txt', 'r') as file:
    # Read the entire contents of the file
    calibration_document = file.read()
    
def get_first_numerical_character(text):
    match = re.search(r'\d', text)
    if match:
        return match.group()
    else:
        return None

def get_last_numerical_character(text):
    # Use the regular expression \d to match any digit, and $ to indicate the end of the line
    match = re.search(r'\d(?=[^\d]*$)', text)
    if match:
        return match.group()
    else:
        return None


split_calibration_document=calibration_document.split('\n')

first_character=list(map(get_first_numerical_character, split_calibration_document))
last_character=list(map(get_last_numerical_character, split_calibration_document))

# Using zip with map
combined_list = [f"{elem1}{elem2}" for elem1, elem2 in zip(first_character, last_character)]

# Drop last observation of NoneNone..
combined_list=combined_list[:-1]

numeric_list = [float(element) for element in combined_list]

sum(numeric_list)


def get_first_numerical_character(text):
    match = re.search(r'\d', text)
    if match:
        return match.group()
    else:
        return None