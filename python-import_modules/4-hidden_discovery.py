#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.seek(16)
        code = marshal.load(f)
    for name in sorted(code.co_names):
        if not name.startswith("__"):
            print(name)
