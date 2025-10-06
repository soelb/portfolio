import ast
import sys

def format_code(code):
    """Parses input Python code, formats it using AST, and returns the formatted output."""
    try:
        tree = ast.parse(code)
        formatted = ast.unparse(tree)
        return formatted
    except SyntaxError as e:
        return f"Syntax Error: {e}"
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
        print("\n🧩 Formatted Code:\n")
        print(formatted_code)

    except FileNotFoundError:
        print(f"File not found: {input_file}")
