import sys
import os
from tfi_runner import run_tfi_file, start_repl

VERSION = "1.0.0"

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ["--version", "-v"]:
        print(f"TFILang v{VERSION}")
        return

    if len(sys.argv) == 1:
        start_repl()
    else:
        run_tfi_file(sys.argv[1])


if __name__ == "__main__":
    main()