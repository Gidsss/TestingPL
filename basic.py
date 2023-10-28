# Define a list of keywords
keywords = ["chan"]

# Define a list of delimiters
data_type_delim = [',', '(', ')', '~', '=']

# Initialize variables to store tokens and the current token being parsed
tokens = []
current_token = ""

# Function to determine the token type
def get_token_type(token):
    if token in keywords:
        return "KEYWORD"
    elif token in data_type_delim:
        return "DELIMITER"
    else:
        return "IDENTIFIER"

# Get input from the user
input_string = input("Enter your code: ")

# State machine to tokenize the input
state = "INITIAL"
for char in input_string:
    if state == "INITIAL":
        if char.isalpha() or char == "_":
            current_token += char
            state = "IDENTIFIER"
        elif char in data_type_delim:
            tokens.append((get_token_type(char), char))
        elif char.isspace():
            continue
        else:
            current_token += char
            state = "OPERATOR"

    elif state == "IDENTIFIER":
        if char.isalnum() or char == "_":
            current_token += char
        else:
            tokens.append((get_token_type(current_token), current_token))
            current_token = ""
            state = "INITIAL"
            if char in data_type_delim:
                tokens.append((get_token_type(char), char))
            elif not char.isspace():
                current_token += char
                state = "OPERATOR"

    elif state == "OPERATOR":
        if char in data_type_delim:
            tokens.append((get_token_type(current_token), current_token))
            current_token = ""
            state = "INITIAL"
            tokens.append((get_token_type(char), char))
        elif not char.isspace():
            current_token += char

# Print the tokens
for token_type, token_value in tokens:
    print(f"Token Type: {token_type}, Token Value: {token_value}")
