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


class Test2SplitBill(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb-python-bth.github.io/website/laromaterial/övning/jobba-i-kursen/"
    FILE = "split"

    def get_output_from_program(self, inp):
        """
        One function for testing print input functions
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                import_module(REPO_PATH, self.FILE)
                return fake_out.getvalue()

    @tags("even")
    def test_a_even_split(self):
        """
        Testar dela på en nota där uträkningen går jämt ut.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [100, 4]
        output_from_program = self.get_output_from_program(self._multi_arguments)
        self.assertIn("25.0 kr", output_from_program)

    @tags("uneven")
    def test_b_uneven_split(self):
        """
        Testar dela på en nota där uträkningen går inte går jämt ut.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [100, 3]
        output_from_program = self.get_output_from_program(self._multi_arguments)
        self.assertIn("33.33 kr", output_from_program)


    @tags("uneven")
    def test_c_uneven_split_one_decimal(self):
        """
        Testar dela på en nota där uträkningen går inte går jämt ut men det blir bara en decimal.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [850, 4]
        output_from_program = self.get_output_from_program(self._multi_arguments)
        self.assertIn("212.5 kr", output_from_program)

    @tags("something")
    def test_d_one_person(self):
        """
        Testar dela på en nota med en person.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [100, 1]
        output_from_program = self.get_output_from_program(self._multi_arguments)
        self.assertIn("100.0 kr", output_from_program)

if __name__ == "__main__":
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
