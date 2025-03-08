# Define token types
TOKEN_TYPES = {
    'IDENTIFIER': 'IDENTIFIER',
    'ASSIGNMENT': 'ASSIGNMENT',
    'NUMBER': 'NUMBER',
    'OPERATOR': 'OPERATOR',
    'PARENTHESIS': 'PARENTHESIS',
    'SEMICOLON': 'SEMICOLON'
}

# Lexer function
def lexical_analyzer(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        char = input_string[i]

        # Ignore whitespaces
        if char.isspace():
            i += 1
            continue

        # Check for identifiers (e.g., variables)
        if char.isalpha():
            identifier = char
            i += 1
            while i < len(input_string) and (input_string[i].isalnum() or input_string[i] == '_'):
                identifier += input_string[i]
                i += 1
            tokens.append((TOKEN_TYPES['IDENTIFIER'], identifier))

        # Check for assignment operator '='
        elif char == '=':
            tokens.append((TOKEN_TYPES['ASSIGNMENT'], char))
            i += 1

        # Check for numbers
        elif char.isdigit():
            number = char
            i += 1
            while i < len(input_string) and input_string[i].isdigit():
                number += input_string[i]
                i += 1
            tokens.append((TOKEN_TYPES['NUMBER'], number))

        # Check for operators
        elif char in '+-*/':
            tokens.append((TOKEN_TYPES['OPERATOR'], char))
            i += 1

        # Check for parentheses
        elif char in '()':
            tokens.append((TOKEN_TYPES['PARENTHESIS'], char))
            i += 1

        # Check for semicolon
        elif char == ';':
            tokens.append((TOKEN_TYPES['SEMICOLON'], char))
            i += 1

        # Handle invalid characters
        else:
            raise ValueError(f"Invalid character '{char}' in input.")
    
    return tokens

# Test cases
if __name__ == "__main__":
    test_input = "x = 10 + 20 * (30 / y);"
    print("Input:", test_input)
    print("Tokens:", lexical_analyzer(test_input))
