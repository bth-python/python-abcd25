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

DBW.assert_(lab.hello, [], "Hello world", 1)

DBW.assert_(lab.magic_number, [], 42, 1)

DBW.assert_(lab.float_str, ["3.141592"], 3.141592, 1)

DBW.assert_(lab.string_length, ["cow say"], 7, 1)

DBW.assert_(lab.round_pi, [math.pi], 3.142, 1)

DBW.assert_(lab.concat_strings, ["One", "Million!"], "One Million!", 2)

DBW.assert_(lab.char_at_position, ["Kebnekaise"], "e", 2)

DBW.assert_(lab.divide_string_number, [], 6, 2)

DBW.assert_(lab.even_or_odd, [7], "Odd", 2)

DBW.assert_(lab.even_or_odd, [12], "Even", 2)

DBW.assert_(lab.password_check, ["Hej"], "Too short", 2)

DBW.assert_(lab.password_check, ["Ett bra lösenord"], "OK", 2)

DBW.assert_(lab.password_check, ["12345"], "OK", 2)


DBW.done()
