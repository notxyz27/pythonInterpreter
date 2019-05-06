# Token types
#
# EOF (end-of-file) toke is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token:
    def __init__(self, tokType, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = tokType
        # token value: 0 - 9, +, or None
        self.value = value

    def __str__(self):
        """
        String representation of the class instance
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return "Token({0}, {1})".format(self.type, self.value)
    
    def __repr__(self):
        return self.__str__()

class Interpreter:
    def __init__(self, expression):
        # client string intput, e.g. "3+5"
        self.expression = expression
        # self.pos is an index into self.expression
        self.pos = 0
        # current token instance
        self.current_token = None
    
    def error(self):
        raise Exception("Error parsing input")
    
    def get_next_token(self):
        """
        Lexical analyzer (also know as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time
        """
        expression = self.expression

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(expression) - 1:
            return Token(EOF, None)
        
        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = expression[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        while current_char.isspace():
            self.pos += 1
            current_char = expression[self.pos]
        count = 0
        while current_char.isdigit():
            count += 1
            self.pos += 1
            if self.pos >= len(expression):
                break
            current_char = expression[self.pos]
        if count > 0:
            token = Token(INTEGER, int(expression[self.pos - count:self.pos]))
            return token
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()
    
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        # print("left: {}".format(left))
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()