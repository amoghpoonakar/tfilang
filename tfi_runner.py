import sys
import random
import traceback
from transpiler import transpile
from error_mapper import map_python_error

ERROR_WARNINGS = [
    "AAGARAA BABUUU 😭",
    "ODIYAMMAAA BUNTYYYY 🗣️",
    "ERA BAABJI YEM CHESTUNNAAV 💀"
]

def extract_line_number(e):
    tb = traceback.extract_tb(e.__traceback__)
    if tb:
        return tb[-1].lineno
    return None

def show_tfi_error(e, mapped, code):
    warning = random.choice(ERROR_WARNINGS)
    line_no = extract_line_number(e)

    lines = code.split("\n")
    if line_no is not None and 1 <= line_no <= len(lines):
        error_line = lines[line_no - 1].strip()
    else:
        error_line = f"(unable to locate source line, Python line {line_no})"

    print("\n")
    print(warning)
    print("\n")
    # Using the mapped error type or the original if mapped is just a string
    error_type = type(mapped).__name__ if not isinstance(mapped, str) else "TFI Error"
    print(error_type)
    print(f"Assalu eh Line Choosaava 👇")
    print(f">>> {error_line}")
    print(mapped)
    print("\n")

def run_tfi_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            tfi_code = f.read()
        python_code = transpile(tfi_code)
        exec(python_code, {})

    except Exception as e:
        mapped = map_python_error(e)
        # We pass tfi_code here to show the original source error
        show_tfi_error(e, mapped, tfi_code)

def start_repl():
    print("UNITED TFI >> Type 'exit()' to quit")
    global_env = {}
    buffer = []
    indent_level = 0

    while True:
        try:
            prompt = "UNITED TFI >> " if indent_level == 0 else "........... >> "
            line = input(prompt)

            if line.strip() == "exit()":
                break

            buffer.append(line)

            # Basic logic for multi-line blocks (like if/for/def)
            if line.strip().endswith(":"):
                indent_level += 1
                continue

            # If we are inside a block, wait for an empty line to execute
            if indent_level > 0:
                if line.strip() == "":
                    full_code = "\n".join(buffer)
                    python_code = transpile(full_code)
                    exec(python_code, global_env)
                    buffer = []
                    indent_level = 0
                continue

            # Single line execution
            full_code = "\n".join(buffer)
            python_code = transpile(full_code)
            exec(python_code, global_env)
            buffer = []

        except Exception as e:
            full_code = "\n".join(buffer)
            mapped = map_python_error(e)
            show_tfi_error(e, mapped, full_code)
            buffer = []
            indent_level = 0

if __name__ == "__main__":
    if len(sys.argv) == 1:
        start_repl()
    else:
        run_tfi_file(sys.argv[1])