import re


KEYWORD_MAP = {
    "aite": "if",
    "lekapothe": "elif",
    "kakapothe": "else",
    "enthavaraku": "while",
    "ippudu": "for",
    "anna_idhi": "def",
    "final_ga": "return",
    "paadu_gajaala": "print",
    "idhigo": "input",
    "mari": "and",
    "leda": "or",
    "aapeyyali": "break",
    "PanWorld": "global",
    "Bokka": "None",
    "enthundi": "len",
    "yentidhi": "type"
}

METHOD_MAP = {
    ".pettaraa(": ".append(",
    ".petteyyi(": ".extend(",
    ".akkadaPettu(": ".insert(",
    ".teseyyi(": ".pop(",
    ".yellipo(": ".remove(",
    ".yekkada(": ".index(",
    ".lekkettu(": ".count(",
    ".saduruko(": ".sort(",
    ".tippeyyi(": ".reverse(",
    ".tashkarinchu(": ".copy(",
}


def transform_postfix_not(code):
    pattern = r"\((.*?)\)\s+kaadhu"
    while re.search(pattern, code):
        code = re.sub(pattern, r"not (\1)", code)
    return code


def remove_idhi_declaration(code):
    return re.sub(r"\bidhi\s+", "", code)


def transform_switch(code):
    lines = code.split("\n")
    new_lines = []
    switch_var = None
    switch_indent = None
    inside_switch = False
    first_case = True

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        # Detect switch start
        if stripped.startswith("choodu_ipuudu"):
            match = re.search(r"\((.*?)\)", stripped)
            if match:
                switch_var = match.group(1)
                switch_indent = indent
                inside_switch = True
                first_case = True
            continue  # remove the switch line completely

        if inside_switch:

            # If indentation returns to or above switch level, switch block ended
            if indent <= switch_indent and stripped != "":
                inside_switch = False

            else:
                # CASE
                if stripped.startswith("aithe_idhi"):
                    values_part = stripped.replace("aithe_idhi", "").replace(":", "").strip()
                    values = [v.strip() for v in values_part.split(",")]

                    condition = " or ".join([f"{switch_var} == {v}" for v in values])
                    keyword = "if" if first_case else "elif"

                    new_lines.append(" " * indent + f"{keyword} {condition}:")
                    first_case = False
                    continue

                # DEFAULT
                elif stripped.startswith("yedho_okkati"):
                    new_lines.append(" " * switch_indent + "else:")
                    continue

        new_lines.append(line)

    return "\n".join(new_lines)

def transpile(code):

    code = transform_switch(code)

    # keyword replacements
    for tfi_word, py_word in KEYWORD_MAP.items():
        code = re.sub(rf"\b{tfi_word}\b", py_word, code)

    code = transform_postfix_not(code)

    code = remove_idhi_declaration(code)

    # method replacements LAST
    for tfi_method, py_method in METHOD_MAP.items():
        code = code.replace(tfi_method, py_method)

    return code