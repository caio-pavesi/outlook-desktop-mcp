'''
Example code for the main.py file. This is the entry point of the application. You can import and use functions from other modules here.
'''

from settings import VAR_1, VAR_2


class Example:
    def __init__(self):
        print("Main class initialized.")

    @property
    def var_one(self) -> str:
        return str(VAR_1)

    @property
    def var_two(self) -> str:
        return str(VAR_2)

def main() -> tuple[str, str]:

    example = Example()

    print(f"VAR_1: {example.var_one}")
    print(f"VAR_2: {example.var_two}")

    return example.var_one, example.var_two

if __name__ == "__main__":
    main()
