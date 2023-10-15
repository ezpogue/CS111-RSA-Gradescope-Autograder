# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import weight,visibility
import subprocess as subprocess
import os
import shutil

class TestAssignment(unittest.TestCase):
  #Test cases must begin with "test"
  #The @weight decorator indicates the number of points this test is worth
  #For documentation of this and other decorators, see:
  # https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils 

  #REPLACE THESE TESTS WITH YOUR OWN TESTS

  @weight(10)
  def test_1(self): #23 55 3 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '23 55' '13' '50 27 9 15 51 50 24 22 13 17 14 10 22' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_2(self):#5 1369 3 *If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.*
    cmd = "printf '%s\n' '5 55' '13' '10 23 34 45 21 10 54 33 32 43 34 10 33' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_3(self):#5 55 3 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '5 1369' '118' '250 878 1281 791 348 379 204 348 1176 379 791 931 204 791 1291 204 716 791 1024 379 1176 878 379 520 379 791 716 63 243 716 791 949 243 716 63 379 949 243 716 878 387 374 791 878 374 791 374 878 949 348 1176 379 623 791 878 716 791 878 374 791 204 1291 1176 418 791 1024 379 387 243 674 374 379 791 716 63 379 418 791 931 204 791 1291 204 716 791 647 379 243 1176 878 669 379 791 63 204 548 791 387 204 949 348 1176 878 387 243 716 379 931 791 1176 878 1281 379 791 878 374 242 250' | ./solution"
    self.compareOutput(cmd)
  
  @weight(10)
  def test_4(self):#12 253 3 *be yourself, everyone else is already taken*
    cmd = "printf '%s\n' '12 253' '45' '108 27 16 236 234 190 23 26 232 16 9 31 169 236 16 70 16 26 234 190 223 16 236 16 9 232 16 236 242 232 236 141 9 26 16 141 190 234 236 231 141 59 16 223 108' | ./solution"
    self.compareOutput(cmd)
  
  @weight(10)
  def test_5(self): #270 611 3 *be yourself, everyone else is already taken*
    cmd = "printf '%s\n' '270 611' '45' '131 27 194 144 196 131 534 337 12 194 404 220 259 144 194 64 194 337 196 131 118 194 144 194 404 12 194 144 155 12 144 378 404 337 194 378 25 196 144 222 378 533 194 118 131' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_6(self): #47 1633 3 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '47 1633' '94' '1102 388 1589 1389 1568 1389 456 1486 1486 1144 1389 144 690 1295 1295 1389 1486 144 1389 1333 1486 841 1389 544 1486 144 1333 767 1568 456 67 1389 791 67 544 388 959 1589 67 456 544 305 1389 388 144 1389 1333 767 1486 1389 1568 959 456 67 67 1389 1486 1589 1389 1333 586 67 1389 544 1568 1144 67 1389 1333 586 388 1589 959 305 1389 1333 586 1568 1333 908 544 1389 1568 1389 1144 1568 348 1486 456 388 1333 1352 1465 1102' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_7(self): #2397 5353 3 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '2397 5353' '94' '2574 4012 395 1050 1833 1050 178 1630 1630 998 1050 332 447 3743 3743 1050 1630 332 1050 2774 1630 3298 1050 2942 1630 332 2774 4986 1833 178 1967 1050 1681 1967 2942 4012 3558 395 1967 178 2942 5176 1050 4012 332 1050 2774 4986 1630 1050 1833 3558 178 1967 1967 1050 1630 395 1050 2774 3646 1967 1050 2942 1833 998 1967 1050 2774 3646 4012 395 3558 5176 1050 2774 3646 1833 2774 4327 2942 1050 1833 1050 998 1833 3177 1630 178 4012 2774 1860 4001 2574' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_8(self): #7 77 3 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '7 77' '13' '2 31 60 47 41 2 50 33 28 57 37 10 33 ' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_9(self): #3 1633 3 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '3 1633' '94' '872 1331 830 1527 27 1527 1468 14 14 109 1527 512 736 1111 1111 1527 14 512 1527 850 14 933 1527 1096 14 512 850 928 27 1468 343 1527 216 343 1096 1331 729 830 343 1468 1096 397 1527 1331 512 1527 850 928 14 1527 27 729 1468 343 343 1527 14 830 1527 850 1000 343 1527 1096 27 109 343 1527 850 1000 1331 830 729 397 1527 850 1000 27 850 11 1096 1527 27 1527 109 27 95 14 1468 1331 850 87 108 872' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_10(self): #5 1501 3 *We live in a society exquisitely dependent on science and technology, in which hardly anyone knows anything about science and technology.*
    cmd = "printf '%s\n' '5 1501' '139' '311 119 296 1485 466 444 1320 296 1485 444 878 1485 243 1485 1381 1412 123 444 296 699 848 1485 296 961 950 55 444 1381 444 699 296 466 848 1485 271 296 1310 296 878 271 296 878 699 1485 1412 878 1485 1381 123 444 296 878 123 296 1485 243 878 271 1485 699 296 123 934 878 1412 466 1412 510 848 578 1485 444 878 1485 119 934 444 123 934 1485 934 243 1369 271 466 848 1485 243 878 848 1412 878 296 1485 546 878 1412 119 1381 1485 243 878 848 699 934 444 878 510 1485 243 1024 1412 55 699 1485 1381 123 444 296 878 123 296 1485 243 878 271 1485 699 296 123 934 878 1412 466 1412 510 848 1078 311' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_11(self): #5 7663 3 *EAT A LIVE FROG FIRST THING IN THE MORNING AND NOTHING WORSE WILL HAPPEN TO YOU THE REST OF THE DAY.*
    cmd = "printf '%s\n' '5 7663' '102' '627 1481 243 4096 4961 243 4961 1414 128 767 1481 4961 2116 4529 2202 5408 4961 2116 128 4529 7385 4096 4961 4096 381 128 6408 5408 4961 128 6408 4961 4096 381 1481 4961 738 2202 4529 6408 128 6408 5408 4961 243 6408 113 4961 6408 2202 4096 381 128 6408 5408 4961 2963 2202 4529 7385 1481 4961 2963 128 1414 1414 4961 381 243 4470 4470 1481 6408 4961 4096 2202 4961 3771 2202 7086 4961 4096 381 1481 4961 4529 1481 7385 4096 4961 2202 2116 4961 4096 381 1481 4961 113 243 3771 5818 627' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_12(self): #7 7387 3 *But if the arrow is straight And the point is slick, It can pierce through dust no matter how thick. So I^ll make my stand And remain as I am And bid farewell and not give a damn.*
    cmd = "printf '%s\n' '7 7387' '181' '3478 1610 2020 4372 5067 265 6631 5067 4372 5389 3586 5067 2187 2801 2801 5597 6875 5067 265 4975 5067 4975 4372 2801 2187 265 3580 5389 4372 5067 2187 6650 6617 5067 4372 5389 3586 5067 246 5597 265 6650 4372 5067 265 4975 5067 4975 1014 265 4255 3339 5930 5067 265 4372 5067 4255 2187 6650 5067 246 265 3586 2801 4255 3586 5067 4372 5389 2801 5597 2020 3580 5389 5067 6617 2020 4975 4372 5067 6650 5597 5067 5452 2187 4372 4372 3586 2801 5067 5389 5597 6875 5067 4372 5389 265 4255 3339 1695 5067 4975 5597 5067 265 3369 1014 1014 5067 5452 2187 3339 3586 5067 5452 6627 5067 4975 4372 2187 6650 6617 5067 2187 6650 6617 5067 2801 3586 5452 2187 265 6650 5067 2187 4975 5067 265 5067 2187 5452 5067 2187 6650 6617 5067 1610 265 6617 5067 6631 2187 2801 3586 6875 3586 1014 1014 5067 2187 6650 6617 5067 6650 5597 4372 5067 3580 265 1316 3586 5067 2187 5067 6617 2187 5452 6650 1695 3478' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_13(self): #5 901 3 *If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.*
    cmd = "printf '%s\n' '5 901' '118' '30 673 332 785 171 589 782 171 828 589 785 568 782 785 713 782 813 785 123 589 828 673 589 487 589 785 813 890 243 813 785 733 243 813 890 589 733 243 813 673 422 769 785 673 769 785 769 673 733 171 828 589 777 785 673 813 785 673 769 785 782 713 828 482 785 123 589 422 243 500 769 589 785 813 890 589 482 785 568 782 785 713 782 813 785 549 589 243 828 673 367 589 785 890 782 587 785 422 782 733 171 828 673 422 243 813 589 568 785 828 673 332 589 785 673 769 291 30' | ./solution"
    self.compareOutput(cmd)

  @weight(10)
  def test_14(self): #20 20 3 hello
    cmd = "printf '%s\n' '20 20' '5' '0 1 16 16 1' | ./solution"
    self.compareOutput(cmd)
  
  @weight(10)
  def test_15(self): #7 1600 3 hello
    cmd = "printf '%s\n' '7 1600' '5' '0 1143 704 704 1073' | ./solution"
    self.compareOutput(cmd)

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