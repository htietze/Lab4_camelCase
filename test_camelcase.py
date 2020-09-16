import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.camelcase('Hello World'))
        self.assertEqual('', camelCase.camelcase(''))
        self.assertEqual('The entered sentence contains special characters or numbers, please try again', camelCase.camelcase('♣️♠️♦️♥️'))
        self.assertEqual('helloWorld', camelCase.camelcase('     Hello   World   '))
        self.assertEqual('hELLOWORLD', camelCase.camelcase(' H e L l O  w o R l D   '))
        self.assertEqual('The entered sentence contains special characters or numbers, please try again', camelCase.camelcase('12345'))
        self.assertEqual('The entered sentence contains special characters or numbers, please try again', camelCase.camelcase('1test test2'))
        # previous test breaks because it ignores the 1 and goes with '1TestTest2' instead
        # Looks like it ignores numbers and that messes with which word it uses.
        self.assertEqual('The entered sentence contains special characters or numbers, please try again', camelCase.camelcase('1 test test 2'))
        # Changed main code to validate and only accept letters