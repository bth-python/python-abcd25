#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""

import os
import sys
import unittest
from io import StringIO
from unittest import TextTestRunner
from unittest.mock import patch

from tester import (ExamTestCase, ExamTestResult, find_path_to_assignment,
                    import_module, setup_and_get_repo_path, tags)

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = setup_and_get_repo_path(FILE_DIR)


class Test3SplitBIllErrors(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    # link_to_assignment = "https://dbwebb-python-bth.github.io/website/laromaterial/övning/jobba-i-kursen/"
    FILE = "split"

    def get_output_from_program(self, inp):
        """
        One function for testing print input functions
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                with self.assertRaises(SystemExit):
                    import_module(REPO_PATH, self.FILE)
                return fake_out.getvalue()

    @tags("error")
    def test_a_0_people(self):
        """
        Testar skicka in 0 personer. Kollar att felhantering funkar.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [100, 0]
        output_from_program = self.get_output_from_program(self._multi_arguments)
        self.assertIn("Varning! Antal personer måste vara minst 1.", output_from_program)


if __name__ == "__main__":
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
