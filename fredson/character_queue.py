from exceptions import FredsonTokenError


class CharacterQueue:
    def __init__(self, string: str):
        self.string = string
        self.size = len(string)
        self.current = 0

    def __len__(self) -> int:
        return self.size - self.current

    def __getitem__(self, index) -> str:
        return self.string[index + self.current]

    def take(self, n) -> str:
        s = self.string[self.current:self.current + n]
        self.current += n
        return s

    def peek(self, n=1) -> str:
        if len(self) == 0:
            self.error("Unexpectedly ran out of characters. Did you forget to terminate a string?")

        n = n if n < len(self) else len(self)
        return self.string[self.current:self.current + n]

    def next(self) -> str:
        if len(self) == 0:
            self.error("Unexpectedly ran out of characters. Did you forget to terminate a string?")

        char = self.string[self.current]
        self.current += 1
        return char

    def ignore(self) -> None:
        self.current += 1

    def error(self, message) -> None:
        error_arrow = "\n" + " " * self.current + "^"
        error_message = f"\n{self.string}{error_arrow}\n{message}"
        raise FredsonTokenError(error_message)

