import sys
from transpiler import transpile
from error_mapper import map_python_error


def run_tfi_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            tfi_code = f.read()

        python_code = transpile(tfi_code)
        exec(python_code, {})

    except Exception as e:
        mapped = map_python_error(e)
        print("TFILang Error ❌")
        print(type(mapped).__name__)
        print(mapped)


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

            if line.strip().endswith(":"):
                indent_level += 1
                continue

            if line.strip() == "":
                full_code = "\n".join(buffer)
                python_code = transpile(full_code)
                exec(python_code, global_env)

                buffer = []
                indent_level = 0
                continue

            if indent_level == 0:
                full_code = "\n".join(buffer)
                python_code = transpile(full_code)
                exec(python_code, global_env)
                buffer = []

        except Exception as e:
            mapped = map_python_error(e)
            print("TFILang Error ❌")
            print(type(mapped).__name__)
            print(mapped)

            buffer = []
            indent_level = 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        start_repl()
    else:
        run_tfi_file(sys.argv[1])