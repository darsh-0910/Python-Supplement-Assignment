import py_compile
import glob
import sys

files = sorted([f for f in glob.glob("*.py")])
errors = []
for f in files:
    try:
        py_compile.compile(f, doraise=True)
    except Exception as e:
        print(f"{f} :: {e}")
        errors.append((f, str(e)))

if not errors:
    print("All files compiled successfully.")
else:
    print(f"{len(errors)} file(s) failed to compile.")
    sys.exit(1)
