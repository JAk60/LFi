import ac
import inspect

# Print the source code of the module
try:
    print(inspect.getsource(ac))
except OSError as e:
    print("Source code not available:", e)

# Print the list of imported modules
print("Imported modules:", dir(ac))
