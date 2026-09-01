from .calculate import Parser

def calculate(text):
  parse = Parser(text)
  return parse.expression()
