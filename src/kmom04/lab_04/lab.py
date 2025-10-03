"""
This file contains the assertions for testing each function in the lab.

Execute the labs like this.
  node lab

Execute the labs from the solutionsfile like this.
  node lab -s
"""

import math
import sys

import answer as laba
import solution as labs
from dbw import DBW

lab = labs if len(sys.argv) > 1 and sys.argv[1] == "-s" else laba

DBW.assert_(lab.concatenate_lists, [['mosquito', 'wasp'], ['lion', 'ozelot']], ['mosquito', 'wasp', 'lion', 'ozelot'], 1)

DBW.assert_(lab.append_to_list, [['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker'], 'icecream'], ['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker', 'icecream'], 1)

DBW.assert_(lab.replace_third_item_in_list, [['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker'], 'potato'], ['Dafoe', 'Sheen', 'potato', 'Depp', 'Whitaker'], 1)

DBW.assert_(lab.sort_list_descending, [["flute", "guitar", "drums", "piano", "bass"]], ['piano', 'guitar', 'flute', 'drums', 'bass'], 1)

DBW.assert_(lab.remove_from_list, [["wasp", "fly", "butterfly", "bumblebee", "mosquito"], "fly"],['wasp', 'butterfly', 'bumblebee', 'mosquito'], 1)

DBW.assert_(lab.summarize_numbers_in_list, [[123, 4, 125, 69, 155]], 476, 2)

DBW.assert_(lab.average_from_list, [[123, 4.11, 125, 69, 155.3]], 95.3, 2)

DBW.assert_(lab.remove_unwanted_sign, ["The?grass?is?growing.", "?"], "The grass is growing.", 3)

DBW.done()
