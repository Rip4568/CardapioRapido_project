from django.test import TestCase

class TestCaseColorFull(TestCase):    
    def assertEqual(self, first, second, msg=None):
        if first == second:
            print("\033[92m" + "SUCCESS: " + str(first) + " is equal to " + str(second) + "\033[0m")
        else:
            print("\033[91m" + "FAILURE: " + str(first) + " is not equal to " + str(second) + "\033[0m")
            super(TestCaseColorFull, self).fail(self._formatMessage(msg, f"{first} != {second}"))

    def assertNotEqual(self, first, second, msg=None):
        if first != second:
            print("\033[92m" + "SUCCESS: " + str(first) + " is not equal to " + str(second) + "\033[0m")
        else:
            print("\033[91m" + "FAILURE: " + str(first) + " is equal to " + str(second) + "\033[0m")
            super(TestCaseColorFull, self).fail(self._formatMessage(msg, f"{first} == {second}"))
