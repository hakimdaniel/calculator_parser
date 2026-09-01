class Parser:
    def __init__(self, text):
        self.text = text.replace(" ", "")
        self.pos = 0

    def number(self):
        start = self.pos

        while self.pos < len(self.text):
            char = self.text[self.pos]

            if char.isdigit() or char == ".":
                self.pos += 1
            else:
                break

        if start == self.pos:
            raise ValueError("Expected number")

        return float(self.text[start:self.pos])

    def term(self):
        result = self.number()

        while self.pos < len(self.text):
            op = self.text[self.pos]

            if op not in "*/":
                break

            self.pos += 1
            right = self.number()

            if op == "*":
                result *= right
            else:
                result /= right

        return result

    def expression(self):
        result = self.term()

        while self.pos < len(self.text):
            op = self.text[self.pos]

            if op not in "+-":
                break

            self.pos += 1
            right = self.term()

            if op == "+":
                result += right
            else:
                result -= right

        return result
        
