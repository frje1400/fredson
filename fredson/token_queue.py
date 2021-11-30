from collections import deque
from dataclasses import dataclass
from fredson_exceptions import FredsonParseError
from token_type import TokenType


@dataclass
class Token:
    token_type: TokenType
    lexeme: str


class TokenQueue:
    def __init__(self, tokens: deque[Token]):
        self.tokens = tokens
        self.token_history = []

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, index):
        return self.tokens[index]

    def popleft(self, error_message=None, *args) -> Token:
        if len(self.tokens) == 0:
            self.error(error_message + ".")

        if self.tokens[0].token_type == TokenType.WHITESPACE:
            self.token_history.append(self.tokens.popleft())
            return self.popleft(error_message, *args)

        if len(args) > 0:
            if not self.match(*args):
                invalid_token = self.tokens.popleft()
                self.token_history.append(invalid_token)
                self.unexpected_token_error(error_message, invalid_token)

        token = self.tokens.popleft()
        self.token_history.append(token)
        return token

    def match(self, *args) -> bool:
        if len(self.tokens) == 0:
            return False

        if self.tokens[0].token_type == TokenType.WHITESPACE:
            self.token_history.append(self.tokens.popleft())
            return self.match(*args)

        for token_type in args:
            if token_type == self.tokens[0].token_type:
                return True

        return False

    def error(self, message: str):
        history = self.rebuild_history(20)
        raise FredsonParseError(f"\n\n{history} <-- \n\n{message}")

    def unexpected_token_error(self, message: str, invalid_token: Token):
        history = self.rebuild_history(20)
        raise FredsonParseError(f"\n\n{history} <-- \n\n{message}, not '{invalid_token.lexeme}'")

    def rebuild_history(self, nbr_of_tokens) -> str:
        """Return the n most recent tokens as a string."""
        history_len = len(self.token_history)
        n = nbr_of_tokens if nbr_of_tokens < history_len else history_len
        history = self.token_history[history_len - n:]
        return "".join([token.lexeme for token in history]).strip()

    def empty_after_parse(self) -> bool:
        """Verifies that the token queue is empty after finishing the parse."""
        if len(self.tokens) == 0:
            return True

        for token in self.tokens:
            self.token_history.append(token)
            if token.token_type != TokenType.WHITESPACE:
                self.error('Unexpected left over character(s) found after parse.')

        return True
