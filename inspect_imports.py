# inspect_imports.py
import sys
import importlib

def show(name: str):
    m = sys.modules[name]
    is_pkg = hasattr(m, "__path__")
    print(f"\n{name}")
    print(f"  type: {type(m)}")
    print(f"  id:   {id(m)}")
    print(f"  file: {getattr(m, '__file__', None)}")
    print(f"  pkg?: {is_pkg}")
    if is_pkg:
        print(f"  path: {list(m.__path__)}")

print("Before importing anything, hello_uv in sys.modules?:", "hello_uv" in sys.modules)

print("\n--- Import 1: import hello_uv ---")
import hello_uv
show("hello_uv")
input("Press Enter to continue...")

print("\n--- Import 2: import hello_uv.nn ---")
import hello_uv.nn
show("hello_uv.nn")
input("Press Enter to continue...")

print("\n--- Import 3: import hello_uv.nn.functional ---")
import hello_uv.nn.functional
show("hello_uv.nn.functional")

input("Press Enter to continue...")

print("\n--- Links (attributes vs sys.modules) ---")
print("hello_uv.nn is sys.modules['hello_uv.nn'] ?",
      hello_uv.nn is sys.modules["hello_uv.nn"])

print("hello_uv.nn.functional is sys.modules['hello_uv.nn.functional'] ?",
      hello_uv.nn.functional is sys.modules["hello_uv.nn.functional"])

print("\n--- What modules are loaded under hello_uv* ---")
for k in sorted([k for k in sys.modules.keys() if k.startswith("hello_uv")]):
    print(" ", k)

print("\n--- Re-import returns same object (singleton behavior) ---")
m1 = importlib.import_module("hello_uv.nn.functional")
m2 = importlib.import_module("hello_uv.nn.functional")
print("same object?", m1 is m2, "id:", id(m1), id(m2))


