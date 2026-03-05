import traceback


class TFILangException(Exception):
    pass


class NameLedhuDhora(TFILangException):
    pass


class SyntaxChooduBhAAi(TFILangException):
    pass


class TypeOkkateKaadhamma(TFILangException):
    pass


class IndexKoduthundiSeena(TFILangException):
    pass


class YemJaruguthundiRaIkkada(TFILangException):
    pass


def extract_line_number(e):
    tb = traceback.extract_tb(e.__traceback__)
    if tb:
        return tb[-1].lineno
    return "Unknown"


def map_python_error(e):
    line_no = extract_line_number(e)

    if isinstance(e, NameError):
        var_name = str(e).split("'")[1]
        return NameLedhuDhora(
            f"Line {line_no}\nAssalu '{var_name}' yevaru dude-uh?"
        )

    elif isinstance(e, SyntaxError):
        return SyntaxChooduBhAAi(
            f"Line {line_no}\nIppudu alaa kuda raastaaraa?"
        )

    elif isinstance(e, TypeError):
        return TypeOkkateKaadhamma(
            f"Line {line_no}\nType mismatch undi ra bhai."
        )

    elif isinstance(e, IndexError):
        return IndexKoduthundiSeena(
            f"Line {line_no}\nYemundhi akkada, yemi ledhu dolla."
        )

    elif isinstance(e, ZeroDivisionError):
        return ZeroDivisionError(
            f"Line {line_no}\nArey ah Zero akkada ela pettav raa?"
        )

    else:
        return YemJaruguthundiRaIkkada(
            f"Line {line_no}\n{str(e)}"
        )