# TFILang

TFILang is a custom programming language that transpiles into Python.
It provides simple readable syntax inspired by conversational keywords while still executing through Python.

---

## Features

* Simple and expressive syntax
* Python transpilation
* Built-in REPL
* Custom error messages
* Switch–case style syntax
* List method shortcuts
* Windows installer

---

# Installation

Download the latest installer from the Releases page:

https://github.com/amoghpoonakar/tfilang/releases

Run the installer and restart your terminal.

After installation you can start the interpreter using:

```
tfi
```

or

```
tfilang
```

---

# Running a TFILang File

```
tfi program.tfi
```

Example:

```
idhi x = 10
paadu_gajaala(x)
```

Output:

```
10
```

---

# TFILang → Python Keyword Mapping

| TFILang       | Python |
| ------------- | ------ |
| aite          | if     |
| lekapothe     | elif   |
| kakapothe     | else   |
| enthavaraku   | while  |
| ippudu        | for    |
| anna_idhi     | def    |
| final_ga      | return |
| paadu_gajaala | print  |
| idhigo        | input  |
| mari          | and    |
| leda          | or     |
| aapeyyali     | break  |
| PanWorld      | global |
| Bokka         | None   |
| enthundi      | len    |
| ikkadidhaaka  | range  |
| yentidhi      | type   |

---

# List Method Mapping

| TFILang         | Python     |
| --------------- | ---------- |
| .pettaraa()     | .append()  |
| .petteyyi()     | .extend()  |
| .akkadaPettu()  | .insert()  |
| .teseyyi()      | .pop()     |
| .yellipo()      | .remove()  |
| .yekkada()      | .index()   |
| .lekkettu()     | .count()   |
| .saduruko()     | .sort()    |
| .tippeyyi()     | .reverse() |
| .tashkarinchu() | .copy()    |

---

# Custom Syntax

## Variable Declaration

TFILang:

```
idhi x = 5
```

Python equivalent:

```
x = 5
```

---

## Postfix NOT Operator

TFILang:

```
(x > 10) kaadhu
```

Python:

```
not (x > 10)
```

---

## Switch-Case Style Syntax

TFILang:

```
choodu_ipuudu(x):

    aithe_idhi 1:
        paadu_gajaala("One")

    aithe_idhi 2,3:
        paadu_gajaala("Two or Three")

    yedho_okkati:
        paadu_gajaala("Other")
```

Python equivalent:

```
if x == 1:
    print("One")

elif x == 2 or x == 3:
    print("Two or Three")

else:
    print("Other")
```

---

# Example Program

TFILang:

```
idhi numbers = [1,2,3]

numbers.pettaraa(4)

paadu_gajaala(numbers)
```

Python Equivalent:

```
numbers = [1,2,3]
numbers.append(4)
print(numbers)
```

---

# Project Structure

```
transpiler.py
error_mapper.py
tfi_runner.py
tfi.py
sample.tfi
```

---

# Author

AmoghVP

GitHub:
https://github.com/amoghpoonakar
