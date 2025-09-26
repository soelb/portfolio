import ast
import sys


def format_code(code):
    try:
        # Parse the input code into an abstract syntax tree (AST)
        tree = ast.parse(code)

        # Use AST to re-generate nicely formatted code
        formatted = ast.unparse(tree)
        return formatted
    except Exception as e:
        return f"Error formatting code: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python formatter.py <file-to-format.py>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            raw_code = file.read()

        formatted_code = format_code(raw_code)

        print("\n🎯 Formatted Code:\n")
        print(formatted_code)

    except FileNotFoundError:
        print(f"File not found: {input_file}")
