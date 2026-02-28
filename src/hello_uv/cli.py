import argparse
from . import greet

def main() -> None:
    p = argparse.ArgumentParser(prog="hello-uv")
    p.add_argument("name", nargs="?", default="world")
    args = p.parse_args()
    print(greet(args.name))
