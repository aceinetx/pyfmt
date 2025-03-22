"""

pyfmt
string formatting python library

aceinet (2022-present)

"""

import ctypes
pyfmt = ctypes.CDLL("libpyfmt.so")

pyfmt.default_fmt.argtypes = ctypes.c_char_p,
pyfmt.default_fmt.restype = ctypes.POINTER(ctypes.c_char)

default_print_function = print

def default_fmt(text: str, *fmt) -> str:
    fmt_args   = list(fmt)
    c_fmt_args = []
   
    # convert format args to c types
    for arg in fmt_args:
        arg_type = type(arg)
        if arg_type == int:
            c_fmt_args.append(ctypes.c_int(arg))
        elif arg_type == str:
            c_fmt_args.append(ctypes.c_char_p(arg.encode()))
        elif arg_type == bool:
            c_fmt_args.append(ctypes.c_bool(arg))
        elif arg_type == float:
            c_fmt_args.append(ctypes.c_double(arg))
        else:
            c_fmt_args.append(ctypes.c_long(id(arg)))

    arg_text   = ctypes.c_char_p(text.encode())
    ret        = pyfmt.default_fmt(arg_text, *c_fmt_args)
    dst        = ctypes.cast(ret, ctypes.c_char_p).value
    if dst != None:
        return dst.decode()
    return ""

def printf(text: str, *fmt) -> None:
    default_print_function(default_fmt(text, *fmt))
