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


class Test3Extra(ExamTestCase):
    """
    Meny options for counting
    """

    @tags("count", "lines", "file")
    def test_a_lines(self):
        """
        Testar att anropa menyval 'write lines' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i filen 'output.txt':
        {correct}
        Den innehöll följande:
        {student}
        """
        self._multi_arguments = ["write lines", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            main.main()
        with open("output.txt", "r", encoding="utf-8") as fd:
            content = fd.read()
        self.assertEqual(content, "17")



    @tags("count", "words", "file")
    def test_a_words(self):
        """
        Testar att anropa menyval 'write words' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i filen 'output.txt':
        {correct}
        Den innehöll följande:
        {student}
        """
        self._multi_arguments = ["write words", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            main.main()
        with open("output.txt", "r", encoding="utf-8") as fd:
            content = fd.read()
        self.assertEqual(content, "199")



    @tags("count", "letters", "file")
    def test_a_letters(self):
        """
        Testar att anropa menyval 'write letters' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i filen 'output.txt':
        {correct}
        Den innehöll följande:
        {student}
        """
        self._multi_arguments = ["write letters", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            main.main()
        with open("output.txt", "r", encoding="utf-8") as fd:
            content = fd.read()
        self.assertEqual(content, "907")



    @tags("frequency", "word_frequency", "file")
    def test_a_word_frequency(self):
        """
        Testar att anropa menyval 'write word_frequency' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i filen 'output.txt':
        {correct}
        Den innehöll följande:
        {student}
        """
        self._multi_arguments = ["write word_frequency", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            main.main()
        with open("output.txt", "r", encoding="utf-8") as fd:
            content = fd.read()
        self.assertEqual(content, 'the: 12 | 6.0%\nto: 8 | 4.0%\nand: 7 | 3.5%\nof: 6 | 3.0%\nstreet: 5 | 2.5%\nhim: 5 | 2.5%\nhe: 5 | 2.5%')


    @tags("frequency", "letter_frequency", "file")
    def test_a_letter_frequency(self):
        """
        Testar att anropa menyval 'write letter_frequency' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i filen 'output.txt':
        {correct}
        Den innehöll följande:
        {student}
        """
        self._multi_arguments = ["write letter_frequency", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            main.main()
        with open("output.txt", "r", encoding="utf-8") as fd:
            content = fd.read()
        self.assertEqual(content, 'e: 108 | 11.9%\nt: 91 | 10.0%\no: 77 | 8.5%\nh: 67 | 7.4%\nn: 66 | 7.3%\ni: 64 | 7.1%\na: 64 | 7.1%')

if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
