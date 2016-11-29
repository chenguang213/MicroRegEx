import unittest

from src.MicroRegEx.Lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_simple_case(self):
        pattern = "abc"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        lexemes = lexer.tokens

        for i in lexemes:
            print(i)

        self.assertEqual(1, 2)

    def test_midlle_case(self):
        pattern = r"a?b+c*(d|e)\\"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        lexemes = lexer.tokens

        for i in lexemes:
            print(i)

        self.assertEqual(1, 2)

    def test_complicate_case(self):
        pattern = r"(((d|e)?)|(a+))+"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        lexemes = lexer.tokens

        for i in lexemes:
            print(i)

        self.assertEqual(1, 2)