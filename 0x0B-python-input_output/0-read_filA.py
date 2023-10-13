#!/usr/bin/python3
"function"


def append_write(filename="", text=""):
    """function that ...."""

    with open(filename, 'a', encoding="utf-8") as f:
        data_writed = f.write(text)
        return data_writed

