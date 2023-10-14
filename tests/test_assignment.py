# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import weight,visibility
import subprocess as subprocess
import os
import shutil
import gen

class TestAssignment(unittest.TestCase):
  #Test cases must begin with "test"
  #The @weight decorator indicates the number of points this test is worth
  #For documentation of this and other decorators, see:
  # https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils 

  #REPLACE THESE TESTS WITH YOUR OWN TESTS

  @weight(10)
  def test_out(self):
    #Compare the stdout of the reference and student solution for helloConsole.py

    self.compareOutput("./CS111RSA\n" + gen(5, 1369, 3, "*If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.*"))

  #DO NOT EDIT BELOW THIS LINE
  def outputDirectory(self):
    return "../reference-output"

  def outputFileName(self, output_source):
    return "%s/%s.%s" % (self.outputDirectory(), self._testMethodName, output_source)

  def compareOutput(self, command, stdout = True, stderr = False, extra_outfiles = []):
    if (hasattr(self, "reference") and self.reference):
      with open(self.outputFileName('out'), 'w') as out, \
      open(self.outputFileName('err'),'w') as err:
        output = subprocess.run(command, stdout=out, stderr=err, shell=True)
        for f in extra_outfiles:
          shutil.move(f, self.outputDirectory())

    else:
      output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
      if (stdout):
        student_out = output.stdout.decode()
        with open(self.outputFileName('out'), 'r') as ref_outfile:
          self.assertEqual(student_out, ref_outfile.read())

      if (stderr):
        student_err = output.stderr.decode()
        with open(self.outputFileName('err'), 'r') as ref_outfile:
          self.assertEqual(student_err, ref_outfile.read())

      for f in extra_outfiles:
        self.assertTrue(os.path.exists(f), "File %s does not exist." % f)
        with open(f, 'r') as student_file, \
        open(self.outputDirectory() + "/" + f,'r') as ref_file:
          self.assertEqual(ref_file.read(), student_file.read())