#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import os
import unittest
from io import StringIO
from unittest.mock import patch

from tester import (ExamTestCase, ExamTestResult, import_module,
                    setup_and_get_repo_path, tags)

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = setup_and_get_repo_path(FILE_DIR)

# Path to file and basename of the file to import
main = import_module(REPO_PATH, "main")


class Test2Typing(ExamTestCase):
    """
    Meny options for counting
    """

    def test_a_quit(self):
        """
        Testar att avsluta med menyval 'q'.
        Kollar bara att programmet inte kraschar vid start.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()




if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
